#!/usr/bin/env python3
"""Build pilot problem JSON files for the backfill languages (it, fr, ru, sw).

For each existing pilot round file, reuses the same problem indices but loads
questions/answers from the per-language MGSM-Symbolic CSV files.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

DATA_DIR = Path("data/mgsm_symbolic")
NEW_LANGS = ("it", "fr", "ru", "sw")

ROUNDS = (
    ("1", "fogbank"),
    ("2", "diverse"),
    ("3a", "drift"),
    ("3b", "format"),
)


def load_csv_rows(lang: str) -> list[dict[str, str]]:
    csv_path = DATA_DIR / f"mgsm_symbolic_{lang}.csv"
    with csv_path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def collect_indices(source: dict) -> list[int]:
    idxs: set[int] = set()
    for problems in source.values():
        for problem in problems:
            idxs.add(int(problem["idx"]))
    return sorted(idxs)


def build_newlangs_file(round_num: str, round_name: str) -> None:
    source_path = DATA_DIR / f"pilot_round{round_num}_{round_name}_problems.json"
    out_path = DATA_DIR / f"pilot_round{round_num}_{round_name}_newlangs_problems.json"

    source = json.loads(source_path.read_text(encoding="utf-8"))
    idxs = collect_indices(source)

    csv_by_lang = {lang: load_csv_rows(lang) for lang in NEW_LANGS}
    out: dict[str, list[dict[str, str | int]]] = {}

    for lang in NEW_LANGS:
        rows = csv_by_lang[lang]
        out[lang] = []
        for idx in idxs:
            if idx >= len(rows):
                raise IndexError(
                    f"{lang}: idx {idx} out of range (csv has {len(rows)} rows)"
                )
            row = rows[idx]
            out[lang].append(
                {
                    "idx": idx,
                    "question": row["question"],
                    "answer_number": row["answer_number"],
                }
            )

    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {out_path} ({len(idxs)} problems × {len(NEW_LANGS)} languages)")


def main() -> None:
    for round_num, round_name in ROUNDS:
        build_newlangs_file(round_num, round_name)


if __name__ == "__main__":
    main()
