---
name: clean-python
description: Python lens for superpowers workflows, based on Mariano Anaya's "Clean Code in Python": Pythonic idioms and protocols, typing, error handling, SOLID in Python, decorators, descriptors, generators and async, pytest, mocks, and tooling (formatter, linter, type checker). Use it whenever superpowers work touches Python code, in brainstorming, writing-plans, test-driven-development with pytest, plan execution, verification, systematic-debugging, and code review. Also use it when asked to review or judge Python code outside a commit range. It never runs its own process.
---

# Clean Python (superpowers lens)

Superpowers owns the process. This lens owns the Python judgment: idioms, types, errors, tests, and tools. It writes Python only inside a superpowers implementation step.

**Lanes**
- **software-design:** module split and interfaces.
- **clean-python:** how each module is written in Python, e.g. a `typing.Protocol`, dataclasses, typed signatures, docstrings, an exception hierarchy.
- **data-intensive:** stores, guarantees, and dataflow. This lens writes the Python that enforces them: transaction retry loops, session handling, idempotency checks.

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
Drop python if no .py file changed and data if no data changed; write "ok" only if that lens flags nothing. Add no questions of your own: state lens decisions as defaults under **Defaults chosen**.

## Inside superpowers steps

Read `references/coordination.md` once per session; it's shared by all three lenses. Then read the section of `references/superpowers-hooks.md` for the current step. For spec content, use `assets/spec-sections.md`. For the reviewer, use `references/review-lens.md`. If tooling is missing, start from `assets/pyproject-tooling.toml`.

## Python review (the one flow this skill starts)

Use this for "is this Pythonic?" or "review this file or package" when there's no commit range. If the request also covers structure or data, run the joint review described in the coordination file.
- **Quick path** (a snippet or short file): findings in chat, with before/after snippets. No document. Ask questions only if the intent is unclear.
- **Full path** (a package, or when the fixes need planning): follow the coordination file's standalone flow, then:
  1. Read for intent. Then walk `references/review-checklist.md` in this order: correctness hazards → design → idioms → docs and typing → tests → tooling. Style comes last, and only when no tool would catch it.
  2. For each finding, give file:line, the problem, why it matters, a before/after snippet, and a severity:
     - **Critical:** a bug, data loss, security, or a swallowed error.
     - **Important:** a problem that will spread.
     - **Minor:** a local issue.

     Keep the review in proportion to the code, and credit what's good.
  3. Write it with `assets/review-template.md` to `docs/superpowers/reviews/YYYY-MM-DD-<topic>-python-review.md`, then self-review, review gate, hand-off.

  Tool claims need tool output.

**Guardrails**
- Follow the project's own conventions and tools over this skill's defaults.
- Don't spend review comments on what a tool catches; recommend the tool instead.
- Refactors preserve behaviour, and go in their own green tasks.

**Deeper references:**
- `references/pythonic.md`: idioms, protocols, decorators, descriptors, generators, async, gotchas.
- `references/design.md`: contracts, errors, SOLID, patterns.
- `references/testing.md`: pytest, mocks, property and mutation testing, refactoring.

*Condensed and paraphrased from Mariano Anaya, "Clean Code in Python" (2nd ed.). Superpowers © Jesse Vincent (MIT).*
