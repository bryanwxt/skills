# Lens rules for subagent-driven-development / executing-plans

<!-- steps-execution:start — identical in software-design, clean-python and data-intensive; check with scripts/check-coordination.sh in the lens repo -->
Read one copy, from any lens, when this superpowers step starts. It holds the shared rules for the step, then one section per lens: skip the sections of lenses that aren't installed. `references/coordination.md` has the rules for every step.


## Shared

**Execution and review**
- **Implementer:** both execution skills work from the plan task itself. subagent-driven-development's `task-brief` script extracts it verbatim, and the brief is the single source of requirements. Add nothing lens-specific to the dispatch. If a task lacks lens content it needs, treat it as a plan gap: rule on it and ledger it, as subagent-driven-development says for plan corrections.
- **Per-task reviewer:** the dispatch is subagent-driven-development's own, and the lenses reach it through two of its inputs:
  - the brief;
  - `[GLOBAL_CONSTRAINTS]`, which is the plan file's `## Global Constraints` lines, copied as they stand in the plan.
- **When a review must look harder at something** (an incident, or "make sure reviewers catch X"), do these steps in order:
  1. Edit the plan: add a concrete Review Focus line (e.g. "two concurrent votes by one user on one poll → exactly one is counted"), or a Global Constraint, and put its pinning test in the task that owns the code.
  2. Ledger the edit as a plan correction.
  3. Dispatch the review as above. The copied Global Constraints and the brief now carry it.

## software-design

### execution (subagent-driven / executing-plans)
- The module card reaches the implementer through the plan task. Add nothing to the dispatch (shared rules above).
- An implementer who finds an interface problem raises it, never silently redesigns. Local fixes inside the module are fine.


## clean-python

### execution (subagent-driven / executing-plans)
The Python rules reach the implementer through the plan task. Add nothing to the dispatch (shared rules above). Report done only with the tool output attached. If the planned interface forces un-Pythonic code, raise it rather than working around it.


## data-intensive

### execution (subagent-driven / executing-plans)
- The guarantee, isolation level, idempotency key, and outbox rule reach the implementer through Global Constraints and the plan task. Add nothing to the dispatch (shared rules above).
- If the planned approach can't provide the guarantee, raise it; don't work around it.
<!-- steps-execution:end -->
