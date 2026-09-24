# Python review: <package / module>

**Path:** quick / full · **Date:** <date> · **Saved at:** `docs/superpowers/reviews/YYYY-MM-DD-<topic>-python-review.md`

## Understanding (written back and confirmed)
- **Prompt:** <…>
- **Areas that matter most:** <…>
- **Constraints:** <Python version, frameworks, API stability>
- **Stated by user:** <only what the user actually said> · **Assumed (defaults accepted or inferred):** <…>

## Tooling status
Missing tooling that hides real defects is an Important finding, not Minor.

| Check | Configured? | Result (output attached) |
|---|---|---|
| Formatter | | |
| Linter | | |
| Type checker | | |
| Tests / coverage | | |

## Findings
Severity: **Critical** (bug, data loss, security, swallowed errors) · **Important** (design or idiom problems that will spread) · **Minor** (local).
Sorted by severity, Critical first. In a joint review, tag each finding with its lens: `[data]`, `[design]` or `[python]`. Assign by concern: schema, constraints and invariants → data; module boundaries → design; idioms, typing and tooling → python.

### 1. <Title> — <Critical / Important / Minor> <[lens] in joint reviews>
- **Where:** <file:line>
- **Problem / why it matters:** <…>
- **Before:**
  ```python
  ```
- **After:**
  ```python
  ```

### 2. …

## What's done well
<…>

## Hand-off
Each fix the user wants becomes its own `superpowers:brainstorming` request, then TDD:
1. <finding #> — <one-line brainstorming prompt>

## Not verified
<…>

## Self-review
Tick only what you actually verified. Anything unticked must appear under "Not verified".

- [ ] Every finding cites code actually read
- [ ] Tool claims backed by output
- [ ] No placeholders, contradictions, or ambiguity
