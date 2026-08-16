# Pilot Findings — mGSM-Symbolic, Multilingual Structural Reasoning Failures

**Raw data**: full generation + inspection output for all 4 rounds (every language, every problem, complete native-language reasoning traces + English glosses + inspection verdicts) is in `raw_pilot_outputs/` alongside this file — this document is a curated summary, not the primary source.

**Method**: Claude Sonnet 5 (this assistant) solved real problems blind — no awareness of any taxonomy, just "solve this like a normal user asked." A separate pass then inspected the traces against ground truth for four failure modes. $0 cost, no API keys, using the publicly released `lrana/MGSM-Symbolic` dataset (HuggingFace, CC-BY-SA 4.0; code: `lranaldii/MGSM-Symbolic` on GitHub) from Ranaldi & Pucci's NAACL 2025 "Multilingual Reasoning via Self-training" (SWATH) paper.

**Caveat before anything else**: this used one model (Claude Sonnet 5) as both the model under test *and* the inspector grading its own output, one sample per problem (no repeated sampling), and 22 distinct problems across 4 pilot rounds (110 language-instances total: 5 languages — zh, th, ja, es, de — in rounds 1–3a, plus bn/te added in round 3b). It is a sanity-check pilot, not a finished experiment. Real target models tested via actual API calls (e.g. the open models SWATH itself tests — Llama-3-8B, Phi-3.5-mini, DeepSeek-7B) still need to be tried, with the inspector held constant so only the generator varies.

---

## Round 1 — "fog bank" rate-change problem (8 instances, same template, zh/th/ja/es/de)

Problem requires: compute an initial rate → recognize wind speed halves after 60 minutes → split the distance into a pre-60-min segment (original rate) and post-60-min segment (halved rate) → sum. A classic multi-part compositional trap.

| Language | Correct |
|---|---|
| Chinese | 0/8 |
| Thai | 0/8 |
| Japanese | 0/8 |
| Spanish | 0/8 |
| German | 8/8 |

**Finding — genuine Compositional Collapse, well-evidenced**: every failing trace *explicitly notices* the wind-halving clause, then *explicitly reasons it away* ("the wind-speed-halving info doesn't affect this calculation; solve directly with the initial rate") and computes a flat single-rate proportion instead. This is not a translation artifact — the model engages with the clause in its own reasoning before discarding it. This is the cleanest, most defensible finding so far.

The language split here is **not** a stable ranking (see round 2) — it's specific to this template's phrasing.

---

## Round 2 — 4 different problem types (8 instances: 2 variants × 4 templates, zh/th/ja/es/de)

Templates: (a) apartment garbage collection with vacancy adjustment + tip %, (b) sequential day-by-day fruit picking with a multiplier day, (c) whale/remora fraction + percentage averaging, (d) overlapping-group class percentages with absentee adjustment.

| Language | Correct (of 7, excluding idx=300 — likely an answer-key rounding artifact, not a reasoning failure) |
|---|---|
| Japanese | 7/7 |
| Spanish | 7/7 |
| German | 5/7 |
| Chinese | 4/7 |
| Thai | 3/7 |

**The ranking flipped completely from round 1** — confirms Compositional Collapse is template-dependent, not a fixed per-language weakness.

### Critical methodological catch: translation-fidelity confound

Traced several "failures" back to the raw source text and found the benchmark's own machine translation (GPT-4o, per SWATH's paper) sometimes **drops the load-bearing clause**, independent of any model behavior:

- **German & Thai, idx 220/221** (fruit-picking multiplier problem): both translations omit the multiplier entirely — German reads "*Friday he picks the same amount as Wednesday*" with no "5×" anywhere, when Spanish/Japanese preserved it (as an untranslated "Quintuple" loanword) and Chinese preserved it via a "quintet" metaphor. The model's answer is a **faithful, correct reading of the actual (corrupted) text it was given** — not a reasoning failure.
- **Chinese, idx 141** (apartment vacancy problem): the Chinese translation converts "8 apartments vacant per building" into "**every** apartment vacant" — a different mistranslation, on a different template, in a different language.

