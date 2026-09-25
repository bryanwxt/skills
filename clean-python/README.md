# clean-python × superpowers

`clean-python` is a Python lens for [superpowers](https://github.com/obra/superpowers). It doesn't run on its own. Superpowers runs the workflow (brainstorm → spec → plan → test-first implementation → verification → review → finish), and this skill supplies the Python judgment at each step: idioms, typing, errors, pytest, and tooling. It's based on Mariano Anaya's *Clean Code in Python*.

## Who does what

| | superpowers | clean-python | software-design |
|---|---|---|---|
| Order of steps, approval gates, questions | ✅ owns | adds Python questions to brainstorming's queue | adds design questions |
| Spec | ✅ `docs/superpowers/specs/` | adds Python subsections under the spec's own headings (layout, errors, testing, tooling) | adds module cards |
| How the system splits into modules | — | — | ✅ |
| How each module is written in Python | — | ✅ protocols, dataclasses, typing, errors, DI | — |
| Plan | ✅ `writing-plans` | exact paths; check commands in Global Constraints; tooling folded into the first task that needs it; Python rules in each task | interfaces in each task's `Interfaces: Produces` |
| Tests | ✅ test-first | pytest idioms, fixtures, mocks at boundaries, Hypothesis | test the public interface |
| "Verified" | ✅ evidence before claims | defines the evidence: pytest, linter, type checker, formatter output | — |
| Code review (commit range) | ✅ reviewer agent | rules reach per-task reviewers through Global Constraints; Python checklist for the final review; checks feedback | same, for design |
| Review of a file or snippet | — | ✅ owns, then hands fixes to brainstorming | — |
| Debugging | ✅ `systematic-debugging` | Python root-cause hypotheses and tools | design follow-ups afterwards |

## How it plays out

**"Build a CLI that syncs invoices from our accounting API."** Brainstorming leads and asks one question at a time. The lens adds the Python choices that matter, such as sync or async (it recommends sync for a CLI unless there's heavy concurrent I/O) and whether to use a Protocol for the API client so tests can inject a fake. The spec gets Python subsections under its own headings: the error hierarchy under Error handling, and package layout, typing level and required checks under Implementation notes. If the repo has no linter or type checker, `writing-plans` folds tooling setup into the first task that needs it, gives exact `src/…` and `tests/…` paths, and ends every task with `pytest`, `ruff`, and `mypy` commands.

**Implementing a plan task.** TDD runs red → green → refactor with pytest. Tests are parametrized for input tables, `pytest.raises` covers errors, and a fake client is injected rather than patched. The implementer follows the Python rules the plan wrote into its task: no mutable defaults or bare `except`, `raise … from e`, `with` for resources, and types and docstrings on public functions. It reports done only with the tool output attached, as `verification-before-completion` requires.

**"This test fails intermittently."** `systematic-debugging` leads. The lens offers Python suspects, such as shared mutable state between tests, iterator exhaustion, `mock.patch` on the wrong name, or naive vs aware datetimes, and tools such as `pytest -x --lf --pdb` and `python -X dev`.

**"Is this module Pythonic?"** There's no commit range, so `clean-python` reviews it directly. Findings are ordered correctness first and style last, with before/after snippets and superpowers' severities. Fixes then go through brainstorming and TDD.

## Setup

Follow [`SETUP.md`](SETUP.md), which is the same in all three lenses. It covers requiring superpowers in the repo's `.claude/settings.json`, copying the lenses into `.claude/skills/`, the shared CLAUDE.md block (installed lenses plus repo facts), and `scripts/check-superpowers.sh`, which confirms the installed superpowers still has every hook point the lenses rely on.

## Files

| File | Used when |
|---|---|
| `SKILL.md` | Always: role, quick rule, hook pointers, pointer to the Python review flow |
| `SETUP.md` | Wiring the lenses into a repo (shared by all three lenses) |
| `scripts/check-superpowers.sh` | Checks the installed superpowers still has every anchor the lenses hook into (shared) |
| `references/coordination.md` | Shared rules for all three lenses (questions, spec outline, plan order, tests, bounded changes, reviews); read once per session |
| `references/standalone.md` | Shared rules for standalone reviews and decisions: routing, joint reviews, flow, findings (shared by all three lenses) |
| `references/python-review.md` | The standalone Python review flow |
| `references/superpowers-hooks.md` | Step-by-step additions for each superpowers skill |
| `references/pythonic.md` | Writing or reviewing Python idioms |
| `references/design.md` | Contracts, errors, SOLID, patterns in Python |
| `references/testing.md` | pytest, mocks, coverage, property/mutation testing, refactoring |
| `references/review-checklist.md` | Full Python review |
| `references/review-lens.md` | Appended to `PLAN_OR_REQUIREMENTS` for the final whole-branch or standalone review |
| `assets/spec-sections.md` | Python subsections for a brainstorming spec, placed under its own headings |
| `assets/pyproject-tooling.toml` | Starter tool config when a project has none |

## Checking it works

| Prompt | Expected |
|---|---|
| "Build a small Python CLI that …" | Brainstorming leads; the spec has Python subsections under its own headings; the plan has verification commands per task |
| "Implement task 3 of the plan" (Python) | Failing pytest test first; the done report includes pytest/ruff/mypy output |
| "Is this file Pythonic?" | clean-python review with before/after snippets; no code rewritten; hand-off to brainstorming |
| "Fix this flaky test" | systematic-debugging leads; Python hypotheses offered in Phase 1 |

## Credit

Condensed and paraphrased from Mariano Anaya, *Clean Code in Python* (2nd ed.). Superpowers © Jesse Vincent, MIT license.
