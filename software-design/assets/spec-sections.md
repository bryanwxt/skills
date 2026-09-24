# Sections to add to a brainstorming spec

Add these inside the superpowers spec (`docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md`). They go alongside brainstorming's own sections (architecture, components, data flow, error handling, testing), not in a separate document. Omit sections that don't apply.

## Likely directions of change
<What will probably change. Module boundaries are drawn around these.>

## Knowledge to hide
| Design decision / knowledge | Owning module |
|---|---|
| … | … |

## Approaches considered
### <Approach A>
<Decomposition in a paragraph: modules and what each hides. Strengths. Weaknesses.>
### <Approach B>
<…>
**Chosen:** <approach or hybrid> — <why the others lost>

## Components (one card per significant module)
### <Module>
- **Abstraction:** <one sentence, without saying how it works>
- **Hides:** <…>
- **Interface:**
  ```
  <signature>   // <one-line interface comment>
  ```
- **Errors:** defined away: <…> · masked: <…> · exposed to callers: <…>
- **Defaults:** <…>
- **Depends on:** <…>

## Layering
<Each layer and the distinct abstraction it provides — no pass-through layers.>

## Cross-module decisions
<Decisions that span modules, recorded once here and referenced from code comments.>

## Red-flag check
<Result of the red-flag pass in spec self-review, and what changed because of it.>
