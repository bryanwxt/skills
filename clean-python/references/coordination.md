# Lens coordination (shared)

<!-- coordination:start — identical in software-design, clean-python and data-intensive; check with scripts/check-coordination.sh -->
These rules apply whenever software-design, clean-python or data-intensive is active in superpowers work. This file is identical in all three skills: read it once per session, and don't reread another lens's copy. Superpowers owns the process. Never skip or reorder its steps, and never add gates inside its flows.

**Installed lenses only.** A repo may install any subset of the three. Every rule below that names a lens applies only if that lens is installed: skip its questions, approach lines, spec subsections, plan-slot lines and lens-check segment. Don't write "n/a" for a missing lens, and don't stand in for it.

**Questions**
- Lens questions join brainstorming's queue: one per message, **at most 6 across all lenses**. Ask only when the answer changes the design; anything else becomes an assumption in the write-back. Skip whatever the context already answers.
- **Choice** (approach, guarantee to pay for, path): put the recommended option first, with its reason.
- **Fact** about the user's world (load, traffic shape, domain rules, team, existing systems, what prompted the request): give ranges plus "Not sure — assume <smallest reasonable>". Never mark an option "recommended" or "default".
- Record every input under one of four labels:
  - **Stated:** the user said it.
  - **Decided:** an approved recommendation on a choice.
  - **Assumed (default accepted):** only for questions actually asked.
  - **Assumed (inferred, not asked).**

  If a conclusion rests on an assumption, say so.
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
- clean-python never sets it; with only clean-python installed, brainstorming's own comparison stands.

Each other active lens adds one line per approach (`design: … · python: …`).

**Spec.** The spec's top-level headings are brainstorming's five design sections plus one closing **Implementation notes** heading. Lens content goes in as `###` subsections under those headings, never as new top-level headings or a second document. Each `assets/spec-sections.md` uses this layout. Skip any subsection that would only say "n/a". Lenses add no approval rounds: each design section is presented and approved once, with its lens subsections inside it.
- **Architecture:** approaches, including rejected ones; likely directions of change; knowledge to hide; load and targets; guarantees; systems of record.
- **Components:** module cards with their Python form; extension points; value objects; layering; cross-module decisions.
- **Data flow:** diagram, data model, replication and partitioning, correctness mechanisms, encoding and schema evolution.
- **Error handling:** the exception hierarchy, then ONE table: failure (for data, the event sequence) → where it's handled (defined away / masked / exposed) and how → exception type → caller-visible? → detection. Data failure-analysis rows go in this table.
- **Testing:** test levels, fakes vs the real engine, property tests.
- **Implementation notes:** runtime, tooling and checks, package layout, injection, concurrency, operations, product facts relied on.

Self-review runs every active lens's checks in one pass and fixes the spec inline. Don't add a section that records self-review results.

**Side effects are dual writes.** Any notification, email, webhook or event tied to a commit must state its delivery semantics: at-most-once after commit, or at-least-once via an outbox and an idempotent consumer. Never write "no dual write" while such a side effect exists.

**Plan.** writing-plans sets the plan's shape: the header, **Global Constraints**, **Review Focus**, and right-sized tasks, each with an `Interfaces: Consumes / Produces` block. Lenses fill those slots. They add no plan sections of their own, and no task that a reviewer couldn't reject separately from its neighbours. The lens content lives in the plan because it's the only place it reaches subagents (see Execution and review).
- **Global Constraints** (one line each, exact values): the invariants that bind every task.
  - data: each guarantee and its mechanism, the isolation level, the idempotency keys, "publish only via the outbox", expand-only schema changes;
  - python: Python version, typing level, the exact check commands;
  - design: knowledge-hiding rules that span tasks, e.g. "only `billing/gateway.py` imports the Stripe SDK".
- **Review Focus:** the lenses propose candidates, as concrete conditions with the expected behaviour, e.g. "two concurrent redeems of one code → exactly one succeeds". writing-plans still keeps the five most likely. Each line gets its pinning test in the task that owns the code.
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

