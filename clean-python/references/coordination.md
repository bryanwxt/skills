# Lens coordination (shared)

<!-- coordination:start — identical in software-design, clean-python and data-intensive; check with scripts/check-coordination.sh -->
These rules apply whenever software-design, clean-python or data-intensive is active in superpowers work. This file is identical in all three skills: read it once per session, and don't reread another lens's copy. Superpowers owns the process. Never skip or reorder its steps, and never add gates inside its flows.

**Questions**
- Lens questions join brainstorming's queue: one per message, **at most 6 across all lenses**. Ask only when the answer changes the design; anything else becomes an assumption in the write-back. Skip whatever the context already answers.
- **Choice** (approach, guarantee to pay for, path): put the recommended option first, with its reason.
- **Fact** about the user's world (load, traffic shape, domain rules, team, existing systems, what prompted the request): give ranges plus "Not sure — assume <smallest reasonable>". Never mark an option "recommended" or "default".
  - An accepted default goes under **Assumed (default accepted)**, never under "Stated".
  - If a conclusion rests on an assumed fact, say so.
- Order, with duplicates merged:
  1. workload and loss tolerance (data);
  2. guarantees, including the delivery semantics of any side effect the feature relies on (data);
  3. change directions and growth horizon, as one question (design + data);
  4. source of truth (data);
  5. what callers must never need to know (design);
  6. concurrency model, as one question (python + data);
  7. extension points, value objects, typing (python), usually as assumptions.

**Approaches.** The 2–3 approaches differ on the dominant risk:
- data-intensive sets the axis when guarantees, scale or multiple stores dominate;
- otherwise software-design sets it;
- clean-python never sets it.

Each other active lens adds one line per approach (`design: … · python: …`).

**Spec.** Fold lens content into brainstorming's sections, never into a second document:
- **Architecture:** approaches, including rejected ones; knowledge to hide; load and targets; guarantees; systems of record.
- **Components:** module cards, with their Python form.
- **Data flow:** diagram, replication and partitioning, schema evolution, layering.
- **Error handling:** ONE table of failure → where it's handled (defined away / masked / exposed) → exception type → caller-visible?
- **Testing.**
- **Implementation notes:** tooling and checks, package layout, operations, product facts relied on.

Self-review runs every active lens's checks in one pass.

**Side effects are dual writes.** Any notification, email, webhook or event tied to a commit must state its delivery semantics: at-most-once after commit, or at-least-once via an outbox and an idempotent consumer. Never write "no dual write" while such a side effect exists.

**Plan order** (skip steps that don't apply):
1. tooling, if missing;
2. characterization tests;
3. behaviour-preserving refactors;
4. interfaces and their comments;
5. schema expansion, constraints, idempotency tables, outbox;
6. implementation, test-first;
7. migrate and backfill, then switch readers;
8. contract the old schema.

Every task ends with its verification commands. If planning changes the approved spec, list the changes and ask before committing them.

**Tests**
- Data-correctness tests (races, constraints, isolation, idempotency, migrations) run against the real database engine, never a mock.
- External services use injected fakes. `mock.patch` is a last resort, patched where the name is looked up.
- Test public interfaces.
- Show the failing run's output before the fix and the passing run's output after it. A summary is not evidence.

**Bounded and trivial changes**
- Open decisions become defaults in the short design. Scope extras (read methods, return types, helper APIs) are defaults, not questions. Ask only when no safe default exists.
- One approval, then implement.
- Include exactly one line: `Lens check: design … · python … · data …`. Write "ok" for a lens with nothing to flag. Include python when Python changes, and data only when data changes.
- Pre-existing problems go under follow-ups.
- Don't open lens reference files; each SKILL.md has a quick rule for this.

**Standalone reviews and decisions**
- **Routing:**
  - structure → software-design audit;
  - Python file or snippet → clean-python review;
  - data flows, stores or an incident → data-intensive review;
  - technology choice → data-intensive decision;
  - anything spanning lenses → **one** joint review.
- **Flow:** announce the path → questions (budget, choice vs fact) → write back what you understood, separating stated from assumed → write the document directly (no section-by-section or finding-by-finding approvals; only a short summary in chat) → self-review → one review gate → hand off to `superpowers:brainstorming`. Never implement in the flow.
- **Location:** `docs/superpowers/{reviews,decisions}/YYYY-MM-DD-<topic>…md`. Commit on a branch.
- **Findings:** sorted by severity (Critical / Important / Minor) and tagged `[data]`, `[design]` or `[python]`. Assign them by concern:
  - schema, constraints, invariants → data;
  - module boundaries → design;
  - idioms, typing, tooling → python.

  Missing tooling that hides defects is Important. Data findings, including side effects in the write path, are written as event sequences.
- **Self-review:** never tick something you haven't verified. Fetch and date product facts, or list them under "Not verified".
- Load templates only when writing the document.

**Task briefs and review**
- A subagent task brief includes only what the task touches:
  - its module card;
  - at most 5 relevant Python rules;
  - the guarantee it must preserve.
- Add a lens's `review-lens.md` to the reviewer only when the diff touches that lens's area.
<!-- coordination:end -->
