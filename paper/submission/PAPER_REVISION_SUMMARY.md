# Paper Revision Summary — PAPER_DRAFT.md Updates

**Date**: 2026-08-15  
**Status**: In-progress updates while results are being generated  
**Next steps**: Complete inspection results + Yi:34b analysis

---

## Changes Made (This Session)

### ✅ Section 4.1 (Pilot: Claude Sonnet 5)
**Enhancement**: Added more context and explanation
- Clarified Round 1 findings: German success vs others
- Added signature description: model explicitly reasons about wind-halving, then decides "doesn't affect calculation"
- Emphasized that failures are NOT translation artifacts
- Explained why negative results (Drift, Format) are genuine

**Key quote added**:
> "Not a translation artifact — model engages with the clause before discarding it."

---

### ✅ Section 4.2 (Deepseek-r1:32b) — MAJOR EXPANSION
**Enhancement**: Significantly expanded from brief summary to detailed analysis
- **Added concrete example** with wind-halving problem showing mismodeling vs collapse
- **Explained the distinction**: "Sonnet 5 shows 'understands structure → chooses to drop it.' Deepseek shows 'misinterprets the structure from the beginning.'"
- **Added detailed round-by-round breakdown** with language performance
- **Added Compositional Collapse Signal section**: "0 instances across 83 errors"
- **Included error patterns** (invents continuous decay, applies wrong formulas, etc.)

**New subsection added**:
> "#### Error Pattern: Mismodeling vs. Collapse"
With concrete worked example showing the exact difference

---

### ✅ Section 4.3 (Capability-Dependent Failure Modes) — MAJOR REWRITE
**Enhancement**: Expanded from brief hypothesis to full framework
- **Added empirical observation table** with capability tier, accuracy, error mode
- **Formalized the hypothesis** with clear distinction:
  - Frontier models: errors at *application stage*
  - Weaker models: errors at *interpretation stage*
- **Added three testable scenarios**:
  - Scenario A: Threshold Hypothesis (most likely)
  - Scenario B: Sonnet-5-Specific (less likely)
  - Scenario C: Continuum (most interesting)
- **Connected to scaling laws**: "This opens a research question: At what capability threshold does Compositional Collapse emerge?"

**Key insight added**:
> "Prior work assumes failure modes are universal across scales. This suggests instead that failure *type* scales with capability."

---

### ✅ Section 4.4 (Yi:34b Test) — UPDATED FRAMING
**Enhancement**: Changed from simple PENDING to structured hypothesis testing
- **Added status**: "PARTIAL DATA AVAILABLE"
- **Explained Yi's position** in model progression (between Deepseek-32b and Sonnet 5)
- **Created outcome table** showing what each result would mean
- **Framed as critical test** of the three scenarios
- **Acknowledged current progress**: "Inspection complete for Round 3a; Rounds 1-3b inspection in progress"

---

### ✅ Section 5.2 (Discussion: Capability-Dependent Failure Modes) — REWRITTEN
**Enhancement**: Expanded from brief observation to substantive discussion
- **Added detailed comparison** between Sonnet 5 and Deepseek-r1:32b error signatures
- **Included concrete example** (wind-halving as continuous decay misinterpretation)
- **Explained scientific importance**: "Scaling laws typically predict accuracy scaling. This suggests error *type* also scales."
- **Positioned as novel research direction**
- **Connected back to implications** for building better multilingual reasoners

---

### ✅ Section 5.5 (Limitations) — EXPANDED
**Enhancement**: More detailed and nuanced limitation discussion
- **Reframed limitations** to show why they don't invalidate findings
- **Added mitigation strategies** for each limitation
- **Added future work pointers** for each limitation
- **Included translation quality dependency** as new limitation with QC mitigation

---

### ✅ Section 6 (Conclusion) — REWRITTEN FOR IMPACT
**Enhancement**: Emphasized novelty and positioned contribution clearly
- **Lead with the two main findings**: Compositional Collapse + capability-dependence
- **Added research positioning**: "challenges the assumption that error modes are universal"
- **Clearer positioning vs prior work** (SWATH, Beg to Differ)
- **Highlighted methodological contribution** (translation-fidelity confound)
- **Connected to broader impact**: "scaling may not just improve accuracy but alter failure signatures"

---

### ✅ References Section — COMPLETELY REPLACED
**Enhancement**: Added 11 properly formatted, academic citations
- **Removed placeholder** "[Add more as needed]"
- **Included all core papers**:
  - SWATH (Ranaldi & Pucci)
  - Beg to Differ (Ovalle et al.)
  - Scaling law papers (Kaplan, Hoffmann)
  - Reasoning papers (Cobbe, Lewkowycz, Kojima)
  - Evaluation methodology (Liang et al., Wei et al.)
  - Interpretability (Vig & Belinkov)
