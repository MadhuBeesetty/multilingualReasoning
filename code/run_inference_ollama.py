#!/usr/bin/env python3
"""Dedicated, Ollama-only entry point for the blind generation pass.

This is a thin wrapper: it reuses build_system_prompt() and run_language()
from run_inference.py and the "ollama" provider from providers.py rather than
duplicating that logic. It exists so running a fully local, offline
model-under-test doesn't require remembering --provider/--base-url flags on
the generic multi-provider CLI — just point it at a problems file.

No API key, no spend — this only talks to a local Ollama server. (The
downstream inspect_traces.py step still calls the real Anthropic API for the
fixed inspector; that part is unchanged and not free.)

Usage:
    python run_inference_ollama.py \\
        --problems ../data/mgsm_symbolic/pilot_round1_fogbank_problems.json \\
        --out ../data/mgsm_symbolic/raw_pilot_outputs/round1_deepseek-r1-14b_generation.json
    # defaults to model deepseek-r1:14b against http://localhost:11434/v1
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Optional

from providers import OLLAMA_DEFAULT_BASE_URL, ProviderError, get_provider
from run_inference import build_system_prompt, run_language

DEFAULT_OLLAMA_MODEL = "deepseek-r1:14b"


def parse_args(argv: Optional[list] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run blind generation against a local Ollama model-under-test."
    )
    parser.add_argument(
        "--problems", required=True, help="Path to a pilot_round*_problems.json file"
    )
    parser.add_argument("--out", required=True, help="Path to write the generation JSON")
    parser.add_argument(
        "--model",
        default=DEFAULT_OLLAMA_MODEL,
        help=f"Ollama model tag, must already be pulled via `ollama pull` (default: {DEFAULT_OLLAMA_MODEL})",
    )
    parser.add_argument(
        "--base-url",
        default=OLLAMA_DEFAULT_BASE_URL,
        help=f"Ollama server URL (default: {OLLAMA_DEFAULT_BASE_URL})",
    )
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
        "--workers", type=int, default=5, help="Thread-pool size for concurrent calls"
    )
    return parser.parse_args(argv)


def main() -> None:
    args = parse_args()

    problems_by_lang = json.loads(Path(args.problems).read_text(encoding="utf-8"))

    try:
        provider = get_provider("ollama", args.model, base_url=args.base_url)
    except ProviderError as e:
        print(f"error: {e}", file=sys.stderr)
        print(
            "Is Ollama running (`ollama serve`) and is the model pulled "
            f"(`ollama pull {args.model}`)?",
            file=sys.stderr,
        )
        sys.exit(1)

    system_prompt = build_system_prompt(args.require_format_tags)

    results = []
    for lang, problems in problems_by_lang.items():
        results.append(run_language(provider, system_prompt, lang, problems, args.workers))

    summary = (
        f"Blind generation run (Ollama, local/offline): model={args.model}, "
        f"base_url={args.base_url}, problems_file={args.problems}, "
        f"require_format_tags={args.require_format_tags}"
    )
    output = {
        "summary": summary,
        "provider": "ollama",
        "model": args.model,
        "base_url": args.base_url,
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
