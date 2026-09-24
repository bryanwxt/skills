---
name: software-design
description: Design-quality lens for superpowers workflows, based on John Ousterhout's "A Philosophy of Software Design": deep modules, information hiding, pulling complexity down, defining errors out of existence, design it twice, and red-flag review. Use it inside superpowers:brainstorming (approaches, component design, spec self-review), superpowers:writing-plans (ordering tasks around interfaces), and superpowers:requesting-code-review / receiving-code-review (module and interface structure). Also use it when asked to audit an existing app's architecture, reduce complexity, or judge whether code is well designed. It reviews design only and never writes production code.
---

# Software Design (superpowers lens)

Superpowers owns the process. This lens owns judgment about modules and interfaces. It never runs its own design process, never writes a second design document, and never writes production code, so it's safe to use while brainstorming's gate is closed.

**Lanes**
- **software-design:** how the system splits into modules, what each module hides, and what its interfaces are.
- **clean-python:** how those interfaces and modules are written in Python.
- **data-intensive:** stores, guarantees, and dataflow. A module card says which module hides those choices.

**The lens.** Good design reduces complexity. Complexity shows up in three ways: change amplification (one change touches many places), cognitive load (a lot to hold in your head), and unknown unknowns (it isn't clear what to change or know). It comes from dependencies and obscurity. The tools:
- **deep modules:** a small interface over a lot of functionality;
- **information hiding:** each design decision lives in one module;
- a different abstraction per layer;
- pull complexity down into the module rather than onto its callers;
- define errors out of existence;
- design it twice.

A finding that causes none of the three symptoms is style, not design.

## Quick rule: bounded and trivial changes

Don't open the reference files. In the one-line lens check, write `design ok` unless the change:
- leaks a decision into a second module;
- adds a pass-through method, layer, or parameter;
- makes an interface shallower.

Put pre-existing design debt under follow-ups.

After the change, end with this exact line (the lens check), shared by all three lenses:
`Lens check: design <ok|note> · python <ok|note> · data <ok|note>`
Drop python if no .py file changed and data if no data changed; write "ok" only if that lens flags nothing. Add no questions of your own: state lens decisions as defaults under **Defaults chosen**.

## Inside superpowers steps

Read `references/coordination.md` once per session; it's shared by all three lenses. Then read the section of `references/superpowers-hooks.md` for the current step:
- brainstorming (context, questions, approaches, module cards, self-review);
- writing-plans;
- TDD;
- execution;
- review;
- debugging;
- finishing.

For spec content, use `assets/spec-sections.md`. For the reviewer, use `references/review-lens.md`.

## Architecture audit (the one flow this skill starts)

Use this for "audit / review the architecture" when there's no commit range. If the request also covers Python or data, run the joint review described in the coordination file. Follow its standalone flow, and add these steps:
1. **Path:** targeted (one module or pain point) or full (whole codebase).
2. **Map:** one line per module saying what it hides. Find hot spots: most-changed files (`git log`), most-imported modules, public APIs.
3. **Walk 1–2 realistic changes** through the code and list every file and concept each one touches.
4. **Red flags** (`references/red-flags.md`) in the hot spots. Rate each module's depth: deep / ok / shallow. Check that adjacent layers use different abstractions.
5. **Each finding:** file:line with evidence, symptom ← cause, and a concrete fix (with interface signatures when proposing a new interface).
6. **Write the audit** with `assets/audit-template.md` to `docs/superpowers/reviews/YYYY-MM-DD-<topic>-design-review.md`, then self-review, review gate, hand-off.

**Guardrails**
- Recommendations must make things simpler for a module's users.
- Never split code just to make pieces smaller.
- Every principle can be overdone.
- If a design issue would restructure components during a bounded task, say so, so brainstorming can step up to the architectural path.
- Cite files and lines, and mark anything you didn't read as unverified.

**Deeper reference:** `references/principles.md`.

*Condensed and paraphrased from John Ousterhout, "A Philosophy of Software Design" (2nd ed.). Superpowers © Jesse Vincent (MIT).*
