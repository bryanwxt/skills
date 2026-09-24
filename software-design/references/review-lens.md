# Design review lens (append to `PLAN_OR_REQUIREMENTS` for the final whole-branch review or a standalone requesting-code-review; never to per-task reviews)

Also review module and interface design, based on *A Philosophy of Software Design*. Report a design issue only if it causes change amplification, cognitive load, or unknown unknowns — otherwise it's style. For each, give file:line, the red flag, the consequence, and a concrete fix.

Check for:
1. **Shallow module** — interface nearly as complex as what it does; wrappers that only rename.
2. **Information leakage** — one decision (format, schema, protocol, constant) known by more than one module.
3. **Temporal decomposition** — modules split by execution order that share the same knowledge.
4. **Overexposure** — callers must set rarely-used options to do the common thing; missing defaults.
5. **Pass-through method or variable** — a layer that only forwards; a parameter threaded through code that doesn't use it.
6. **Special-general mixture** — a general mechanism with code for one specific caller.
7. **Conjoined code** — two pieces that can't be understood without reading each other.
8. **Too many exceptions / special cases** — errors callers must handle that the module could define away or handle itself.
9. **Config sprawl** — knobs the module could decide itself.
10. **Same abstraction in adjacent layers** — two layers with the same method list.
11. **Vague or hard-to-describe names/interfaces** — interface comments that need many caveats.
12. **Comments** — repeating the code, or interface docs describing implementation.

Severity: Important if the issue is in a module others depend on and will spread with future changes; otherwise Minor. Don't recommend splitting code just to make it smaller — only when it gives cleaner abstractions.
