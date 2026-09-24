#!/usr/bin/env bash
# Verifies references/coordination.md is identical in the three superpowers lens skills. Run from the repo root.
set -euo pipefail
files=(software-design/references/coordination.md
       clean-python/references/coordination.md
       data-intensive/references/coordination.md)
status=0
for f in "${files[@]:1}"; do
  if ! cmp -s "${files[0]}" "$f"; then echo "DRIFT: $f differs from ${files[0]}"; diff "${files[0]}" "$f" || true; status=1; fi
done
[ $status -eq 0 ] && echo "OK: coordination.md identical in ${#files[@]} skills"
exit $status
