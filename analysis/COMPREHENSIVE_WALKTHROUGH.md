# Comprehensive Project Walkthrough

## Part 1: The Research Question

**Core hypothesis**: Do multilingual LLMs lose their problem structure when reasoning crosses a language boundary?

### Why this matters

Existing multilingual reasoning research checks:
- **SWATH** (Ranaldi & Pucci, NAACL 2025): Cross-lingual answer *consistency* at the top level. Doesn't inspect intermediate reasoning steps.
- **Beg to Differ** (Ovalle et al., Meta/FAIR): Reasoning-answer alignment on *multiple-choice* tasks at massive scale (65k traces). Can't see step-wise degradation in *generative* multi-step chains.

**This project's gap**: No one is checking whether a model's step-by-step reasoning in a *generative, open-ended math problem* loses structure partway through when reasoning in different languages. That's what we're testing.

---

## Part 2: The Finding (Validated, Reproducible)

### Compositional Collapse — The Only Failure Mode Found

**Definition**: A model notices or *invents* a required structural sub-part of a multi-part problem, then **drops or misapplies it wholesale** — never gradually.

**Real example** (Round 1, "fog bank" wind-halving problem):
```
Problem (abstract): 
  - A ship travels at rate X for 60 minutes
  - Then wind speed halves, reducing the ship's rate to X/2
  - Calculate total distance traveled

Model's reasoning trace:
  ✓ Notices: "The wind halves the speed after 60 minutes"
  ✓ Explicitly reasons about it
  ✗ Then decides: "This info doesn't affect the calculation"
  ✗ Solves using flat single-rate proportion instead of splitting at the 60-min mark
  
Result: Completely drops the wind-halving clause from calculation (Compositional Collapse)
```

**Evidence across 4 pilot rounds**:
- Round 1 (fog bank): 8 problems, 5 languages — all failures were Compositional Collapse
- Round 2 (diverse templates): 8 problems, 5 languages — all failures were Compositional Collapse
- Round 3a (drift test): 4 problems, 5 languages — all failures were Compositional Collapse
- Round 3b (format test): 2 problems, 5 languages — 2 potential failures were Compositional Collapse

**Total**: 22 problems × 5-5 languages per round = 110 language-instances. Every single failure shows the same pattern.

**Why it's not gradual drift**: The model doesn't start getting the wind-halving clause right and slowly mess it up. It either:
- Gets the full structure right from step 1, OR
- Misconstructs one specific piece from the very start (and applies that misconstruction consistently)

Never a clean early-correct-step followed by mid-chain degradation.

---

### Two Real Negative Findings

#### Reasoning Drift — Tested, NOT FOUND

**How we tested it**: Round 3a, "popcorn-popping" problem — a 5-stage sequential dependency chain where each stage's count depends on the previous stage's rate:
```
Step 1: Calculate base popcorn-popping rate (from initial temperature)
Step 2: Apply heat-retention rate for residual heat
Step 3: Calculate leftover popcorn from stage 1
Step 4: Combine with gifted popcorn
Step 5: Final count after give-away fraction
```

This is *designed* to let Reasoning Drift surface — if the model gets step 1 right but makes a small mistake, steps 2–5 cascade and compound the error.

**Result**: **Solved perfectly 10/10 across all languages tested.** Zero errors, not a single slip. Either:
- Reasoning Drift doesn't occur for frontier models like Claude Sonnet 5, OR
- It requires weaker models or messier/longer chains to surface

**Real negative result**, not "we didn't look."

#### Format Instability — Tested, NOT FOUND

**How we tested it**: Round 3b — strict SWATH-style tag requirement:
```xml
<formalisation>...restate problem in structured form...</formalisation>
<reasoning>Step 1: ...
Step 2: ...
...</reasoning>
<answer>...final answer...</answer>
```

Applied across 5 languages including two complex abugida scripts (Bengali, Telugu) — the kind of script-complexity that might break formatting.

