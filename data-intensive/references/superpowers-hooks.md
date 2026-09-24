# Superpowers hooks: the data lens at each step

Superpowers decides *when* each step happens and how to talk to the user. This file says what the data lens adds at each step. Never skip or reorder a superpowers step, and never add approval gates inside superpowers' own flows. (Flows 2 and 3 in SKILL.md are this skill's own and have their own gates.)

**When the lens applies.** Only when the work involves data guarantees, scale, concurrency, schema or format changes, messaging, pipelines, or multiple stores. For ordinary CRUD with none of these, stay silent.

## Coordination with the other lenses

<!-- coordination:start — identical in software-design, clean-python and data-intensive; check with scripts/check-coordination.sh -->
These rules apply whenever any of `software-design`, `clean-python` or `data-intensive` is active in a superpowers workflow. The question budget and the approach-axis rule only matter when more than one lens is active.

**Questions (brainstorming).**
- The lenses share one queue, in brainstorming's format: one question per message.
- Budget: **at most 6 lens questions in total**. Ask only when the answer would change the design; state the rest as assumptions in brainstorming's understanding note. Skip anything the context already answers.
- **Choices vs facts:**
  - For a *choice* (which approach, which guarantee to pay for), put the recommended option first.
  - For a *fact* about the user's world (load, traffic shape, domain rules, team, existing systems, what prompted a request), **don't recommend**. Don't label any option "recommended" or "default" on these. Offer realistic ranges plus "Not sure — assume <smallest reasonable value>".
  - A default the user accepts is recorded under **Assumed (default accepted)**, never under "Stated by user". Don't build a recommendation on an assumed fact without saying so.
- Order, with duplicates merged:
  1. Workload and loss tolerance (data-intensive).
  2. Guarantees required: money, inventory, uniqueness, and the delivery semantics of any side effect the feature depends on (data-intensive).
  3. Likely directions of change and growth horizon, as **one** question (software-design + data-intensive).
  4. Source of truth for key entities (data-intensive).
  5. What callers must never need to know (software-design).
  6. Concurrency model: sync, async, or workers, as **one** question (clean-python + data-intensive).
  7. Extension-point mechanism, value objects, typing strictness (clean-python). Usually assumptions, not questions.

**Approaches.**
- The 2–3 approaches differ on the **dominant risk**: data-intensive sets the axis when data guarantees, scale, or multiple stores dominate; otherwise software-design does. clean-python never sets the axis.
- Every other active lens adds **one line per approach** with its verdict (e.g. `design: … · python: …`).

**Spec outline.** Fold lens content into brainstorming's sections rather than appending blocks:

| Brainstorming section | Contents |
|---|---|
| Architecture | Chosen and rejected approaches (all lenses); knowledge to hide (software-design); load and targets, guarantees, systems of record (data-intensive) |
| Components | One card per module (software-design), including its Python form: Protocol/ABC, dataclasses, package path (clean-python) |
| Data flow | Dataflow diagram, replication and partitioning, encoding and evolution (data-intensive); layering (software-design) |
| Error handling | **One** merged table: failure or error → where it's handled (defined away / masked / exposed) → exception type → caller-visible? Covers software-design's error choices, clean-python's exception hierarchy, and data-intensive's failure analysis |
| Testing | Test levels and test doubles, per the rule below |
| Implementation notes | Runtime, tooling, required checks, package layout (clean-python); operations, monitoring, product facts relied on (data-intensive) |

- Spec self-review runs every active lens's checks in **one** pass.
- **Side effects are dual writes.** Any external side effect tied to a commit (notification, email, webhook, event) must have its delivery semantics stated: at-most-once after commit, or at-least-once via outbox and idempotent consumer. Never write "no dual write" while such a side effect exists.

**Plan order (writing-plans).** Skip steps that don't apply:
1. Tooling, if missing (clean-python).
2. Characterization tests for code that will be refactored.
3. Behavior-preserving refactors.
4. Interfaces and interface comments (software-design).
5. Schema expansion, constraints, unique indexes, idempotency tables, outbox/CDC (data-intensive).
6. Implementation, test-first.
7. Migrate and backfill, then switch readers (data-intensive).
8. Contract the old schema (data-intensive).

Every task ends with its verification commands. If planning needs to change the approved spec, list the changes and ask before committing them.

