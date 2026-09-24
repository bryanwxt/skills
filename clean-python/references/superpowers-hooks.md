# Superpowers hooks: Python at each step

Superpowers decides *when* each step happens and how to talk to the user. This file says what the Python lens adds at each step. Never skip or reorder a superpowers step, and never add approval gates of your own.

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
1. brainstorming: architectural path
2. brainstorming: bounded and spike paths
3. writing-plans
4. test-driven-development
5. subagent-driven-development / executing-plans
6. verification-before-completion
7. requesting-code-review / receiving-code-review
8. systematic-debugging
9. finishing-a-development-branch
10. What this skill never does

---

## 1. brainstorming: architectural path

**Explore project context.** Note:
- Python version.
- Packaging: `pyproject.toml`, and whether it uses a `src/` layout.
- Dependency manager.
- Formatter, linter, and type checker, and whether CI runs them.
- Typing level: none, partial, or strict.
- Test framework and layout.
- Framework conventions (Django, FastAPI, and so on).
- Sync or async codebase.

Follow what exists. Record gaps (e.g. no type checker in CI) as design inputs, not as fixes to make now.

**Clarifying questions.** When other lenses are active, the coordination section's shared budget and order apply. Add only the Python choices that change the design, asked in brainstorming's format (one per message, multiple choice, recommended option first). Skip any the context already answers.
- *Sync or async?* Recommend matching the codebase. Choose async only when the workload is dominated by concurrent I/O.
- *Extension points:* `typing.Protocol` (structural, recommended for plug-ins and test doubles) or ABC (when you need shared implementation or registration)?
- *Value objects:* `@dataclass(frozen=True)`, or a validation library such as pydantic at I/O boundaries (recommended: dataclasses inside, validation at the edges)?
- *Typing strictness* for new code: recommend `mypy --strict` for new modules, relaxed per-module for legacy code.

**Approaches.** The module decomposition comes from `software-design` if it's active. The Python lens compares approaches on how naturally each maps to Python:
- protocols, dataclasses, and generators rather than frameworks of classes;
- dependencies injected, not created inside;
- testability without heavy patching.

**Design sections and spec.** Add the "Python implementation notes" section from `assets/spec-sections.md` to brainstorming's spec:
- package layout and public API (`__init__.py` / `__all__`);
- extension points (Protocols/ABCs);
- value objects and data classes;
- error hierarchy (one package base exception; translation at boundaries);
- dependency injection points;
- sync or async;
- typing level;
- tools and checks that must pass.

Don't write a separate document.

**Spec self-review.** Add a Python check to brainstorming's pass:
- Could each component be tested without its real external dependencies?
- Is there a single place each exception type is defined?
- Are frameworks and SDKs kept at the edges, away from domain logic?
- Is any inheritance there only to reuse code?

## 2. brainstorming: bounded and spike paths

