#!/usr/bin/env python3
"""Inspection pass: given a run_inference.py generation file and the original
problems file, use a FIXED inspector model (claude-sonnet-5, always, via the
Anthropic SDK) to extract answers, judge correctness, and look for evidence
of each failure mode in the project's taxonomy.

This is the ONLY place answer extraction and taxonomy judgments happen —
never in run_inference.py, and never via naive regex — matching how the
original pilot worked and avoiding biasing what counts as "the answer".

Usage:
    python inspect_traces.py --generation ../data/mgsm_symbolic/raw_pilot_outputs/round1_llama3-8b_generation.json \\
        --problems ../data/mgsm_symbolic/pilot_round1_fogbank_problems.json \\
        --out ../data/mgsm_symbolic/raw_pilot_outputs/round1_llama3-8b_full.json
"""

from __future__ import annotations

import argparse
import json
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import anthropic
from tqdm import tqdm

from providers import ProviderError, build_anthropic_client

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# Hardcoded, never a CLI arg, never derived from providers.DEFAULT_ANTHROPIC_MODEL.
# Keeping the inspector fixed regardless of what generated the traces is the
# whole point of this experimental design.
INSPECTOR_MODEL = "claude-sonnet-5"

# claude-sonnet-5 runs adaptive thinking by default when `thinking` is
# omitted, and max_tokens is a hard cap on thinking + response text combined.
# A small budget risks the model exhausting it on invisible thinking before
# emitting the JSON body (stop_reason == "max_tokens", truncated/invalid
# JSON). Sized generously (well under the ~16K non-streaming timeout guard)
# and paired with an explicit stop_reason check below rather than relying on
# json.loads to fail with an opaque error.
INSPECTOR_MAX_TOKENS = 8192

# Deliberately excludes idx and ground_truth_answer — those are known values
# we own and inject after the call, not something we ask the model to
# transcribe (removes one source of transcription error).
FINDING_SCHEMA = {
    "type": "object",
    "properties": {
        "extracted_answer": {
            "type": "string",
            "description": "The model-under-test's final answer, exactly as it literally appears in the trace (do not recompute it).",
        },
        "math_correct": {
            "type": "boolean",
            "description": "Whether extracted_answer is numerically equivalent to the ground truth answer.",
        },
        "compositional_collapse_evidence": {
            "type": "string",
            "description": "Quoted evidence of compositional collapse, or the literal string 'none'.",
        },
        "reasoning_drift_evidence": {
            "type": "string",
            "description": "Quoted evidence of reasoning drift, or the literal string 'none'.",
        },
        "format_instability_evidence": {
            "type": "string",
            "description": "Quoted evidence of format instability, or the literal string 'none'.",
        },
        "brief_verdict": {
            "type": "string",
            "description": "One paragraph summarizing the verdict for this trace.",
        },
    },
    "required": [
        "extracted_answer",
        "math_correct",
        "compositional_collapse_evidence",
        "reasoning_drift_evidence",
        "format_instability_evidence",
        "brief_verdict",
    ],
    "additionalProperties": False,
}

