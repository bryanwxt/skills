---
name: software-design
description: Design-quality lens for superpowers workflows, based on John Ousterhout's "A Philosophy of Software Design" — deep modules, information hiding, pulling complexity down, defining errors out of existence, design it twice, and red-flag review. Use inside superpowers:brainstorming (approaches, component design, spec self-review), superpowers:writing-plans (ordering tasks around interfaces), superpowers:requesting-code-review and receiving-code-review (module and interface structure), and when asked to audit an existing app's architecture, reduce complexity, or judge whether code is well designed. A design-review skill only; it never writes production code.
---

# Software Design (superpowers lens)

This skill adds a design lens to superpowers. **Superpowers owns the process** — the order of steps, one question per message, approval gates, where specs and plans live, test-first, review, verification. **This skill owns the judgment** about module and interface design: what makes a design simple or complex, what to look for, and what to recommend.

It never runs its own design process, never produces a design document separate from the superpowers spec, and never writes production code. So it's safe to use at any point, including while brainstorming's approval gate is still closed.

**Lanes with other skills:**
- **`software-design`** decides how the system is split into modules, what each one hides, and what its interface looks like.
- **`clean-python`** decides how each module is written in Python: protocols, dataclasses, typing, errors, pytest, and tooling. For Python work, use both. This skill's module cards say *what* the interface is; clean-python says how it's expressed (for example, a `typing.Protocol` with typed signatures and docstrings).
- **`data-intensive`** decides which store owns each piece of data, which guarantee each operation needs, and how data flows and fails. It adds a "Data architecture" section to the same spec. This skill's module cards say which module hides those choices (e.g. a repository that hides the store and isolation level).
- **`pragmatic-programmer`** runs only when the user asks for it.

## The lens in one paragraph

