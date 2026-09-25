# Phase 2b: Storyline as a Lesson Design (Teach)

Backward design is test-driven development for teaching. Decide what "done" looks like (what learners can *do*), write the checks that prove it, and then write **just enough** material to get learners from one check to the next. Content is written last.

## Steps, in order. Each step has a deliverable in `storyline.md`.

### 1. Personas (1–3)
Each persona has five parts:
1. **Background.**
2. **What they already know.** Tools and concepts, especially the ones you'll build analogies from.
3. **What *they* think they want.**
4. **How this session actually helps them.**
5. **Special needs.** Language, accessibility, their machine or OS, time pressure.

Also decide: **novices or competent practitioners?**
- **Novices** need a mental model before facts. Give them a guided tutorial with worked examples first.
- **Competent practitioners** need gap-filling: a reference or a task-focused session.

One session rarely serves both groups well, so choose.

### 2. Scope brainstorm
Always answer the first question, plus 2–3 of the others:
- What problems will learners solve?
- What concepts and techniques will they learn?
- What tools will they use?
- What jargon will you define?
- Which analogies from their world will you use?
- **Which misconceptions do you expect?** List them. They drive the checks.
- What datasets or examples will you use? Pick realistic ones from the learners' world, not foo/bar.

Also write **out of scope**, explicitly.

Use the **what-to-teach grid** to prioritise:
- Things that are quick to learn and useful go **first**. This is the early win.
- Things that are hard but useful are deferred or scaffolded.
- Things that are hard and rarely needed are cut.

### 3. Concept map
Draw the concept map as text:
- Nodes are concepts, and each edge is a **labelled** relationship. Example: `pivot table —summarises→ source range`.
- Count the new items per chunk. Keep each chunk to about 5 new items (working memory holds roughly 4–7).
- If a chunk has more, split it into a separate episode.

### 4. Learning objectives (about 1 per 15–20 min, 3–6 total)
- Each objective is one sentence with a **measurable verb**, a context, and criteria.
  - Bad: "understand pivot tables".
  - Good: "build a pivot table that totals sales by region and month from a raw export, and explain why a blank row breaks it".
- Bloom verbs:
  - Remember: list, name.
  - Understand: explain, classify.
  - Apply: use, build.
  - Analyze: compare.
  - Evaluate: choose, critique.
  - Create: design.
- Introductory sessions mostly sit in Understand and Apply.
- Never write "understand X", "learn about X", or "be familiar with X".

### 5. Summative exercise (the capstone)
Write 1–2 end-of-session exercises **fully**, with a worked solution. They prove the objectives are met and the tooling actually works. Write them before anything else in the material.

**Environment walk-through.** For hands-on sessions, trace what each learner's environment looks like after every exercise, in order, starting from the fresh setup. Check for:
- shared resources that many learners will touch at once (one shared file, one account, one database);
- state that an earlier step leaves behind and that breaks a later one;
- demos that would change what learners are working on;
- setup steps that are needed but missing (credentials, config).

Write down the resource layout, e.g. "one repo per pair, made from a template; the instructor's demo repo is separate".

### 6. Formative checks
Place **one check every 10–15 minutes**, each taking 1–2 minutes, and more often when teaching remotely. Each check tests one objective or one misconception. Choose a type:
- **Diagnostic MCQ.** Every wrong option maps to a *named misconception*. Include an "I don't know" option and no joke answers. Plan your response to each vote pattern:
  - All correct: move on.
  - One wrong answer dominates: address that misconception.
  - Votes spread out: re-explain a different way.
  - A few wrong: help them one-to-one.
- **Predict-then-run.** Learners predict the output before every demo.
- **Parsons problem.** Order jumbled lines of code or commands.
- **Faded example.** Repeat the worked example with progressively more blanks.
- **Fill in the blank, tracing, or minimal fix.**
- **Label a diagram.**
- **Match or rank.**

Never a blank page: learners extend or modify something that already works. Formative checks must practise exactly the kinds of problem the capstone uses.

### 7. Order into episodes, which gives you the outline
- Order the checks by dependency and complexity. **That order is the outline.**
- Plan 3–4 episodes per hour. Each episode runs: short explanation or live demo → check or exercise → debrief.
- Give each explanation its own mini-pyramid: point first, then 2–4 supporting ideas, then a worked example.
- Plan breaks and put minute cards before each one.
- Reserve 10–15% of the time as buffer for setup failures and questions.

### 8. Explanation plan per episode
For each episode, record:
- **Model before facts.** Which picture or analogy (ADEPT: Analogy, Diagram, Example, Plain language, Technical detail)?
- **Misconception.** State the wrong model, then refute it. This works better than only explaining the right one.
- **Worked examples.** Show 2+ that vary in surface details, and name the subgoals.
- **Live demo or slide.** Skills are taught by live demonstration. Slides carry diagrams and concepts, not code walkthroughs.

### 9. Overview, written last
A one-paragraph pitch, the objectives, the prerequisites, and the setup instructions to send ahead.

## Output: `storyline.md` (Teach)

```
Personas: <…>                      Level: novice | competent
In scope / out of scope: <…>
Misconceptions: M1 <…>, M2 <…>
Concept map: <edges with labels>
Objectives: O1 <verb …> …
Capstone: <full exercise + solution sketch>
Episodes:
  E1 (0:00–0:15) <objective> — explain: <model/analogy> — check: <type, targets M#>
  E2 …
Breaks / minute cards / buffer: <…>
Setup to send ahead: <…>
```

The Teach version of the 30-second test is: **can you list the objectives and show which check proves each one?** If an objective has no check, it isn't an objective. If a check has no objective, cut it.

**Gate (HARD):** show the lesson design and ask for approval or changes. No slides or material until the user says yes.
