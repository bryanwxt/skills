# Superpowers hooks: what to do at each step

Superpowers decides *when* each step happens and how to talk to the user. This file says what the design lens adds at each step. Never skip or reorder a superpowers step, and never add approval gates of your own.

## Contents
1. brainstorming — architectural path
2. brainstorming — bounded and spike paths
3. writing-plans
4. test-driven-development
5. subagent-driven-development / executing-plans
6. requesting-code-review / receiving-code-review
7. systematic-debugging
8. finishing-a-development-branch
9. What this skill never does

---

## 1. brainstorming — architectural path

**Explore project context.** For existing code, note the modules the work will touch and write one line each on what it hides. Note leaked knowledge you'll have to live with or fix. Brainstorming allows targeted improvements to code the work touches, but not unrelated refactoring — flag the rest as design debt.

**Clarifying questions.** Add these to brainstorming's queue, asked in its format: one per message, multiple choice where possible, recommended option first. Skip any the request already answers.
- *Where is this likely to change?* (e.g. new data sources / new output formats / scale / new user types). Module boundaries go around decisions likely to change.
- *What's the common case?* The interface should make it trivial; rare cases can take more effort.
- *Which details should callers never need to know?* (storage, formats, protocols, vendor APIs, retry policy…)
Only ask what changes the design; the rest are your own assumptions, written back in brainstorming's understanding note.

**Propose 2–3 approaches = design it twice.**
- Start from the list of design decisions and knowledge in the system; each significant one should belong to exactly one module. Decompose around knowledge, not around the order things happen (that's temporal decomposition, which leaks knowledge).
- Make the approaches differ in **decomposition** (where the boundaries are and what each module hides), not in cosmetic details.
- Compare each on: simplest interface for the common case; how much each module hides; generality without extra caller effort; performance where it matters; weaknesses. Lead with the recommendation, as brainstorming requires.
- If none is attractive, use the weaknesses found to generate another.

**Present design sections.** In the *components* section, give each significant module a card (`assets/spec-sections.md`):
- abstraction in one sentence (without saying how it works);
- what it hides;
- interface — signatures with a one-line comment each, written before any implementation;
- errors: defined away / masked / aggregated / exposed;
- defaults it picks so callers don't have to.
In *error handling*, prefer defining errors out of existence and masking them low down; list only the errors callers genuinely must handle. In *data flow*, check each layer offers a different abstraction (no pass-through layers). If a module is hard to name or its interface comment is hard to write briefly, the decomposition is probably wrong — revise it before presenting.

**Spec self-review.** Alongside brainstorming's placeholder, consistency, scope and ambiguity checks, run the red-flag pass on the design: shallow module, information leakage, temporal decomposition, overexposure, pass-through method or variable, special-general mixture, conjoined modules, too many exceptions, configuration sprawl, hard-to-name or hard-to-describe components. Fix inline, as brainstorming says.

**Spec contents.** Add the sections from `assets/spec-sections.md` to brainstorming's spec (`docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md`), including the rejected approaches and why they lost. Never write a second design document.

## 2. brainstorming — bounded and spike paths

**Bounded.** Before presenting the short in-chat design, check the change in about 30 seconds:
- Does it put knowledge about one decision into a second module?
- Does it add a pass-through method, layer, or parameter?
- Does it add a parameter, option, or exception callers must now think about — could the module handle it instead?
- Does it add a special case to a general mechanism?
If yes, mention it in one line of the in-chat design with the simpler alternative. If the fix would restructure components, say so: under brainstorming's rules the task steps up to the architectural path.

**Spike.** The output is an answer, not code you keep, so don't apply the lens to spike code. If the spike's answer implies a design choice, mention it in the recommendation.

## 3. writing-plans

- **Increments are abstractions, not features.** When a feature needs a new abstraction, plan tasks that build that abstraction properly, rather than a sliver of it per feature.
- **Interface first.** For each new module, the first task defines its public interface and interface comments (from the spec's module card); later tasks implement it behind that interface. Tests in each task target the interface (see §4).
- **Refactors separate from behavior changes.** Put structural changes in their own tasks, each kept green by existing tests, before tasks that change behavior.
- **Name what each task's module hides** in the task description, so implementers don't leak it elsewhere.
- **Keep tasks within one module where possible.** A task that must edit many modules for one change is a sign of leakage — flag it back to the spec rather than planning around it.

## 4. test-driven-development

- Write tests against the module's **public interface** and documented behavior, not its internal helpers. Deep modules have small interfaces, so this keeps tests few and stable, and lets implementations change freely.
- The interface comment written in the spec says what to test: arguments, results, side effects, errors, defaults.
- If a test needs lots of setup or mocks to reach the code, that's a design signal (too many dependencies or a leaky interface) — note it for the reviewer rather than working around it silently.
- Tests-first holds: interface signatures and comments come from the spec and plan; the failing test comes before implementation code.

## 5. subagent-driven-development / executing-plans

- Include the relevant module card (abstraction, hides, interface) in each task brief so implementers keep the knowledge where it belongs.
- If an implementer finds a red flag the plan didn't anticipate (e.g. the interface forces callers to know a detail), **raise it** to the controller or user instead of quietly redesigning. Small local fixes inside the module are fine; interface changes go back through the spec.

## 6. requesting-code-review / receiving-code-review

**Requesting.** Only when the diff changes module boundaries or interfaces: when filling the reviewer template, append `references/review-lens.md` to the `PLAN_OR_REQUIREMENTS` text, along with the spec's module cards for the modules touched. The reviewer runs in a separate agent and won't otherwise know the lens. Map severities: data loss, security, or broken invariants are Critical; design red flags that will cause change amplification in modules others depend on are Important; local naming, comments, and minor shallowness are Minor.

**Receiving.** receiving-code-review requires checking feedback before acting. For design feedback:
- Check it against the principles. "Split this class up" or "extract smaller functions" is only right if it produces cleaner abstractions — splitting that creates shallow modules, pass-throughs, or conjoined pieces makes things worse. Push back with the reason.
- "Add a config option / parameter" pushes a decision onto callers — ask whether the module could decide itself.
- Accept feedback that reveals leakage, special cases, or unclear interfaces.

## 7. systematic-debugging

- Don't redesign during debugging. Find and fix the root cause as systematic-debugging says.
- After the fix, if the root cause was a design problem (the same knowledge in two places, a special case in a general mechanism, an error that should have been defined away), note it as a follow-up. The user can then run a new brainstorming request for it.

## 8. finishing-a-development-branch

Optionally, in the branch summary, list design debt the work revealed (one line each: location, red flag, suggested fix) so it isn't lost. Don't fix it on this branch unless the user asks.

## 9. What this skill never does

- Run its own question round, approval gate, or design document.
- Write production code or implementation plans.
- Decide brainstorming's path (spike / bounded / architectural) — only point out when hidden complexity should step it up.
- Override superpowers' rules. If a principle here seems to conflict with a superpowers rule, follow superpowers and mention the tension to the user.
