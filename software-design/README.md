# software-design × superpowers

`software-design` is a design lens for [superpowers](https://github.com/obra/superpowers). It doesn't run on its own. Superpowers runs the workflow (brainstorm → spec → plan → test-first implementation → review → finish), and this skill supplies the judgment about module and interface design at each step, based on John Ousterhout's *A Philosophy of Software Design*.

## Who does what

| | superpowers | software-design |
|---|---|---|
| Order of steps, approval gates | ✅ owns | never adds its own |
| Asking you questions | ✅ one per message, recommended option first | adds design questions to brainstorming's queue |
| Design document | ✅ the spec in `docs/superpowers/specs/` | adds sections to that spec (never a second doc) |
| Implementation plan | ✅ `writing-plans` | fills the plan's slots: module cards and `Interfaces: Produces` per task, knowledge-hiding rules in Global Constraints; abstractions not features |
| Tests | ✅ test-first (`test-driven-development`) | says what to test: the module's public interface |
| Code review | ✅ `requesting-` / `receiving-code-review` | design rules reach per-task reviewers through Global Constraints; design checklist for the final review; checks design feedback |
| Debugging | ✅ `systematic-debugging` | notes design root causes as follow-ups afterwards |
| Architecture audit of an existing app | — | ✅ owns, then hands each fix to brainstorming |
| Writing production code | ✅ | never |

## With clean-python

For Python projects, install [`clean-python`](../clean-python/) too. The two split the work:

| Question | Skill |
|---|---|
| How should the system be split into modules, and what should each hide? | software-design |
| What should each module's interface be, and which errors should it define away? | software-design |
| How is that interface expressed in Python (Protocol vs ABC, dataclasses, type hints, docstrings)? | clean-python |
| Is the code Pythonic, typed, and error-safe? How is it tested with pytest? Which tools must pass? | clean-python |

In a brainstorming spec, both lenses add subsections under the spec's own headings: software-design adds module cards to Components, and clean-python adds their Python form plus Implementation notes. In the plan, software-design puts each module's interface in its task's `Interfaces: Produces` block and clean-python supplies exact file paths and verification commands. Per-task reviewers get both lenses' rules through the plan's Global Constraints; both checklists go to the final whole-branch review.

## How it plays out

**"Build a notification service."** Brainstorming classifies it as architectural and asks its questions one at a time. The lens adds a couple (where will this change? what should callers never need to know?). When brainstorming proposes 2–3 approaches, they differ in how the system is split up and what each part hides, and the lens compares them. The design sections get a card per module: abstraction, what it hides, interface, errors, defaults. The spec self-review includes a red-flag pass. Then `writing-plans` gives each module's interface to the task that first produces it (its `Interfaces: Produces` block), before any task that consumes it, and implementation follows test-first against those interfaces.

**"Add a `--dry-run` flag."** Brainstorming classifies it as bounded. Before the short in-chat design, the lens does a quick check: does the flag leak into modules that shouldn't care, or add a pass-through parameter? If the clean fix would restructure things, it says so, and brainstorming steps up to the architectural path.

**"Review the architecture of this repo."** Superpowers' review covers a range of commits, not a whole app, so `software-design` runs an audit: system map, a walk through a couple of realistic changes, red flags with file and line evidence, and severities in superpowers' terms. It ends with a hand-off list. Each fix you want goes back through brainstorming and writing-plans.

**Code review of a finished task.** The reviewer runs as a separate agent with a fixed template. Per-task reviewers see design rules through the plan's Global Constraints. The final whole-branch review gets the lens's checklist (`references/review-lens.md`) in `PLAN_OR_REQUIREMENTS`, so it also looks at module and interface design. When feedback comes back, `receiving-code-review` checks it; the lens pushes back on "split it smaller" when that would create shallow pieces.

**"Fix this failing test."** `systematic-debugging` runs. The lens stays out of the way until the root cause is found, then notes a design follow-up if the cause was structural (e.g. the same format parsed in two places).

## Setup

Follow [`SETUP.md`](SETUP.md), which is the same in all three lenses. It covers requiring superpowers in the repo's `.claude/settings.json`, copying the lenses into `.claude/skills/`, the shared CLAUDE.md block (installed lenses plus repo facts), and `scripts/check-superpowers.sh`, which confirms the installed superpowers still has every hook point the lenses rely on.

## Files

| File | Used when |
|---|---|
| `SKILL.md` | Always: role, hook table, audit procedure |
| `SETUP.md` | Wiring the lenses into a repo (shared by all three lenses) |
| `scripts/check-superpowers.sh` | Checks the installed superpowers still has every anchor the lenses hook into (shared) |
| `references/coordination.md` | Shared rules for all three lenses (questions, spec outline, plan order, tests, bounded changes, reviews); read once per session |
| `references/superpowers-hooks.md` | Step-by-step additions for each superpowers skill |
| `references/principles.md` | The design principles, condensed |
| `references/red-flags.md` | Red flags, how to detect them in code, how to fix them |
| `references/review-lens.md` | Appended to `PLAN_OR_REQUIREMENTS` for the final whole-branch or standalone review |
| `assets/spec-sections.md` | Design subsections for a brainstorming spec, placed under its own headings |
| `assets/audit-template.md` | Architecture audit output |

## Checking it works

Superpowers' `writing-skills` recommends testing skills with realistic prompts. Three to try:

| Prompt | Expected |
|---|---|
| "Build a new notification service" | Brainstorming leads; the spec has module cards and a red-flag check; no separate design doc |
| "Review the architecture of this repo" | software-design audit, ending with brainstorming hand-offs; no code written |
| "Fix this failing test" | systematic-debugging leads; software-design silent until a possible design follow-up at the end |

## Credit

Principles condensed and paraphrased from John Ousterhout, *A Philosophy of Software Design* (2nd ed.). Superpowers © Jesse Vincent, MIT license.
