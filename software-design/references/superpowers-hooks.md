# Superpowers hooks: what to do at each step

Superpowers decides *when* each step happens and how to talk to the user. This file says what the design lens adds at each step. Never skip or reorder a superpowers step, and never add approval gates of your own.

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
1. brainstorming — architectural path
2. brainstorming — bounded and spike paths
3. writing-plans
4. test-driven-development
5. subagent-driven-development / executing-plans
6. requesting-code-review / receiving-code-review
7. systematic-debugging
8. finishing-a-development-branch
9. What this skill never does

---

## 1. brainstorming — architectural path

**Explore project context.** For existing code, note the modules the work will touch and write one line each on what it hides. Note leaked knowledge you'll have to live with or fix. Brainstorming allows targeted improvements to code the work touches, but not unrelated refactoring — flag the rest as design debt.

**Clarifying questions.** When other lenses are active, the coordination section's shared budget and order apply. Add these to brainstorming's queue, asked in its format: one per message, multiple choice where possible, recommended option first. Skip any the request already answers.
- *Where is this likely to change?* (e.g. new data sources / new output formats / scale / new user types). Module boundaries go around decisions likely to change.
- *What's the common case?* The interface should make it trivial; rare cases can take more effort.
- *Which details should callers never need to know?* (storage, formats, protocols, vendor APIs, retry policy…)
Only ask what changes the design; the rest are your own assumptions, written back in brainstorming's understanding note.

**Propose 2–3 approaches = design it twice.**
- Start from the list of design decisions and knowledge in the system; each significant one should belong to exactly one module. Decompose around knowledge, not around the order things happen (that's temporal decomposition, which leaks knowledge).
- Make the approaches differ in **decomposition** (where the boundaries are and what each module hides), not in cosmetic details.
- Compare each on: simplest interface for the common case; how much each module hides; generality without extra caller effort; performance where it matters; weaknesses. Lead with the recommendation, as brainstorming requires.
- If none is attractive, use the weaknesses found to generate another.

**Present design sections.** In the *components* section, give each significant module a card (`assets/spec-sections.md`):
- abstraction in one sentence (without saying how it works);
- what it hides;
- interface — signatures with a one-line comment each, written before any implementation;
- errors: defined away / masked / aggregated / exposed;
- defaults it picks so callers don't have to.
In *error handling*, prefer defining errors out of existence and masking them low down; list only the errors callers genuinely must handle. In *data flow*, check each layer offers a different abstraction (no pass-through layers). If a module is hard to name or its interface comment is hard to write briefly, the decomposition is probably wrong — revise it before presenting.

**Spec self-review.** Alongside brainstorming's placeholder, consistency, scope and ambiguity checks, run the red-flag pass on the design: shallow module, information leakage, temporal decomposition, overexposure, pass-through method or variable, special-general mixture, conjoined modules, too many exceptions, configuration sprawl, hard-to-name or hard-to-describe components. Fix inline, as brainstorming says.

**Spec contents.** Add the sections from `assets/spec-sections.md` to brainstorming's spec (`docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md`), including the rejected approaches and why they lost. Never write a second design document.

## 2. brainstorming — bounded and spike paths

**Bounded.** (With other lenses active, use the coordination section's combined check instead.) Before presenting the short in-chat design, check the change in about 30 seconds:
- Does it put knowledge about one decision into a second module?
- Does it add a pass-through method, layer, or parameter?
- Does it add a parameter, option, or exception callers must now think about — could the module handle it instead?
- Does it add a special case to a general mechanism?
If yes, mention it in one line of the in-chat design with the simpler alternative. If the fix would restructure components, say so: under brainstorming's rules the task steps up to the architectural path.

**Spike.** The output is an answer, not code you keep, so don't apply the lens to spike code. If the spike's answer implies a design choice, mention it in the recommendation.

## 3. writing-plans

With other lenses active, follow the coordination section's plan order; the points below add detail.

- **Increments are abstractions, not features.** When a feature needs a new abstraction, plan tasks that build that abstraction properly, rather than a sliver of it per feature.
- **Interface first.** For each new module, the first task defines its public interface and interface comments (from the spec's module card); later tasks implement it behind that interface. Tests in each task target the interface (see §4).
- **Refactors separate from behavior changes.** Put structural changes in their own tasks, each kept green by existing tests, before tasks that change behavior.
- **Name what each task's module hides** in the task description, so implementers don't leak it elsewhere.
- **Keep tasks within one module where possible.** A task that must edit many modules for one change is a sign of leakage — flag it back to the spec rather than planning around it.

## 4. test-driven-development

- Write tests against the module's **public interface** and documented behavior, not its internal helpers. Deep modules have small interfaces, so this keeps tests few and stable, and lets implementations change freely.
- The interface comment written in the spec says what to test: arguments, results, side effects, errors, defaults.
- If a test needs lots of setup or mocks to reach the code, that's a design signal (too many dependencies or a leaky interface) — note it for the reviewer rather than working around it silently.
- Tests-first holds: interface signatures and comments come from the spec and plan; the failing test comes before implementation code.

## 5. subagent-driven-development / executing-plans

- Include the relevant module card (abstraction, hides, interface) in each task brief so implementers keep the knowledge where it belongs.
- If an implementer finds a red flag the plan didn't anticipate (e.g. the interface forces callers to know a detail), **raise it** to the controller or user instead of quietly redesigning. Small local fixes inside the module are fine; interface changes go back through the spec.

## 6. requesting-code-review / receiving-code-review

**Requesting.** Only when the diff changes module boundaries or interfaces: when filling the reviewer template, append `references/review-lens.md` to the `PLAN_OR_REQUIREMENTS` text, along with the spec's module cards for the modules touched. The reviewer runs in a separate agent and won't otherwise know the lens. Map severities: data loss, security, or broken invariants are Critical; design red flags that will cause change amplification in modules others depend on are Important; local naming, comments, and minor shallowness are Minor.

**Receiving.** receiving-code-review requires checking feedback before acting. For design feedback:
- Check it against the principles. "Split this class up" or "extract smaller functions" is only right if it produces cleaner abstractions — splitting that creates shallow modules, pass-throughs, or conjoined pieces makes things worse. Push back with the reason.
- "Add a config option / parameter" pushes a decision onto callers — ask whether the module could decide itself.
- Accept feedback that reveals leakage, special cases, or unclear interfaces.

## 7. systematic-debugging

- Don't redesign during debugging. Find and fix the root cause as systematic-debugging says.
- After the fix, if the root cause was a design problem (the same knowledge in two places, a special case in a general mechanism, an error that should have been defined away), note it as a follow-up. The user can then run a new brainstorming request for it.

## 8. finishing-a-development-branch

Optionally, in the branch summary, list design debt the work revealed (one line each: location, red flag, suggested fix) so it isn't lost. Don't fix it on this branch unless the user asks.

## 9. What this skill never does

- Run its own question round, approval gate, or design document.
- Write production code or implementation plans.
- Decide brainstorming's path (spike / bounded / architectural) — only point out when hidden complexity should step it up.
- Override superpowers' rules. If a principle here seems to conflict with a superpowers rule, follow superpowers and mention the tension to the user.
