---
name: clean-python
description: 'Use when superpowers work (brainstorming, planning, TDD with pytest, execution, verification, debugging, code review) touches Python code; when asked whether Python code is Pythonic, well typed, or well tested; or when the repo''s CLAUDE.md lists clean-python as an installed lens. Based on Anaya''s "Clean Code in Python".'
---

# Clean Python (superpowers lens)

Superpowers owns the process. This lens owns the Python judgment: idioms, types, errors, tests, and tools. It writes Python only inside a superpowers implementation step.

**The lens**
- Leave style to tools: formatter, linter, and type checker, run in CI.
- Use the language's protocols (iteration, context managers, properties, dataclasses) instead of hand-rolling them.
- Keep functions small and at one level of abstraction.
- Type public interfaces.
- Raise specific exceptions, at the right level, chained with `from e`, and never swallowed.
- Inject dependencies.
- Prefer composition to inheritance when the goal is reuse.
- Test the public interface with pytest.
- Practicality beats purity.

## Quick rule: bounded and trivial changes

Don't open the reference files. Always write the `python …` part of the one-line lens check. Flag:
- a mutable default;
- a bare `except`;
- a flag parameter;
- a dependency created inside a function;
- an undeclared new dependency;
- a new public function without a type hint or docstring.

Verify with the project's own tools and show their output. Put pre-existing problems under follow-ups.

After every code change, including debugging fixes, end with the lens-check line. Its segments, in this order: `design` if software-design is installed; `python` if clean-python is installed and a .py file changed; `data` if data-intensive is installed and data changed. Write "ok" only if that lens flags nothing. E.g. only clean-python installed → `Lens check: python ok`; all three installed, a .py change, no data → `Lens check: design ok · python ok`.

Lenses add no questions, and they don't replace brainstorming's. When the request doesn't say what the change is for, brainstorming's first message is its one purpose question and nothing else; lens defaults wait for the design message. In the design, list at most 3 lens defaults the user might not expect under **Defaults chosen**, or leave the list out.

## Inside superpowers steps

When brainstorming classifies the request as bounded or a spike, the quick rule above is all this lens needs: open no reference files for it. Otherwise, at each superpowers step, read two files, one copy each from any lens:
- `references/coordination.md`, the first time only;
- that step's file: `references/steps/brainstorming.md`, `writing-plans.md`, `tdd.md`, `execution.md`, `verification.md`, `review.md`, `debugging.md` or `finishing.md`.

Each step file has the shared rules and a section per lens; skip lenses that aren't installed.

For the final whole-branch or a standalone reviewer, use `references/review-lens.md` (per-task reviewers get lens rules only through the plan's Global Constraints). If tooling is missing, start from `assets/pyproject-tooling.toml`.

## Python review (the one flow this skill starts)

For "is this Pythonic?" or "review this file or package" with no commit range, follow `references/python-review.md`.

**Guardrails**
- Follow the project's own conventions and tools over this skill's defaults.
- Don't spend review comments on what a tool catches; recommend the tool instead.
- Refactors preserve behaviour and are green before behaviour changes.

**Deeper references:**
- `references/pythonic.md`: idioms, protocols, decorators, descriptors, generators, async, gotchas.
- `references/design.md`: contracts, errors, SOLID, patterns.
- `references/testing.md`: pytest, mocks, property and mutation testing, refactoring.

*Condensed and paraphrased from Mariano Anaya, "Clean Code in Python" (2nd ed.). Superpowers © Jesse Vincent (MIT).*
