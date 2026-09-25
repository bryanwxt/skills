You are simulating an agent that uses the superpowers workflow plus the lens skills below. Do not invoke any skills; read the files directly.

Lens skills (read SKILL.md, references/coordination.md, references/superpowers-hooks.md, assets/spec-sections.md in each):
{{LENS_DIRS}}

Superpowers skills (read SKILL.md of brainstorming, writing-plans, subagent-driven-development, and subagent-driven-development/task-reviewer-prompt.md): {{SUPERPOWERS}}

Scenario: an approved spec for a Python/Postgres "gift card redemption" service. Redeeming a code must happen exactly once even under concurrent requests and client retries; a confirmation email is sent after redemption; a new `redemptions` table is added; a `GiftCardService` module hides the ledger. The repo has no linter or type checker configured. Execution will use subagent-driven-development.

Follow the files as written (do not improve on them; if they conflict, say which files and what you'd do). Answer under 450 words, using exactly these section labels:

SPEC HEADINGS: the spec's ## headings in order, and which lens's content goes under each.
TASKS: the plan's task titles, in order, one per line as "Task N: title".
GLOBAL CONSTRAINTS: the plan's Global Constraints lines.
REVIEW FOCUS: the plan's Review Focus lines.
DISPATCH: for Task 2's implementer, what lens content goes where (plan text vs dispatch prompt) and how it gets there.
TASK REVIEWER: what lens content Task 2's per-task reviewer receives, via which template slot.
FINAL REVIEWER: what lens content the final whole-branch reviewer receives, via which slot.
CONFLICTS: any conflicts between the lens files and superpowers, or "none".
