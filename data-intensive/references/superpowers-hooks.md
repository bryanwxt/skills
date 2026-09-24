# Superpowers hooks: the data lens at each step

Superpowers decides *when* each step happens and how to talk to the user. This file says what the data lens adds at each step. Never skip or reorder a superpowers step, and never add approval gates inside superpowers' own flows. (Flows 2 and 3 in SKILL.md are this skill's own and have their own gates.)

**When the lens applies.** Only when the work involves data guarantees, scale, concurrency, schema or format changes, messaging, pipelines, or multiple stores. For ordinary CRUD with none of these, stay silent.

## Contents
1. brainstorming: architectural path (the data track)
2. brainstorming: bounded and spike paths
3. writing-plans
4. test-driven-development
5. subagent-driven-development / executing-plans
6. verification-before-completion
7. systematic-debugging
8. requesting-code-review / receiving-code-review
9. finishing-a-development-branch
10. What this skill never does

---

## 1. brainstorming: architectural path (the data track)

**Explore project context.** Note:
- the existing stores;
- the source of truth for each entity;
- the actual isolation level in use (check the config; defaults differ by product);
- replication setup;
- queues and pipelines;
- the migration tooling;
- any dual writes already present.

**Clarifying questions.** Add the data questions from `question-bank.md` §1 to brainstorming's queue, in its format: one per message, multiple choice, recommended option first. Order them by dependency: workload, then guarantees, then source of truth, then freshness, then growth, then operational constraints. Skip any the context answers. State unknown numbers as assumptions in brainstorming's understanding note.

**Approaches.** Build 2–3 data architectures that differ in substance:
- where the source of truth lives;
- how derived data is produced (synchronous, CDC, batch);
- whether to partition, and by what key;
- where correctness is enforced.

Compare them on: guarantees met, scaling headroom against the stated growth, behaviour under the named failures, operational burden, and cost of change later. Lead with the recommendation. Say explicitly when a single database is enough.

**Design sections and spec.** Add the sections from `assets/spec-sections.md` to brainstorming's spec. Put the data-specific failure analysis under brainstorming's "error handling" and the dataflow diagram under "data flow". Don't write a second document.

**Spec self-review.** Add these checks to brainstorming's pass:
- Every entity has one source of truth; everything else is derived and rebuildable.
- Every guarantee is named precisely, and the mechanism that enforces it is stated.
- No dual writes to two systems from application code. Use an outbox or CDC instead.
- Every retried write has an idempotency key enforced at the final store.
- No ordering by wall-clock time across nodes. No locks without fencing tokens.
- Schema changes are expand → migrate → contract, each step deployable on its own.
- The failure analysis covers leader loss, network partition, consumer bug, and clock skew.
- Product facts are cited and dated.

## 2. brainstorming: bounded and spike paths

**Bounded.** Before the short in-chat design, check the change quickly. Does it:
- read-modify-write shared data without an atomic update, compare-and-set, or lock?
- check-then-act (check availability, then insert) without a constraint or serializable isolation?
- write to a second system (cache, search, queue) directly instead of through the outbox or CDC?
- change a schema or message format in a way old readers or writers can't handle?
- add a retry without idempotency?

If yes, say so in one line with the fix. If the fix restructures data flow, say so, so brainstorming can step up to the architectural path.

**Spike.** When a design question hinges on a measurement (throughput, tail latency, lock contention), suggest the spike as brainstorming describes, with the metric and the pass/fail threshold stated up front.

## 3. writing-plans

- **Schema changes as expand → migrate → contract**, each step its own task and independently deployable:
  - add the new structure;
  - dual-read or dual-write via one path, and backfill;
  - switch readers;
  - remove the old structure.

  Note which DDL operations lock or rewrite tables in this database.
