# Design: <system name>

## Problem
<What the system must do, for whom, and the constraints (scale, performance, platform, team).>

## Likely directions of change
<What will probably change in the next year or two. Module boundaries are drawn around these.>

## What matters most
<The few things the design is structured around (the leverage points), and what is deliberately de-emphasized.>

## Knowledge to hide
| Design decision / knowledge | Owning module |
|---|---|
| … | … |

## Alternatives considered
### Option A: <name>
<Sketch: modules and key interfaces in a paragraph. Strengths. Weaknesses.>
### Option B: <name>
<…>
### Decision
<Which option (or hybrid) and why the others lost.>

## Modules
### <Module name>
- **Abstraction:** <one sentence>
- **Hides:** <…>
- **Interface:**
  ```
  <signature>   // <one-line interface comment>
  ```
- **Errors:** defined away: <…> · masked: <…> · exposed: <…>
- **Defaults:** <…>
- **Depends on:** <…>

## Layering
<Each layer and the distinct abstraction it provides.>

## Cross-module decisions
<Decisions that span modules, documented once here and referenced from the code.>

## Red-flag check
<Result of running the red-flag list against this design, and what was changed.>

## Open questions
<…>
