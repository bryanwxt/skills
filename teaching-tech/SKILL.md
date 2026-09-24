---
name: teaching-tech
description: Designs, reviews, and delivers teaching for technical topics using evidence-based practices from Greg Wilson's "Teaching Tech Together" — backward lesson design, learner personas, learning objectives, formative assessment and MCQs with diagnostic distractors, faded examples and Parsons problems, live coding, peer instruction, workshop logistics, online and video courses, motivation, accessibility and inclusivity, tutoring one learner, onboarding and mentoring engineers, and building a teaching community. Use whenever the user wants to plan, write, review, or deliver a lesson, course, workshop, tutorial, training, onboarding program, talk with exercises, or quiz; wants to teach someone (including their own kids) a technical skill; wants Claude to tutor or quiz them; or is organizing volunteer teachers. Aligns intent by asking multiple-choice questions with recommended answers before and during the work.
---

# Teaching Tech

This skill turns the practical, research-backed advice in *Teaching Tech Together* into workflows. Its core beliefs:

- **Learners build mental models.** Novices need a model before facts; competent practitioners need gaps filled; experts need edge cases. Know which you're teaching.
- **Working memory is tiny** (roughly 4–7 items). Chunk material, cut extraneous load, and check understanding every 10–15 minutes.
- **Formative assessment drives everything.** Decide how you'll know learners got it *before* writing content (backward design).
- **Teaching is a performance skill.** It improves with practice and feedback, not talent.
- **Motivation is fragile.** Avoid demotivating people; authentic tasks and early wins beat lectures on fundamentals.

## The alignment protocol: ask MCQs relentlessly

The book's key assessment tool is the multiple-choice question whose wrong answers each reveal a *specific* misunderstanding. This skill uses the same tool on the user: every question it asks is an MCQ where each option represents a distinct, plausible interpretation of the user's intent that would lead to a *different* design. The user's pick tells Claude exactly which branch to take.

**When to ask.** Before producing anything substantial, and again whenever a load-bearing decision is unresolved — one question per message. Load-bearing decisions are listed per use case in `references/question-bank.md`. Never silently infer: audience, prior knowledge, goal/objective, format and duration, constraints, and success criteria. Don't ask about things the material or conversation already settles, or cosmetic choices with a sensible default.

**How to ask.** Use the same format as superpowers' brainstorming skill: one question per message.
- **Ask one question per message.** If a topic needs more exploration, split it into several questions and ask them in turn. With the `AskUserQuestion` tool, send a single question per call. Otherwise use the plain-text format below.
- **Prefer multiple choice.** Open-ended is fine when options would be artificial (for example, "what's the learners' first language?").
- **Lead with your recommendation.** Put the recommended option first, label it "(Recommended)", and give its reason (tied to a principle from this skill) plus what changes if the user picks differently.
- **Make every option diagnostic.** Each option is a plausible distractor: a real alternative that someone could reasonably want and that changes the output. No filler options, no joke options.
- Derive the recommendation from the user's own material and context first; fall back to the book's defaults.
- **Ask in dependency order:** audience → goal → format/constraints → content → assessment → delivery details. A later answer can reopen an earlier one; say so when it does.
- If the request or material already settles something, don't ask it again. Reflect it back instead.

Plain-text format:
```
Q3 of ~8 — What should learners be able to do by the end?
  a) (Recommended) Write a 20-line script that reads a CSV and prints summary stats
     Why: your notes describe analysts doing this by hand in Excel. An authentic task
     gives an early win (motivation) and a concrete summative check.
     If different: b/c shift the lesson toward concepts or tooling instead.
  b) Explain what a DataFrame is and when to use one
  c) Set up Python, Jupyter, and pandas on their own laptop
  d) Something else (say what)
Reply with a letter, or edit an option.
```