INSPECTOR_SYSTEM_PROMPT = """You are grading a math-reasoning transcript that you did NOT produce, \
against a known ground-truth answer. The transcript comes from a different model being tested; \
your job is to inspect it objectively, not to re-solve the problem from scratch.

For each transcript you will be given: the original question, the ground-truth numeric answer, \
and the model-under-test's raw output. Do the following:

1. Extract the model's final answer exactly as it literally appears in the trace. Do not recompute \
or "correct" it — report what the model actually said its answer was.
2. Judge math_correct by independently checking numeric equivalence between the extracted answer and \
the ground truth (e.g. "89" and "89%" should be treated as equivalent if the question calls for a \
percentage; a wrong unit or wrong magnitude is not equivalent). Use your own judgment of the arithmetic, \
not just string matching.
3. Look for evidence of each of these three failure modes, quoting the exact text as evidence, or \
writing exactly "none" if you find no evidence of it:
   - compositional_collapse: a required sub-part of the problem is noticed or invented by the model, \
then dropped entirely or misapplied wholesale later in the reasoning (not a gradual arithmetic slip — a \
whole sub-part disappearing or being handled incorrectly as a unit).
   - reasoning_drift: the early steps of the reasoning are correct, but a later step introduces an error \
that cascades through the rest of the solution.
   - format_instability: only relevant when the generation prompt required a strict structural output \
format (you will be told whether this applies to the current trace). Look for structural tags that are \
malformed, missing, or reordered relative to what was required.
4. Write a brief one-paragraph verdict summarizing your assessment of this trace.

Be precise and evidence-based. Quote exact substrings from the trace as evidence; do not paraphrase \
evidence fields. If a failure mode is not present, the corresponding evidence field must be exactly "none"."""

OVERALL_SUMMARY_SYSTEM_PROMPT = """You are synthesizing a batch of per-problem grading results for one \
language into a single paragraph. You will be given each problem's index, whether it was judged \
mathematically correct, and its brief verdict. Write one paragraph summarizing overall accuracy for \
this language's batch and any recurring failure pattern you notice across the verdicts."""


# ---------------------------------------------------------------------------
# Inspector calls
# ---------------------------------------------------------------------------


def inspect_one(
    client: anthropic.Anthropic,
    lang: str,
    problem: dict,
    raw_output: str,
    format_required: bool,
) -> dict:
    """Send one transcript to the fixed inspector and return a finding dict
    with idx/ground_truth_answer injected. Raises on failure — the caller
    substitutes a fallback finding."""
    format_note = (
        ""
        if format_required
        else (
            "\n\nNote: this run did NOT require a structural output format, so "
            "format_instability_evidence must always be exactly \"none\" for this trace."
        )
    )
    user_prompt = (
        f"Language: {lang}\n\n"
        f"Question:\n{problem['question']}\n\n"
        f"Ground truth answer: {problem['answer_number']}\n\n"
        f"Model-under-test raw output:\n{raw_output}"
        f"{format_note}"
    )

    response = client.messages.create(
        model=INSPECTOR_MODEL,
        max_tokens=INSPECTOR_MAX_TOKENS,
        system=INSPECTOR_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_prompt}],
        output_config={"format": {"type": "json_schema", "schema": FINDING_SCHEMA}},
    )

    if response.stop_reason == "max_tokens":
        # Fail loudly and specifically here instead of letting json.loads
        # raise an opaque JSONDecodeError on the truncated body below.
        raise RuntimeError(
            f"inspector response truncated at max_tokens={INSPECTOR_MAX_TOKENS} "
            "(stop_reason=max_tokens) before completing JSON output"
        )

    text = next(block.text for block in response.content if block.type == "text")
    finding = json.loads(text)
    finding["idx"] = problem["idx"]
    finding["ground_truth_answer"] = problem["answer_number"]
    return finding


def summarize_language(client: anthropic.Anthropic, findings: list[dict]) -> str:
    digest_lines = []
    for f in findings:
        digest_lines.append(
            f"idx {f['idx']}: math_correct={f['math_correct']} — {f['brief_verdict']}"
        )
    digest = "\n".join(digest_lines)

    response = client.messages.create(
        model=INSPECTOR_MODEL,
        max_tokens=INSPECTOR_MAX_TOKENS,
        system=OVERALL_SUMMARY_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": digest}],
    )
    if response.stop_reason == "max_tokens":
        raise RuntimeError(
            f"inspector summary truncated at max_tokens={INSPECTOR_MAX_TOKENS} "
            "(stop_reason=max_tokens)"
        )
    return "".join(block.text for block in response.content if block.type == "text")


