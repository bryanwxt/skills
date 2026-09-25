You are grading one anonymous answer against a fixed rubric. Read only the files named here.

Context: {{CONTEXT}}
{{FIXTURE}}
The answer to grade: {{ANSWER}}

Rubric. For each item, `hit` is true only if the answer states it explicitly (not implied, not "could be considered"). Quote at most 20 words of evidence for each hit; use "" for a miss.
{{ITEMS}}

{{FP}}

Reply with ONLY this JSON object:
{"items": {"<item id>": {"hit": true|false, "evidence": "..."}, ...}, "false_positives": <number>, "false_positive_examples": ["..."]}
