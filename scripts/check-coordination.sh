#!/usr/bin/env bash
# Verifies the shared "Coordination with the other lenses" block is identical
# in the three superpowers lens skills. Run from the repo root.
set -euo pipefail
files=(software-design/references/superpowers-hooks.md
       clean-python/references/superpowers-hooks.md
       data-intensive/references/superpowers-hooks.md)
extract() { sed -n '/<!-- coordination:start/,/<!-- coordination:end -->/p' "$1"; }
ref=$(extract "${files[0]}")
[ -n "$ref" ] || { echo "No coordination block in ${files[0]}"; exit 1; }
status=0
for f in "${files[@]:1}"; do
  if ! diff <(echo "$ref") <(extract "$f") >/dev/null; then
    echo "DRIFT: $f differs from ${files[0]}"; diff <(echo "$ref") <(extract "$f") || true; status=1
  fi
done
[ $status -eq 0 ] && echo "OK: coordination block identical in ${#files[@]} files"
exit $status
