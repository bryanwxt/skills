#!/usr/bin/env bash
# Verifies the files shared by the three superpowers lens skills are identical. Run from the repo root.
set -euo pipefail
lenses=(software-design clean-python data-intensive)
shared=(references/coordination.md SETUP.md scripts/check-superpowers.sh)
status=0
for s in "${shared[@]}"; do
  for l in "${lenses[@]:1}"; do
    if ! cmp -s "${lenses[0]}/$s" "$l/$s"; then
      echo "DRIFT: $l/$s differs from ${lenses[0]}/$s"; diff "${lenses[0]}/$s" "$l/$s" || true; status=1
    fi
  done
done
[ $status -eq 0 ] && echo "OK: ${shared[*]} identical in ${#lenses[@]} skills"
exit $status
