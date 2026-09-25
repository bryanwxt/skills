# Lens rules for systematic-debugging

<!-- steps-debugging:start — identical in software-design, clean-python and data-intensive; check with scripts/check-coordination.sh in the lens repo -->
Read one copy, from any lens, when this superpowers step starts. It holds the shared rules for the step, then one section per lens: skip the sections of lenses that aren't installed. `references/coordination.md` has the rules for every step.


## software-design

### systematic-debugging
- Don't redesign mid-fix.
- After the fix, record any design root cause (duplicated knowledge, a special case in a general mechanism, an error that should have been defined away) as a follow-up.


## clean-python

### systematic-debugging
- **Phase 1 suspects:**
  - mutable default or shared class attribute;
  - late-binding closure;
  - iterator consumed twice;
  - subclassing `dict` or `list`;
  - `__getattr__` not raising `AttributeError`;
  - patching the wrong name;
  - import-time side effects;
  - `is` vs `==`;
  - float precision;
  - naive vs aware datetimes;
  - bytes vs str;
  - blocking calls in async code;
  - asserts stripped by `-O`.
- **Tools:** `breakpoint()`, `python -X dev`, `faulthandler`, `tracemalloc`, `pytest -x --lf -vv --pdb`, `-W error`, `cProfile`.
- **After the fix:** keep the regression test, and search for sibling occurrences to list as follow-ups.


## data-intensive

### systematic-debugging
- **Phase 1:** name at least 2 suspects from `references/review-checklist.md` Part 2, with one line each on why it's ruled in or out, before reading further:
  - stale read → replication lag;
  - lost update → read-modify-write race;
  - duplicates → a retry without idempotency;
  - two leaders → no fencing;
  - later write overwritten → last-write-wins with clock skew;
  - hot shard → key skew;
  - derived store drift → dual write.
- Reproduce races with two connections, and show the failing output before the fix.
- **After the fix:**
  - keep the regression test;
  - name any remaining duplicate sources of truth (e.g. a counter vs a row count) as follow-ups;
  - don't fold "not found" into a domain error.

  Architectural causes become a flow-B review or a brainstorming request. End with the lens-check line from SKILL.md.
<!-- steps-debugging:end -->
