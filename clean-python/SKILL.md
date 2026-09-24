---
name: clean-python
description: Python lens for superpowers workflows, based on Mariano Anaya's "Clean Code in Python" — Pythonic idioms and protocols, typing, error handling, SOLID in Python, decorators, descriptors, generators and async, pytest, mocks, and tooling (formatter, linter, type checker). Use whenever superpowers work touches Python code — brainstorming a Python design, writing-plans for a Python project, test-driven-development with pytest, executing plan tasks in Python, verification before completion, systematic-debugging of Python bugs, and requesting or receiving code review of Python — and when asked to review or judge Python code that isn't a commit range. Never runs its own process.
---

# Clean Python (superpowers lens)

This skill adds a Python lens to superpowers. **Superpowers owns the process**: the order of steps, one question per message, approval gates, where specs and plans live, test-first, review, and verification. **This skill owns the Python judgment**: which idioms, types, tests, tools, and error handling make Python code clean, and what to look for when it isn't.

It never runs its own question round, design document, plan, or approval gate. It writes Python only inside a superpowers implementation step (a TDD cycle or a plan task).

**Lanes with other skills:**
- **`software-design`** decides how the system is split into modules and what each one hides. **clean-python** decides how each module is written in Python: protocols, dataclasses, typing, errors, iteration, and tests.
- **`data-intensive`** decides stores, guarantees, and dataflow. clean-python writes the Python that enforces them, for example the transaction retry loop, session handling, and idempotency-key checks.
- **`pragmatic-programmer`** runs only when the user asks for it.

## The lens in one paragraph

Clean Python reads well and changes safely. Formatting and style are left to tools (formatter, linter, type checker in CI). Human attention goes to intent:
- Use the language's protocols (iteration, context managers, properties, dataclasses) rather than hand-rolled equivalents.
- Keep functions small and at one level of abstraction.
- Type-annotate public interfaces.
- Raise specific exceptions at the right level and never swallow them.
- Inject dependencies instead of creating them inside.
- Prefer composition to inheritance for code reuse.
- Test the public interface with pytest.
- Every principle is a guideline: practicality beats purity.

Reference files:
- `references/superpowers-hooks.md`: exactly what to do at each superpowers step. **Read it whenever this skill is active.**
- `references/pythonic.md`: idioms, protocols, decorators, descriptors, generators, async, gotchas.
- `references/design.md`: contracts, errors, cohesion and coupling, SOLID in Python, patterns, architecture (the Python side; module decomposition is `software-design`'s job).
- `references/testing.md`: pytest, fixtures, mocks, coverage, property-based and mutation testing, refactoring safely.
- `references/review-checklist.md`: the full Python smell checklist with fixes.
- `references/review-lens.md`: a short checklist to paste into the superpowers code reviewer's prompt.
- `assets/pyproject-tooling.toml`: starter config for black, ruff, mypy, pytest, and coverage.
- `assets/spec-sections.md`: Python sections to add to a brainstorming spec.
- `README.md`: the human-facing guide to using this skill with superpowers.

## Where it plugs in

| Superpowers step | What this skill adds | Details |
|---|---|---|
| `brainstorming`: explore context | Python version, packaging, tooling present, typing level, test setup, framework conventions | hooks §1 |
| `brainstorming`: questions and approaches | Python-specific choices that change the design (sync vs async, Protocol vs ABC, dataclass vs model library, typing strictness), asked in brainstorming's format | hooks §1 |
| `brainstorming`: design sections and spec | A "Python implementation notes" section: package layout, extension points, value objects, error hierarchy, dependency injection, typing | hooks §1, `assets/spec-sections.md` |
| `brainstorming`: bounded path | A quick Python check of the change (mutable defaults, swallowed errors, a new flag argument, a new dependency) | hooks §2 |
| `writing-plans` | Exact file paths per package layout; a tooling task if checks are missing; verification commands in every task | hooks §3 |
| `test-driven-development` | pytest idioms: parametrize, fixtures, `pytest.raises`, Hypothesis; mocks only at boundaries with autospec, patched where looked up | hooks §4 |
| `subagent-driven-development` / `executing-plans` | Pythonic implementation rules for each task; run the formatter, linter, and type checker before reporting done | hooks §5 |
| `verification-before-completion` | The commands that count as evidence: `pytest`, `ruff check`, `mypy`, formatter check, with their output | hooks §6 |
| `requesting-code-review` | `references/review-lens.md` pasted into the reviewer's requirements | hooks §7 |
| `receiving-code-review` | Check Python feedback against the idioms before acting; push back on suggestions that make code less Pythonic | hooks §7 |
| `systematic-debugging` | Python-specific hypotheses and tools (mutable defaults, late binding, iterator exhaustion, patch location, `breakpoint()`, `-X dev`, `tracemalloc`) | hooks §8 |
| `finishing-a-development-branch` | All tool checks green; optional list of Python debt found | hooks §9 |

## The one thing this skill starts: a Python code review outside a commit range

Superpowers' review covers a range of commits. When the user asks to review a Python file, package, or snippet, or asks "is this Pythonic?", this skill reviews it directly:

1. **Read for intent:** what is the code trying to do, and does its structure show that?
2. **Walk `references/review-checklist.md`** in priority order: correctness hazards, then design, idioms, docs and typing, tests, and tooling. Style goes last, and only if no tool would catch it.
3. **Write each finding** with location (file:line), the problem, why it matters, and a short before/after snippet. Use superpowers' severities:
   - **Critical:** a bug, data loss, a security issue, or swallowed errors.
   - **Important:** design or idiom problems that will spread.
   - **Minor:** local issues.
4. **Credit what's done well.** Keep the review in proportion: a 20-line script doesn't need architecture advice.
5. **Follow `superpowers:verification-before-completion`:** if you claim a check fails or passes, run it and show the output.
6. **Hand off.** Fixes the user wants go through `superpowers:brainstorming` (brainstorming decides bounded vs architectural), then TDD. Don't rewrite the code inside the review.

## Rules

- Follow superpowers' conventions:
  - one question per message, recommended option first;
  - specs in `docs/superpowers/specs/`;
  - plans via `writing-plans`;
  - a failing test before implementation code.
- Say when you're using the lens: "Using clean-python for the pytest structure."
- Follow the project's existing conventions and tools over this skill's defaults. Suggest `assets/pyproject-tooling.toml` only when checks are missing.
- Don't spend review comments on what a tool would catch. Recommend the tool instead.
- Refactoring is a behavior-preserving change. It needs green tests before and after, and goes in its own plan tasks, separate from behavior changes.
- If a principle here conflicts with a superpowers rule, follow superpowers and mention the tension.

## Credit

Condensed and paraphrased from Mariano Anaya, *Clean Code in Python* (2nd ed.). Superpowers is by Jesse Vincent (MIT), included in this repo as a reference at `vendor/superpowers`.
