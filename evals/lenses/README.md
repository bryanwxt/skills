# Lens evals

Scenario tests for the three superpowers lenses (software-design, clean-python, data-intensive). Rerun them after editing a lens, and after a superpowers update that passes `scripts/check-superpowers.sh` but might still change behaviour.

## Run

```bash
bash evals/lenses/run.sh                 # all scenarios, 3 runs each, Sonnet
bash evals/lenses/run.sh -n 5 s2         # 5 runs of the pressure scenario
bash evals/lenses/run.sh -m haiku s1 s3a # other models
```

- **Needs:** the `claude` CLI and an installed superpowers, found the same way as `check-superpowers.sh` (or set `SUPERPOWERS_SKILLS`).
- **Isolation:** each run is headless (`claude -p`) with `--setting-sources project --disable-slash-commands`. Your user settings, plugin hooks and installed skills don't leak in. Runs only get Read, Glob and Grep, and read the lens files straight from this checkout.
- **Output:** results land in `evals/lenses/results/<timestamp>-<model>/` (gitignored), one file per run, followed by a score.

## Scenarios

| | Scenario | What it catches |
|---|---|---|
| s1 | Full flow: gift-card spec → plan → dispatch → reviewers, all three lenses | spec headings out of shape, standalone tooling or interface tasks, `review-lens.md` sent to per-task reviewers, final review missing `PLAN_OR_REQUIREMENTS` |
| s2 | Controller under pressure: a race shipped last week, "whatever it takes", plus a plan gap | lens files, excerpts or checklists leaking into the per-task reviewer |
| s3a | Only clean-python installed (Python CLI) | wrong lens-check line (must be `Lens check: python ok`), standing in for missing lenses |
| s3b | Only data-intensive installed (Go service) | wrong lens-check line (must be `Lens check: data ok\|note`) |
| s4 | Standalone requests: "Postgres or DynamoDB?", "review the architecture" | wrong lens or flow, missing path announcement, wrong output path |
| s5 | Trigger test: 10 requests, lenses that must and must not load | descriptions over- or under-triggering |

## Scoring

`score.py` flags the known failure shapes automatically. Treat the flags as hints: automated counts overstate both failures and passes, so read every flagged run and skim the clean ones. Variance matters too: if runs disagree about the same step, the wording isn't binding even when most runs pass.

Reference results from September 2026 (Sonnet, superpowers 6.4.1):

| Scenario | Result |
|---|---|
| s1 | 5/5 correct |
| s2 | 1 in 5 runs leaks lens content under pressure (a prohibition-worded variant scored 3/5; the recipe wording holds at about 1/5) |
| s3a, s3b | 3/3 each |
| s5 | 69/69 checks over 3 runs |

To score an existing results directory again: `python3 evals/lenses/score.py <dir>`.
