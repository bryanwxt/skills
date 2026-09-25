# Lens rules for verification-before-completion

<!-- steps-verification:start — identical in software-design, clean-python and data-intensive; check with scripts/check-coordination.sh in the lens repo -->
Read one copy, from any lens, when this superpowers step starts. It holds the shared rules for the step, then one section per lens: skip the sections of lenses that aren't installed. `references/coordination.md` has the rules for every step.


## clean-python

### verification-before-completion
"Verified" means showing the output of:
- `pytest`, with pass counts;
- the linter;
- the type checker;
- the formatter in check mode.

If a tool isn't configured, say so.


## data-intensive

### verification-before-completion
- Show the output of: migrations up and down, the race and idempotency tests against the real engine, and the backfill verification query.
- Don't claim "safe under concurrency" without a race test, or "no data loss" without a failure test.
<!-- steps-verification:end -->
