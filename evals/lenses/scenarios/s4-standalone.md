You are simulating an agent that has the lens skills below installed alongside superpowers. Do not invoke any skills; read files directly. Start from each lens's SKILL.md and open only the files it tells you to open for these requests.

Lens skills:
{{LENS_DIRS}}
Superpowers: {{SUPERPOWERS}}

Request 1: "Postgres or DynamoDB for our user-session store? We're a 3-person team already running Postgres."
Request 2: "Review the architecture of this TypeScript repo and tell me what to fix."

Follow the files as written. Answer under 400 words, using exactly these section labels:

R1 LENS AND FLOW: which lens and which of its flows handle Request 1, and the path you'd announce.
R1 OUTPUT: what you'd produce, and its file path if any.
R2 LENS AND FLOW: which lens and flow handle Request 2.
R2 OUTPUT: what you'd produce, and its file path.
FILES OPENED: every lens file you opened, in order.
