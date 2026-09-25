# Lens coordination (shared)

<!-- coordination:start — identical in software-design, clean-python and data-intensive; check with scripts/check-coordination.sh -->
These rules apply whenever software-design, clean-python or data-intensive is active in superpowers work. This file is identical in all three skills: read one copy, once per session. Superpowers owns the process. Never skip or reorder its steps, and never add gates inside its flows.

**Installed lenses only.** A repo may install any subset of the three. Every rule below that names a lens applies only if that lens is installed: skip its questions, approach lines, spec subsections, plan-slot lines and lens-check segment. Don't write "n/a" for a missing lens, and don't stand in for it.

**Lanes.**
- **software-design:** how the system splits into modules, what each hides, and what the interfaces are. A module card says which module hides each data choice.
- **clean-python:** how those modules are written in Python (Protocols, dataclasses, typed signatures, the exception hierarchy), including the Python that enforces data guarantees (transaction retry loops, session handling, idempotency checks).
- **data-intensive:** which store owns each piece of data, which guarantee each operation needs, how data flows, replicates, partitions and evolves, and what happens on failure.

**Where the rules live.** Read this file once per session. At each superpowers step, read that step's file once (one copy, from any lens): `references/steps/brainstorming.md`, `writing-plans.md`, `tdd.md`, `execution.md` (subagent-driven-development or executing-plans), `verification.md`, `review.md` (requesting- or receiving-code-review), `debugging.md` or `finishing.md`. Each holds the shared rules for the step and one section per lens. Read nothing for other steps.

A bounded or trivial change needs only each SKILL.md's quick rule. Standalone reviews and decisions (audits, Python reviews, technology choices, data reviews) follow `references/standalone.md`.

**Side effects are dual writes.** Any notification, email, webhook or event tied to a commit must state its delivery semantics: at-most-once after commit, or at-least-once via an outbox and an idempotent consumer. Never write "no dual write" while such a side effect exists.

**Tests**
- Data-correctness tests (races, constraints, isolation, idempotency, migrations) run against the real database engine, never a mock.
- External services use injected fakes. `mock.patch` is a last resort, patched where the name is looked up.
- Test public interfaces.
- Show the failing run's output before the fix and the passing run's output after it. A summary is not evidence.
<!-- coordination:end -->
