# Multilingual Structural Reasoning Failures

Investigating structural reasoning failures in multilingual LLM chain-of-thought — pilot evidence for a reproducible "Compositional Collapse" mode on the public mGSM-Symbolic benchmark.

**Status: early-stage research.** Pilot findings are real and reproducible, but this is not yet a paper. See [`PLAN.md`](PLAN.md) for the full working plan and current status.

## The idea

Existing multilingual reasoning diagnostics either check whether a model's *finished* answer is logically supported by its reasoning on multiple-choice tasks ("Beg to Differ," Ovalle et
 al., Meta/FAIR), or measure cross-lingual answer *consistency* without inspecting intermediate steps (SWATH — Ranaldi & Pucci, NAACL 2025, the anchor paper for this project). Neither c
an see whether a **generative, multi-step reasoning chain** loses its structure partway through when reasoning crosses a language boundary. That gap is what this project tests.

## What's been found so far

A $0 pilot (Claude Sonnet 5 solving real problems blind, then a separate pass inspecting the traces against ground truth) on the publicly released `mGSM-Symbolic` dataset, across 22 dis
tinct problems and 4 independent test designs:

- **Compositional Collapse — confirmed, reproducible, and so far the only failure mode observed.** The model notices or invents a required structural piece of a multi-part problem, then
 drops or misapplies it wholesale — never a slip that develops gradually.
- **Reasoning Drift — tested with a template built specifically to elicit it, and not found.** Solved perfectly across every language tried.
- **Format Instability — tested under a strict structural output requirement across 5 scripts (including Bengali and Telugu), and not found.**
- **A methodological side-finding**: the benchmark's own machine translation sometimes drops load-bearing clauses in specific language/template pairs — a confound that has to be ruled o
ut before attributing any accuracy gap to model reasoning.

Full writeup with per-language tables and quoted evidence: [`data/mgsm_symbolic/PILOT_FINDINGS.md`](data/mgsm_symbolic/PILOT_FINDINGS.md). Raw generation + inspection output backing eve
ry claim: [`data/mgsm_symbolic/raw_pilot_outputs/`](data/mgsm_symbolic/raw_pilot_outputs/).

**Current limitation**: every result above used one model (Claude Sonnet 5) as both the generator and the inspector grading its own output. The next phase re-runs the same problem sets
against independently-hosted target models via real API calls, holding the inspector fixed so only the generator varies.

## Repo layout

```
PLAN.md                          # working plan, status, next steps
requirements.txt                 # Python deps
code/                            # analysis/inference scripts (empty for now)
data/mgsm_symbolic/
  mgsm_symbolic_{lang}.csv       # real mGSM-Symbolic data, 7 languages
  pilot_round*_*.json            # exact problem sets used per pilot round
  raw_pilot_outputs/*.json       # full raw model output backing PILOT_FINDINGS.md
  PILOT_FINDINGS.md              # curated findings writeup
```
- _archive/ — old broken/superseded plan, stays local only
- Multilingual Reasoning via Self.docx — copyrighted paper copy, stays local only
- .claude/ — Claude Code's local settings, not project content

Simplest way to do the move: copy the whole multilingualReasoning folder to its new location, cd in, git init, then git add PLAN.md requirements.txt code/ data/ (explicitly, not git add .) so you don't accidentally stage _archive/ or the .docx even though .gitignore should already block them. Want me to walk through the actual git init + first commit once you've made the copy?

✻ Cogitated for 9s

❯ give me a github description for this files

GitHub "About" description (one-liner):

▎ Investigating structural reasoning failures in multilingual LLM chain-of-thought — pilot evidence for a reproducible "Compositional Collapse" mode on the public mGSM-Symbolic benchmark.

Alternative, slightly more detailed:

▎ Early-stage research on how multi-step LLM reasoning degrades across languages. Built on Ranaldi & Pucci's mGSM-Symbolic dataset (NAACL 2025); pilot data shows a reproducible "Compositional
▎ Collapse" failure and rules out reasoning drift and format instability under targete