**Implication**: any cross-lingual accuracy comparison on this dataset (or similar MT-generated multilingual benchmarks) risks conflating *model reasoning failure* with *benchmark translation failure* unless each flagged failure is traced back to source text. This is the same class of concern Beg to Differ (Ovalle et al., Meta/FAIR, arXiv:2512.22712) flagged about their own back-translation QC (they only spot-checked Spanish) — this pilot found concrete instances of exactly that problem in a different, widely-usable dataset.

---

## Round 3a — Reasoning Drift test (4 instances: 2 templates × 2 variants, zh/th/ja/es/de)

Templates deliberately chosen for genuine sequential dependency: (a) a 5-stage popcorn-popping-rate chain where each stage's count depends on the prior stage's rate, plus a residual-heat step and a give-away fraction; (b) a declining-weekly-collection-rate problem (signatures collected across remaining weeks, one sister's rate dropping 5/week).

| Language | Popcorn (idx 451/458) | Autographs (idx 271/272) |
|---|---|---|
| Chinese | 2/2 correct | 0/2 (Compositional Collapse) |
| Thai | 2/2 correct | 1/2 (Compositional Collapse) |
| Japanese | 2/2 correct | 2/2 correct |
| Spanish | 2/2 correct | 2/2 correct |
| German | 2/2 correct | 0/2 (Compositional Collapse) |

**The popcorn template — built specifically to give Reasoning Drift room to occur — was solved perfectly, 10/10, across every language.** No errors of any kind. **Every failure that did occur (autographs template) was diagnosed as Compositional Collapse, not Drift**: the model invents an unwarranted "declining rate" mechanic and misapplies it consistently from its first use — in Chinese this produces mathematically impossible *negative* weekly signature counts — rather than a slip that starts correct and cascades forward.

**Reasoning Drift was not observed.** Not in this round, not in round 2's sequential day-by-day fruit-picking chains either. Across every long sequential chain tested so far, the model either gets the whole structure right or misconstructs one specific piece wholesale from the start — never a clean early-correct chain that quietly derails partway through.

---

## Round 3b — Format Instability test (2 instances, strict tag-format requirement, zh/th/bn/te/es)

Required output wrapped in SWATH's own tag schema — `<formalisation>...</formalisation><reasoning>Step 1: ...</reasoning><answer>...</answer>` — on a moderate-complexity percentage problem, across 5 scripts including two never tested before (Bengali, Telugu — both complex abugida scripts).

**Result: 10/10 well-formed.** Every response had all three tags present, correctly opened/closed/ordered, sequential step numbering with no gaps or duplicates, no leaked content, no encoding corruption, no premature truncation — regardless of script complexity. **Format Instability was not observed anywhere**, even under an explicit structural demand.

(Side finding, unrelated to format: math correctness split sharply by language on this problem — Thai and Spanish got both right, Chinese/Bengali/Telugu got both wrong, Chinese and Bengali converging on the identical wrong answer. Possibly another translation-fidelity or misreading issue on the "which puppies count as spotted" clause — flagged for later, not yet traced to source.)

---

## What's confirmed vs. still open (updated after 4 rounds)

**Confirmed real and reproducible — the central finding:**
- **Compositional Collapse is the only failure mode observed across 20 real problems, 3 distinct problem designs, and 5 languages.** Every single failure — fog-bank distractor (round 1), apartment/vacancy scope error (round 2), declining-rate misapplication (round 3a) — is the same shape: the model engages with or invents a required structural piece, then drops or misapplies it wholesale, not a slip that develops mid-chain.
- mGSM-Symbolic (and likely similar MT-generated benchmarks) has real, language-and-template-specific translation defects that must be checked before attributing accuracy differences to model behavior (round 2).

**Tested and NOT found (real negative results, not just absence of data):**
- **Reasoning Drift** — tested with a template specifically built for it (clean 5-stage dependency chain); solved perfectly 10/10 across all languages. Either this failure shape doesn't occur for a model this capable, or it needs longer/messier chains or a weaker model to surface.
- **Format Instability** — tested under an explicit strict structural demand across 5 scripts including two complex abugida scripts never tried before (Bengali, Telugu); held up perfectly 10/10.

**Still open:**
- Real target models (only Claude Sonnet 5 tested so far as the model under test) — Drift/Format Instability's absence may be specific to a frontier model; SWATH's own weaker open models (Llama-3-8B, Phi-3.5-mini, DeepSeek-7B) are the natural next test.
- Repeated sampling (only one draw per problem throughout).