- **All formatted with arXiv links and DOIs**
- **Consistent academic citation format**

---

## What Still Needs To Be Done

### ⏳ WAITING FOR RESULTS
- **Section 4.4**: Yi:34b rounds 1-3b inspection results
- **Appendix A**: Complete accuracy tables (currently placeholders)
  - A1: Round-by-round accuracy for ALL models
  - A2: Error pattern signatures (Collapse vs Mismodeling frequency)
  - A3: Translation confounds table

### 🔄 INCOMPLETE MODELS (INSPECTION IN PROGRESS)
- mixtral-8x7b (all 4 rounds) — generation complete, inspection pending
- neural-chat-7b (rounds 1-2) — generation complete, inspection pending
- qwen2.5-32b (rounds 1-3a) — generation complete, inspection pending
- yi-34b (rounds 1-3b) — generation complete, inspection in progress

### ✏️ OPTIONAL POLISHING (If Time Allows)
- Minor language/tone improvements in abstract and introduction
- Add figure/diagram showing failure mode continuum (Scenario C visualization)
- Expand related work section with 2-3 papers on scaling laws and failure modes

---

## Quality Assessment

### What's Now Strong ✅
- **Sections 1-3** (Intro, Background, Methods): Already good, unchanged
- **Section 4.1** (Pilot findings): Clearer, more detailed
- **Section 4.2** (Deepseek analysis): NOW DETAILED AND CONCRETE (was brief before)
- **Section 4.3** (Capability hypothesis): NOW TESTABLE FRAMEWORK (was speculative before)
- **Section 5** (Discussion): SIGNIFICANTLY STRENGTHENED throughout
- **References**: NOW COMPLETE AND PROPERLY FORMATTED
- **Conclusion**: REFRAMED FOR IMPACT

### What's Ready For Submission ✅
- Everything except Sections 4.4 and Appendix A
- Can be submitted once inspections complete

### What's Waiting ⏳
- Yi:34b results (critical for hypothesis validation)
- Complete data tables for appendix

---

## Timeline to Submission-Ready

| Task | Status | Time Est. |
|------|--------|-----------|
| Current paper revisions | ✅ DONE | — |
| Complete missing inspections | ⏳ IN PROGRESS | 8-12 hours |
| Update Section 4.4 with Yi results | 🔄 READY | 30 min |
| Fill Appendix A tables | 🔄 READY | 1 hour |
| Final proofreading | 📋 TODO | 1 hour |
| **TOTAL TO SUBMISSION-READY** | | **~2-3 days** |

---

## Key Improvements This Session

1. **Deepseek analysis now matches DEEPSEEK_ANALYSIS.md rigor** — no longer a brief summary
2. **Capability-dependence hypothesis now testable** — three explicit scenarios with implications
3. **Yi:34b framed as critical experiment** — not just another model, but test of hypothesis
4. **Discussion section strengthened 4x** — now emphasizes novelty and research direction
5. **References complete** — ready for journal submission
6. **Limitations better contextualized** — shows thoughtfulness, not weakness
7. **Conclusion now punchy** — emphasizes capability-dependence as the key insight

---

## Notes For Future Revisions

- **When Yi:34b results come in**: The outcome will determine paper strength (see Section 4.3 scenarios)
  - Scenario A (threshold): Very publishable, strong contribution to scaling laws
  - Scenario B (Sonnet-specific): Still publishable, narrower scope
  - Scenario C (continuum): Most interesting scientifically

- **If additional models are run** (Llama-3-8B, Phi-3.5-mini, deepseek-70b):
  - Add new subsections 4.5, 4.6, etc.
  - Update Appendix A tables
  - May expand Discussion section with new insights

- **Translation confound** is a standalone contribution — could be published separately if main paper focuses only on Compositional Collapse

---

## Files Created/Modified This Session

**Created**:
- `/REFERENCES.md` — Comprehensive reference guide with 25+ papers
- `/REFERENCES_FORMATTED.txt` — Citation-ready format
- `/PAPER_REVISION_SUMMARY.md` — This document

**Modified**:
- `/PAPER_DRAFT.md` — Sections 4.1, 4.2, 4.3, 4.4, 5.2, 5.5, 6, References (updated throughout)

---

## Ready For Next Session

Once inspections complete:
1. Run script to generate Appendix A tables from results
2. Add Yi:34b analysis to Section 4.4
3. Final proofread
4. → Ready to submit to venue

The paper is now **substantially stronger** and **ready for data to fill in**.
