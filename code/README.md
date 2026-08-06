# Multilingual Reasoning — Real-Model Experiment Runner

Re-runs the pilot's methodology against a real, independently-hosted
model-under-test (generator), while keeping Claude Sonnet 5 fixed as the
inspector — so only the generator varies across experiments.

## Setup

```bash
pip install -r ../requirements.txt
pip install -U anthropic  # required: repo pin (>=0.28.0) predates output_config
                           # structured outputs, current model IDs, and the
                           # refusal stop reason used by these scripts
```

## Environment variables (never pass keys as CLI args)

- `ANTHROPIC_API_KEY` — always required (used by the fixed inspector always,
  and by the generator if `--provider anthropic`).
- `OPENROUTER_API_KEY` — required only if `--provider openrouter`.

## Usage

Two-step pipeline: generate, then inspect.

```bash
python run_inference.py --problems ../data/mgsm_symbolic/pilot_round1_fogbank_problems.json \
  --provider openrouter --model meta-llama/llama-3-8b-instruct \
  --out ../data/mgsm_symbolic/raw_pilot_outputs/round1_llama3-8b_generation.json

python inspect_traces.py --generation ../data/mgsm_symbolic/raw_pilot_outputs/round1_llama3-8b_generation.json \
  --problems ../data/mgsm_symbolic/pilot_round1_fogbank_problems.json \
  --out ../data/mgsm_symbolic/raw_pilot_outputs/round1_llama3-8b_full.json
```

Works unmodified on any of the four `pilot_round*_problems.json` files.

## Notes

- `--require-format-tags` (off by default) adds the strict
  `<formalisation>/<reasoning>/<answer>` structural requirement to the
  generation prompt — only use it with `pilot_round3b_format_problems.json`-style
  runs.
- `--workers` controls generation/inspection concurrency (default 5).
- Failed generations/inspections are recorded inline (`[GENERATION_ERROR]` /
  `[INSPECTION_ERROR]` markers) rather than aborting the run, so a
  partially-failed run still produces usable output.
- `inspect_traces.py` always uses `claude-sonnet-5` as the inspector,
  regardless of what generated the traces — this is intentional.