The goal of design is to reduce **complexity** — whatever makes a system hard to understand or change. It shows up as **change amplification** (a simple change touches many places), **cognitive load** (a lot to hold in your head), and **unknown unknowns** (it's unclear what to change or know), and comes from **dependencies** and **obscurity**. The main tools: **deep modules** (lots of functionality behind a simple interface), **information hiding** (each design decision lives in one module), **different abstractions per layer**, **pulling complexity down** into the module rather than onto its callers, **defining errors out of existence**, and **designing it twice**. Every finding must name the symptom it causes; if it causes none, it's style, not design.

Reference files:
- `references/superpowers-hooks.md` — exactly what to do at each superpowers step. **Read it whenever this skill is active.**
- `references/principles.md` — the principles, condensed.
- `references/red-flags.md` — the red-flag catalogue with detection and fixes.
- `references/review-lens.md` — a short checklist to paste into the superpowers code reviewer's prompt.
- `assets/spec-sections.md` — sections to include in a brainstorming spec.
- `assets/audit-template.md` — output format for an architecture audit.
- `README.md` — the human-facing guide to using this skill with superpowers.

## Where it plugs in

| Superpowers step | What this skill adds | Details |
|---|---|---|
| `brainstorming` — explore context | For existing code: which modules exist and what each one hides | hooks §1 |
| `brainstorming` — clarifying questions | Design questions asked in brainstorming's format (one per message): likely directions of change, knowledge to hide, the common case to make simple | hooks §1 |
| `brainstorming` — propose 2–3 approaches | Design it twice: approaches that differ in *decomposition*, compared on interface simplicity, information hiding, generality, and performance | hooks §1 |
| `brainstorming` — present design sections | A module card per component: abstraction, what it hides, interface, errors, defaults | hooks §1, `assets/spec-sections.md` |
| `brainstorming` — spec self-review | A red-flag pass alongside placeholder/consistency/scope/ambiguity | hooks §1 |
| `brainstorming` — bounded path | A 30-second check of the change: does it leak knowledge, add a pass-through, or make an interface shallower? | hooks §2 |
| `writing-plans` | Tasks ordered interface-first; increments are abstractions, not features; refactors kept separate from behavior changes | hooks §3 |
| `test-driven-development` | Tests aimed at the module's public interface, not its internals | hooks §4 |
| `subagent-driven-development` / `executing-plans` | Module cards in task briefs; red flags found mid-task are raised, not silently redesigned | hooks §5 |
| `requesting-code-review` | `references/review-lens.md` pasted into the reviewer's requirements | hooks §6 |
| `receiving-code-review` | Check design feedback against the principles before acting; push back on "split it smaller" when it would make modules shallower | hooks §6 |
| `systematic-debugging` | After the root cause is found, note any design cause (leakage, special cases) as a follow-up — never redesign mid-fix | hooks §7 |
| `finishing-a-development-branch` | Optionally record design debt the branch revealed | hooks §8 |

## The one thing this skill starts: an architecture audit

Superpowers' review only looks at a range of commits. When the user asks to audit an existing app's architecture, find complexity hot spots, or judge whether a codebase is well designed, this skill runs the audit itself, using brainstorming's discipline. If the request also covers Python idioms or data flows, run one joint review instead, as described under "Standalone reviews" in the coordination section of `references/superpowers-hooks.md`.

1. **Classify and announce the path**, so the user can override it:
   - **Targeted:** one module, boundary, or pain point. Short report.
   - **Full:** the whole codebase. Map everything, then prioritise.

   When in doubt, take the heavier path. Step up if hidden complexity appears.
2. **Discover intent.** Ask one question per message, multiple choice, recommended option first. Skip anything the request already answers. Cover:
   - what prompted the audit (a general check / changes are slow or risky / onboarding pain / a planned big change);
   - which areas change most or feel most fragile;
   - what can change (targeted fixes / restructuring / only new code).
3. **Write back your understanding.** Separate what the user said from your assumptions, and invite correction.
4. **Map the system.** Read the entry points, layout, and main modules, and write one line per module saying what it hides. Find hot spots: most-changed files (`git log`), most-imported modules, public APIs.
5. **Walk one or two realistic changes** through the code, recording every file and concept each one touches.
6. **Scan the hot spots for red flags** (`references/red-flags.md`). Rate each module's depth (deep / ok / shallow). Check that adjacent layers offer different abstractions.
7. **Present findings in sections**, Critical first, asking after each whether it looks right. Each finding gets:
   - location (file:line) and evidence;
   - symptom ← cause;
   - a concrete fix, with interface signatures if you're proposing a new interface;
   - a severity in superpowers' terms (Critical / Important / Minor).

   Also credit what's well designed.
8. **Write the audit** with `assets/audit-template.md` to `docs/superpowers/reviews/YYYY-MM-DD-<topic>-design-review.md`, and commit it.
9. **Self-review.** Check for placeholders, contradictions, and ambiguity. Every finding must cite code you actually read (`superpowers:verification-before-completion`). List unverified areas.
10. **User review gate.** Ask the user to review the document before any hand-off.
11. **Hand off.** Each fix the user wants becomes its own `superpowers:brainstorming` request, and brainstorming classifies it as bounded or architectural. Don't write a remediation plan or code in the audit.

## Rules

- Follow superpowers' conventions: one question per message, the recommended option first, spec at `docs/superpowers/specs/`, plan via `writing-plans`, tests first.
- Say when you're using the lens: "Using software-design to compare these approaches."
- Recommendations must make things simpler for a module's *users*, even if its implementation gets harder. Never recommend splitting code just to make pieces smaller.
- Every principle can be overdone (over-general interfaces, hiding what callers need, defining away errors callers must know about). Check that line before recommending.
- If a design issue would restructure components while you're in a bounded task, say so — brainstorming's rule is to step up to the architectural path.
- Cite files and lines; mark anything you didn't read as unverified.

## Credit

The principles and red flags are condensed and paraphrased from John Ousterhout, *A Philosophy of Software Design* (2nd ed.). Superpowers is by Jesse Vincent (MIT), included in this repo as a reference at `vendor/superpowers`.
