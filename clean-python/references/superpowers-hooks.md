# Superpowers hooks: Python at each step

Superpowers decides *when* each step happens and how to talk to the user. This file says what the Python lens adds at each step. Never skip or reorder a superpowers step, and never add approval gates of your own.

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

**Clarifying questions.** Add only the Python choices that change the design, asked in brainstorming's format (one per message, multiple choice, recommended option first). Skip any the context already answers.
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

**Bounded.** Before the short in-chat design, check the change quickly:
- Does it add a mutable default, a bare `except`, or a boolean flag parameter that switches behaviour?
- Does it grow a function's argument list past what a caller can reasonably gather? If so, suggest a parameter object.
- Does it add a dependency? Justify it, and put it in the package's dependencies, not just installed locally.
- Does it create a dependency inside a function where it should be injected?

Mention anything found in one line of the in-chat design. If fixing it would restructure components, say so, so brainstorming can step up to the architectural path.

**Spike.** Spike code is throwaway, so don't polish it. Note in the recommendation any Python finding that affects the real design (e.g. "the library is sync-only").

## 3. writing-plans

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
- **Mocks** only at external boundaries:
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

**Requesting.** When filling the reviewer template, append `references/review-lens.md` to the `PLAN_OR_REQUIREMENTS` text, together with the spec's Python implementation notes. The reviewer runs in a separate agent and won't otherwise know the lens. Map severities:
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