- **Backfills and reprocessing** are tasks with resumability, batch size, throttling, and a verification query.
- **Outbox or CDC setup comes before** any task that publishes events or updates derived stores.
- **Correctness tasks first:** constraints, unique indexes, and idempotency tables before the code that relies on them.
- **Verification commands** in each task include the data checks: migration up and down on a copy, the race test, the idempotency test.

## 4. test-driven-development

Beyond unit tests, the data lens adds these failing-first tests where they apply:
- **Race tests:** two connections with explicit interleaving (A reads, B reads, A writes and commits, B writes and commits). Then assert the invariant: no double booking, balance ≥ 0, unique username.
- **Idempotency tests:** send the same request or message twice (and out of order) and assert a single effect.
- **Migration tests:** old code against the new schema and new code against the old schema (forward and backward compatibility); a round-trip that keeps unknown fields.
- **Rerun tests:** running a batch or stream job twice gives the same output.
- **Failure injection:** a timeout with unknown outcome followed by a retry; a consumer crash before commit.
- **Property tests** for invariants across random operation sequences.

Run these against the real database engine (e.g. a container), not a mock. Isolation and constraint behaviour can't be mocked faithfully.

## 5. subagent-driven-development / executing-plans

Include in task briefs, where relevant:
- the guarantee this task must preserve, and its enforcement mechanism;
- "no dual writes: publish via the outbox";
- the isolation level assumed;
- the idempotency key to enforce.

If an implementer finds that the plan's approach can't provide the guarantee (for example, the database's "repeatable read" doesn't prevent lost updates), they must raise it, not work around it.

## 6. verification-before-completion

For data work, "verified" includes, with output shown:
- migrations applied and rolled back on a copy;
- race and idempotency tests passing against the real engine;
- the backfill verification query matching expectations;
- product facts cited if the change relies on them.

Don't claim "safe under concurrency" without a race test, or "no data loss" without a failure test.

## 7. systematic-debugging

Follow systematic-debugging's phases. In Phase 1 (root cause), use the symptom table in `review-checklist.md` Part 2 to generate hypotheses:
- stale reads after a write → replication lag;
- lost updates → read-modify-write race;
- duplicates → retries without idempotency;
- two leaders → failover without fencing;
- later write overwritten → last-write-wins with clock skew;
- one hot shard → key skew;
- derived store disagrees with the source → dual writes.

For each hypothesis, name the metric, log, or reproduction that would confirm it. Reproduce races with the two-connection interleaving from §4. After the fix, keep the regression test. If the cause was architectural (dual writes, wrong guarantee), note it as a follow-up: a flow-3 review or a new brainstorming request.

## 8. requesting-code-review / receiving-code-review

**Requesting.** Only when the diff touches schemas, migrations, queries or transactions, queues or events, caches or derived stores, or concurrency: append `references/review-lens.md` to `PLAN_OR_REQUIREMENTS`, together with the spec's "guarantees required" section. Otherwise leave it out, to keep the reviewer's prompt short. Severities:
- **Critical:** data loss, silent corruption, a broken invariant.
- **Important:** a race or duplicate under realistic load or failure.
- **Minor:** everything else.

**Receiving.** Check data feedback before acting:
- Accept anything that closes a race, adds idempotency, or removes a dual write.
- Push back on:
  - "add a cache" without a plan for invalidating it;
  - "use a distributed transaction" across heterogeneous systems (prefer outbox or CDC);
  - "just retry" without idempotency;
  - "move to NoSQL / microservices for scale" without a named load parameter.

## 9. finishing-a-development-branch

Confirm that migrations are reversible or have a documented roll-forward, and that the data tests pass. Optionally list data-architecture debt found (one line each) for a later flow-3 review.

## 10. What this skill never does

- Add gates or question rounds inside superpowers' flows, beyond adding questions to brainstorming's queue.
- Write production code or implementation plans.
- Decide brainstorming's path, or module decomposition (that's `software-design`), or Python idioms (that's `clean-python`).
- Override superpowers' rules. On conflict, follow superpowers and mention the tension.
