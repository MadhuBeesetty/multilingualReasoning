#!/bin/bash
# Backfill generation for small models on Apple M4 Pro
# GENERATION ONLY (no inspection) — optimized for local laptop execution
# Generates raw traces only; inspection done separately with Claude API later

set -e

cd "$(dirname "$0")" || exit 1

# ============================================================================
# CONFIG
# ============================================================================

MODELS=(
    "phi3.5"
    "neural-chat:7b"
    "mistral-nemo:12b"
    "deepseek-r1:14b"
)

ROUNDS=(
    "1:fogbank"
    "2:diverse"
    "3a:drift"
    "3b:format"
)

DATA_DIR="data/mgsm_symbolic"
OUT_DIR="$DATA_DIR/raw_pilot_outputs"
LOG_FILE="backfill_generation.log"
WORKERS=8  # M4 Pro: 12 cores, 24GB RAM — 8 workers is good balance

# ============================================================================
# LOGGING
# ============================================================================

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"
}

log_section() {
    echo "" | tee -a "$LOG_FILE"
    echo "================================================================================" | tee -a "$LOG_FILE"
    echo "$*" | tee -a "$LOG_FILE"
    echo "================================================================================" | tee -a "$LOG_FILE"
}

# ============================================================================
# INITIALIZATION
# ============================================================================

log_section "BACKFILL GENERATION - LAPTOP (M4 Pro)"
log "Timestamp: $(date)"
log "Models: ${MODELS[@]}"
log "Rounds: ${ROUNDS[@]}"
log "New languages: it, fr, ru, sw"
log "Workers: $WORKERS"
log "Log file: $LOG_FILE"
log "NOTE: Generation only (no inspection) — inspection done separately later"

# ============================================================================
# PRE-FLIGHT CHECKS
# ============================================================================

log_section "PRE-FLIGHT CHECKS"

# Check Ollama is reachable
log "Checking Ollama server..."
if curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
    log "✅ Ollama server reachable"
else
    log "❌ ERROR: Ollama server not found at http://localhost:11434"
    log "Please run: ollama serve"
    exit 1
fi

# Check Python
log "Checking Python environment..."
if python --version 2>&1 | tee -a "$LOG_FILE"; then
    log "✅ Python available"
else
    log "❌ ERROR: Python not found"
    exit 1
fi

# Check required scripts exist
log "Checking scripts..."
if [ ! -f "code/run_inference_ollama.py" ]; then
    log "❌ ERROR: code/run_inference_ollama.py not found"
    exit 1
fi
if [ ! -f "code/create_filtered_problems.py" ]; then
    log "❌ ERROR: code/create_filtered_problems.py not found"
    exit 1
fi
log "✅ All scripts found"

# ============================================================================
# STEP 1: CREATE FILTERED PROBLEM FILES
# ============================================================================

log_section "STEP 1: Creating Filtered Problem Files"

if [ -f "$DATA_DIR/pilot_round1_fogbank_newlangs_problems.json" ]; then
    log "✅ Filtered problems already exist, skipping creation"
else
    log "Creating filtered problem files..."
    python code/create_filtered_problems.py 2>&1 | tee -a "$LOG_FILE"
    log "✅ Filtered problems created"
fi

# Verify all 4 filtered files exist
for round_spec in "${ROUNDS[@]}"; do
    IFS=':' read -r round_num round_name <<< "$round_spec"
    filtered_file="$DATA_DIR/pilot_round${round_num}_${round_name}_newlangs_problems.json"
    if [ ! -f "$filtered_file" ]; then
        log "❌ ERROR: Missing $filtered_file"
        exit 1
    fi
done
log "✅ All 4 filtered problem files verified"

# ============================================================================
# STEP 2: GENERATION PASS (ALL MODELS)
# ============================================================================

log_section "STEP 2: Generation Pass - All Models"

TOTAL_MODELS=${#MODELS[@]}
TOTAL_ROUNDS=${#ROUNDS[@]}
TOTAL_RUNS=$((TOTAL_MODELS * TOTAL_ROUNDS))
CURRENT_RUN=0

for model_idx in "${!MODELS[@]}"; do
    model="${MODELS[$model_idx]}"
    model_num=$((model_idx + 1))

    log_section "MODEL $model_num/$TOTAL_MODELS: $model"
    log "Starting generation for $model..."

    for round_spec in "${ROUNDS[@]}"; do
        IFS=':' read -r round_num round_name <<< "$round_spec"
        CURRENT_RUN=$((CURRENT_RUN + 1))

        PROBLEMS_FILE="$DATA_DIR/pilot_round${round_num}_${round_name}_newlangs_problems.json"
        GEN_FILE="$OUT_DIR/round${round_num}_${model}_backfill_generation.json"

        log "[$CURRENT_RUN/$TOTAL_RUNS] Round $round_num ($round_name)"
        log "  → Generating traces (workers=$WORKERS)..."

        if python code/run_inference_ollama.py \
            --problems "$PROBLEMS_FILE" \
            --model "$model" \
            --out "$GEN_FILE" \
            --workers "$WORKERS" 2>&1 | tee -a "$LOG_FILE"; then

            # Verify output file
            if [ -f "$GEN_FILE" ]; then
                FILE_SIZE=$(du -h "$GEN_FILE" | cut -f1)
                log "  ✅ Generated ($FILE_SIZE)"
            else
                log "  ❌ ERROR: Output file not created"
                exit 1
            fi
        else
            log "❌ Generation failed for $model round $round_num"
            exit 1
        fi
    done

    log "✅ $model generation complete!"
done

# ============================================================================
# STEP 3: VERIFICATION
# ============================================================================

log_section "VERIFICATION"

EXPECTED_FILES=$((TOTAL_MODELS * TOTAL_ROUNDS))
ACTUAL_FILES=$(ls "$OUT_DIR"/*backfill*generation.json 2>/dev/null | wc -l)

log "Expected generation files: $EXPECTED_FILES (${TOTAL_MODELS} models × ${TOTAL_ROUNDS} rounds)"
log "Actual generation files: $ACTUAL_FILES"

if [ "$ACTUAL_FILES" -eq "$EXPECTED_FILES" ]; then
    log "✅ All generation files created successfully"
else
    log "⚠️  File count mismatch (expected $EXPECTED_FILES, got $ACTUAL_FILES)"
fi

# List all backfill generation files with sizes
log "Backfill generation files created:"
ls -lh "$OUT_DIR"/*backfill*generation.json 2>/dev/null | awk '{print "  " $9 " (" $5 ")"}' | tee -a "$LOG_FILE"

TOTAL_SIZE=$(du -sh "$OUT_DIR"/*backfill*generation.json 2>/dev/null | tail -1 | awk '{print $1}')
log "Total size of generation files: $TOTAL_SIZE"

# ============================================================================
# COMPLETION
# ============================================================================

log_section "GENERATION COMPLETE ✅"
log "Timestamp: $(date)"
log "All results in: $OUT_DIR"
log "Log file: $LOG_FILE"
log ""
log "Next steps:"
log "  1. Commit generation files to GitHub"
log "  2. Run inspection pass separately (with Claude API) when ready"
log "  3. Merge backfill results with original 7-language results in analysis"
log ""

echo ""
echo "================================================================================"
echo "✅ GENERATION FINISHED SUCCESSFULLY"
echo "================================================================================"
echo "Files: $ACTUAL_FILES/$EXPECTED_FILES created"
echo "Size: $TOTAL_SIZE"
echo "Location: $OUT_DIR"
echo "Log: $LOG_FILE"
echo ""
echo "Ready to commit to GitHub!"
