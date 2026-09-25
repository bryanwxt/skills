#!/usr/bin/env bash
# A/B value eval: the same tasks with bare superpowers vs superpowers plus the lenses,
# graded by a blind judge against rubrics of planted problems.
# Usage: bash evals/lenses/value/run.sh [-n reps] [-m model] [-J judge-model] [-j parallel] [task ...]
#   tasks: v1 (design) v2 (review) v3 (debug) v4 (bounded change); default: all
set -euo pipefail

HERE=$(cd "$(dirname "$0")" && pwd)
ROOT=$(cd "$HERE/../../.." && pwd)

if [ "${1:-}" = "--one" ]; then   # internal: --one <prompt-file> <out-json> <model> <add-dir>...
  prompt=$2; dest=$3; model=$4; shift 4
  claude -p --model "$model" --output-format json --setting-sources project --disable-slash-commands \
    --no-session-persistence --allowedTools Read Glob Grep --add-dir "$@" < "$prompt" > "$dest" 2> "$dest.err" \
    || echo "run failed: $dest"
  exit 0
fi

reps=5; model=sonnet; judge=opus; jobs=6
while getopts "n:m:J:j:" o; do
  case $o in n) reps=$OPTARG;; m) model=$OPTARG;; J) judge=$OPTARG;; j) jobs=$OPTARG;; *) exit 2;; esac
done
shift $((OPTIND-1))
tasks=("$@"); [ ${#tasks[@]} -eq 0 ] && tasks=(v1 v2 v3 v4)

command -v claude >/dev/null || { echo "needs the claude CLI"; exit 1; }
SP=$(bash "$ROOT/software-design/scripts/check-superpowers.sh" | sed -n 's/^superpowers: //p')
[ -n "$SP" ] || { echo "superpowers not found; set SUPERPOWERS_SKILLS"; exit 1; }

out="$HERE/results/$(date +%Y%m%d-%H%M%S)-$model"
mkdir -p "$out/runs"
python3 "$HERE/value.py" prepare "$out" "$SP" "$ROOT" "${tasks[@]}"
dirs="$ROOT $(dirname "$SP") $out"
echo "superpowers: $SP"
echo "results: $out (${tasks[*]}; bare vs lens; $reps runs each; model $model; judge $judge)"

echo "1/3 answering"
for t in "${tasks[@]}"; do for arm in bare lens; do for i in $(seq 1 "$reps"); do
  echo "$out/prompts/$t-$arm.md $out/runs/$t-$arm-$i.json"
done; done; done |
  xargs -P "$jobs" -n 2 sh -c 'bash "$0" --one "$1" "$2" "'"$model"'" '"$dirs" "$HERE/run.sh"
python3 "$HERE/value.py" extract "$out"

echo "2/3 judging (blind)"
python3 "$HERE/value.py" blind "$out"
for p in "$out"/judge/*.prompt.md; do echo "$p ${p%.prompt.md}.json"; done |
  xargs -P "$jobs" -n 2 sh -c 'bash "$0" --one "$1" "$2" "'"$judge"'" '"$dirs" "$HERE/run.sh"

echo "3/3 summary"
python3 "$HERE/value.py" summarize "$out"
