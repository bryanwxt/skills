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

After every code change, including debugging fixes, end with the lens-check line. Its segments, in this order: `design` if software-design is installed; `python` if clean-python is installed and a .py file changed; `data` if data-intensive is installed and data changed. Write "ok" only if that lens flags nothing. E.g. only clean-python installed → `Lens check: python ok`; all three installed, a .py change, no data → `Lens check: design ok · python ok`.

Lenses add no questions, and they don't replace brainstorming's. When the request doesn't say what the change is for, brainstorming's first message is its one purpose question and nothing else; lens defaults wait for the design message. In the design, list at most 3 lens defaults the user might not expect under **Defaults chosen**, or leave the list out.

## Inside superpowers steps

When brainstorming classifies the request as bounded or a spike, the quick rule above is all this lens needs: open no reference files for it. Otherwise, at each superpowers step, read two files, one copy each from any lens:
- `references/coordination.md`, the first time only;
- that step's file: `references/steps/brainstorming.md`, `writing-plans.md`, `tdd.md`, `execution.md`, `verification.md`, `review.md`, `debugging.md` or `finishing.md`.

Each step file has the shared rules and a section per lens; skip lenses that aren't installed.

For the final whole-branch or a standalone reviewer, use `references/review-lens.md` (per-task reviewers get lens rules only through the plan's Global Constraints).

## Architecture audit (the one flow this skill starts)

For "audit / review the architecture" with no commit range, follow `references/audit.md`.

**Deeper reference:** `references/principles.md`.

*Condensed and paraphrased from John Ousterhout, "A Philosophy of Software Design" (2nd ed.). Superpowers © Jesse Vincent (MIT).*
