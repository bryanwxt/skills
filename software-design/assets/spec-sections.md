# Design subsections for a brainstorming spec

These go inside the superpowers spec (`docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md`) as `###` subsections under brainstorming's own headings, the layout set in `references/coordination.md` (Spec). Never add them as new top-level headings or in a separate document. Omit any subsection that doesn't apply. The red-flag pass happens in spec self-review and fixes the spec inline; it gets no section of its own.

## Architecture

### Likely directions of change
<What will probably change. Module boundaries are drawn around these.>

### Knowledge to hide
| Design decision / knowledge | Owning module |
|---|---|
| … | … |

### Approaches considered
**<Approach A>:** <Decomposition in a paragraph: modules and what each hides. Strengths. Weaknesses.>
**<Approach B>:** <…>
**Chosen:** <approach or hybrid> — <why the others lost>

## Components

### <Module> (one card per significant module)
- **Abstraction:** <one sentence, without saying how it works>
- **Hides:** <…>
- **Interface:**
  ```
  <signature>   // <one-line interface comment>
  ```
- **Errors:** defined away: <…> · masked: <…> · exposed to callers: <…>
- **Defaults:** <…>
- **Depends on:** <…>

### Layering
<Each layer and the distinct abstraction it provides — no pass-through layers.>

### Cross-module decisions
<Decisions that span modules, recorded once here and referenced from code comments.>
