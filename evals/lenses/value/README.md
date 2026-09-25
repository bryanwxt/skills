# Lens value eval

Do the lenses make superpowers' output better, and is that worth the extra tokens? This runs the same tasks twice: superpowers alone (**bare**), and superpowers plus software-design, clean-python and data-intensive (**lens**). A blind judge then grades every answer against a rubric of problems planted in the task.

The integration evals in `../` check that the lenses wire in correctly. This one checks whether they're worth having.

## Run

```bash
bash evals/lenses/value/run.sh                   # all four tasks, 5 runs per arm, Sonnet answers, Opus judge
bash evals/lenses/value/run.sh -n 3 v2 v3        # fewer runs, some tasks
bash evals/lenses/value/run.sh -m haiku -J opus  # other answer / judge models
```

The isolation is the same as `../run.sh` (headless `claude -p`, no user settings, hooks or installed skills). Results, the judge's grades and `summary.md` land in `results/<timestamp>-<model>/` (gitignored).

## Tasks

| | Task | Planted problems (rubric) | Superpowers files (both arms) | Extra for the lens arm |
|---|---|---|---|---|
| v1 | Write up the spec and plan for gift card redemption | concurrent redemption, client retries, email in the transaction, adding a column to a 12M-row table, Stripe used from two places, race tests on a real DB | brainstorming, writing-plans | each lens's SKILL.md, hooks (brainstorming and writing-plans sections), spec-sections; coordination.md once |
| v2 | Review a diff | check-then-act race, mutable default, bare `except`, pass-through layer, NOT NULL column on 12M rows, email inside the transaction, DB mocked in tests, a test that can't fail | code-reviewer.md | the three `review-lens.md` appended to `PLAN_OR_REQUIREMENTS`, as the lenses do for a final review |
| v3 | Debug duplicate orders from a report | redelivery past the SQS visibility timeout; check-then-insert without a unique constraint; a fix at the database; a test with two deliveries on a real DB; red herrings (replica lag, cache) not ranked first | systematic-debugging | each lens's SKILL.md and debugging hook; coordination.md once |
| v4 | Reply to a small bounded request (`--limit`) | harm check: stays in scope, validates input, plans a test; words and questions asked | brainstorming | each lens's SKILL.md |

## How grading works

- **Blinding:** each answer is copied under a random id, with lens names, book authors, lens file names and `Lens check` lines replaced by `[redacted]`. The judge sees one answer at a time with its rubric, never the arm.
- **Strict hits:** a rubric item counts only if the answer states it explicitly. For v2, the judge also counts false positives (claims about the code that are wrong).
- **Cost:** tokens, cost and time come from `claude -p --output-format json`.

## Limits

- Planted problems measure whether known hazards get caught, not overall design quality.
- Redaction hides names, not style: lens answers use some distinctive vocabulary (e.g. "event sequence", "module card"), so the blinding is partial.
- Each task simulates one step of the process from its files, not a full multi-turn session.
- One set of fixtures, mostly Python/Postgres. The lenses might matter less (or more) elsewhere.

## Results: September 2026 (Sonnet answers, Opus judge, superpowers 6.4.1, 5 runs per arm)

After replacing lens examples that matched the fixtures (see the lens repo history), with the per-step file layout:

| Task | Rubric items hit, bare → lens | Where they differ | Cost (median), bare → lens |
|---|---|---|---|
| v1 design (gift cards) | 5.6 → **6** of 6 | Stripe isolated in one module 1/5 → 5/5 (with no example naming it); race tests on a real DB | $0.09 → $0.17 |
| v1b design (clinic booking) | 5.6 → **6** of 6 | calendar isolation and real-DB tests | $0.09 → $0.18 |
| v2 review | 8 → 8 of 8 | none: both arms find every planted defect (the fixture is too easy) | $0.07 → $0.08 |
| v3 debug | 5.2 → **6** of 6 | real-DB regression test with two deliveries | $0.06 → $0.11 |
| v4 bounded (purpose given) | 3 → 3 of 3 | none; same length (318 vs 327 words) | $0.07 → $0.09 |

With the purpose left out of the v4 request, both arms ask brainstorming's purpose question (lens 5/5 runs, bare 3–5/5).

**Reading it:**
- The lenses add the things Sonnet doesn't volunteer on design and debugging work: isolating a dependency behind one module, and correctness tests against a real database. That holds on a second domain too.
- They add nothing where Sonnet is already at the ceiling (the review fixture), and nothing on small changes except a little cost.
- Cost is about 1.8–1.9× on design and debugging steps. Most of it is extra turns, because headless runs read one file per turn. Fewer, larger files cost less than many small ones.
- n = 5 per arm, Sonnet only, two design domains, mostly Python/Postgres.
