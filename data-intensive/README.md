# data-intensive × superpowers

`data-intensive` is a data-systems lens for [superpowers](https://github.com/obra/superpowers), based on Martin Kleppmann's *Designing Data-Intensive Applications*. It judges what guarantees each component gives, what they cost, and what happens when things fail.

Superpowers runs the build workflow. This skill:
- layers a **data track** into brainstorming when you design a data architecture from scratch;
- runs **technology choices** and **data architecture / incident reviews** itself, using brainstorming's discipline;
- adds data checks to planning, tests, verification, debugging, and code review.

## What it does

| You ask | What happens |
|---|---|
| "Design the data architecture for a multi-tenant billing system" | `superpowers:brainstorming` leads (architectural path). The data track adds its questions (load, guarantees, source of truth, freshness, growth, ops, loss tolerance), 2–3 data architectures compared on guarantees and failure behaviour, data subsections under the spec's own headings, and data checks in the spec self-review. Stop after the spec if you only want the design; otherwise `writing-plans` follows. |
| "Postgres or DynamoDB for this?" | **Technology choice**, brainstorming-style. It classifies the path (quick / decision / spike), asks one question at a time, writes back its understanding, compares categories and then products, checks current product docs, presents in sections, writes a decision record to `docs/superpowers/decisions/`, self-reviews, waits for your review, then hands adoption to brainstorming. |
| "Review our order pipeline" / "Why did we lose writes on Tuesday?" | **Data architecture review**, brainstorming-style. Targeted or full; intent questions; a system map with the guarantee each link provides; findings as concrete event sequences with superpowers' severities; a report in `docs/superpowers/reviews/`; your review; fixes handed to brainstorming. |
| "Add a `reserve seat` endpoint" (bounded) | A quick data check inside brainstorming's short design: race, check-then-act, dual write, schema compatibility, retry without idempotency. |
| Executing a plan with a migration | Guarantees in the plan's Global Constraints and race/duplicate conditions in Review Focus; tasks as expand → migrate → contract; failing-first race and idempotency tests against the real engine; verification includes migrate up/down and backfill checks. |
| "Orders are occasionally duplicated" (live) | `superpowers:systematic-debugging` leads. The lens supplies hypotheses from its symptom table and a two-connection reproduction of the race. |
| Code review of a change touching schemas, queues, or transactions | Per-task reviewers get the data rules through Global Constraints. The data review checklist goes to the final whole-branch or standalone reviewer, only when the diff touches data. |

## Using it with software-design and clean-python

The three lenses answer different questions. Superpowers runs the process for all of them, and each adds its own sections to the **same** brainstorming spec, never separate documents.

| Question | Skill |
|---|---|
| Which store owns each piece of data? Which guarantee does each operation need? How does data flow, replicate, partition, and evolve? What happens on failure? | **data-intensive** |
| How is the code split into modules, what does each hide, and what are its interfaces? | **software-design** |
| How is it written in Python: typing, dataclasses and Protocols, errors, pytest, tooling? | **clean-python** |

**Example: a payments feature in Python.**

| Step | data-intensive | software-design | clean-python |
|---|---|---|---|
| Brainstorming questions | load, guarantees (exactly-once charge), source of truth | likely change directions, what callers shouldn't know | sync vs async, Protocol for the payment gateway |
| Approaches | single DB + outbox vs event-sourced ledger | where the module boundaries sit in each | how naturally each maps to Python |
| Spec | data subsections: guarantees and idempotency keys (Architecture), outbox → CDC (Data flow), failure rows (Error handling) | module cards: `PaymentService` hides gateway, retries, idempotency storage | Python subsections: `PaymentError` hierarchy (Error handling), package layout and typing level (Implementation notes) |
| Plan | guarantees in Global Constraints; double-charge in Review Focus; expand/migrate/contract; outbox in or before the first publisher | module cards and `Interfaces: Produces` per task | exact paths; ruff/mypy/pytest per task |
| Tests | race test on double charge; duplicate-message test | tests aimed at `PaymentService`'s interface | pytest parametrize, injected fake gateway |
| Review | Global Constraints per task; data lens in the final review | same, design | same, Python |
| Debugging | symptom → cause table | design follow-up afterwards | Python suspects and tools |

**Keep the reviewer's prompt short.** Each lens is added only when the diff touches its area:
- data changes → data-intensive;
- module or interface changes → software-design;
- Python files → clean-python.

## Setup

Follow [`SETUP.md`](SETUP.md), which is the same in all three lenses. It covers requiring superpowers in the repo's `.claude/settings.json`, copying the lenses into `.claude/skills/`, the shared CLAUDE.md block (installed lenses plus repo facts), and `scripts/check-superpowers.sh`, which confirms the installed superpowers still has every hook point the lenses rely on.

## Files

| File | Used when |
|---|---|
| `SKILL.md` | Always: ground rules, quick rule, hook pointers, pointer to Flows A and B |
| `SETUP.md` | Wiring the lenses into a repo (shared by all three lenses) |
| `scripts/check-superpowers.sh` | Checks the installed superpowers still has every anchor the lenses hook into (shared) |
| `references/coordination.md` | Shared rules for all three lenses (questions, spec outline, plan order, tests, bounded changes, reviews); read once per session |
| `references/standalone.md` | Shared rules for standalone reviews and decisions: routing, joint reviews, flow, findings (shared by all three lenses) |
| `references/flows.md` | Flow A (technology choice) and Flow B (data architecture or incident review) |
| `references/superpowers-hooks.md` | The data track for brainstorming and additions to every other superpowers step |
| `references/question-bank.md` | Questions with recommended defaults for design, tech choice, review |
| `references/foundations.md` … `derived-data.md` | Topic knowledge (models, storage, encoding, replication, partitioning, transactions, distributed systems, pipelines) |
| `references/decision-guides.md` | Trade-off tables for technology choices |
| `references/review-checklist.md` | Review questions; symptom → cause → fix table |
| `references/review-lens.md` | Appended to `PLAN_OR_REQUIREMENTS` for the final whole-branch or standalone review when the diff touches data |
| `assets/spec-sections.md` | Data subsections for a brainstorming spec, placed under its own headings |
| `assets/decision-record-template.md` | Technology decision records |
| `assets/review-template.md` | Data architecture / incident reviews |

## Checking it works

| Prompt | Expected |
|---|---|
| "Design the data architecture for <system>" | Brainstorming leads; data questions one per message; spec has data subsections under its own headings; no separate design doc |
| "Kafka or SQS for <use>?" | Path announced; one question per message; categories before products; cited product facts; decision record; review gate; hand-off |
| "Review the data flow in <repo>" | Path announced; system map with guarantees; findings as event sequences; report in `docs/superpowers/reviews/`; hand-off |
| "Add a CRUD endpoint for user preferences" | Lens stays silent (no guarantees, scale, or concurrency concern) |

## Credit

Condensed and paraphrased from Martin Kleppmann, *Designing Data-Intensive Applications* (O'Reilly, 1st ed., 2017). Superpowers © Jesse Vincent, MIT license.
