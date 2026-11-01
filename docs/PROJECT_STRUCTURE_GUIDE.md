# 📂 PROJECT STRUCTURE GUIDE

**Status**: ✅ Reorganized for clarity and professionalism

---

## 🎯 WHERE TO START

### For Paper Submission
```
👉 START HERE: docs/START_HERE.md
   ↓
   Review: paper/PAPER_DRAFT.md
   ↓
   Quality Check: paper/submission/FINAL_REVIEW.md
```

### For Understanding the Research
```
👉 Read: docs/PROJECT_OVERVIEW.md
   ↓
   Deep Dive: analysis/PILOT_FINDINGS.md
   ↓
   Replication: analysis/DEEPSEEK_ANALYSIS.md
```

### For Running Experiments
```
👉 Check: code/README.md
   ↓
   Generate: python code/run_inference.py
   ↓
   Inspect: python code/inspect_traces.py
```

---

## 📁 FOLDER ORGANIZATION

### `/docs` — Documentation & Guides
🎯 **START HERE**: All user-facing documentation
```
docs/
├── START_HERE.md              ← Read this first (submission guide)
├── GIT_UPLOAD_GUIDE.md        ← How to push changes to GitHub
├── PROJECT_OVERVIEW.md        ← High-level project overview
├── PLAN.md                    ← Research plan & roadmap
└── guides/                    ← [Future: setup & usage guides]
```

**Why this folder?**
- Central location for all documentation
- Clear entry point (START_HERE.md)
- Guides for contributors

---

### `/paper` — The Paper & References
📄 **THE ACTUAL MANUSCRIPT**
```
paper/
├── PAPER_DRAFT.md             ← Main manuscript (7,500+ words) ⭐
├── REFERENCES.md              ← Reference guide (25+ papers)
├── REFERENCES_FORMATTED.txt   ← Copy-paste ready citations
└── submission/                ← Submission-specific documents
    ├── FINAL_REVIEW.md        ← Quality audit (✅ PUBLICATION READY)
    ├── PAPER_READY_FOR_SUBMISSION.md
    ├── PAPER_COMPLETION_SUMMARY.md
    └── PAPER_REVISION_SUMMARY.md
```

**Why this structure?**
- All paper-related files in one place
- `/submission` subfolder for journal-specific versions
- Easy to find references and citations

---

### `/analysis` — Research Findings & Analysis
🔬 **RESEARCH EVIDENCE & VALIDATION**
```
analysis/
├── PILOT_FINDINGS.md          ← Original $0 pilot findings
├── DEEPSEEK_ANALYSIS.md       ← Deepseek-r1:32b analysis
├── THESIS_VERIFICATION.md     ← Thesis validation ✅
├── COMPREHENSIVE_WALKTHROUGH.md
└── session-reports/           ← Session-specific documentation
    ├── SESSION_STATUS.md      ← Completion status
    ├── BEFORE_AFTER_COMPARISON.md
    └── [future session reports]
```

**Why this structure?**
- Separates findings from paper
- Clear evidence trail
- Session reports for reproducibility

---

### `/code` — Implementation
💻 **REPRODUCIBLE EXPERIMENTS**
```
code/
├── README.md                  ← Code usage & setup ⭐
├── run_inference.py           ← Generate with any provider
├── run_inference_ollama.py    ← Generate with local Ollama
├── inspect_traces.py          ← Grade with fixed inspector
├── providers.py               ← API provider abstraction
└── utils/                     ← [Future: utility modules]
```

**Why this structure?**
- All experiment code in one place
- Clear entry points (run_inference.py, inspect_traces.py)
- Provider abstraction keeps code clean

---

### `/data` — Problem Sets & Results
📊 **RAW DATA & OUTPUTS**
```
data/
└── mgsm_symbolic/
    ├── pilot_round1_fogbank_problems.json       (8 problems)
    ├── pilot_round2_diverse_problems.json       (8 problems)
    ├── pilot_round3a_drift_problems.json        (4 problems)
    ├── pilot_round3b_format_problems.json       (2 problems)
    ├── mgsm_symbolic_*.csv                     (Source data: 7 languages)
    └── raw_pilot_outputs/                      (All results)
        ├── *_generation.json                   (Model outputs)
        └── *_full.json                         (Inspection results)
```

**Why this structure?**
- Keeps data separate from code
- Raw outputs preserved for reproducibility
- Clear problem set organization

---

