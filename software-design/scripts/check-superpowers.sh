#!/usr/bin/env bash
# Checks that the installed superpowers still has every anchor the lenses hook into.
# Identical in software-design, clean-python and data-intensive. Run: bash scripts/check-superpowers.sh
# Override the location with SUPERPOWERS_SKILLS=/path/to/superpowers/skills.
set -uo pipefail

TESTED_VERSION="6.4.1"

find_skills_dir() {
  if [ -n "${SUPERPOWERS_SKILLS:-}" ]; then echo "$SUPERPOWERS_SKILLS"; return; fi
  local best="" best_key=""
  for d in "$HOME"/.claude/plugins/cache/*/superpowers/*/skills; do
    [ -d "$d" ] || continue
    local v; v=$(basename "$(dirname "$d")")
    # zero-padded sort key so 6.10.0 sorts after 6.9.0
    local key; key=$(echo "$v" | awk -F. '{printf "%05d%05d%05d", $1, $2, $3}')
    if [ -z "$best_key" ] || [[ "$key" > "$best_key" ]]; then best="$d"; best_key="$key"; fi
  done
  echo "$best"
}

SKILLS=$(find_skills_dir)
if [ -z "$SKILLS" ] || [ ! -d "$SKILLS" ]; then
  echo "FAIL: superpowers not found. Install it from obra/superpowers-marketplace, or set SUPERPOWERS_SKILLS."
  exit 1
fi
VERSION=$(basename "$(dirname "$SKILLS")")
echo "superpowers: $SKILLS"

status=0
# file|exact text the lenses rely on|what breaks without it
anchors=(
  "brainstorming/SKILL.md|**Spike**|path names the lenses key bounded/spike behaviour on"
  "brainstorming/SKILL.md|**Bounded**|path names the lenses key bounded/spike behaviour on"
  "brainstorming/SKILL.md|**Architectural**|path names the lenses key bounded/spike behaviour on"
  "brainstorming/SKILL.md|Cover: architecture, components, data flow, error handling, testing|the spec headings lens subsections sit under"
  "brainstorming/SKILL.md|docs/superpowers/specs/|where specs are written"
  "writing-plans/SKILL.md|## Global Constraints|plan slot for lens invariants"
  "writing-plans/SKILL.md|## Review Focus|plan slot for lens failure modes"
  "writing-plans/SKILL.md|**Interfaces:**|per-task slot for module interfaces"
  "writing-plans/SKILL.md|## Task Right-Sizing|rule the lens dependency order works with"
  "subagent-driven-development/SKILL.md|scripts/task-brief|brief = plan task verbatim, so lens content must live in the plan"
  "subagent-driven-development/task-reviewer-prompt.md|[GLOBAL_CONSTRAINTS]|per-task reviewer's only lens input"
  "requesting-code-review/code-reviewer.md|[PLAN_OR_REQUIREMENTS]|where review-lens.md goes for final reviews"
)
for a in "${anchors[@]}"; do
  IFS='|' read -r file text why <<< "$a"
  if [ -f "$SKILLS/$file" ] && grep -qF -- "$text" "$SKILLS/$file"; then
    echo "  ok       $file: $text"
  else
    echo "  MISSING  $file: $text  ($why)"
    status=1
  fi
done

if [ $status -ne 0 ]; then
  echo "FAIL: superpowers $VERSION has changed where the lenses hook in. Lens hooks may point at mechanisms that no longer exist; check the lens repo for an update before relying on them."
elif [ "$VERSION" != "$TESTED_VERSION" ]; then
  echo "OK (with warning): all anchors present, but superpowers $VERSION differs from the tested $TESTED_VERSION. Re-run the lens scenarios if behaviour looks off."
else
  echo "OK: superpowers $VERSION matches the tested version and every anchor is present."
fi
exit $status
