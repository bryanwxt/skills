# Standalone reviews and decisions (shared)

<!-- standalone:start — identical in software-design, clean-python and data-intensive; check with scripts/check-coordination.sh in the lens repo -->
For work outside a superpowers build: architecture audits, Python reviews, technology choices, and data or incident reviews. This file is identical in all three lenses: read one copy, never another lens's. Read `coordination.md` first (also one copy); its question rules apply here too.

- **Routing:**
  - structure → software-design audit;
  - Python file or snippet → clean-python review;
  - data flows, stores or an incident → data-intensive review;
  - technology choice → data-intensive decision;
  - anything spanning lenses → **one** joint review.
- **Joint reviews:** load each covered lens with the Skill tool, and use the union of their templates' self-review items.
- **Flow:** announce the path → questions (budget, choice vs fact) → post the write-back **in chat** with the four labels, in the same message that says the document is being written → write the document directly (no section-by-section or finding-by-finding approvals; only a short summary in chat) → self-review → one review gate → hand off to `superpowers:brainstorming`. Never implement in the flow.
- **Location:** `docs/superpowers/{reviews,decisions}/YYYY-MM-DD-<topic>…md`. Commit on a branch.
- **Findings:** sorted by severity (Critical / Important / Minor) and tagged `[data]`, `[design]` or `[python]`. Assign them by concern:
  - schema, constraints, invariants → data;
  - module boundaries → design;
  - idioms, typing, tooling → python.

  Missing tooling that hides defects is Important. Data findings, including side effects in the write path, are written as event sequences.
- **Self-review:** check that findings are sorted Critical → Minor, and never tick something you haven't verified. Fetch and date product facts, or list them under "Not verified".
- Load templates only when writing the document.
<!-- standalone:end -->
