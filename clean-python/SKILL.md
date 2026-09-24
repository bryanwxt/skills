---
name: clean-python
description: Applies clean-code practices for Python when designing, writing, reviewing, or refactoring Python code — Pythonic idioms and protocols, contracts and error handling, cohesion and coupling, SOLID in Python, decorators, descriptors, generators and async, testing with pytest and mocks, design patterns, and clean architecture. Use whenever the user writes, reviews, refactors, or asks how to structure Python code, a Python package, or a Python service, or asks whether some Python is "Pythonic", clean, or well designed.
---

# Clean Python

Clean code is code that other people can read, understand, and change safely. Formatting and style are necessary but not enough: the real question is whether the code expresses its ideas clearly and keeps technical debt low. Leave formatting to tools and spend human (and Claude) attention on design and intent.

This skill has four modes. Pick one from the request, or combine them (e.g. review → refactor):

| Mode | When | Output |
|---|---|---|
| **Design** | New module, package, or service; "how should I structure this?" | Component sketch, key interfaces with type hints and docstrings, dependency direction |
| **Write** | "Write a function/class/script that…" | Idiomatic, typed, documented code plus tests |
| **Review** | "Review this", PRs, "is this Pythonic?" | Prioritized findings with before/after snippets |
| **Refactor** | "Clean this up", "reduce duplication", legacy code | Safety net of tests first, then small verified steps |

Reference files (read when the mode calls for them):

- `references/pythonic.md` — idioms and protocols: slicing, context managers, comprehensions, properties, dataclasses, iteration, magic methods, decorators, descriptors, generators, async, and common gotchas. Read for Write, Review, and Refactor.
- `references/design.md` — contracts, defensive programming, error handling, cohesion/coupling, DRY/YAGNI/KIS, EAFP, inheritance vs composition, function arguments, SOLID, patterns, and architecture. Read for Design and Review.
- `references/testing.md` — unit testing, pytest, fixtures, mocks, coverage, property-based and mutation testing, and safe refactoring. Read for Write and Refactor.
- `references/review-checklist.md` — a code-smell checklist with fixes. Read for Review.
- `assets/pyproject-tooling.toml` — a starter tool config (formatter, linter, type checker, tests, coverage).

If the `software-design` skill is also installed, use it for module-level and system-level complexity questions (deep modules, information hiding), and this skill for Python-specific implementation and idioms.

## Baseline for all modes

1. **Automate the boring parts.** Code should pass an autoformatter (black or ruff format), a linter (pylint, flake8, or ruff), and a type checker (mypy or pyright), all run in CI. If the project has none, suggest `assets/pyproject-tooling.toml`. Don't spend review comments on things a tool would catch — recommend the tool instead.
2. **Follow PEP 8** and the project's existing conventions. Consistency with the codebase beats personal preference.
3. **Type-annotate public interfaces.** Annotations document intent and let tools catch mistakes. They complement docstrings, they don't replace them.
4. **Docstrings explain, comments are rare.** Public modules, classes, and functions get docstrings describing what they do, their inputs, outputs, and exceptions. Inline comments should explain *why* something non-obvious is done, never restate the code. Don't leave commented-out code.
5. **Practicality beats purity.** Every principle here is a guideline. When following one would make the code worse for the situation at hand, say so and don't follow it.

## Mode: Design

1. Clarify the domain: what the code must do, what will likely change, and what external things it touches (databases, APIs, files, frameworks).
2. Separate concerns into cohesive components with low coupling. Keep the domain logic independent of frameworks and I/O; put adapters at the edges and have them depend on the domain, not the other way round (dependency inversion). Read `references/design.md` §Architecture.
3. Name components after domain concepts so the structure reveals intent.
4. Define the key interfaces: abstract base classes or `typing.Protocol` for extension points, small interfaces rather than large ones, dependencies passed in (injected) rather than created inside.
5. Plan the package layout: group by similarity, avoid giant modules, keep constants and shared definitions in predictable places, and expose the public API through `__init__.py` / `__all__`.
6. Plan testability: every component should be testable without its real external dependencies.
7. Show the design as type-hinted signatures with docstrings before writing implementations.

## Mode: Write

1. Start from the interface: signature with type hints and a docstring.
2. Write it the Pythonic way — see `references/pythonic.md`. Prefer the language's protocols (iteration, context managers, properties, dataclasses) to hand-rolled equivalents.
3. Keep functions small and doing one thing, at one level of abstraction. Keep argument lists short; group related arguments into an object.
4. Handle errors deliberately: raise specific exceptions at the right level of abstraction, chain them with `raise … from e`, never silence them with a bare `except: pass`.
5. Write tests alongside the code (pytest). Cover the normal case, boundaries, equivalence classes, and edge cases.
6. Run the formatter, linter, type checker, and tests if they're available, and fix what they report before presenting the code.

## Mode: Review

1. Read the code for intent first: what is it trying to do, and does the structure reflect that?
2. Walk `references/review-checklist.md`. For each finding give: location, the problem, why it matters (readability, maintainability, correctness, testability), and a concrete before/after snippet.
3. Prioritize: correctness bugs and dangerous patterns (mutable defaults, swallowed exceptions, shared state in descriptors or class attributes) first, then design problems (coupling, cohesion, SOLID violations), then idioms, and style last (and only if no tool covers it).
4. Credit what's done well.
5. Keep it proportional: a 20-line script doesn't need architecture advice.

## Mode: Refactor

1. **Tests first.** If the code has no tests covering the behaviour you're about to change, write characterization tests before touching it. Refactoring means changing structure without changing behaviour, and tests are the only proof of that.
2. Find the smells with `references/review-checklist.md`.
3. Change in small steps, running tests after each: rename, extract function, introduce parameter object, replace conditional with polymorphism, replace inheritance with composition, extract a decorator for repeated cross-cutting logic, split a large module into a package that re-exports the old names.
4. Keep the public interface stable where callers depend on it. When a module grows too big, turn it into a package whose `__init__.py` imports the old names so nothing breaks.
5. Update the tests as the code evolves — test code deserves the same care as production code.
6. Summarize what changed and why, and note anything left for later.

## Credit

Condensed and paraphrased from Mariano Anaya, *Clean Code in Python* (2nd ed.). The book is worth reading in full for the worked examples.
