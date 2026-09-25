# Python review (clean-python)

Use this for "is this Pythonic?" or "review this file or package" when there's no commit range. If the request also covers structure or data, run one joint review (`references/standalone.md` (shared by all lenses; if you've already read any lens's copy this session, use that one)).
- **Quick path** (a snippet or short file): findings in chat, with before/after snippets. No document. Ask questions only if the intent is unclear.
- **Full path** (a package, or when the fixes need planning): follow the standalone flow in `references/standalone.md`, then:
  1. Read for intent. Then walk `references/review-checklist.md` in this order: correctness hazards → design → idioms → docs and typing → tests → tooling. Style comes last, and only when no tool would catch it.
  2. For each finding, give file:line, the problem, why it matters, a before/after snippet, and a severity:
     - **Critical:** a bug, data loss, security, or a swallowed error.
     - **Important:** a problem that will spread.
     - **Minor:** a local issue.

     Keep the review in proportion to the code, and credit what's good.
  3. Write it with `assets/review-template.md` to `docs/superpowers/reviews/YYYY-MM-DD-<topic>-python-review.md`, then self-review, review gate, hand-off.

  Tool claims need tool output.
