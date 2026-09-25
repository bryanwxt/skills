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

After the change, end with this exact line (the lens check), shared by all three lenses:
`Lens check: design <ok|note> · python <ok|note> · data <ok|note>`
Build it from installed lenses only, as `coordination.md` shows (e.g. only clean-python installed → `Lens check: python ok`); drop python if no .py file changed and data if no data changed; write "ok" only if that lens flags nothing. Add no questions of your own: state lens decisions as defaults under **Defaults chosen**.

## Inside superpowers steps

Read `references/coordination.md` once per session; it's shared by all three lenses. Then read the section of `references/superpowers-hooks.md` for the current step. For spec content, use `assets/spec-sections.md`. For the final whole-branch or a standalone reviewer, use `references/review-lens.md` (per-task reviewers get lens rules only through the plan's Global Constraints). If tooling is missing, start from `assets/pyproject-tooling.toml`.

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