**Bounded.** (With other lenses active, use the coordination section's combined check instead.) Before the short in-chat design, check the change quickly:
- Does it add a mutable default, a bare `except`, or a boolean flag parameter that switches behaviour?
- Does it grow a function's argument list past what a caller can reasonably gather? If so, suggest a parameter object.
- Does it add a dependency? Justify it, and put it in the package's dependencies, not just installed locally.
- Does it create a dependency inside a function where it should be injected?

Mention anything found in one line of the in-chat design. If fixing it would restructure components, say so, so brainstorming can step up to the architectural path.

**Spike.** Spike code is throwaway, so don't polish it. Note in the recommendation any Python finding that affects the real design (e.g. "the library is sync-only").

## 3. writing-plans

With other lenses active, follow the coordination section's plan order; the points below add detail.

- **Exact paths.** Use the package layout from the spec (e.g. `src/<pkg>/…`, `tests/…` mirroring it). writing-plans needs exact file paths; give them.
- **Tooling first if missing.** If the project lacks a formatter, linter, type checker, or test config, the first task adds them (start from `assets/pyproject-tooling.toml`, adapted to the project's Python version) with CI wiring, before feature tasks. Skip this if tools exist.
- **Verification commands in every task.** Each task ends with the exact commands and expected results, for example:
  - `pytest tests/<area> -q` (pass)
  - `ruff check <paths>` (clean)
  - `mypy <package>` (clean)
  - `black --check <paths>` or `ruff format --check`
- **Interface tasks** (if `software-design` is active) become typed signatures plus docstrings in the task. The tests in the same task pin down the documented behaviour.
- **Refactor tasks are separate** and behaviour-preserving. If code lacks tests, the first task writes characterization tests.
- **Big modules:** plan the split into a package whose `__init__.py` re-exports the old names, so imports keep working.

## 4. test-driven-development

- **Red:** write the failing test in pytest.
  - Use `@pytest.mark.parametrize` for input tables and `pytest.raises(SomeError, match=…)` for errors.
  - Put fixtures in `conftest.py` when shared, and keep them small.
  - Test the public interface, not private helpers.
- **Choose cases** from boundaries, equivalence classes, and edge cases (empty, `None`, huge, Unicode, duplicates). Use Hypothesis for properties that should always hold (round-trips, invariants).
- **Mocks** only at external boundaries, and never for the database in data-correctness tests (see the coordination section):
  - Use `create_autospec` or `spec=` so bad calls fail.
  - `mock.patch` where the name is looked up, not where it's defined.
  - Needing many patches is a design signal. Prefer injecting a fake through the constructor, and flag it for review.
- **Green:** write the simplest Pythonic implementation that passes (see `references/pythonic.md`).
- **Refactor:** once green, apply idioms (comprehensions, `enumerate`/`zip`, context managers, dataclasses, `@property`) and rerun tests and tools.
- **Watch the failure mode.** The test should fail for the expected reason (an assertion or the expected exception), not a `NameError` or `ImportError` from a typo.

## 5. subagent-driven-development / executing-plans

Include these rules in each Python task brief:
- Type-annotate public functions. Give public modules, classes, and functions docstrings covering args, returns, and raises.
- No mutable default arguments, bare `except`, `except Exception: pass`, or `assert` for validation.
- When translating exceptions, use `raise … from e`.
- Resources always use `with`.
- Inject dependencies; don't instantiate them inside business logic.
- Prefer composition over inheritance for reuse; subclass `UserDict`/`UserList` rather than `dict`/`list`.
- Keep functions small. For many related arguments, use a dataclass parameter object.
- Use generators for large or lazy sequences.
- No blocking I/O inside `async def`.
- Before reporting a task done, run the task's verification commands and include their output.
- If the plan's interface forces un-Pythonic code (e.g. Java-style getters), raise it rather than silently changing the interface.

## 6. verification-before-completion

For Python work, "verified" means running these and showing the output:
- `pytest` (the relevant suite, or all tests before merge), with pass counts;
- the linter (`ruff check` / `flake8` / `pylint`, whatever the project uses);
- the type checker (`mypy` / `pyright`);
- the formatter in check mode.

Don't claim "tests pass" or "type-clean" without the output. If a tool isn't configured, say so rather than implying it passed.

## 7. requesting-code-review / receiving-code-review

**Requesting.** Only when the diff touches Python files: when filling the reviewer template, append `references/review-lens.md` to the `PLAN_OR_REQUIREMENTS` text, together with the spec's Python implementation notes. The reviewer runs in a separate agent and won't otherwise know the lens. Map severities:
- **Critical:** correctness hazards (mutable defaults causing shared state, swallowed exceptions, resource leaks, blocking the event loop).
- **Important:** design and idiom problems in shared code.
- **Minor:** local idioms and naming.

**Receiving.** receiving-code-review requires checking feedback before acting. For Python feedback:
- Accept suggestions that remove correctness hazards, add types or docstrings to public APIs, or replace hand-rolled code with language protocols.
- Push back, with reasons, on:
  - inheritance purely for code reuse;
  - getter/setter methods instead of attributes or `@property`;
  - double-underscore "private" names;
  - catching broad exceptions "to be safe";
  - premature abstraction (YAGNI);
  - metaclasses or descriptors where a function or property would do.
- If feedback is about style a tool should enforce, suggest adding the tool rule instead of hand-fixing.

## 8. systematic-debugging

Follow systematic-debugging's phases. The Python lens adds candidate hypotheses and tools for Phase 1 (root cause).

**Common Python root causes:**
- Mutable default arguments or mutable class attributes shared across instances.
- Late binding in closures and lambdas in loops.
- An iterator or generator consumed twice.
- Subclassing `dict`/`list` where built-in methods bypass overrides.
- `__getattr__` not raising `AttributeError`.
- `mock.patch` applied where the name is defined, not where it's looked up.
- Import-time side effects, including decorators doing work at definition time.
- `is` vs `==`.
- Float precision; naive vs aware datetimes; text vs bytes and encodings.
- Blocking calls inside async code.
- Assertions stripped by `-O`.

**Tools:**
- `breakpoint()`/pdb; `python -X dev` (extra warnings and checks); `faulthandler` for hangs and crashes; `tracemalloc` for memory growth.
- `pytest -x --lf -vv`, and `pytest --pdb` to drop into the failure.
- `-W error` to make warnings fatal.
- `python -m cProfile` for performance.

**After the fix:**
- The regression test stays (systematic-debugging requires it).
- If the cause was a Python anti-pattern that could exist elsewhere, search for siblings (e.g. `grep -rn "def .*=\[\]"`) and note them as follow-ups.

## 9. finishing-a-development-branch

Before presenting the finish options, confirm that all configured Python checks are green (tests, linter, type checker, formatter). Optionally list Python debt the branch revealed (one line each: location, smell, fix) so it isn't lost.

## 10. What this skill never does

- Run its own questions, approval gate, design doc, or plan.
- Write code outside a superpowers implementation step.
- Decide brainstorming's path, or module decomposition (that's `software-design`).
- Override superpowers' rules. On conflict, follow superpowers and mention the tension.
