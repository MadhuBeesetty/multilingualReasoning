# Project Overview: Multilingual Structural Reasoning Failures

**TL;DR**: Investigating why multilingual LLMs fail on multi-step math reasoning when reasoning crosses language boundaries. Pilot confirmed a real, reproducible "Compositional Collapse" failure mode across 22 diverse problems in 7 languages. Now ramping up to test real independent models via API calls instead of self-grading.

---

## What This Project Is

A research effort to identify and characterize structural reasoning failures in multilingual math problem solving. The focus is on **generative, multi-step reasoning chains** — specifically, whether a model loses its problem structure partway through when reasoning in languages other than English.

**Key differentiator from prior work:**
- **SWATH** (Ranaldi & Pucci, NAACL 2025, the anchor paper) measures cross-lingual answer *consistency* at the top-level, but doesn't inspect intermediate steps
- **Beg to Differ** (Ovalle et al., Meta/FAIR) checks reasoning-answer alignment on MCQ tasks at massive scale (65k traces) but can't see step-wise degradation in open-ended generative chains
- **This project** specifically tests whether structured reasoning collapses *during* the generation of a multi-step chain when crossing a language boundary — the blind spot both prior works have

---

## The Core Finding (Validated, Reproducible)

**Compositional Collapse** — A model notices or *invents* a required structural sub-part of a multi-part problem, then **drops or misapplies it wholesale** (not a gradual slip). 

**Evidence:**
- Confirmed across **22 distinct problems** in 4 independent pilot designs
- **5 languages tested so far**: Chinese (zh), Thai (th), Japanese (ja), Spanish (es), German (de), plus Bengali (bn) and Telugu (te) added for format-stress testing
- **110 language-instances total** across 4 pilot rounds
- Every failure shows the same shape: model engages with or constructs a structural clause, then reasons it away entirely or applies it wrong from the start — never a slip that *develops gradually* mid-chain
- **Cleanest example** (Round 1): wind-halving in a rate-change problem. Model explicitly notices "wind speed halves after 60 minutes," then explicitly reasons: "this info doesn't affect this calculation" and solves with a single flat rate instead of splitting the distance into pre/post-60-min segments

---

## Two Real Negative Findings (Not Absence of Data)

Both were tested using templates *specifically designed* to elicit the failure mode:

### Reasoning Drift — NOT FOUND
- **Template**: 5-stage popcorn-popping-rate chain where each stage's count depends on the prior stage's rate (round 3a)
- **Result**: Solved perfectly **10/10 across all languages**, no errors of any kind
- **Implication**: Either this failure shape doesn't occur for frontier models like Claude Sonnet 5, or it requires weaker target models or messier chains

### Format Instability — NOT FOUND
- **Template**: Strict SWATH-style tag requirement (`<formalisation>...</formalisation><reasoning>...</reasoning><answer>...</answer>`) across 5 scripts including complex abugida scripts (Bengali, Telugu)
- **Result**: **10/10 well-formed**, all tags present, correctly ordered, no encoding corruption, no truncation
- **Implication**: Format breaking under structural demands is not a real failure mode at this scale

---

## Key Methodological Discovery (Confound Alert)

**The mGSM-Symbolic benchmark's own machine translation has language/template-specific failures** that corrupt the source problems before any model ever sees them:

Examples found in Round 2:
- **German & Thai (idx 220/221)**: multiplier problem — both translations omit the 5× multiplier entirely. German reads "*Friday he picks the same amount as Wednesday*" (no multiplier clause), while Spanish/Japanese preserved it. Model answers are *correct readings of corrupted text*.
- **Chinese (idx 141)**: apartment vacancy problem — MT converts "8 apartments vacant per building" into "**every** apartment vacant" — a different meaning entirely

**Why this matters**: Any cross-lingual accuracy comparison on this dataset (or similar MT-generated multilingual benchmarks) risks conflating *model reasoning failure* with *benchmark translation failure*. This is the same concern Beg to Differ flagged about their own back-translation QC.

---

## Current Limitation (Being Fixed)

Every pilot result so far used **Claude Sonnet 5 as both the model-under-test AND the inspector** grading its own output — a self-grading loop with inherent blind spots.

**What's next**: Real target models via actual API calls, keeping the inspector (Sonnet 5) fixed so *only the generator varies*. This lets us see whether Drift/Format Instability are genuinely absent or just invisible to frontier models.

---

## Repo Structure