### `/results` — Summary Analysis
📈 **[OPTIONAL: For future summary statistics]**
```
results/
├── ACCURACY_SUMMARY.txt       (Model accuracy comparison)
├── ERROR_MODES_SUMMARY.txt    (Error type frequencies)
└── CAPABILITY_ANALYSIS.txt    (Capability tier analysis)
```

---

### `/` Root Level (Minimal)
🏠 **ONLY ESSENTIAL PROJECT FILES**
```
├── README.md                  ← Project overview (→ points to docs/)
├── requirements.txt           ← Python dependencies
├── LICENSE                    ← MIT or CC-BY-SA 4.0
├── .gitignore                 ← Git configuration
└── [Organized subfolders above]
```

---

## 🗺️ COMPLETE VISUAL MAP

```
multilingualReasoning/
│
├── 📄 README.md               ← Start here for overview
├── 📋 requirements.txt
├── 📜 LICENSE
├── .gitignore
│
├── 📂 docs/                   ← Documentation (go here first!)
│   ├── 👉 START_HERE.md       ← ⭐ BEGIN HERE
│   ├── GIT_UPLOAD_GUIDE.md
│   ├── PROJECT_OVERVIEW.md
│   ├── PLAN.md
│   └── guides/                (Planned: setup & usage)
│
├── 📂 paper/                  ← The Actual Paper
│   ├── 👉 PAPER_DRAFT.md      ← ⭐ 7,500+ words, complete
│   ├── REFERENCES.md
│   ├── REFERENCES_FORMATTED.txt
│   └── submission/
│       ├── FINAL_REVIEW.md
│       ├── PAPER_READY_FOR_SUBMISSION.md
│       ├── PAPER_COMPLETION_SUMMARY.md
│       └── PAPER_REVISION_SUMMARY.md
│
├── 📂 analysis/               ← Research Evidence
│   ├── PILOT_FINDINGS.md
│   ├── DEEPSEEK_ANALYSIS.md
│   ├── THESIS_VERIFICATION.md
│   ├── COMPREHENSIVE_WALKTHROUGH.md
│   └── session-reports/
│       ├── SESSION_STATUS.md
│       └── BEFORE_AFTER_COMPARISON.md
│
├── 💻 code/                   ← Implementation
│   ├── README.md              ← Code setup & usage
│   ├── run_inference.py
│   ├── run_inference_ollama.py
│   ├── inspect_traces.py
│   ├── providers.py
│   └── utils/
│
├── 📊 data/                   ← Raw Data
│   └── mgsm_symbolic/
│       ├── pilot_round*.json
│       ├── mgsm_symbolic_*.csv
│       └── raw_pilot_outputs/
│           ├── *_generation.json
│           └── *_full.json
│
├── 📈 results/                ← Analysis summaries (planned)
│
└── 📦 _archive/               ← Old superseded work
```

---

## ✅ QUICK NAVIGATION

| Want to... | Go to... |
|-----------|----------|
| **Submit paper** | `docs/START_HERE.md` |
| **Read the paper** | `paper/PAPER_DRAFT.md` |
| **Check paper quality** | `paper/submission/FINAL_REVIEW.md` |
| **Understand findings** | `analysis/PILOT_FINDINGS.md` |
| **See validation** | `analysis/THESIS_VERIFICATION.md` |
| **Run experiments** | `code/README.md` |
| **Get problem sets** | `data/mgsm_symbolic/pilot_round*.json` |
| **View all results** | `data/mgsm_symbolic/raw_pilot_outputs/` |
| **Check project plan** | `docs/PLAN.md` |
| **See what changed** | `analysis/session-reports/` |

---

## 🚀 NEXT STEPS

### For Paper Submission
1. Read: `docs/START_HERE.md`
2. Review: `paper/PAPER_DRAFT.md`
3. Check: `paper/submission/FINAL_REVIEW.md`
4. Submit!

### For GitHub Upload
1. Read: `docs/GIT_UPLOAD_GUIDE.md`
2. Run git commands
3. Push to main

### For Contributing
1. Read: `docs/PROJECT_OVERVIEW.md`
2. Check: `code/README.md`
3. Run: `python code/run_inference.py`

---

## 📊 ORGANIZATION BENEFITS

✅ **Clarity** — Clear purpose for each folder  
✅ **Discoverability** — Easy to find what you need  
✅ **Scalability** — Room to grow without chaos  
✅ **Professionalism** — GitHub-ready structure  
✅ **Collaboration** — Easy for others to navigate  
✅ **Reproducibility** — All data & code organized  

---

**Structure created**: 2026-08-16  
**Status**: ✅ Ready for GitHub upload  
**Next**: Run `docs/GIT_UPLOAD_GUIDE.md` to push changes