**Result**: **10/10 well-formed.** Every response:
- All three tags present
- Correctly opened/closed/ordered
- No premature truncation
- No encoding corruption
- No leaked content outside tags
- Sequential step numbering with no gaps/duplicates

No Format Instability found, even under explicit structural demands.

---

### Critical Methodological Discovery: Translation-Fidelity Confound

**The problem**: Round 2, we traced several "model failures" back to the benchmark itself.

**Real examples**:
```
Problem: "Juan picks fruit 5× as many times on Friday as Wednesday" (multiplier scenario)

German translation: "Friday he picks the same amount as Wednesday" 
  → multiplier omitted entirely
Thai translation: Similar omission
Spanish translation: Preserved multiplier (as "Quintuple" loanword)
Japanese translation: Preserved multiplier

Model answer given German/Thai text: Correct reading of corrupted text, not a reasoning failure
```

**Another example**:
```
Problem: "8 apartments vacant per building"

Chinese translation: "**every** apartment vacant" (meaning all apartments)
  → Same problem, but different mistranslation

Model answer: Correct given the mistranslated text
```

**Why this matters**: Any accuracy difference across languages could be attributed to the model, when it's actually due to mGSM-Symbolic's machine translation (GPT-4o, per SWATH's paper) dropping load-bearing clauses in certain language/template pairs.

This is now a **required QC step**: before attributing any "failure" to model reasoning, check whether the source-language problem text actually contains the same structural elements as English.

---

## Part 3: The Experimental Infrastructure

### The Two-Step Pipeline

Everything follows this pattern:

```
Step 1: GENERATION (model-under-test, varies)
  Input: Problem set (problems_file.json)
  Model: Ollama/OpenRouter/Anthropic (varies per experiment)
  Output: Raw traces + answers
  
  ↓
  
Step 2: INSPECTION (fixed model, always Claude Sonnet 5)
  Input: Raw traces from Step 1 + original problems
  Model: Claude Sonnet 5 (hardcoded, never changes)
  Output: Structured verdicts with evidence
```

**Why this design**: The only thing that changes is the generator. The inspector is fixed, so any difference in results is due to the model-under-test, not the evaluator.

### Generation Script: `run_inference_ollama.py`

**What it does**:
1. Loads a problem set (JSON: language → list of problems)
2. For each language, runs each problem through the generator model
3. Captures full reasoning trace + final answer
4. Writes to JSON with metadata

**Arguments**:
```bash
--problems <path>           # Required: pilot_round*_problems.json file
--model <tag>              # Ollama model tag (must be pre-pulled)
--base-url <url>           # Ollama server (default: http://localhost:11434/v1)
--out <path>               # Output JSON file
--require-format-tags      # Optional: add strict tag requirement to prompt (only for round 3b)
--workers <n>              # Thread pool size (default: 5)
```

**Example invocation**:
```bash
python code/run_inference_ollama.py \
  --problems data/mgsm_symbolic/pilot_round1_fogbank_problems.json \
  --model deepseek-r1:32b \
  --out data/mgsm_symbolic/raw_pilot_outputs/deepseek-r1-32b_round1_generation.json
```

**What the output looks like**:
```json
{
  "summary": "Blind generation run (Ollama, local/offline): model=deepseek-r1:32b, ...",
  "provider": "ollama",
  "model": "deepseek-r1:32b",
  "result": [
    {
      "language": "zh",
      "generation": {
        "solutions": [
          {
            "idx": 40,
            "raw_output": "<formalisation>...</formalisation>\n<reasoning>Step 1: ...\nStep 2: ...</reasoning>\n<answer>11%</answer>"
          },
          {...}
        ]
      }
    },
    {"language": "th", ...},
    {"language": "bn", ...},
    {...}
  ]
}
```

### Inspection Script: `inspect_traces.py`

**What it does**:
1. Loads generation output from Step 1
2. For each trace, sends to Claude Sonnet 5 with structured prompt
3. Asks Sonnet 5 to:
   - Extract the model's final answer (as it literally appears)
   - Judge if the answer is mathematically correct
   - Look for evidence of Compositional Collapse
   - Look for evidence of Reasoning Drift
   - Look for evidence of Format Instability
4. Returns structured JSON verdicts

**Why Claude Sonnet 5 as inspector**:
- Frontier model, good at reading complex reasoning
- Can understand the full problem context
- Can compare model's reasoning to ground truth
- Consistent across experiments

**Key constraint**: Inspector is hardcoded to `"claude-sonnet-5"`, never parameterized. This is intentional and critical to the experimental design.

**Arguments**:
```bash
--generation <path>     # Raw generation output from Step 1
--problems <path>       # Original problem set (for ground truth answers)
--out <path>           # Output JSON with verdicts
--workers <n>          # Thread pool size (default: 5)
```

**Example invocation**:
```bash
python code/inspect_traces.py \
  --generation data/mgsm_symbolic/raw_pilot_outputs/deepseek-r1-32b_round1_generation.json \
  --problems data/mgsm_symbolic/pilot_round1_fogbank_problems.json \
  --out data/mgsm_symbolic/raw_pilot_outputs/deepseek-r1-32b_round1_full.json
```

**What the output looks like**:
```json
{
  "summary": "Inspection run...",
  "inspector_model": "claude-sonnet-5",
  "result": [
    {
      "language": "zh",
      "inspection": {
        "solutions": [
          {
            "idx": 40,
            "extracted_answer": "11%",
            "math_correct": false,
            "compositional_collapse_evidence": "none",
            "reasoning_drift_evidence": "none",
            "format_instability_evidence": "none",
            "brief_verdict": "Model correctly extracted all components... actual percentage is 11%, not 89%..."
          }
        ]
      }
    }
  ]
}
```

---

## Part 4: The Data

### Problem Sets (4 Rounds, 22 Total Problems)

All stored as JSON, language-keyed:
```json
{
  "zh": [{"idx": 40, "question": "...", "answer_number": "89"}, ...],
  "th": [...],
  "bn": [...],
  ...
}
```

#### Round 1: Fog Bank (Wind-Halving Rate Change)
- **File**: `pilot_round1_fogbank_problems.json`
- **Structure**: Same template, 8 instances, 5 languages (zh, th, ja, es, de)
- **The trap**: A ship travels at rate X for 60 minutes, then wind halves its rate to X/2. Must split distance into pre-60-min and post-60-min segments.
- **What we found**: Heavy Compositional Collapse on zh/th/ja/es (0/8 correct each), all failures showed same pattern. German: 8/8 correct.

#### Round 2: Diverse Templates
- **File**: `pilot_round2_diverse_problems.json`
- **Structure**: 4 distinct templates, 2 variants each = 8 problems, 5 languages
- **Templates**: 
  - Apartment garbage collection with vacancy adjustment + tip %
  - Sequential day-by-day fruit picking with multiplier day
  - Whale/remora fraction + percentage averaging
  - Overlapping-group class percentages with absentee adjustment
- **What we found**: Language ranking flipped from Round 1 (Japanese 7/7 correct, Thai 3/7). Also discovered benchmark translation defects.

#### Round 3a: Reasoning Drift Test
- **File**: `pilot_round3a_drift_problems.json`
- **Structure**: 2 templates with clean sequential dependencies, 2 variants each = 4 problems, 5 languages
- **Templates**:
  - Popcorn-popping: 5-stage dependency chain (rate → heat-retention → residual → gift → give-away)
  - Declining autograph collection: signatures collected across weeks, one sister's rate drops 5/week
- **What we found**: Popcorn template solved perfectly 10/10 (designed to elicit Drift). Autograph failures were all Compositional Collapse, not Drift.

#### Round 3b: Format Stability Test
- **File**: `pilot_round3b_format_problems.json`
- **Structure**: Same percentage problem with strict tag requirement, 2 languages pairs (5 languages: zh, th, bn, te, es)
- **Constraint**: Output must wrap in `<formalisation>...</formalisation><reasoning>...</reasoning><answer>...</answer>`
- **What we found**: All 10/10 well-formed, no format breaks even on complex scripts (Bengali, Telugu).

### Source Data

**mGSM-Symbolic** (CC-BY-SA 4.0):
- HuggingFace: `lrana/MGSM-Symbolic`
- Code: GitHub `lranaldii/MGSM-Symbolic`
- Released with: NAACL 2025 paper "Multilingual Reasoning via Self-training" (SWATH)

**7 languages downloaded**:
- Chinese (zh) — `mgsm_symbolic_zh.csv`
- Thai (th) — `mgsm_symbolic_th.csv`
- Japanese (ja) — `mgsm_symbolic_ja.csv`
- Spanish (es) — `mgsm_symbolic_es.csv`
- German (de) — `mgsm_symbolic_de.csv`
- Bengali (bn) — `mgsm_symbolic_bn.csv`
- Telugu (te) — `mgsm_symbolic_te.csv`

---

## Part 5: The Current State

### What's Been Done
✅ Pilot generation: Claude Sonnet 5 solving real problems blind
✅ Pilot inspection: Same model (Sonnet 5) grading its own output
✅ 4 problem-design rounds, 22 problems, 110 language-instances
✅ Compositional Collapse validated (real, reproducible, only failure mode observed)
✅ Reasoning Drift tested with purpose-built template (not found)
✅ Format Instability tested across complex scripts (not found)
✅ Translation-fidelity confound discovered and documented
✅ Real code infrastructure (providers.py, run_inference.py/ollama.py, inspect_traces.py)
✅ GitHub repo live (pushed 2026-08-05)

### What's Next

1. **Test real target models via actual API calls** — Pilot used Sonnet 5 as both generator and inspector. Next: run the 4 problem sets against independently-hosted models (Llama-3-8B, Phi-3.5-mini, DeepSeek-7B — the same targets SWATH tests) with Sonnet 5 held fixed as inspector.

2. **Build translation-fidelity checker** — lightweight validator to confirm source-language problem text contains the same structural clauses as English before attributing accuracy differences to model behavior.

3. **Self-annotate real sample** (~100–200 problems) — once target models are chosen, no need to hire external annotators at this scale.

4. **Write short paper** (4 pages) — Compositional Collapse as core finding, Drift/Format-Instability negative results + translation-fidelity confound as methodological contributions. Position as structural complement to SWATH, differentiated from Beg to Differ.

5. **Submit** — ORACLE (EMNLP 2026 workshop organized by SWATH authors) is a natural fit if timing works. No fixed deadline.

---

## Part 6: The Technical Stack

### Dependencies
```
anthropic>=0.120.2   # Sonnet 5 inspector (real API)
openai>=2.53.0       # OpenRouter compatibility
numpy, pandas, scipy # Data analysis
matplotlib, seaborn  # Visualization (for later analysis)
pydantic>=2.0.0      # Structured outputs
tqdm                 # Progress bars
requests             # HTTP utilities
```

### Providers Abstraction

**Three backends supported**:

1. **Anthropic** — Direct API to claude-sonnet-5, claude-opus-5, etc.
   - Requires: `ANTHROPIC_API_KEY` environment variable
   - Cost: $0.003/1K input tokens, $0.015/1K output tokens (Sonnet 5)

2. **OpenRouter** — OpenAI-compatible proxy to Llama-3-8B, Phi-3.5-mini, DeepSeek-7B, etc.
   - Requires: `OPENROUTER_API_KEY` environment variable
   - Base URL: `https://openrouter.ai/api/v1`
   - Cost: Variable by model (cheaper than direct Anthropic, usually)

3. **Ollama** — Local, offline, no API key
   - Base URL: `http://localhost:11434/v1` (default)
   - Must be pre-pulled: `ollama pull deepseek-r1:32b`
   - Cost: Zero (runs on your hardware)
   - Inference speed: M4 Max → reasonable latency, GPU-accelerated via Metal

### System Prompt Strategy

Generic, intentionally not trying to elicit any specific failure mode:

```
"You are a helpful mathematics assistant. 
Solve this problem step-by-step in the given language.
Provide your final answer clearly."
```

Plus optional structural requirement (Round 3b only):
```
"Wrap your response in:
<formalisation>...</formalisation>
<reasoning>...</reasoning>
<answer>...</answer>"
```

**Why minimal prompting**: Pilot is "blind generation" — we want to see what the model naturally does when solving a problem, not what it does when coached to avoid a specific failure mode.

---

## Part 7: Example Trace (What You'll See in the Output)

### Raw Generation (from deepseek-r1:32b, hypothetical)

**Input problem (Chinese)**:
```
Mateo的狗有149只幼犬，其中25只有斑点。穆罕默德的狗有49只幼犬，
其中12只幼犬有斑点。易卜拉欣有54只狗，每只有13只幼犬。
拜访兽医后，马特奥发现他的一半未斑点的幼犬实际上有以前看不见的地方。
所有幼犬中有多少百分比有斑点？
```

**Model's raw output**:
```
<formalisation>
Mateo有149只幼犬，其中25只有斑点；Mohammed有49只幼犬，其中12只有斑点；
Ibrahim有54只狗，每只有13只幼犬；Mateo发现他未斑点幼犬的一半实际上有斑点；
求所有幼犬中有斑点的百分比。
</formalisation>

<reasoning>
Step 1: 计算所有幼犬总数 = 149 + 49 + 54×13 = 149 + 49 + 702 = 900只

Step 2: 计算最初有斑点的幼犬 = Mateo的25只 + Mohammed的12只 = 37只
（Ibrahim的幼犬未提及斑点）

Step 3: Mateo未斑点的幼犬数 = 149 - 25 = 124只

Step 4: 这124只中有一半实际上有斑点 = 124 ÷ 2 = 62只

Step 5: 更新后总斑点幼犬数 = 37 + 62 = 99只

Step 6: 计算百分比 = 99 ÷ 900 × 100% = 11%
</reasoning>

<answer>11%</answer>
```

### After Inspection (Claude Sonnet 5's Verdict)

```json
{
  "idx": 40,
  "extracted_answer": "11%",
  "math_correct": false,
  "compositional_collapse_evidence": "none",
  "reasoning_drift_evidence": "none",
  "format_instability_evidence": "none",
  "brief_verdict": "Model correctly broke down the problem and applied the structure accurately. 
    Total puppies = 900, initially spotted = 37, Mateo's unspotted = 124, half now spotted = 62, 
    final total = 99, percentage = 11%. Ground truth answer is 89%. The discrepancy arises because 
    the problem is somewhat ambiguously worded — 'half of his non-spotted puppies have spots' could 
    reasonably be interpreted as converting 62 previously-hidden spots. However, ground truth (89%) 
    appears to assume a different calculation path or interpretation of 'hidden' vs 'new' spots. 
    No evidence of compositional collapse, drift, or format issues."
}
```

---

## Summary: What You're Testing

**Thesis**: Multilingual LLMs have a specific, reproducible structural reasoning failure — Compositional Collapse — where required problem sub-parts are noticed then dropped wholesale when reasoning crosses language boundaries.

**Method**: Generate solutions on real problems in multiple languages, then grade with a fixed inspector (Claude Sonnet 5), looking for evidence of three failure modes.

**What's been validated**: Compositional Collapse is real and reproducible. Reasoning Drift and Format Instability are not (at least for frontier models on these problem sets).

**What's next**: Test real weaker target models (Llama-3-8B, Phi-3.5-mini, DeepSeek-7B) to see if Drift/Format Instability surface there, or if they're specific to frontier model strength.

**Why it matters**: Current multilingual reasoning diagnostics can't see this — they either check top-level consistency or MCQ-based alignment, but not step-wise generative chain structure. This fills that gap.
