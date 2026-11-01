# Multilingual Structural Reasoning Failures

Investigating structural reasoning failures in multilingual LLM chain-of-thought — evidence for a reproducible "Compositional Collapse" failure mode on the public `mGSM-Symbolic` benchmark.

**Status: 🎓 Accepted at CogMI 2026 (Camera-Ready Final)**  
📄 Camera-Ready Paper: [`paper/submission/cogmi2026_camera_ready_FINAL.pdf`](paper/submission/cogmi2026_camera_ready_FINAL.pdf)  
📝 Manuscript Source: [`paper/PAPER_DRAFT.md`](paper/PAPER_DRAFT.md)  
📋 Submission Package: [`paper/submission/`](paper/submission/)

---

## The Core Idea

Existing multilingual reasoning diagnostics either check whether a model's *finished* answer is logically supported by its reasoning on multiple-choice tasks (*"Beg to Differ"*, Ovalle et al., Meta/FAIR), or measure cross-lingual answer *consistency* without inspecting intermediate steps (*SWATH* — Ranaldi & Pucci, NAACL 2025). 

Neither inspects whether a **generative, multi-step reasoning chain** loses its structural integrity partway through when reasoning in languages other than English. This project characterizes that exact failure mode.

---

## Key Findings

1. **Compositional Collapse**:
   - A distinct frontier-model failure mode where the model explicitly notices or invents a required structural sub-piece of a multi-part problem (e.g. rate changes, segmented conditions), reasons about it, but then drops or misapplies it mid-chain to solve using an oversimplified single formula.
2. **Capability-Dependent Failure Modes**:
   - **Frontier Models (e.g. Claude Sonnet)**: Exhibit Compositional Collapse (accurate structural understanding, failure at the application/retention stage).
   - **Open-Weight / Smaller Models (DeepSeek-R1 14B/32B, Yi-34B, Mistral, Neural-Chat, Phi-3.5)**: Exhibit *mismodeling* from the start (misinterpreting discrete step changes as continuous decay or applying incorrect physical models), rather than noticing and dropping clauses.
3. **Reasoning Drift & Format Instability Ruled Out**:
   - Tested under explicit 5-stage sequential dependencies (popcorn template) and strict structural tag constraints across complex scripts (including Bengali and Telugu); models maintained chain integrity and tags without drift or corruption.
4. **Benchmark Translation Artifacts**:
   - Machine translation in `mGSM-Symbolic` occasionally drops load-bearing clauses in specific language/template pairs — a confound that must be isolated before attributing accuracy drops to model reasoning.

---

## Repository Structure

```
├── paper/
│   ├── PAPER_DRAFT.md               # Complete manuscript draft
│   ├── REFERENCES.md                # Comprehensive reference documentation
│   ├── REFERENCES_FORMATTED.txt     # Formatted citations
│   └── submission/                  # Submission checklists, final review & revision logs
│
├── code/
│   ├── run_inference.py             # Inference pipeline for hosted API providers
│   ├── run_inference_ollama.py      # Inference pipeline for local Ollama models
│   ├── inspect_traces.py           # Automated trace grader with fixed inspector
│   ├── providers.py                 # Provider abstraction (Anthropic, OpenAI, Ollama)
│   ├── create_filtered_problems.py  # Utility for problem filtering
│   ├── backfill_generate_laptop.sh  # Batch generation script for local models
│   └── README.md                    # Detailed execution and reproduction guide
│
├── data/
│   └── mgsm_symbolic/
│       ├── mgsm_symbolic_{lang}.csv # Benchmark problems in 11 languages
│       ├── PILOT_FINDINGS.md        # Original curated pilot findings
│       ├── pilot_round*.json        # Exact problem slices used per test round
│       └── raw_pilot_outputs/       # Raw generation and inspection JSON traces
│
├── analysis/
│   ├── PILOT_FINDINGS.md            # Detailed pilot findings and quoted evidence
│   ├── DEEPSEEK_ANALYSIS.md         # DeepSeek-R1-32B replication and mismodeling analysis
│   ├── THESIS_VERIFICATION.md       # Soundness and hypothesis verification
│   ├── COMPREHENSIVE_WALKTHROUGH.md # Section-by-section walkthrough
│   └── session-reports/             # Per-session status and comparison logs
│
├── evaluations/
│   └── human_reviews/               # Native speaker review packets across 9 languages
│
├── docs/
│   ├── START_HERE.md                # Comprehensive project index and navigation guide
│   ├── PROJECT_OVERVIEW.md          # High-level research summary
│   ├── PLAN.md                      # Working plan and research trajectory
│   ├── GIT_UPLOAD_GUIDE.md          # Guide for git syncing
│   ├── PROJECT_STRUCTURE_GUIDE.md   # Original repo structure documentation
│   ├── REORGANIZATION_COMPLETE.md   # Reorganization changelog
│   └── references/                  # Reference documents
│
├── logs/                            # Local run logs
└── requirements.txt                 # Python dependencies
```

---

## Quickstart & Replication

### 1. Environment Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Running Inference
Generate reasoning traces with an API provider (e.g., Anthropic):
```bash
python code/run_inference.py \
  --provider anthropic \
  --model claude-3-5-sonnet-20241022 \
  --problems data/mgsm_symbolic/pilot_round1_fogbank_problems.json \
  --out data/mgsm_symbolic/raw_pilot_outputs/my_run_generation.json
```

Or run locally using Ollama:
```bash
python code/run_inference_ollama.py \
  --model deepseek-r1:32b \
  --problems data/mgsm_symbolic/pilot_round1_fogbank_problems.json \
  --out data/mgsm_symbolic/raw_pilot_outputs/deepseek_generation.json
```

### 3. Inspecting Traces
Evaluate and grade the generated reasoning chains against ground truth using the fixed inspector:
```bash
python code/inspect_traces.py \
  --generation data/mgsm_symbolic/raw_pilot_outputs/my_run_generation.json \
  --problems data/mgsm_symbolic/pilot_round1_fogbank_problems.json \
  --out data/mgsm_symbolic/raw_pilot_outputs/my_run_full.json
```

---

## Data & Attribution

Problem instances are derived from `mGSM-Symbolic` ([HuggingFace: `lrana/MGSM-Symbolic`](https://huggingface.co/datasets/lrana/MGSM-Symbolic), CC-BY-SA 4.0; code: [`lranaldii/MGSM-Symbolic`](https://github.com/lranaldii/MGSM-Symbolic)), released alongside:

> Ranaldi, L., & Pucci, A. (2025). *Multilingual Reasoning via Self-training*. Proceedings of NAACL 2025.

Data files redistributed in this repository retain their CC-BY-SA 4.0 terms.
