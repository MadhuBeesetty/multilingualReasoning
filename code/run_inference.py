#!/usr/bin/env python3
"""Blind generation pass: call the model-under-test on each problem in a
pilot_round*_problems.json file and record its raw output.

No answer extraction, no taxonomy judgments happen here — that is entirely
the job of inspect_traces.py. This script only ever asks the model to solve
the problem naturally, with zero mention of the failure taxonomy being
studied.

Usage:
    python run_inference.py --problems ../data/mgsm_symbolic/pilot_round1_fogbank_problems.json \\
        --provider openrouter --model meta-llama/llama-3-8b-instruct \\
        --out ../data/mgsm_symbolic/raw_pilot_outputs/round1_llama3-8b_generation.json
"""

from __future__ import annotations

import argparse
import json
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Optional

from tqdm import tqdm

from providers import Provider, ProviderError, get_provider

# ---------------------------------------------------------------------------
# Prompt construction
# ---------------------------------------------------------------------------

_BASE_SYSTEM_PROMPT = (
    "You will be given a math word problem. It may be written in a language "
    "other than English. Solve it as a real user would expect: read the "
    "problem carefully, work through it, and respond in the same language "
    "the problem is written in. State your final numeric answer clearly "
    "at the end of your response."
)

# Only used when --require-format-tags is set (round-3b-style runs). Mirrors
# the exact <formalisation>/<reasoning>/<answer> tag and "Step N: ..." shape
# observed in the existing round3b_format_test_raw.json pilot output.
#
# Design note: this structural instruction is given in English even though
# the problem itself is in the target language. That's a deliberate
# simplification (avoids maintaining ~7 localized instruction strings), not
# an oversight — it can be swapped for a localized version later without
# touching any other part of the pipeline.
_FORMAT_TAGS_SUFFIX = (
    "\n\nRespond using exactly this structure, with no text outside the tags:\n"
    "<formalisation>Restate the key facts of the problem in your own words.</formalisation>\n"
    "<reasoning>Step 1: ...\nStep 2: ...\n(continue as needed)</reasoning>\n"
    "<answer>Your final numeric answer only.</answer>"
)


def build_system_prompt(require_format_tags: bool) -> str:
    if require_format_tags:
        return _BASE_SYSTEM_PROMPT + _FORMAT_TAGS_SUFFIX
    return _BASE_SYSTEM_PROMPT


# ---------------------------------------------------------------------------
# Per-problem / per-language workers
# ---------------------------------------------------------------------------


def solve_one(provider: Provider, system_prompt: str, idx: int, question: str) -> dict:
    """Call the provider for one problem. Never raises — a failed generation
    is recorded inline as an error marker so one bad call can't abort the
    batch."""
    try:
        raw_output = provider.generate(system_prompt, question)
    except Exception as e:  # noqa: BLE001 - deliberately broad, see docstring
        raw_output = f"[GENERATION_ERROR] {type(e).__name__}: {e}"
    return {"idx": idx, "raw_output": raw_output}


def run_language(
    provider: Provider,
    system_prompt: str,
    lang: str,
    problems: list[dict],
    workers: int,
) -> dict:
    solutions: list[dict] = []
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(solve_one, provider, system_prompt, p["idx"], p["question"]): p
            for p in problems
        }
        for future in tqdm(
            as_completed(futures), total=len(futures), desc=f"[{lang}] generating"
        ):
            solutions.append(future.result())

    solutions.sort(key=lambda s: s["idx"])
    return {"language": lang, "generation": {"solutions": solutions}}


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def parse_args(argv: Optional[list] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run blind generation against a real model-under-test."
    )
    parser.add_argument(
        "--problems", required=True, help="Path to a pilot_round*_problems.json file"
    )
    parser.add_argument(
        "--provider", required=True, choices=["anthropic", "openrouter"]
    )
    parser.add_argument(
        "--model", required=True, help="Model id for the chosen provider"
    )
    parser.add_argument("--out", required=True, help="Path to write the generation JSON")
    parser.add_argument(
        "--require-format-tags",
        action="store_true",
        default=False,
        help=(
            "Add the <formalisation>/<reasoning>/<answer> structural "
            "requirement to the generation prompt. Only use this with "
            "round3b-style (format_problems.json) runs. Off by default."
        ),
    )
    parser.add_argument(
        "--base-url",
        default=None,
        help="Override the API base URL (only meaningful with --provider openrouter)",
    )
    parser.add_argument(
        "--workers", type=int, default=5, help="Thread-pool size for concurrent calls"
    )
    return parser.parse_args(argv)


def main() -> None:
    args = parse_args()

    problems_by_lang = json.loads(Path(args.problems).read_text(encoding="utf-8"))

    provider_kwargs = {}
    if args.base_url is not None and args.provider == "openrouter":
        provider_kwargs["base_url"] = args.base_url

    try:
        provider = get_provider(args.provider, args.model, **provider_kwargs)
    except ProviderError as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)

    system_prompt = build_system_prompt(args.require_format_tags)

    results = []
    for lang, problems in problems_by_lang.items():
        results.append(run_language(provider, system_prompt, lang, problems, args.workers))

    summary = (
        f"Blind generation run: provider={args.provider}, model={args.model}, "
        f"problems_file={args.problems}, require_format_tags={args.require_format_tags}"
    )
    output = {
        "summary": summary,
        "provider": args.provider,
        "model": args.model,
        "require_format_tags": args.require_format_tags,
        "result": results,
    }

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"Wrote generation output to {out_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
