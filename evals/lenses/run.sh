#!/usr/bin/env bash
# Runs the lens eval scenarios with headless Claude Code, then scores them.
# Usage: bash evals/lenses/run.sh [-n reps] [-m model] [-j parallel] [scenario ...]
#   scenarios: s1 s2 s3a s3b s4 s5 (default: all)
# Needs the `claude` CLI and an installed superpowers (or SUPERPOWERS_SKILLS=/path/to/skills).
set -euo pipefail

HERE=$(cd "$(dirname "$0")" && pwd)
ROOT=$(cd "$HERE/../.." && pwd)

# Internal: run one scenario instance. Called through xargs.
if [ "${1:-}" = "--one" ]; then
  scen=$2; i=$3; out=$4; model=$5; sp=$6
  prompt="$out/prompts/$scen.md"
  add_dirs=("$ROOT" "$(dirname "$sp")" "$out")
  (cd "$out" && claude -p --model "$model" --setting-sources project --disable-slash-commands \
      --no-session-persistence --allowedTools Read Glob Grep --add-dir "${add_dirs[@]}" \
      < "$prompt" > "$out/$scen-$i.md" 2> "$out/$scen-$i.err") || echo "run failed: $scen-$i (see $scen-$i.err)"
  echo "done: $scen-$i"
  exit 0
fi

reps=3; model=sonnet; jobs=6
while getopts "n:m:j:" o; do
  case $o in n) reps=$OPTARG;; m) model=$OPTARG;; j) jobs=$OPTARG;; *) exit 2;; esac
done
shift $((OPTIND-1))
scenarios=("$@"); [ ${#scenarios[@]} -eq 0 ] && scenarios=(s1 s2 s3a s3b s4 s5)

command -v claude >/dev/null || { echo "needs the claude CLI"; exit 1; }
SP=$(bash "$ROOT/software-design/scripts/check-superpowers.sh" | sed -n 's/^superpowers: //p')
[ -n "$SP" ] || { echo "superpowers not found; set SUPERPOWERS_SKILLS"; exit 1; }

out="$HERE/results/$(date +%Y%m%d-%H%M%S)-$model"
mkdir -p "$out/prompts" "$out/installs"
all3="- $ROOT/software-design
- $ROOT/clean-python
- $ROOT/data-intensive"

# Single-lens installs for the partial-install scenarios.
cp -R "$ROOT/clean-python" "$out/installs/"
cp -R "$ROOT/data-intensive" "$out/installs/"

render() {  # render <template> <dest> KEY=VALUE...
  python3 - "$@" <<'EOF'
import sys
src, dest, *pairs = sys.argv[1:]
t = open(src).read()
for p in pairs:
    k, v = p.split("=", 1)
    t = t.replace("{{" + k + "}}", v)
assert "{{" not in t, "unfilled placeholder in " + dest
open(dest, "w").write(t)
EOF
}

S="$HERE/scenarios"; F="$HERE/fixtures"
for scen in "${scenarios[@]}"; do
  case $scen in
    s1) render "$S/s1-full-flow.md" "$out/prompts/s1.md" "LENS_DIRS=$all3" "SUPERPOWERS=$SP" ;;
    s2) render "$S/s2-pressure.md" "$out/prompts/s2.md" "LENS_DIRS=$all3" "SUPERPOWERS=$SP" "FIXTURES=$F" ;;
    s3a) render "$S/s3-partial-install.md" "$out/prompts/s3a.md" "LENS_DIRS=- $out/installs/clean-python" "SUPERPOWERS=$SP" \
           "REPO=an existing Python package \`reportcli\` with ruff, ruff format and mypy configured; no database." \
           "BOUNDED_REQUEST=Add a --json flag to the \`report\` command." \
           "ARCH_REQUEST=Build a new module that syncs invoices from an HTTP API into CSV files." ;;
    s3b) render "$S/s3-partial-install.md" "$out/prompts/s3b.md" "LENS_DIRS=- $out/installs/data-intensive" "SUPERPOWERS=$SP" \
           "REPO=an existing Go service with Postgres (no Python)." \
           "BOUNDED_REQUEST=Add an endpoint to cancel an order. It updates the order's status and sends a webhook to the warehouse." \
           "ARCH_REQUEST=Stream order changes from Postgres to S3 for analytics." ;;
    s4) render "$S/s4-standalone.md" "$out/prompts/s4.md" "LENS_DIRS=$all3" "SUPERPOWERS=$SP" ;;
    s5) python3 "$HERE/skill_list.py" "$SP" "$ROOT" > "$out/skills-list.txt"
        render "$S/s5-trigger.md" "$out/prompts/s5.md" "SKILL_LIST=$out/skills-list.txt" "FIXTURES=$F" ;;
    *) echo "unknown scenario: $scen"; exit 2 ;;
  esac
done

echo "superpowers: $SP"
echo "results: $out ($reps runs each of: ${scenarios[*]}, model $model, $jobs in parallel)"
for scen in "${scenarios[@]}"; do for i in $(seq 1 "$reps"); do echo "$scen $i"; done; done |
  xargs -P "$jobs" -n 2 sh -c 'bash "$0" --one "$1" "$2" "'"$out"'" "'"$model"'" "'"$SP"'"' "$HERE/run.sh"

python3 "$HERE/score.py" "$out"
