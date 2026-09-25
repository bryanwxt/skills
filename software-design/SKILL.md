---
name: software-design
description: 'Use when superpowers work (brainstorming, writing-plans, code review) decides how code splits into modules or what their interfaces expose; when asked to audit an app''s architecture, reduce complexity, or judge whether code is well designed; or when the repo''s CLAUDE.md lists software-design as an installed lens. Based on Ousterhout''s "A Philosophy of Software Design".'
---

# Software Design (superpowers lens)

Superpowers owns the process. This lens owns judgment about modules and interfaces. It never runs its own design process, never writes a second design document, and never writes production code, so it's safe to use while brainstorming's gate is closed.

**The lens.** Good design reduces complexity. Complexity shows up in three ways: change amplification (one change touches many places), cognitive load (a lot to hold in your head), and unknown unknowns (it isn't clear what to change or know). It comes from dependencies and obscurity. The tools:
- **deep modules:** a small interface over a lot of functionality;
- **information hiding:** each design decision lives in one module;
- a different abstraction per layer;
- pull complexity down into the module rather than onto its callers;
- define errors out of existence;
- design it twice.

A finding that causes none of the three symptoms is style, not design. Every principle can be overdone: never split code just to make pieces smaller.

## Quick rule: bounded and trivial changes

Don't open the reference files. In the one-line lens check, write `design ok` unless the change:
- leaks a decision into a second module;
- adds a pass-through method, layer, or parameter;
- makes an interface shallower.

Put pre-existing design debt under follow-ups.

After the change, end with this exact line (the lens check), shared by all three lenses:
`Lens check: design <ok|note> · python <ok|note> · data <ok|note>`
Build it from installed lenses only, as `coordination.md` shows (e.g. only clean-python installed → `Lens check: python ok`); drop python if no .py file changed and data if no data changed; write "ok" only if that lens flags nothing. Add no questions of your own: state lens decisions as defaults under **Defaults chosen**.

## Inside superpowers steps

Read `references/coordination.md` once per session; it's shared by all three lenses. Then read the section of `references/superpowers-hooks.md` for the current step:
- brainstorming (context, questions, approaches, module cards, self-review);
- writing-plans;
- TDD;
- execution;
- review;
- debugging;
- finishing.

For spec content, use `assets/spec-sections.md`. For the final whole-branch or a standalone reviewer, use `references/review-lens.md` (per-task reviewers get lens rules only through the plan's Global Constraints).

## Architecture audit (the one flow this skill starts)

For "audit / review the architecture" with no commit range, follow `references/audit.md`.

**Deeper reference:** `references/principles.md`.

*Condensed and paraphrased from John Ousterhout, "A Philosophy of Software Design" (2nd ed.). Superpowers © Jesse Vincent (MIT).*
