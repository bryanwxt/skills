# Architecture audit (software-design)

Use this for "audit / review the architecture" when there's no commit range. If the request also covers Python or data, run one joint review (`references/standalone.md` (shared by all lenses; if you've already read any lens's copy this session, use that one)). Follow the standalone flow there, and add these steps:
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
