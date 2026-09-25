# Lens rules for writing-plans

<!-- steps-writing-plans:start — identical in software-design, clean-python and data-intensive; check with scripts/check-coordination.sh in the lens repo -->
Read one copy, from any lens, when this superpowers step starts. It holds the shared rules for the step, then one section per lens: skip the sections of lenses that aren't installed. `references/coordination.md` has the rules for every step.


## Shared

**Plan.** writing-plans sets the plan's shape: the header, **Global Constraints**, **Review Focus**, and right-sized tasks, each with an `Interfaces: Consumes / Produces` block. Lenses fill those slots. They add no plan sections of their own, and no task that a reviewer couldn't reject separately from its neighbours. The lens content lives in the plan because it's the only place it reaches subagents (see `references/steps/execution.md`: implementers and per-task reviewers read only the plan).
- **Global Constraints** (one line each, exact values): the invariants that bind every task.
  - data: each guarantee and its mechanism, the isolation level, the idempotency keys, "publish only via the outbox", expand-only schema changes;
  - python: Python version, typing level, the exact check commands;
  - design: knowledge-hiding rules that span tasks, e.g. "only `search/indexer.py` imports the Elasticsearch client".
- **Review Focus:** the lenses propose candidates, as concrete conditions with the expected behaviour, e.g. "two concurrent votes by one user on one poll → exactly one is counted". writing-plans still keeps the five most likely. Each line gets its pinning test in the task that owns the code.
- **Each task:**
  - `Interfaces: Produces` holds the typed signatures with their one-line interface comments;
  - the body carries the module card for any module the task creates or reshapes, at most 5 applicable Python rules, and the guarantee the task must preserve, plus the test that proves it.

**Dependency order** (applies across right-sized tasks; skip what doesn't apply):
1. tooling config and interface stubs fold into the first task whose deliverable needs them, never a standalone task;
2. characterization tests before any behaviour-preserving refactor of that code, in the same task or an earlier one;
3. refactors are green before behaviour changes;
4. a module's interface lands in the task that first produces it, before any task that consumes it;
5. constraints, unique indexes, idempotency tables and the outbox land in or before the first task that relies on them;
6. schema changes: expand → migrate and backfill → switch readers → contract, each a separately deployable task.

Every task ends with its verification commands. List every deviation from the approved spec (including test strategy) under **Deviations**, and ask before committing it.

## software-design

### writing-plans
Fill writing-plans' slots as the shared rules above describe:
- Build in increments of abstractions, not features.
- The task that first produces a module puts its signatures and interface comments in `Interfaces: Produces`, and its module card (abstraction, what it hides, errors) in the task body.
- Global Constraints: one line per knowledge-hiding rule that spans tasks ("only `X` knows `Y`").
- Behaviour-preserving refactors are green before behaviour changes. A refactor is its own task only if a reviewer could reject it on its own.
- A task that edits many modules for one change points to leakage; send it back to the spec.


## clean-python

### writing-plans
Fill writing-plans' slots as the shared rules above describe:
- Give exact `src/…` and `tests/…` paths.
- **Global Constraints:** Python version, typing level, and the exact check commands.
- **Missing tooling:** the first task that needs the checks adds the formatter, linter, type checker and pytest config, wired into CI, in its opening steps. Never make it a standalone task.
- Every task ends with commands and their expected results: `pytest …`, `ruff check …`, `mypy …`, and the formatter check.
- `Interfaces: Produces` gives typed signatures, each with its docstring summary.
- Each task body lists the Python rules that apply to it (at most 5):
  - types and docstrings on public functions;
  - no mutable defaults, bare `except`, or `assert` used for validation;
  - `raise … from e`;
  - `with` for resources;
  - inject dependencies;
  - composition rather than inheritance for reuse;
  - no blocking I/O in `async def`.
- Big modules become packages that re-export the old names.


## data-intensive

### writing-plans
Fill writing-plans' slots as the shared rules above describe:
- **Global Constraints:** each guarantee and its mechanism, the isolation level (read from config), the idempotency keys, "publish only via the outbox", expand-only schema changes.
- **Review Focus:** race, duplicate, retry and failover conditions as concrete lines, e.g. "the same import file processed twice → its rows stored once". Put the pinning test in the task that owns the code.
- **Each task** names the guarantee it preserves and the test that proves it.
- Schema change as expand → migrate → contract, one independently deployable task per step. Note any DDL that locks or rewrites a table.
- Backfills are resumable and throttled, and end with a verification query.
- The outbox or CDC lands in or before the first task that publishes events.
- Constraints, unique indexes, and idempotency tables land in or before the first task that relies on them.
- Verification includes migrate up and down on a copy, plus the race and idempotency tests.
<!-- steps-writing-plans:end -->
