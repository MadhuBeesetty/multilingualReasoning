# 📋 COMPLETE PROJECT INDEX & SUBMISSION GUIDE

**Project**: Compositional Collapse in Frontier Models: Capability-Dependent Failure Modes in Multilingual Reasoning  
**Status**: 🎓 ACCEPTED & CAMERA-READY COMPLETE (CogMI 2026)  
**Camera-Ready Paper**: `paper/submission/cogmi2026_camera_ready_FINAL.pdf`

---

## 📄 CORE PAPERS & MANUSCRIPTS

**🎯 Official Deliverables**:
- [`paper/submission/cogmi2026_camera_ready_FINAL.pdf`](../paper/submission/cogmi2026_camera_ready_FINAL.pdf) — **Camera-Ready Accepted Paper**
- [`paper/PAPER_DRAFT.md`](../paper/PAPER_DRAFT.md) — Full source manuscript (7,500+ words)
  - Abstract & 6 main sections (Intro, Background, Methods, Results, Discussion, Conclusion)
  - Appendix A1-A5 with complete evaluation tables
  - References and reproducibility details

---

## 📚 SUPPORTING DOCUMENTATION

### Research Analysis & Evidence
- [`analysis/PILOT_FINDINGS.md`](../analysis/PILOT_FINDINGS.md) — Foundational pilot evidence and failure signatures
- [`analysis/DEEPSEEK_ANALYSIS.md`](../analysis/DEEPSEEK_ANALYSIS.md) — Replication and mismodeling analysis on DeepSeek-R1-32B
- [`analysis/THESIS_VERIFICATION.md`](../analysis/THESIS_VERIFICATION.md) — Main thesis validation and theoretical framing
- [`analysis/COMPREHENSIVE_WALKTHROUGH.md`](../analysis/COMPREHENSIVE_WALKTHROUGH.md) — Detailed walkthrough of findings
- [`analysis/session-reports/`](../analysis/session-reports/) — Session status and comparative progress reports

### Paper & Submission Materials
- [`paper/submission/cogmi2026_camera_ready_FINAL.pdf`](../paper/submission/cogmi2026_camera_ready_FINAL.pdf) — Accepted camera-ready PDF
- [`paper/submission/FINAL_REVIEW.md`](../paper/submission/FINAL_REVIEW.md) — Comprehensive quality audit
- [`paper/submission/PAPER_READY_FOR_SUBMISSION.md`](../paper/submission/PAPER_READY_FOR_SUBMISSION.md) — Submission verification report
- [`paper/submission/PAPER_REVISION_SUMMARY.md`](../paper/submission/PAPER_REVISION_SUMMARY.md) — Revisions and improvements summary
- [`paper/submission/PAPER_COMPLETION_SUMMARY.md`](../paper/submission/PAPER_COMPLETION_SUMMARY.md) — Completion milestones
- [`paper/REFERENCES.md`](../paper/REFERENCES.md) — Bibliography and paper taxonomy
- [`paper/REFERENCES_FORMATTED.txt`](../paper/REFERENCES_FORMATTED.txt) — Copy-ready citation texts

### Project Navigation & Planning
- [`docs/PROJECT_OVERVIEW.md`](PROJECT_OVERVIEW.md) — High-level executive summary
- [`docs/PLAN.md`](PLAN.md) — Research evolution and roadmap
- [`docs/PROJECT_STRUCTURE_GUIDE.md`](PROJECT_STRUCTURE_GUIDE.md) — Project component guide
- [`docs/REORGANIZATION_COMPLETE.md`](REORGANIZATION_COMPLETE.md) — Reorganization history
- [`docs/references/`](references/) — Third-party reference materials

---

## 💾 DATA & CODE

### Data Locations
```
data/mgsm_symbolic/
  ├── mgsm_symbolic_{lang}.csv                  (11 languages)
  ├── pilot_round1_fogbank_problems.json        (8 problems, 40 instances)
  ├── pilot_round2_diverse_problems.json        (8 problems, 40 instances)
  ├── pilot_round3a_drift_problems.json         (4 problems, 20 instances)
  ├── pilot_round3b_format_problems.json        (2 problems, 10 instances)
  ├── PILOT_FINDINGS.md                         (Curated findings)
  └── raw_pilot_outputs/                        (Raw generation + inspection results)
```

### Code Locations
```
code/
  ├── run_inference.py                          (Generate traces with API providers)
  ├── run_inference_ollama.py                   (Generate traces with local Ollama)
  ├── inspect_traces.py                         (Grade traces with fixed inspector)
  ├── providers.py                              (API provider abstraction)
  ├── create_filtered_problems.py               (Problem filter utility)
  ├── backfill_generate_laptop.sh               (Local batch generation script)
  └── README.md                                 (Detailed code guide)
```

### Evaluations
```
evaluations/
  └── human_reviews/                           (Native speaker review packets in 9 languages)
      ├── README.md
      └── review_{lang}.md
```

---

## 🎯 KEY FINDINGS AT A GLANCE

### The Main Claim
**Compositional Collapse** — A frontier-model failure mode where:
1. Model notices/invents problem structure
2. Explicitly reasons about it
3. Then drops or ignores it mid-chain
4. Solves with an oversimplified flat model

### The Novel Insight
**Failure modes are capability-dependent**:
- Frontier (Claude Sonnet): Compositional Collapse (failure during application/retention)
- Large/Medium models (DeepSeek-R1-32B, Yi-34B, Mistral, Phi-3.5): Mismodeling (failure during interpretation from the start)
