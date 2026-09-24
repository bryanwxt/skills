# Decision: <short title>

**Path:** decision / spike-then-decision · **Status:** proposed / accepted / superseded by <link> · **Date:** <date>
**Saved at:** `docs/superpowers/decisions/YYYY-MM-DD-<topic>.md`

## Understanding (written back and confirmed)
- **Outcome wanted:** <…>
- **Workload:** <load parameters and access patterns>
- **Non-negotiable guarantees:** <named precisely>
- **Constraints:** <operational model, existing stack, budget, team>
- **Stated by user:** <only what the user actually said> · **Assumed (defaults accepted or inferred):** <…>

## Options
| Option | Fits the workload because | Fails or strains because | Failure behaviour (leader loss, partition, retry) | Operational cost | Exit cost |
|---|---|---|---|---|---|
| A (recommended) | | | | | |
| B | | | | | |
| C | | | | | |

## Spike results (if any)
<What was measured, how, results, threshold, and "throwaway code discarded".>

## Decision
<One sentence.>

## Consequences
- **Easier:**
- **Harder / given up:**
- **Guarantees we now rely on:**
- **Product facts relied on:**

  | Claim | Source | Checked on |
  |---|---|---|

## Revisit when
<The load level, requirement, or product change that reopens this.>

## Hand-off
Adopting this is a new `superpowers:brainstorming` request: <one-line prompt>.

## Self-review
Tick only what you actually verified. Anything unticked must appear under "Not verified".

- [ ] No placeholders, contradictions, or ambiguity
- [ ] Guarantees named precisely
- [ ] Failure behaviour covered for each option
- [ ] Product facts fetched and dated (or listed under Not verified)
- [ ] The recommendation says which assumed facts it depends on
- [ ] "Revisit when" stated