```
PLAN.md                    # working plan, status, next steps (primary source of truth)
README.md                  # project overview (this file is more detailed)
requirements.txt           # Python dependencies
code/
  providers.py             # API abstraction (Anthropic, OpenRouter, Ollama)
  run_inference.py         # generate solutions against a target model
  run_inference_ollama.py  # dedicated entry point for offline Ollama
  inspect_traces.py        # grade the traces using fixed inspector (Sonnet 5)
  README.md                # detailed usage & environment setup
data/mgsm_symbolic/
  mgsm_symbolic_{lang}.csv # real mGSM-Symbolic data (7 languages: zh, th, ja, es, de, bn, te)
  pilot_round*_*.json      # exact problem sets used per pilot round (4 rounds, 22 total problems)
  raw_pilot_outputs/       # full raw model output backing PILOT_FINDINGS.md
    round1_fogbank_raw.json
    round2_diverse_templates_raw.json
    round3a_drift_test_raw.json
    round3b_format_test_raw.json
  PILOT_FINDINGS.md        # curated findings writeup (full evidence)

_archive/                  # old superseded plan (broken data pipeline, fabricated results)
                           # kept locally for reference, not in version control
```

---

## Data Source & Attribution

**mGSM-Symbolic**: Multi-language, multi-script collection of grade-school-level symbolic math problems.
- **Source**: HuggingFace `lrana/MGSM-Symbolic` (CC-BY-SA 4.0)
- **Code**: GitHub `lranaldii/MGSM-Symbolic`
- **Released with**: NAACL 2025 paper "Multilingual Reasoning via Self-training" (SWATH) by Ranaldi & Pucci
- **License**: CC-BY-SA 4.0 — data files in this repo retain original terms

---

## The Workflow (Two-Step Pipeline)

All experiments follow this pattern:

```bash
# Step 1: Generate solutions with a target model
python run_inference.py \
  --problems ../data/mgsm_symbolic/pilot_round1_fogbank_problems.json \
  --provider openrouter --model meta-llama/llama-3-8b-instruct \
  --out ../data/mgsm_symbolic/raw_pilot_outputs/round1_llama3-8b_generation.json

# Step 2: Grade the traces using fixed inspector (Claude Sonnet 5)
python inspect_traces.py \
  --generation ../data/mgsm_symbolic/raw_pilot_outputs/round1_llama3-8b_generation.json \
  --problems ../data/mgsm_symbolic/pilot_round1_fogbank_problems.json \
  --out ../data/mgsm_symbolic/raw_pilot_outputs/round1_llama3-8b_full.json
```

**Free option**: Use Ollama for generation (no API cost, runs locally), then pay only for the fixed Sonnet 5 inspector pass:

```bash
python run_inference_ollama.py --problems ... --out ...
python inspect_traces.py --generation ... --problems ... --out ...
```

---

## Next Steps (From PLAN.md)

1. **Test real target models via actual API calls** — re-run the 4 pilot problem sets against independently-hosted models (Llama-3-8B, Phi-3.5-mini, DeepSeek-7B — same targets as SWATH itself tests). Keep Sonnet 5 as fixed inspector.

2. **Build a translation-fidelity checker** — before attributing any failure to model reasoning, verify the source-language problem text actually contains the same load-bearing clauses as English.

3. **Self-annotate a real sample** (~100–200 problems) once target models are chosen — no need to hire external annotators at this scale.

4. **Write a short paper** (4 pages) once findings are solid — positioned as a structural complement to SWATH, explicitly differentiated from Beg to Differ's MCQ-based lens.

5. **Submit** to an appropriate venue once ready. ORACLE (EMNLP 2026 workshop organized by SWATH's authors) is a natural fit, but no fixed deadline — building this properly first.

---

## Important Notes for Future Work

- **Don't trust old memory/docs**: The original 6-category taxonomy, 7-week plan, and hired-annotator budget ($2,830) are archived and superseded. The real current state lives in `PLAN.md` and `PILOT_FINDINGS.md`.

- **The anchor paper summary is incomplete**: The local `.docx` copy of SWATH is a ~7,500-character secondhand brainstorm, not the actual paper. Any claim about specific models, benchmarks, or methodology from SWATH needs verification against the published paper itself.

- **One model as both generator and inspector is a known limitation**, not a feature — results are robust, but independent models still need to be tested to rule out self-grading blind spots.

---

## Contact & Status

- **Status**: Early-stage research, real findings, not yet submitted anywhere
- **No fixed deadline** — moving at a pace that allows proper methodology
- **GitHub**: https://github.com/MadhuBeesetty/multilingualReasoning (pushed 2026-08-05)
- **License**: Data files CC-BY-SA 4.0 (MGSM-Symbolic source); code license TBD
