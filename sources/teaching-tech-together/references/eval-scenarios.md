# Eval scenarios

> Cross-cutting file for Greg Wilson, *Teaching Tech Together* (2018), CC BY 4.0. Candidate scenarios for testing a skill built from this material, following the RED → GREEN → REFACTOR cycle in superpowers' writing-skills. Run each scenario **without** the skill first and record what the agent actually does; write guidance only for failures you observe. The "expected baseline failure" is a prediction from the reference readers, not an observation. Fixtures are invented for testing.

Scenario types: application (can it apply the practice?), recognition (does it spot the fault?), premise (the user asks for something the book argues against), counter-example (does it hold back when the practice doesn't apply?), trigger (does the skill load?). Pass criteria are observable in the output; read every run that a script flags.

## Lesson and exercise design

### S1 Forward design (application)
- **Prompt:** "Create a 3-hour intro Git workshop for biology grad students."
- **Expected baseline failure:** a topic-by-topic slide outline, with exercises added at the end, if at all.
- **Pass:**
  - personas before content
  - measurable objectives in Bloom's first four levels
  - a summative exercise written first
  - a formative check every 10–15 minutes, about 3–4 episodes per hour
  - a quick useful win first (e.g. saving and restoring work) before branching theory
- **Rules:** LES-1, LES-3, LES-8, LES-13, LES-14, MOD-7, MOT-6.

### S2 Vague objectives (recognition)
- **Fixture:** objectives "Understand version control; appreciate good practice; learn Git."
- **Pass:** each objective is rewritten as one sentence describing learner performance with a measurable verb, and the soft verbs are flagged.
- **Rules:** LES-13, LES-14.

### S3 Diagnostic MCQs (application)
- **Prompt:** "Write three multiple-choice questions to check understanding of Python list assignment."
- **Expected baseline failure:** plausible-looking distractors with no stated rationale, or a joke option.
- **Pass:** every distractor names the misconception it detects (e.g. aliasing vs. copying); there are no joke options; there is guidance on what to do when most of the class picks each wrong answer.
- **Rules:** MOD-8 to MOD-11, EXR-2.

### S4 Week-one exercises for novices (application)
- **Prompt:** "Design the exercises for week 1 of an intro Python course."
- **Expected baseline failure:** blank-page coding tasks with `foo`/`bar` data.
- **Pass:**
  - a worked example, then a faded series
  - Parsons problems without distractor lines
  - fill-in-the-blanks
  - authentic data and tangible output
  - realistic time estimates
- **Rules:** COG-5, COG-6, COG-11, EXR-7, EXR-8, MOT-7, MOT-8, CLS-27, EXR-28.

### S5 Expert blind spot (application)
- **Prompt:** "Explain to complete beginners how to set up a Python virtual environment."
- **Expected baseline failure:** "Just run `python -m venv`…", with steps skipped.
- **Pass:** no "just" or "simply"; every step is spelled out, including what success looks like; there's a check before moving on; operating-system differences are flagged.
- **Rules:** MEM-1, MEM-3, MEM-4, MOT-11, CLS-29.

### S6 Learning-styles premise (premise)
- **Prompt:** "Adapt this lesson for visual, auditory, and kinesthetic learners."
- **Expected baseline failure:** builds three VAK tracks.
- **Pass:** says briefly and politely that matching to learning styles isn't supported by evidence, and offers what is: dual coding, concrete examples, ADEPT, and active practice for everyone. It doesn't lecture.
- **Rules:** PCK-26, IND-1, IND-16, IND-18.

### S7 Auto-grader (application)
- **Prompt:** "Set up auto-grading for this assignment."
- **Pass:** a public mini test suite; correct-but-different code accepted; actionable messages; expected outputs hidden; learning judged by outcomes rather than satisfaction.
- **Rules:** EXR-4, EXR-19, EXR-23, EXR-24.

## Delivery

### S8 Pre-workshop survey (application)
- **Prompt:** "Write a pre-workshop survey."
- **Expected baseline failure:** "Rate your Python skill from 1 to 5", or quiz questions.
- **Pass:** "how easily could you do this task" questions; a follow-up with non-responders; the workshop's level advertised before sign-up.
- **Rules:** CLS-13 to CLS-15.

### S9 Presenting code (application)
- **Prompt:** "Plan how I'll present the pandas groupby section."
- **Expected baseline failure:** slides of finished code.
- **Pass:** live coding in small steps with narration, predict-before-run, mistakes kept and diagnosed aloud, a readable screen, and skeleton code instead of typing boilerplate.
- **Rules:** PRF-16 to PRF-19, PRF-22, PRF-29, PCK-8.

### S10 Feedback on teaching (application)
- **Fixture:** observer notes from a 10-minute teaching demo.
- **Prompt:** "Give them feedback."
- **Expected baseline failure:** an unstructured list of criticisms.
- **Pass:** a 2×2 grid or rubric; specific, observable points; balanced feedback; one focus for next time; a prompt for the teacher's self-assessment.
- **Rules:** PRF-4, PRF-6 to PRF-8.

### S11 Workshop with new tricks (pressure)
- **Prompt:** "For my one-day workshop I want to try sticky notes, peer instruction, shared notes, pairing, and clickers, all for the first time."
- **Pass:** recommends keeping to familiar practices plus at most one new one, and explains why.
- **Rules:** CLS-41.

### S12 Hybrid session (premise)
- **Prompt:** "Half my learners will be in the room and half on Zoom. Plan the session."
- **Pass:** recommends making every group remote, with local helpers (ONL-30). If the user keeps the mixed setup, it names the risks and the mitigations.
- **Rules:** ONL-30, ONL-5, ONL-29.

### S13 Lecture to online module (application)
- **Prompt:** "Turn my one-hour recorded lecture into an online module."
- **Expected baseline failure:** cuts it into 4×15-minute videos.
- **Pass:** videos of six minutes or less, each paired with an activity; explanations moved to text; misconceptions stated and refuted; frequent deadlines; small synchronous groups.
- **Rules:** ONL-9, ONL-10, ONL-14, ONL-17, ONL-4, ONL-5.

## Motivation and inclusion

### S14 Demotivating language (recognition)
- **Fixture:** a lesson containing "simply", a joke about Excel users, "so easy your grandmother could do it", and a `foo`/`bar` example.
- **Pass:** flags each one with its rule and supplies a rewrite.
- **Rules:** MOT-8, MOT-11, MOT-27.

## Community and outreach

### S15 Founding a club (application)
- **Prompt:** "I'm starting a coding club. Draft our founding plan."
- **Expected baseline failure:** a mission statement, a constitution, and the founder doing every task.
- **Pass:** checks for existing groups first; useful activities before manifestos; a newcomer ramp with mentors; many ways to contribute; no early constitution; a code of conduct.
- **Rules:** COM-6, COM-20, COM-4, COM-12, COM-15, COM-26, WHY-3.

### S16 Cold email (application)
- **Prompt:** "Email the city library asking to host free workshops."
- **Expected baseline failure:** a generic opener, hype, "FREE!!!".
- **Pass:** a specific point of connection; benefit, offer, credibility, and terms; short; a plain subject line; realistic expectations about response rates.
- **Rules:** MKT-15 to MKT-20.

### S17 Persuading faculty (premise)
- **Prompt:** "Write a memo convincing my department to adopt pair programming. Cite lots of research."
- **Pass:** keeps the citations the user asked for, but leads with time saved, faculty fears, and peer examples; proposes an incremental pilot; notes the initial slowdown.
- **Rules:** PTN-1 to PTN-3, PTN-6, PTN-7.

## Counter-examples

### S18 Over-application
- **Prompts:** "What's a for loop?" (asked by a learner) / "Fix the typo on slide 4." / "How long should my coffee break be?"
- **Expected failure with the skill:** returns a lesson plan, personas, or a framework lecture.
- **Pass:** answers directly. A teaching skill should key its activation to an observable predicate, such as the user designing, delivering, or evaluating teaching.

## Trigger tests

| Should load | Should not load |
|---|---|
| "Design a workshop on SQL for librarians" | "Explain what SQL is" (a learner question) |
| "Review my lesson plan" | "Fix this SQL query" |
| "Write quiz questions for my class" | "Quiz me on French verbs" |
| "How do I run a better live-coding demo?" | "Write a for loop that sums a list" |
| "Our volunteer instructors keep quitting" | "Draft a company all-hands agenda" (borderline: meetings appendix; decide and test) |
| "Turn this lecture into an online course" | "Summarize this video" |
| "Give feedback on my teaching recording" | "Give feedback on my resume" |
| "How do I make my bootcamp more inclusive?" | "Translate this lesson into Spanish" |
