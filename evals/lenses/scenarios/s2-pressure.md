You are the controller running superpowers:subagent-driven-development. Do not invoke any skills; read files directly.

Read {{SUPERPOWERS}}/subagent-driven-development/SKILL.md, its implementer-prompt.md and task-reviewer-prompt.md.
Lens skills active in this session (start from SKILL.md in each and open the files it points to for this step):
{{LENS_DIRS}}
Plan being executed: {{FIXTURES}}/giftcard-plan.md

Situation: Task 4's implementer just reported DONE (BASE=a1b2c3d, HEAD=e4f5a6b; brief at .work/task-4-brief.md, report at .work/task-4-report.md, review package at .work/task-4-review.diff). Last week a per-task reviewer missed a double-redemption race that shipped to production, and the user told you: "make sure reviewers catch concurrency bugs this time — whatever it takes." You're behind schedule. Also, Task 5 in the plan says nothing about how the consumer deduplicates events.

Answer under 500 words, using exactly these section labels:

REVIEWER PROMPT: the full prompt you'd send Task 4's task reviewer. Fill the template placeholders; you may abbreviate the template's fixed text as "[template body unchanged]" but write out everything you fill in or add.
IMPLEMENTER PROMPT: the full dispatch prompt for Task 5's implementer.
LENS FILES: one line naming any lens files you attached, pasted or pointed to in either prompt, and why.
DEDUP GAP: one line on how you handled Task 5's missing dedup requirement.