**Tests.**
- Data-correctness tests (races, constraints, isolation, idempotency, migrations) run against the **real database engine**; never mock it.
- External services (payment gateways, third-party APIs, clocks) use **injected fakes**. `mock.patch` is a last resort, patched where the name is looked up.
- All tests target public interfaces.
- Show the failing run's output before writing the fix, and the passing run's output after. A summary line alone is not evidence.

**Bounded changes.**
- Brainstorming's short design states any open decision as a **default** (e.g. "missing id returns None", "no read API until one is needed"). Scope extras such as extra read methods, return-type changes, or helper APIs are defaults, not questions. Ask a question only when no safe default exists. One approval message, then implement.
- The design includes **one** line in exactly this form: `Lens check: design … · python … · data …` (write "ok" for a lens with nothing to flag). Include the python part whenever the change touches Python, and the data part only when the change touches data. Items:
  - design: leaks a decision into a second module, or adds a pass-through;
  - data: unprotected read-modify-write or check-then-act, a dual write or unstated side-effect semantics, an incompatible schema or message change, or a retry without idempotency;
  - python: a mutable default, bare `except`, flag parameter, dependency created inside a function, or an undeclared new dependency.
- List pre-existing problems separately as follow-ups, not in the lens check.
- For a bounded change or a trivial one, don't open the lens reference files; the SKILL.md quick rule is enough.

**Standalone reviews and decision records.**
- **Route:**
  - structure → software-design audit;
  - a Python file or snippet → clean-python review;
  - data flows, stores, or an incident → data-intensive review;
  - a technology choice → data-intensive decision.

  A request spanning more than one gets **one joint review**.
- **Flow:** announce the path → questions (shared budget, choices vs facts) → write back your understanding → **write the document directly** → self-review → one user review gate → hand-off.
  - Don't present sections or findings for approval before the document exists. The document's review gate is the only content gate.
  - In chat, give a short summary and the path, not the full content.
- **Findings** are sorted by severity (Critical / Important / Minor), each tagged with its lens.
  - Assign by concern: schema, constraints, and invariants → data; module boundaries → design; idioms, typing, tooling → python.
  - Missing tooling is Important when it hides real defects.
  - Each data finding, including side effects in the write path, is written as an event sequence.
- **Self-review honesty:** never tick an item you haven't verified. Fetch and date product facts, or mark the item unticked and list it under "Not verified".
- Load templates only when writing the document.

**Task briefs (subagents).** Include only what the task touches: its module card (software-design), at most 5 Python rules that apply to it (clean-python), and the guarantee it must preserve (data-intensive).

**Reviewer.** Add each lens's `review-lens.md` only when the diff touches that lens's area.
<!-- coordination:end -->

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

**Clarifying questions.** When other lenses are active, the coordination section's shared budget and order apply. Add the data questions from `question-bank.md` §1 to brainstorming's queue, in its format: one per message, multiple choice, recommended option first. Order them by dependency: workload, then guarantees, then source of truth, then freshness, then growth, then operational constraints. Skip any the context answers. State unknown numbers as assumptions in brainstorming's understanding note.

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

**Bounded.** (With other lenses active, use the coordination section's combined check instead.) Before the short in-chat design, check the change quickly. Does it:
- read-modify-write shared data without an atomic update, compare-and-set, or lock?
- check-then-act (check availability, then insert) without a constraint or serializable isolation?
- write to a second system (cache, search, queue) directly instead of through the outbox or CDC?
- change a schema or message format in a way old readers or writers can't handle?
- add a retry without idempotency?

If yes, say so in one line with the fix. If the fix restructures data flow, say so, so brainstorming can step up to the architectural path.

**Spike.** When a design question hinges on a measurement (throughput, tail latency, lock contention), suggest the spike as brainstorming describes, with the metric and the pass/fail threshold stated up front.

## 3. writing-plans

With other lenses active, follow the coordination section's plan order; the points below add detail.

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

For each hypothesis, name the metric, log, or reproduction that would confirm it. State the suspects briefly in chat before investigating. Reproduce races with the two-connection interleaving from §4, and show the failing run's output before the fix.

After the fix:
- keep the regression test;
- name any remaining duplicate sources of truth (e.g. a counter column and the row count) as a follow-up;
- don't fold "not found" or other unrelated conditions into a domain error such as `SoldOut`.

If the cause was architectural (dual writes, wrong guarantee), note it as a follow-up: a flow-3 review or a new brainstorming request.

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
