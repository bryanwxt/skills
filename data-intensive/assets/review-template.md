# Data architecture review: <system or incident>

**Path:** targeted / full · **Date:** <date> · **Saved at:** `docs/superpowers/reviews/YYYY-MM-DD-<topic>-data-review.md`

## Understanding (written back and confirmed)
- **Trigger:** <…>
- **Flows in scope:** <…>
- **Guarantees the business assumes:** <named precisely>
- **What can change:** <…>
- **Stated by user:** <…> · **Assumed:** <…>

## System map
```mermaid
flowchart LR
  %% components, stores, and the guarantee each link provides
```
| Entity | System of record | Derived copies and how they're kept in sync | Guarantee actually provided |
|---|---|---|---|

Isolation level in use: <per database, from config> · Replication: <topology, sync/async> · Partitioning: <keys>

## Incident timeline (if applicable)
| Time | Event | Evidence |
|---|---|---|

## Findings
Severity uses superpowers' scale: **Critical** (data loss, silent corruption, broken invariants), **Important** (correctness or availability problems under load or failure), **Minor**.

### 1. <Title> — <Critical / Important / Minor>
- **Where:** <component, file:line, config>
- **What goes wrong:** <concrete event sequence>
- **Likelihood / impact:** <…>
- **Evidence:** <what you read or ran>
- **Fix:** <change, and what it gives up>
- **Size:** <bounded / probably architectural> (brainstorming makes the final call)

### 2. …

## What's sound
<Parts that are correct and worth keeping.>

## Hand-off
Each fix the user wants becomes its own `superpowers:brainstorming` request. Suggested order (highest blast radius first):
1. <finding #> — <one-line brainstorming prompt>

## Not verified
<Areas not read or tested, and conclusions that depend on them.>

## Self-review
- [ ] Every finding has evidence and an event sequence
- [ ] Guarantees named precisely
- [ ] Product facts cited and dated
- [ ] Unverified areas listed