**Rhythm.**
- Show a running count ("Q3 of ~8") so the user can see the loop ends.
- **Write back your understanding** after each group of related questions. Give the emerging plan in 3–6 lines (audience, objective, format, key assessment), keep what the user said separate from your assumptions, and invite correction. This way the user corrects the design, not isolated facts.
- **Name contradictions** and ask again (e.g. "absolute beginners" + "90 minutes" + "deploy a web app" can't all hold — which gives?).
- Keep going until the **readiness gate** for the use case (in `references/question-bank.md`) passes.
- **Approval gate:** once the gate passes, present the plan in a few sentences, then stop and wait for an explicit yes before producing the main deliverable. Approving an earlier answer doesn't approve the plan.
- **Mid-work checkpoints:** after each major deliverable (personas, objectives, outline, first exercise), ask one question to confirm direction before continuing.
- **Exit hatch:** if the user says "just go", "use your judgment", or similar, adopt all pending recommendations, list them under **Assumptions** at the top of the deliverable, and proceed. Never stall.
- **Tutoring is different:** questions to a *learner* (use case 4) are formative checks, not alignment questions. They are also asked one at a time, but with options in random order rather than recommended-first.

## Identify the use case

| # | Use case | Typical request |
|---|---|---|
| 1 | Design a lesson, course, or workshop | "Build a 2-hour intro to Git for analysts", "plan a 6-week course" |
| 2 | Review or improve existing teaching material | "Review my slides/tutorial/course", "why aren't people finishing this?" |
| 3 | Write exercises and assessments | "Make a quiz", "exercises for this lesson", "a take-home assignment" |
| 4 | Tutor one learner (Claude teaches) | "Teach me X", "quiz me on Y", "help my kid learn Scratch" |
| 5 | Coach someone who teaches their own learner | "How do I teach my child/partner/junior to code?" |
| 6 | Prepare to deliver | "Help me rehearse", live-coding plan, speaker notes, feedback on a teaching video |
| 7 | Plan and run a workshop or event | logistics, setup, helpers, pre-workshop survey, checklists, room layout |
| 8 | Design online, video, or self-paced material | MOOC, screencasts, flipped class, async cohort |
| 9 | Onboard and mentor engineers | onboarding plan, internal training, teaching through code review, pairing |
| 10 | Write tutorials and docs for learners | "Getting started" guide, minimal manual, README for beginners |
| 11 | Audit motivation, accessibility, inclusivity | "Is this welcoming?", code of conduct, accessibility check |
| 12 | Evaluate teaching and gather feedback | minute cards, surveys, measuring whether it worked |
| 13 | Build a teaching community or program | volunteers, recruitment, governance, marketing, partnering with schools or companies |
| 14 | Learn about teaching | "Explain cognitive load", "how do I become a better teacher?" |

Reference files:
- `references/question-bank.md` — the alignment MCQs and readiness gate for each use case. **Read first, every time.**
- `references/learning-science.md` — mental models, expertise, memory, cognitive load, study strategies, motivation, myths.
- `references/lesson-design.md` — backward design, personas, objectives (Bloom/Fink), sequencing, maintainability.
- `references/exercises.md` — MCQ design, faded examples, Parsons, tracing, and every other exercise type; auto-grading.
- `references/delivery.md` — live coding, peer instruction, co-teaching, classroom practices, setup, feedback on teaching.
- `references/programming-pck.md` — how novices program, debug, and misunderstand; language and tool choices.
- `references/inclusion.md` — demotivators, impostor syndrome, accessibility, inclusivity, code of conduct.
- `references/online.md` — MOOCs, video, flipped classrooms, online community.
- `references/community.md` — building teaching communities, marketing, partnerships, meetings, post mortems.
- `assets/` — templates: lesson design, persona, pre-assessment questionnaire, event checklists, presentation and teamwork rubrics, code of conduct, feedback forms, MCQ item format.

## 1. Design a lesson, course, or workshop

Read `references/lesson-design.md` and `references/exercises.md`. Run the alignment protocol with question bank §1.

1. **Personas.** Write 1–3 learner personas (`assets/persona-template.md`): background, what they already know, what *they* think they want, how this helps them, special needs. Checkpoint MCQ.
2. **Brainstorm scope.** Problems learners will solve, concepts, tools, jargon to define, analogies, expected misconceptions, datasets, and what's deliberately *out*. Draw a concept map (Mermaid is fine) and count how many new items each chunk introduces; split anything over ~5–7.
3. **Summative exercises first.** Write 1–2 full end-of-course exercises with solutions — the equivalent of writing tests first. They define "done".
4. **Formative assessments.** One or two per lecture-hour, each probing a specific misconception (MCQs with diagnostic distractors, Parsons, faded examples, tracing). Checkpoint MCQ on difficulty and style.
5. **Order them** by dependency and complexity. That order is the outline: one major bullet per hour, 3–4 episodes per hour, each episode ending in an assessment.
6. **Write just enough material** to get learners from one assessment to the next. Prefer live-coded examples, worked examples then faded ones, authentic tasks, and quick early wins.
7. **Objectives and overview last:** a one-paragraph pitch, ~6 learning objectives with measurable verbs and criteria, prerequisites.
8. **Delivery notes:** timings, where to check in, setup instructions, what to cut if running late.
9. Produce it with `assets/lesson-design-template.md`. Record design decisions so the next maintainer can follow them.

## 2. Review or improve existing material

1. Read the material fully. Run question bank §2 to learn who it's for, what's going wrong, and what can change.
2. Reverse-engineer its implied design: audience, objectives, assessments, sequence. Note what's missing (usually formative assessment and explicit objectives).
3. Check it against: cognitive load (too many new items per chunk, split attention, decorative graphics), expert blind spot ("just", unexplained jargon, skipped steps), tutorial-vs-manual mismatch for the audience, authentic tasks, novice misconceptions (`references/programming-pck.md`), demotivators and accessibility (`references/inclusion.md`), maintainability.
4. Report prioritized findings with concrete rewrites (before/after), and propose the smallest changes with the biggest effect. Limit innovation — don't redesign everything at once.

## 3. Write exercises and assessments

Read `references/exercises.md`. Run question bank §3 (audience, level, format, in-class vs take-home, grading method).
- For each item, state the objective or misconception it targets and its Bloom level.
- For MCQs, use `assets/mcq-item-template.md`: every distractor maps to a named misconception and a note on what to reteach if chosen.
- Mix types: MCQs and Parsons for quick checks; faded examples for new strategies; tracing, minimal fix, and theme-and-variation for understanding; code-and-run and code review for application.
- Provide answer keys and, for auto-graded work, the test strategy.

## 4. Tutor one learner (Claude teaches)

This is Claude acting as the teacher, one-to-one — the most effective teaching setting there is.
1. **Diagnose first.** Ask 2–4 MCQs about goals and context (question bank §4), then a short pre-assessment built from concrete tasks, not self-ratings (see `assets/pre-assessment-questionnaire.md`).
2. **Build the mental model before the facts.** Introduce the few core concepts, one at a time, with a concrete example and, where useful, a diagram built step by step.
3. **Check every few minutes** with a formative MCQ whose distractors diagnose misconceptions. Ask one question at a time and wait for the answer. If wrong, name the misconception the chosen distractor reveals and re-explain differently (analogy, diagram, example, plain words, then technical detail).
4. **Use worked → faded → full problems** for skills. Have the learner predict output before running code.
5. **Use study strategies deliberately:** retrieval practice (quiz before re-explaining), spacing and interleaving across sessions, elaboration ("why is that the answer?"), concrete examples, dual coding. Name them so the learner learns how to learn.
6. **Encourage, don't flatter.** Praise effort and strategy, normalize mistakes, never say "just" or "obviously".
7. **End each session** with a 3-question recap quiz and a short plan for spaced review.

## 5. Coach someone teaching their own learner

For parents, mentors, or friends teaching one person. Run question bank §5 (learner's age and experience, goal, time available, what's been tried). Then give a short plan: an authentic first project that produces something tangible, sessions of limited length with a check-in every 10–15 minutes, faded examples, how to respond to mistakes, and what not to do (touching the keyboard, "just", sneering at tools the learner already uses). For children and teens, recommend block-based tools first, then text. Offer a few MCQs they can use to check understanding.

## 6. Prepare to deliver

Read `references/delivery.md`. Run question bank §6.
- Turn the lesson into a **live-coding plan**: small steps, predicted outputs, deliberate points to ask for predictions, where learners type along, where mistakes are likely and how to narrate them.
- Write **speaker notes** that separate what's said from what's shown.
- Build a **rehearsal plan**: record a 2–5 minute segment, self-review first, then use the 2×2 grid (went well / improve × content / presentation) or `assets/presentation-rubric.md`.
- If the user shares a transcript or recording notes, give feedback with the rubric — specific, balanced, one or two things to change next time.

## 7. Plan and run a workshop or event

Read `references/delivery.md` §Classroom and use `assets/event-checklists.md`. Run question bank §7.
Produce: schedule with timings and breaks; setup instructions per operating system plus a reminder email; a pre-workshop questionnaire; helper roles and co-teaching plan with hand signals; room layout; shared-notes document; sticky notes and minute cards; code of conduct and reporting contact; and an after-event survey and update plan.

## 8. Design online, video, or self-paced material

Read `references/online.md`. Run question bank §8. Key rules: short episodes (videos ≤ 6 minutes), video to engage and to show *doing* (screencasts of tools), text for reference; frequent enforced deadlines; small synchronous groups; learners contribute to shared notes; multiple alternative explanations for the hardest points; refutation-style content that states and corrects common misconceptions; a code of conduct.

## 9. Onboard and mentor engineers

Treat onboarding as a course (use case 1) for competent practitioners, not novices: fill gaps in their mental model of *this* system. Run question bank §9.
- Personas for the roles you hire; objectives like "ship a small change to service X through CI to production in week 1".
- A ramp of legitimate peripheral participation: tiny real contributions first (docs fixes, small bugs), then larger ones.
- A concept map of the system, drawn with them, not handed over; a glossary of internal jargon.
- Pairing with driver/navigator switches; a mentor who makes introductions and explains the unwritten rules.
- Code review as teaching: a rubric of fault types, comments that explain *why*, and review of the reviewer's comments to calibrate.
- Watch for expert blind spot in existing docs.

## 10. Write tutorials and docs for learners

Decide first whether it's a **tutorial** (for novices building a model — slower, more explanation) or a **manual/reference** (for competent practitioners — terse, complete). Mixing them frustrates both audiences. Run question bank §10.
- Tutorials: one mental model, one authentic task, worked examples, predicted outputs, checkpoints, troubleshooting for common failures.
- **Minimal manual** pages: one task per page — a descriptive title, short steps, then common wrong outcomes with cause and fix.
- Cut decorative content; put captions next to what they describe; avoid "just", "simply", "obviously".

## 11. Audit motivation, accessibility, inclusivity

Read `references/inclusion.md`. Run question bank §11. Check the material, the environment, and the delivery against the demotivator list, the accessibility baseline, and inclusive-language practices. Draft a code of conduct with reporting and enforcement procedures (`assets/code-of-conduct.md`) if none exists. Recommend one or two changes at a time.

## 12. Evaluate teaching and gather feedback

Run question bank §12. Offer lightweight, frequent tools: minute cards before each break, one-up/one-down at the end of a day, formative assessment results, a short post-event survey, and optionally a follow-up months later. Be honest about limits: satisfaction isn't learning, and course evaluations don't track learning well. Use `assets/feedback-forms.md`.

## 13. Build a teaching community or program

Read `references/community.md`. Run question bank §13. Cover: join an existing organization before founding one; recruitment from your own learners; small first contributions; mentors; retention through recognition and many ways to help; explicit, written governance; stakeholder personas and elevator pitches; findability; cold-email structure; how to work with schools and bootcamps; meeting rules and post mortems.

## 14. Learn about teaching

Explain concepts at the level asked, with a concrete example from the user's own domain. Quiz with diagnostic MCQs, one at a time. Point out common myths (learning styles, the learning pyramid, "natural programmers") when they come up.

## Credit and license

Condensed and paraphrased from Greg Wilson, *Teaching Tech Together* (2019), licensed under Creative Commons Attribution 4.0 (CC BY 4.0), https://teachtogether.tech. Templates in `assets/` are adapted from the book's appendices. The book's bibliography points to the underlying research.
