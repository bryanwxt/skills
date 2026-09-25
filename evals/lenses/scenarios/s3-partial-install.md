You are simulating an agent using the superpowers workflow with exactly ONE lens skill installed. Do not invoke any skills; read files directly.

Installed lens (start from SKILL.md and open the files it points to for the steps involved):
{{LENS_DIRS}}
No other lens is installed.
Superpowers: read brainstorming/SKILL.md and writing-plans/SKILL.md under {{SUPERPOWERS}}

Repo: {{REPO}}

Request 1 (bounded): "{{BOUNDED_REQUEST}}" Assume the short design was approved and implemented with no issues found.
Request 2 (architectural): "{{ARCH_REQUEST}}"

Follow the files as written; don't improve on them. Answer under 450 words, using exactly these section labels:

DEFAULTS CHOSEN: the "Defaults chosen" list from Request 1's short design.
LENS CHECK: the exact final lens-check line for Request 1, alone on the line.
SPEC HEADINGS: Request 2's spec ## headings in order, with the ### lens subsections under each.
GLOBAL CONSTRAINTS: Request 2's plan Global Constraints lines.
GAPS: every instruction you couldn't follow, or that referred to a lens that isn't installed, and what you did.
