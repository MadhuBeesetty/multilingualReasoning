# Human Review Evaluation Packets

This directory contains human verification protocols and questionnaires across 9 languages for validating AI chain-of-thought (CoT) reasoning traces against ground truth.

## Purpose

These review sheets are designed for native and fluent bilingual speakers to evaluate model reasoning traces on mathematical word problems from the `mGSM-Symbolic` benchmark.

The core question each review evaluates is **Compositional Collapse**:
> Did the model explicitly notice or state a key structural detail (e.g., a rate change, a quantity to exclude, or a piecewise condition), but then drop or misuse it in a subsequent reasoning step, rather than misunderstanding the problem from the beginning?

## Language Packets

- [`review_de.md`](review_de.md) — German
- [`review_es.md`](review_es.md) — Spanish
- [`review_fr.md`](review_fr.md) — French
- [`review_it.md`](review_it.md) — Italian
- [`review_ja.md`](review_ja.md) — Japanese
- [`review_ru.md`](review_ru.md) — Russian
- [`review_sw.md`](review_sw.md) — Swahili
- [`review_th.md`](review_th.md) — Thai
- [`review_zh.md`](review_zh.md) — Chinese

Each packet includes the question, expected ground-truth answer, model trace, and evaluation rubric (Yes / No / Not sure).
