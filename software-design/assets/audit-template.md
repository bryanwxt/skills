# Architecture audit: <application>

**Scope:** <what was read, what was sampled, what wasn't read>
**Date:** <date>

## Summary
<3–5 sentences: overall health, the biggest source of complexity, and the single highest-leverage change.>

## System map
| Module | Abstraction it provides | What it hides | Depth (deep / ok / shallow) |
|---|---|---|---|

Dependency notes: <direction, cycles, adjacent layers with the same abstraction>
Hot spots: <most-changed, most-imported, most-feared — with how you found them>

## Change walkthroughs
### <Realistic change>
Files and concepts touched: <list>. Complexity observed: <symptom, with specifics>.

## Findings
Severity uses superpowers' scale: **Critical** (data loss, security, broken invariants), **Important** (design problems that spread with future changes in modules others depend on), **Minor** (local).

### 1. <Short title> — <Critical / Important / Minor>
- **Where:** <file:line>
- **Red flag:** <name>
- **Evidence:** <2–3 lines from the code you read>
- **Symptom ← cause:** <e.g. change amplification ← information leakage>
- **Fix:** <concrete change; new interface signatures if proposing one>
- **Size:** <bounded / probably architectural> (brainstorming makes the final call)

### 2. …

## What's working well
<Patterns worth copying elsewhere.>

## Hand-off
Each fix the user wants becomes its own `superpowers:brainstorming` request, then `superpowers:writing-plans`. Suggested order (highest leverage first; note any that must go together):
1. <finding #> — <one-line brainstorming prompt>
2. …

## Not verified
<Areas not read and conclusions that depend on them.>
