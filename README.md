# Agreeing on the Answer but Not the Reason: Measurement Limits of LLM Reasoning Failure Taxonomies

<div align="center">

[![arXiv](https://img.shields.io/badge/arXiv-2611.13140-b31b1b.svg)](https://arxiv.org/abs/2611.13140)
[![IEEE CogMI 2026](https://img.shields.io/badge/IEEE_CogMI-2026-blue.svg)](https://arxiv.org/abs/2611.13140)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/Data_License-CC_BY--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)

**Madhu Sudhan Rao Beesetty**  
PayPal, Inc. · San Jose, CA, USA  
[madhusudhanbeesetty@gmail.com](mailto:madhusudhanbeesetty@gmail.com)

📄 **[Read the Paper on arXiv](https://arxiv.org/abs/2611.13140)** | 📦 **[Camera-Ready PDF](paper/submission/cogmi2026_camera_ready_FINAL.pdf)**

</div>

---

## Abstract

Failure taxonomies for LLM reasoning are increasingly reported as measurements: papers state what fraction of a model's errors fall into named categories, then compare those fractions across models. We show that for one such category the reported fraction is largely a property of the measurement procedure.

We defined **Compositional Collapse** — a model notices a required structural sub-part of a problem, then drops or misapplies it — and measured it across **12 models** and **11 languages** on a public multilingual math benchmark (**2,316 graded records**). Three findings follow:

1. **50.1% of failures carry evidence for more than one category**, so the reported plurality is set by the order in which the classifier tests them — reversing two tests moves it in 11 of 12 models, and across all six effective orderings Collapse's share of failures spans **26.4% to 76.4%**.

2. **Agreement collapses for the category but not for the task.** Native speakers of all eleven languages judged 179 transcripts, agreeing with the inspector at **κ = 0.932** on answer correctness and **κ = 0.093** on Collapse. A second independent native speaker per language re-rated 142 of those items; the two humans agree with each other at **κ = 0.659** while each agrees with the inspector at κ ≈ 0.094. The category is therefore reproducible between humans but not reproduced by the original inspector — an *instrument-validation failure* rather than an intrinsically unusable construct.

3. Re-running the identical inspector model (Claude Sonnet 5) with the human instructions verbatim raises κ against Human 2 from **0.147 to 0.636**, approaching the human–human reference of 0.659. The gap is therefore **largely attributable to the prompt, not the model**.

We recommend **four cheap checks** before failure-mode rates are compared across models: report label co-occurrence, permute the tie-break, validate on a shared independent sample, and audit systematic disagreements.

---

## Key Findings

| Finding | Result |
|---------|--------|
| Multi-label overlap rate | **50.1%** of failures qualify for >1 category |
| Collapse rate range (across all test orderings) | **26.4% → 76.4%** on identical data |
| Inspector vs. human — answer correctness | **κ = 0.932** (97.8% agreement) |
| Inspector vs. human — Collapse category | **κ = 0.093** (near chance) |
| Human 1 vs. Human 2 — Collapse category | **κ = 0.659** (83.5% agreement) |
| Re-prompted inspector vs. Human 2 | **κ = 0.636** (prompt was the fix, not the model) |
| Models evaluated | **12** (frontier + open-weight) |
| Languages evaluated | **11** |
| Total graded records | **2,316** |

---

## Why This Matters

> *"If you define a failure taxonomy and report that 'Model A has 72% Compositional Collapse errors,' you are mostly reporting a property of your classifier's test order and prompt — not a property of the model."*

This paper is a **methodological audit** of a standard practice in LLM evaluation: using an LLM-as-a-judge to classify why a model fails. Our result is not that failure taxonomies are useless — it is that **they require instrument validation before cross-model comparison**.

---

## The Four Recommended Checks

Before publishing failure-mode rates across models:

1. **Report label co-occurrence** — what fraction of your failures qualify for >1 category?
2. **Permute the tie-break order** — does the nominal plurality change when you reorder your classifier tests?
3. **Validate on a shared human sample** — does κ between your judge and human raters exceed 0.6 on a held-out sample?
4. **Audit systematic disagreements** — do mismatches concentrate in specific languages, templates, or problem types? If so, trace them to benchmark translation quality before attributing them to model behavior.

---

## Cite This Work

If you use this paper or the data/code in this repository, please cite:

```bibtex
@inproceedings{beesetty2026agreeing,
  title     = {Agreeing on the Answer but Not the Reason: Measurement Limits of {LLM} Reasoning Failure Taxonomies},
  author    = {Beesetty, Madhu Sudhan Rao},
  booktitle = {Proceedings of the IEEE International Conference on Cognitive Machine Intelligence (CogMI)},
  year      = {2026},
  url       = {https://arxiv.org/abs/2611.13140}
}
```

---

## Repository Structure

```
├── paper/
│   ├── PAPER_DRAFT.md                        # Full manuscript source
│   ├── REFERENCES.md                          # Annotated bibliography (25+ papers)
│   ├── REFERENCES_FORMATTED.txt               # Copy-ready citations
│   └── submission/
│       ├── cogmi2026_camera_ready_FINAL.pdf   # Accepted camera-ready paper
│       ├── FINAL_REVIEW.md                    # Pre-submission quality audit
│       └── PAPER_REVISION_SUMMARY.md          # Revision history
│
├── code/
│   ├── run_inference.py             # Inference pipeline (Anthropic / OpenRouter API)
│   ├── run_inference_ollama.py      # Inference pipeline (local Ollama models)
│   ├── inspect_traces.py            # Automated trace grader with fixed LLM inspector
│   ├── providers.py                 # Provider abstraction layer
│   ├── create_filtered_problems.py  # Problem set filtering utility
│   ├── backfill_generate_laptop.sh  # Batch generation script for local models
│   └── README.md                    # Detailed code usage guide
│
├── data/
│   └── mgsm_symbolic/
│       ├── mgsm_symbolic_{lang}.csv           # Benchmark data in 11 languages
│       ├── PILOT_FINDINGS.md                  # Curated pilot findings
│       ├── pilot_round{1,2,3a,3b}_*.json      # Exact problem sets per test round
│       └── raw_pilot_outputs/                 # All raw generation + inspection traces
│           ├── *_generation.json              # Model reasoning traces (28 files)
│           └── *_full.json                    # Graded inspection results
│
├── analysis/
│   ├── PILOT_FINDINGS.md            # Foundational pilot evidence with quoted traces
│   ├── DEEPSEEK_ANALYSIS.md         # DeepSeek-R1-32B mismodeling analysis
│   ├── THESIS_VERIFICATION.md       # Hypothesis soundness verification
│   ├── COMPREHENSIVE_WALKTHROUGH.md # Section-by-section research walkthrough
│   └── session-reports/             # Incremental session progress reports
│
├── evaluations/
│   └── human_reviews/               # Native speaker review packets (9 of 11 languages)
│       ├── README.md                # Human review protocol documentation
│       └── review_{lang}.md         # Per-language annotator packets (de, es, fr, it, ja, ru, sw, th, zh)
│
├── docs/
│   ├── START_HERE.md                # Complete project index and navigation
│   ├── PROJECT_OVERVIEW.md          # High-level executive summary
│   └── PLAN.md                      # Research trajectory and evolution
│
└── requirements.txt                 # Python dependencies
```

---

## Quickstart & Replication

### 1. Environment Setup
```bash
git clone https://github.com/MadhuBeesetty/multilingualReasoning
cd multilingualReasoning
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Generate Reasoning Traces

**Using an API provider (Anthropic / OpenRouter):**
```bash
python code/run_inference.py \
  --provider anthropic \
  --model claude-3-5-sonnet-20241022 \
  --problems data/mgsm_symbolic/pilot_round1_fogbank_problems.json \
  --out data/mgsm_symbolic/raw_pilot_outputs/my_run_generation.json
```

**Using a local model via Ollama:**
```bash
python code/run_inference_ollama.py \
  --model deepseek-r1:32b \
  --problems data/mgsm_symbolic/pilot_round1_fogbank_problems.json \
  --out data/mgsm_symbolic/raw_pilot_outputs/deepseek_generation.json
```

### 3. Inspect & Grade Traces
```bash
python code/inspect_traces.py \
  --generation data/mgsm_symbolic/raw_pilot_outputs/my_run_generation.json \
  --problems data/mgsm_symbolic/pilot_round1_fogbank_problems.json \
  --out data/mgsm_symbolic/raw_pilot_outputs/my_run_full.json
```

---

## Data & Attribution

Benchmark problems are from **mGSM-Symbolic**:
- HuggingFace: [`lrana/MGSM-Symbolic`](https://huggingface.co/datasets/lrana/MGSM-Symbolic) (CC-BY-SA 4.0)
- GitHub: [`lranaldii/MGSM-Symbolic`](https://github.com/lranaldii/MGSM-Symbolic)
- Released alongside:

> Ranaldi, L., & Pucci, A. (2025). *Multilingual Reasoning via Self-training*. Proceedings of NAACL 2025.

All redistributed data files in this repository retain their original **CC-BY-SA 4.0** license terms.

---

## Related Work

This paper builds on and critically examines:

| Paper | Relevance |
|-------|-----------|
| [SWATH — Ranaldi & Pucci, NAACL 2025](https://arxiv.org/abs/2501.04327) | Anchor benchmark dataset (mGSM-Symbolic) and cross-lingual consistency baseline |
| [Beg to Differ — Ovalle et al., Meta/FAIR (arXiv:2512.22712)](https://arxiv.org/abs/2512.22712) | Reasoning-answer alignment at scale (65k MCQ traces); inspires the inspector design |
| [Chain-of-Thought Prompting — Wei et al., NeurIPS 2022](https://arxiv.org/abs/2201.11903) | Foundational chain-of-thought methodology |
| [LLM-as-a-Judge — Zheng et al., 2023](https://arxiv.org/abs/2306.05685) | The standard practice being audited |

---

## Keywords

`LLM evaluation` · `LLM-as-judge` · `inter-rater reliability` · `construct validity` · `multilingual reasoning` · `chain-of-thought` · `reasoning failure analysis` · `mGSM-Symbolic` · `Cohen's kappa` · `NLP benchmarking`
