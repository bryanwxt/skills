# clean-python: hooks per superpowers step

Rules shared with the other lenses (questions, spec outline, plan order, tests, bounded changes, reviews) live in `coordination.md`. This file adds only the Python lens.

## brainstorming (architectural)
- **Context:** note the Python version, packaging (`pyproject`, `src/` layout), dependency manager, formatter, linter, type checker, typing level, test setup, framework conventions, and whether the code is sync or async. Follow what exists; gaps become design inputs.
- **Choices** (within the shared budget, usually as assumptions):
  - sync or async: match the codebase, and use async only for I/O-bound concurrency;
  - `Protocol` (plug-ins and test doubles) or ABC (shared implementation);
  - `@dataclass(frozen=True)` inside, with validation (e.g. pydantic) at the edges;
  - `mypy --strict` for new modules.
- **Approaches:** add one line per approach on how naturally it maps to Python. Prefer protocols, dataclasses, and generators over class frameworks. Dependencies should be injected, and the design testable without heavy patching.
- **Spec** (Implementation notes and Components, via `assets/spec-sections.md`): package layout and `__all__`, extension points, value objects, the exception hierarchy (one package base, translated at the boundaries), injection points, concurrency, typing level, required checks.
- **Self-review:** can each component be tested without its real dependencies? Is each exception defined in one place? Are frameworks kept at the edges? Is any inheritance there only for reuse?

## brainstorming (bounded / spike)
- **Bounded:** use the SKILL.md quick rule. If a function's argument list grows too long, suggest a parameter object. A new dependency goes into the package's declared dependencies.
- **Spike:** don't polish throwaway code. Report Python findings that affect the real design, e.g. "the library is sync-only".

## writing-plans
- Give exact `src/…` and `tests/…` paths.
- If tooling is missing, the first task adds formatter, linter, type checker, and pytest config, wired into CI.
- Every task ends with commands and their expected results: `pytest …`, `ruff check …`, `mypy …`, and the formatter check.
- Interface tasks produce typed signatures with docstrings.
- Big modules become packages that re-export the old names.

## test-driven-development
- **Red:**
  - Use `@pytest.mark.parametrize` for tables of cases, `pytest.raises(…, match=…)` for errors, and small fixtures in `conftest.py`.
  - Cover boundaries, equivalence classes, and edge cases: empty, `None`, huge, unicode, duplicates.
  - Use Hypothesis for invariants.
  - The test must fail for the expected reason, not with a `NameError` or `ImportError`.
- **Doubles:** follow the coordination rule. Use `create_autospec` or `spec=`. Many patches is a design signal: inject a fake instead.
- **Green / refactor:** write the simplest Pythonic code, then apply idioms: comprehensions, `enumerate`/`zip`, `with`, dataclasses, `@property`. Rerun the tests and tools.

## execution (subagent-driven / executing-plans)
Add at most 5 rules to each task brief, picking the ones that apply:
- types and docstrings on public functions;
- no mutable defaults, bare `except`, or `assert` used for validation;
- `raise … from e`;
- `with` for resources;
- inject dependencies;
- composition rather than inheritance for reuse;
- no blocking I/O in `async def`.

Report done only with the tool output attached. If the planned interface forces un-Pythonic code, raise it rather than working around it.

## verification-before-completion
"Verified" means showing the output of:
- `pytest`, with pass counts;
- the linter;
- the type checker;
- the formatter in check mode.

If a tool isn't configured, say so.

## requesting- / receiving-code-review
- **Requesting:** only when Python files change, append `review-lens.md` and the spec's Python notes.
  - Critical: correctness hazards.
  - Important: idiom or design problems in shared code.
  - Minor: local issues.
- **Receiving:**
  - Accept fixes for hazards, typing of public APIs, and replacing hand-rolled code with protocols.
  - Push back on inheritance just to reuse code, getters and setters, `__private` names, broad `except` "to be safe", premature abstraction, and metaclass or descriptor tricks where a function would do.
  - Style feedback belongs in tool config.

## systematic-debugging
- **Phase 1 suspects:**
  - mutable default or shared class attribute;
  - late-binding closure;
  - iterator consumed twice;
  - subclassing `dict` or `list`;
  - `__getattr__` not raising `AttributeError`;
  - patching the wrong name;
  - import-time side effects;
  - `is` vs `==`;
  - float precision;
  - naive vs aware datetimes;
  - bytes vs str;
  - blocking calls in async code;
  - asserts stripped by `-O`.
- **Tools:** `breakpoint()`, `python -X dev`, `faulthandler`, `tracemalloc`, `pytest -x --lf -vv --pdb`, `-W error`, `cProfile`.
- **After the fix:** keep the regression test, and search for sibling occurrences to list as follow-ups.

## finishing-a-development-branch
- All configured checks green. Optionally list the Python debt the branch revealed.
