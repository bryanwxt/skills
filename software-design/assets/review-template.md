# Design review: <application name>

**Scope:** <what was reviewed, what was sampled, what wasn't read>
**Date:** <date>

## Summary
<3–5 sentences: overall health, the biggest source of complexity, and the single highest-leverage change.>

## System map
| Module | Abstraction it provides | What it hides | Depth (deep / ok / shallow) |
|---|---|---|---|
| … | … | … | … |

Dependency notes: <direction, cycles, layers with the same abstraction>
Hot spots (most changed / most feared): <list>

## Change walkthroughs
### <Realistic change 1>
Files and concepts touched: <list>. Complexity observed: <change amplification / cognitive load / unknown unknowns, with specifics>.

## Top recommendations
Ordered by complexity removed from hot spots.

### 1. <Short imperative title>
- **Where:** <files / modules>
- **Red flag:** <name>
- **Evidence:** <2–3 lines citing the code>
- **Symptom → cause:** <e.g. change amplification ← information leakage>
- **Fix:** <concrete change; include the new interface signatures if proposing one>
- **Effort / impact:** <S/M/L> / <low/med/high>
- **Principle:** <e.g. "Pull complexity downward">

### 2. …

## Other findings
| # | Where | Red flag | Fix | Effort | Impact |
|---|---|---|---|---|---|
| … | … | … | … | … | … |

## What's working well
<Patterns worth copying elsewhere in the codebase.>

## Suggested sequence
<Incremental steps, each leaving the system in a better state. Note any that must happen together.>

## Caveats
<What wasn't read, assumptions made, conclusions that depend on them.>
