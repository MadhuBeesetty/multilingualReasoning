# Plan: Multilingual Structural Reasoning Failures

**Status**: Early pilot confirmed real signal. Not yet a paper. No fixed deadline — building this properly, submitting when ready.

## The idea

Existing multilingual reasoning diagnostics either check whether a model's *finished* answer is logically supported by its reasoning on multiple-choice tasks (Beg to Differ, Meta/FAIR, arXiv:2512.22712), or measure cross-lingual answer *consistency* without inspecting intermediate steps (SWATH / Ranaldi & Pucci, NAACL 2025, arXiv anchor paper — this project's original inspiration). Neither can see whether a **generative, multi-step reasoning chain** loses its structure partway through when reasoning crosses a language boundary.

**Working focus** (narrowed twice now — first from an original 6-category taxonomy, then again after 4 pilot rounds):
1. **Compositional Collapse** — reasoning drops or misapplies a required sub-part of a multi-part problem. **Confirmed real, reproducible, and so far the *only* failure mode observed** — across 20 real problems, 3 distinct problem designs, and 5 languages. See `data/mgsm_symbolic/PILOT_FINDINGS.md`.
2. **Reasoning Drift** — early steps correct, later steps cascade into error. **Tested with a template built specifically to elicit it (a clean 5-stage dependency chain) and NOT found** — solved perfectly 10/10 across every language. Real negative result, not absence of data.
3. **Format Instability** — output structure breaks under a structural demand. **Tested under a strict SWATH-style tag requirement across 5 scripts (including two never tried before, Bengali and Telugu) and NOT found** — held up perfectly 10/10.

Script Bias was dropped as a headline claim — Beg to Differ already showed this at much larger scale (65k traces, Meta/FAIR). Cross-lingual Retrieval Failure was dropped — out of scope for closed-book math tasks.

**Current read**: this is looking less like "three categories to build a taxonomy around" and more like one solid, well-evidenced finding (Compositional Collapse) plus two informative negative results that may be specific to testing against a frontier model (Claude Sonnet 5) rather than the weaker open models the anchor paper (SWATH) actually targets.

## Why this is real (not just a hypothesis)

A $0, no-API-key pilot (Claude Sonnet 5 solving real problems blind, then a separate pass checking for failure evidence) on the publicly released `mGSM-Symbolic` dataset found:
- A clean, textually-evidenced Compositional Collapse pattern, reproduced across 3 independent problem designs: the model *notices or invents* a required structural piece, then either *reasons it away* or *misapplies it wholesale from the start* — never a slip that develops gradually.
- A genuine second finding: the benchmark's own machine translation sometimes drops the load-bearing clause in specific language/template combinations, which would be misread as "model failure" if not traced back to the source text. This is a real, citable methodological point in its own right.
- Two clean negative results (Drift, Format Instability) obtained by specifically designing tests meant to elicit them — not just failing to look.

Full details: `data/mgsm_symbolic/PILOT_FINDINGS.md`.

## What's in this folder

- `data/mgsm_symbolic/` — real, public MGSM-Symbolic data (7 languages downloaded so far: zh, th, ja, es, de, bn, te), the pilot problem sets, the raw generation+inspection output backing every claim (`raw_pilot_outputs/`), and the curated findings writeup (`PILOT_FINDINGS.md`).
- `code/` — empty for now. Next real code needed: a translation-fidelity checker and a real-model inference script (see below).
- `requirements.txt` — Python deps for the next phase (Anthropic/OpenAI-compatible API clients, data/analysis stack).

**Gitignored, present locally but not in version control:**
- `Multilingual Reasoning via Self.docx` — source copy of the anchor paper (Ranaldi & Pucci, "Multilingual Reasoning via Self-training", NAACL 2025). Third-party copyrighted material — kept locally for reference, cite via the published paper rather than redistributing this file.
- `_archive/` — everything from the first planning pass (7-week/6-category/4-model plan). Kept locally for reference, not in use — it assumed datasets and inference pipelines that turned out to be broken or fabricated, and a paper novelty position that didn't hold up once the real competing literature was checked. Not deleted, just left out of the fresh repo.

## Next steps (in order, no fixed dates)

1. **Test real target models via actual API calls** — the $0 self-testing loop (Claude Sonnet 5 solving its own problems, then grading itself) has now given a clear, stable signal (Compositional Collapse only) and two real negative results; further self-pilots have diminishing returns, since generator and inspector being the same model can't rule out a self-grading blind spot. API budget is now available. Re-run the same problem sets (`pilot_round*_*.json`) against an independently-hosted model — keep Sonnet 5 as the fixed inspector so only the generator varies. SWATH's own paper tests Llama-3-8B, Phi-3.5-mini, DeepSeek-7B — good candidates, and worth re-testing Drift/Format Instability there too, since a weaker model may show what a frontier model doesn't.
2. **Build a lightweight translation-fidelity check** — before counting anything as a model failure, verify the source-language problem text actually contains the same load-bearing clauses as English. Cheap, and now known to be necessary.
3. **Self-annotate a real sample** (~100-200 problems) once target models are chosen — no need to hire annotators at this scale.
4. **Write a short paper** (4 pages) once findings are solid — positioned as a structural complement to SWATH, explicitly differentiated from Beg to Differ's MCQ-based lens. Likely framing: Compositional Collapse as the core finding, with the Drift/Format-Instability negative results and the translation-fidelity confound as supporting methodological contributions.
5. **Submit** to whatever the next realistic open venue is once it's actually ready. (ORACLE — the EMNLP 2026 workshop organized by the SWATH authors — is a natural fit if a future cycle's timing works out; not chasing its Aug 2026 deadline, which passed too fast to reach given other commitments.)