**Tests**
- Data-correctness tests (races, constraints, isolation, idempotency, migrations) run against the real database engine, never a mock.
- External services use injected fakes. `mock.patch` is a last resort, patched where the name is looked up.
- Test public interfaces.
- Show the failing run's output before the fix and the passing run's output after it. A summary is not evidence.

**Bounded and trivial changes**
- **Lenses add no questions** (brainstorming's own bounded checklist may ask its one). Resolve each lens decision with the smallest safe default, including scope extras, and list it under **Defaults chosen** in the short design. Then ask for one approval and implement.
- After every code change, including debugging fixes, write this line exactly: `Lens check: design <ok|note> · python <ok|note> · data <ok|note>`.
  - Build the line from these segments, in this order:
    - `design` if software-design is installed;
    - `python` if clean-python is installed and a .py file changed;
    - `data` if data-intensive is installed and data changed.
  - Examples:
    - only clean-python installed, a .py file changed → `Lens check: python ok`;
    - only data-intensive installed, a Go repo, data changed → `Lens check: data ok`;
    - all three installed, a .py file changed, no data → `Lens check: design ok · python ok`.
  - Write "ok" only if that lens flags nothing.
- Pre-existing problems go under follow-ups.
- Don't open lens reference files; each SKILL.md has a quick rule for this.

**Standalone reviews and decisions**
- **Routing:**
  - structure → software-design audit;
  - Python file or snippet → clean-python review;
  - data flows, stores or an incident → data-intensive review;
  - technology choice → data-intensive decision;
  - anything spanning lenses → **one** joint review.
- **Joint reviews:** load each covered lens with the Skill tool, and use the union of their templates' self-review items.
- **Flow:** announce the path → questions (budget, choice vs fact) → post the write-back **in chat** with the four labels, in the same message that says the document is being written → write the document directly (no section-by-section or finding-by-finding approvals; only a short summary in chat) → self-review → one review gate → hand off to `superpowers:brainstorming`. Never implement in the flow.
- **Location:** `docs/superpowers/{reviews,decisions}/YYYY-MM-DD-<topic>…md`. Commit on a branch.
- **Findings:** sorted by severity (Critical / Important / Minor) and tagged `[data]`, `[design]` or `[python]`. Assign them by concern:
  - schema, constraints, invariants → data;
  - module boundaries → design;
  - idioms, typing, tooling → python.

  Missing tooling that hides defects is Important. Data findings, including side effects in the write path, are written as event sequences.
- **Self-review:** check that findings are sorted Critical → Minor, and never tick something you haven't verified. Fetch and date product facts, or list them under "Not verified".
- Load templates only when writing the document.

**Execution and review**
- **Implementer:** both execution skills work from the plan task itself. subagent-driven-development's `task-brief` script extracts it verbatim, and the brief is the single source of requirements. Add nothing lens-specific to the dispatch. If a task lacks lens content it needs, treat it as a plan gap: rule on it and ledger it, as subagent-driven-development says for plan corrections.
- **Per-task reviewer:** the dispatch is subagent-driven-development's own, and the lenses reach it through two of its inputs:
  - the brief;
  - `[GLOBAL_CONSTRAINTS]`, which is the plan file's `## Global Constraints` lines, copied as they stand in the plan.
- **When a review must look harder at something** (an incident, or "make sure reviewers catch X"), do these steps in order:
  1. Edit the plan: add a concrete Review Focus line (e.g. "two concurrent redeems of one code → exactly one succeeds"), or a Global Constraint, and put its pinning test in the task that owns the code.
  2. Ledger the edit as a plan correction.
  3. Dispatch the review as above. The copied Global Constraints and the brief now carry it.
- **Final whole-branch review** (either execution skill), **or a standalone requesting-code-review:** append a lens's `review-lens.md` to `PLAN_OR_REQUIREMENTS` only when the diff touches that lens's area.
<!-- coordination:end -->
