#!/bin/bash
# Run a practice trial for tiny-chess-01-r9.
# Usage: ./run_trial.sh <trial> [engine_dir]
#   trial: 0, 1, or 2 (practice/trial-N)
#   engine_dir: dir holding main.py (default: this script's dir)
set -u
TRIAL="${1:-0}"
ENG="${2:-$(dirname "$0")}"
KIT="$HOME/workspace/makefun/tiny-chess-01-kit"
PORT="${3:-18241}"
STATE="/tmp/r9_state_t$TRIAL"
rm -rf "$STATE"; mkdir -p "$STATE"
# Start env server
MAKEFUN_ENV_DATA_DIR="$KIT/practice/trial-$TRIAL/input/env" \
MAKEFUN_STATE_DIR="$STATE" \
MAKEFUN_ENV_PORT="$PORT" \
node "$KIT/program/env/server.mjs" > "$STATE/env.log" 2>&1 &
ENVPID=$!
# Wait for ready file
for i in $(seq 1 50); do
  [ -f "$STATE/ready" ] && break
  sleep 0.2
done
cat "$STATE/ready" 2>/dev/null
echo "env pid $ENVPID"
# Run the engine
cd "$ENG"
MAKEFUN_ENV_URL="http://127.0.0.1:$PORT" \
MAKEFUN_TRIAL_SEED="r9trial$TRIAL" \
timeout 1700 python3 main.py > "$STATE/engine.log" 2>&1
echo "engine exit: $?"
# Export state from env server
kill -TERM $ENVPID
sleep 1
kill -9 $ENVPID 2>/dev/null
ls -la "$STATE/export/" 2>/dev/null
# Score
MAKEFUN_OUTPUT_DIR="$STATE/export" \
MAKEFUN_REFERENCE_DIR="$KIT/practice/trial-$TRIAL/reference" \
MAKEFUN_SCORES_DIR="$STATE/scores" \
node "$KIT/program/scorer/score.mjs"
echo "--- state games ---"
python3 -c "
import json
d=json.load(open('$STATE/export/state.json'))
for g in d['games']:
    print(g['game'], g['opponent'], g['colour'], g['outcome'], g['reason'], len(g['moves']), 'plies')
"