def _fallback_finding(problem: dict, error: Exception) -> dict:
    return {
        "idx": problem["idx"],
        "extracted_answer": "",
        "ground_truth_answer": problem["answer_number"],
        "math_correct": False,
        "compositional_collapse_evidence": "none",
        "reasoning_drift_evidence": "none",
        "format_instability_evidence": "none",
        "brief_verdict": f"[INSPECTION_ERROR] {type(error).__name__}: {error}",
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def parse_args(argv=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Inspect generation traces with a fixed Claude Sonnet 5 inspector."
    )
    parser.add_argument(
        "--generation", required=True, help="Path to run_inference.py's output JSON"
    )
    parser.add_argument(
        "--problems",
        required=True,
        help="Path to the original pilot_round*_problems.json (question text + ground truth)",
    )
    parser.add_argument("--out", required=True, help="Path to write the combined JSON")
    parser.add_argument(
        "--workers", type=int, default=5, help="Thread-pool size for concurrent inspector calls"
    )
    return parser.parse_args(argv)


def main() -> None:
    args = parse_args()

    generation = json.loads(Path(args.generation).read_text(encoding="utf-8"))
    problems_by_lang = json.loads(Path(args.problems).read_text(encoding="utf-8"))

    try:
        client = build_anthropic_client()
    except ProviderError as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)

    # Defaults to False for backward compatibility with generation files that
    # predate the require_format_tags field.
    format_required = generation.get("require_format_tags", False)

    result = []
    for lang_block in generation["result"]:
        # A --problems file that doesn't exactly match --generation (stale
        # file, renamed/missing language, idx mismatch) must not take down
        # every already-completed language's findings and billed inspector
        # calls. Validate the per-language shape up front and skip just this
        # language on failure, rather than letting a KeyError propagate.
        try:
            lang = lang_block["language"]
            if lang not in problems_by_lang:
                raise KeyError(f"language {lang!r} not present in --problems file")
            problems_by_idx = {p["idx"]: p for p in problems_by_lang[lang]}
            solutions = lang_block["generation"]["solutions"]
        except KeyError as e:
            print(
                f"warning: skipping language due to problems/generation mismatch: {e}",
                file=sys.stderr,
            )
            continue

        findings: list[dict] = []
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = {}
            for sol in solutions:
                try:
                    idx = sol["idx"]
                    raw_output = sol["raw_output"]
                    problem = problems_by_idx[idx]
                except KeyError as e:
                    findings.append(
                        _fallback_finding(
                            {"idx": sol.get("idx", -1), "answer_number": None},
                            KeyError(
                                f"malformed solution or missing problem mapping "
                                f"for language {lang!r}: {e}"
                            ),
                        )
                    )
                    continue
                futures[
                    executor.submit(
                        inspect_one, client, lang, problem, raw_output, format_required
                    )
                ] = problem

            for future in tqdm(
                as_completed(futures), total=len(futures), desc=f"[{lang}] inspecting"
            ):
                problem = futures[future]
                try:
                    findings.append(future.result())
                except Exception as e:  # noqa: BLE001 - one bad call shouldn't abort the batch
                    findings.append(_fallback_finding(problem, e))

        findings.sort(key=lambda f: f["idx"])
        try:
            overall_summary = summarize_language(client, findings)
        except Exception as e:  # noqa: BLE001 - a summary failure shouldn't abort the run
            overall_summary = f"[SUMMARY_ERROR] {type(e).__name__}: {e}"

        result.append(
            {
                "language": lang,
                "generation": lang_block["generation"],
                "inspection": {"findings": findings, "overall_summary": overall_summary},
            }
        )

    output = {
        "summary": (
            f"{generation.get('summary', 'Generation run')} | Inspected with fixed inspector "
            f"{INSPECTOR_MODEL} (Claude Sonnet 5), independent of the generation provider/model."
        ),
        "provider": generation.get("provider"),
        "model": generation.get("model"),
        "result": result,
    }

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"Wrote inspection output to {out_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