Suggested topics/tags (GitHub repo topics field, for discoverability):
llm, multilingual-nlp, reasoning, chain-of-thought, llm-evaluation, nlp-research

Want me to also draft a short opening paragraph for a README.md (separate from PLAN.md), or is the repo description alone enough for now?

✻ Cogitated for 12s

❯ yes give me read me also

⏺ Write(/Users/mbeesetty/Documents/AI-paper-research/multilingualReasoning/README.md)

Wrote 43 lines to /Users/mbeesetty/Documents/AI-paper-research/multilingualReasoning/README.md
# Multilingual Structural Reasoning Failures

Investigating structural reasoning failures in multilingual LLM chain-of-thought — pilot evidence for a reproducible "Compositional Collapse" mode on the public mGSM-Symbolic benchmark.

**Status: early-stage research.** Pilot findings are real and reproducible, butSee [`PLAN.md`](PLAN.md) for the full working plan and current status.

## The idea

Existing multilingual reasoning diagnostics either check whether a model's *finished* answer is logically supported by its reasoning on multiple-choice tasks ("Beg to Differ," Ovalle et
 al., Meta/FAIR), or measure cross-lingual answer *consistency* without inspecting intermediate steps (SWATH — Ranaldi & Pucci, NAACL 2025, the anchor paper for this project). Neither c
an see whether a **generative, multi-step reasoning chain** loses its structureoning crosses a language boundary. That gap is what this project tests.

## What's been found so far

A $0 pilot (Claude Sonnet 5 solving real problems blind, then a separate pass inspecting the traces against ground truth) on the publicly released `mGSM-Symbolic` dataset, across 22 dis
tinct problems and 4 independent test designs:

- **Compositional Collapse — confirmed, reproducible, and so far the only failure mode observed.** The model notices or invents a required structural piece of a multi-part problem, then
 drops or misapplies it wholesale — never a slip that develops gradually.
- **Reasoning Drift — tested with a template built specifically to elicit it, and not found.** Solved perfectly across every language tried.
- **Format Instability — tested under a strict structural output requirement acBengali and Telugu), and not found.**
- **A methodological side-finding**: the benchmark's own machine translation so clauses in specific language/template pairs — a confound that has to be ruled o
ut before attributing any accuracy gap to model reasoning.

Full writeup with per-language tables and quoted evidence: [`data/mgsm_symbolic/PILOT_FINDINGS.md`](data/mgsm_symbolic/PILOT_FINDINGS.md). Raw generation + inspection output backing eve
ry claim: [`data/mgsm_symbolic/raw_pilot_outputs/`](data/mgsm_symbolic/raw_pilo

**Current limitation**: every result above used one model (Claude Sonnet 5) as both the generator and the inspector grading its own output. The next phase re-runs the same problem sets
against independently-hosted target models via real API calls, holding the inspector fixed so only the generator varies.

## Repo layout

```
PLAN.md                          # working plan, status, next steps
requirements.txt                 # Python deps
code/                            # analysis/inference scripts (empty for now)
data/mgsm_symbolic/
  mgsm_symbolic_{lang}.csv       # real mGSM-Symbolic data, 7 languages
  pilot_round*_*.json            # exact problem sets used per pilot round
  raw_pilot_outputs/*.json       # full raw model output backing PILOT_FINDINGS.md
  PILOT_FINDINGS.md              # curated findings writeup
```

## Data & attribution

Problems are from `mGSM-Symbolic` (HuggingFace: `lrana/MGSM-Symbolic`, CC-BY-SA 4.0; code: `lranaldii/MGSM-Symbolic` on GitHub), released alongside Ranaldi & Pucci's "Multilingual Reaso
ning via Self-training" (SWATH), NAACL 2025. Redistributed data files here reta.0 license — attribute the source dataset/paper if you reuse them.

## License

Not yet decided for the code/analysis in this repo — data files carry their own CC-BY-SA 4.0 terms as noted above.
