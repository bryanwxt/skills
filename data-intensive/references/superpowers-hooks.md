# data-intensive: hooks per superpowers step

Rules shared with the other lenses (questions, spec outline, plan order, tests, bounded changes, reviews) live in `coordination.md`. This file adds only the data lens. Stay silent on work with no data-guarantee, scale, concurrency, schema, messaging, or multi-store concern.

## brainstorming (architectural): the data track
- **Context:** note:
  - the stores;
  - the source of truth for each entity;
  - the actual isolation level (from config);
  - replication;
  - queues and pipelines;
  - migration tooling;
  - dual writes already present.
- **Questions:** use `question-bank.md` §1, within the shared budget and order. Load and domain answers are facts; guarantees are choices.
- **Approaches:** 2–3 data architectures that differ in substance:
  - where the source of truth lives;
  - how derived data is produced (sync, CDC, batch);
  - whether to partition, and by what key;
  - where correctness is enforced.

  Compare them on guarantees met, headroom against growth, failure behaviour, operational burden, and cost of change. Say plainly when one database is enough.
- **Spec** (`assets/spec-sections.md`, placed under brainstorming's headings):
  - Architecture: load and targets, guarantees → mechanisms, systems of record;
  - Data flow: the diagram, data model, replication and partitioning, correctness mechanisms, encoding and evolution;
  - Error handling: failure-analysis rows in the shared error table;
  - Testing: tests against the real engine;
  - Implementation notes: operations, product facts.
- **Self-review:**
  - one source of truth per entity;
  - every guarantee is named, along with its mechanism;
  - no dual writes (use an outbox or CDC);
  - every side effect has stated delivery semantics;
  - retried writes carry an idempotency key enforced at the store;
  - no ordering by wall clock across nodes;
  - no locks without fencing;
  - schema changes are expand → migrate → contract;
  - the failure analysis covers leader loss, partition, a consumer bug, and clock skew;
  - product facts are cited and dated.

## brainstorming (bounded / spike)
- **Bounded:** use the SKILL.md quick rule. If the fix would restructure the dataflow, say so, so brainstorming can step up.
- **Spike:** state the metric and the pass/fail threshold before running it.

## writing-plans
Fill writing-plans' slots as `coordination.md` (Plan) describes:
- **Global Constraints:** each guarantee and its mechanism, the isolation level (read from config), the idempotency keys, "publish only via the outbox", expand-only schema changes.
- **Review Focus:** race, duplicate, retry and failover conditions as concrete lines, e.g. "the same webhook delivered twice → one charge". Put the pinning test in the task that owns the code.
- **Each task** names the guarantee it preserves and the test that proves it.
- Schema change as expand → migrate → contract, one independently deployable task per step. Note any DDL that locks or rewrites a table.
- Backfills are resumable and throttled, and end with a verification query.
- The outbox or CDC lands in or before the first task that publishes events.
- Constraints, unique indexes, and idempotency tables land in or before the first task that relies on them.
- Verification includes migrate up and down on a copy, plus the race and idempotency tests.

## test-driven-development
Add failing-first tests where relevant, run against the real engine:
- **Race:** two connections with explicit interleaving, then assert the invariant.
- **Idempotency:** the same request or message twice, and out of order, gives one effect.
- **Migration:** old code on the new schema, new code on the old schema, and unknown fields preserved.
- **Rerun:** running a job twice gives the same output.
- **Failure injection:** a timeout followed by a retry, and a crash before commit.
- **Property tests** for invariants.

## execution (subagent-driven / executing-plans)
- The guarantee, isolation level, idempotency key, and outbox rule reach the implementer through Global Constraints and the plan task. Add nothing to the dispatch (`coordination.md`, Execution and review).
- If the planned approach can't provide the guarantee, raise it; don't work around it.

## verification-before-completion
- Show the output of: migrations up and down, the race and idempotency tests against the real engine, and the backfill verification query.
- Don't claim "safe under concurrency" without a race test, or "no data loss" without a failure test.

## systematic-debugging
- **Phase 1:** name at least 2 suspects from `review-checklist.md` Part 2, with one line each on why it's ruled in or out, before reading further:
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

  Architectural causes become a flow-B review or a brainstorming request. End with the lens-check line from coordination.md.

## requesting- / receiving-code-review
- **Requesting:** per-task reviews get data rules only through Global Constraints; the Review Focus lines are pinned by tests. For the final whole-branch review or a standalone requesting-code-review, and only when the diff touches schemas, migrations, transactions, queues, caches, or concurrency, append `review-lens.md` and the spec's guarantees to `PLAN_OR_REQUIREMENTS`.
  - Critical: loss, corruption, broken invariants.
  - Important: races or duplicates under load or failure.
  - Minor: everything else.
- **Receiving:**
  - Accept fixes that close races, add idempotency, or remove dual writes.
  - Push back on:
    - caches without an invalidation plan;
    - XA or 2PC across heterogeneous systems;
    - "just retry" without idempotency;
    - "move to NoSQL" without a named load parameter.

## finishing-a-development-branch
- Migrations are reversible, or have a documented roll-forward.
- Data tests pass.
- Optionally list data debt.
