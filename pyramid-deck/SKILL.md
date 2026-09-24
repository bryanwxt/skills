---
name: pyramid-deck
description: Builds a presentation end to end, from whatever the user has (a bare topic, rough notes, a report, data, a transcript, or an old deck), using Barbara Minto's Pyramid Principle. The skill owns the narrative and the structure. It defines the problem, writes the Situation-Complication-Question-Answer introduction, builds and tests the pyramid, storyboards it into action-titled slides, scripts speaker notes, and then renders the deck. When intent or material is unclear, it asks question after question, and every question carries a recommended answer drawn from the book. Use this skill whenever the user wants to make, plan, outline, storyline, restructure, or fix a presentation, deck, pitch, slides, board or steering-committee update, proposal, recommendation, or progress review, even if they only say "help me present X" or "turn this into slides".
---

# Pyramid Deck

This skill turns any starting material into a presentation whose storyline follows the Pyramid Principle. The storyline is the product. Slides are the last step and follow mechanically from it. Most bad decks are bad because the thinking was never arranged. The prose and the chart styling are rarely the cause. So spend most of the effort on phases 1–4 and don't open a slide tool until the storyline passes its checks.

Read these reference files when the phase calls for them. Each one paraphrases the relevant chapters of *The Minto Pyramid Principle*:

- `references/pyramid-rules.md`: the three rules, vertical and horizontal logic, deduction vs induction, logical order, MECE, and how to summarize groupings. Read it before building or testing any pyramid.
- `references/introductions.md`: SCQA, the four standard questions, the common business and consulting patterns, and problem definition (R1/R2). Read it in Phase 2.
- `references/slides.md`: mapping the pyramid to slides, text-slide rules, exhibit-slide rules, and the storyboard and script procedure. Read it in Phases 5–6.
- `references/question-bank.md`: the question bank, with a recommended answer and a book rationale for each question. Read it before asking anything.

## Core stance

1. **Think first, write later.** No slide gets drafted until the governing thought, the Key Line, and the introduction are agreed. Words that are already written tend to feel finished even when the thinking behind them is muddled, which is why the order matters.
2. **Ask relentlessly, but never empty-handed.** Every question carries a recommended answer, a one-line reason tied to a pyramid principle, and the practical consequence of choosing differently. The user should be able to reply "yes" to most questions.
3. **Top-down first, bottom-up to reconcile.** Try to state the Question and the Answer before anything else. Use the user's material to test the answer and fill in the pyramid beneath it.
4. **Say which principle you are applying.** When you restructure the user's ideas, name the rule briefly so they learn it and can push back.

## The questioning protocol

This protocol decides whether the skill works, so follow it closely.

**When to ask.** Ask whenever one of these load-bearing elements is unknown or ambiguous. Don't infer silently:

- Audience: who they are, what they already know, and what decision or action is wanted from them
- The Question the deck answers, and the Answer (the governing thought)
- Situation and Complication, meaning what the audience already accepts as true
- The Key Line: the 2–5 points that directly answer the question raised by the governing thought
- Setting: live talk vs read-ahead vs both, length, and output format

Don't ask about anything you can settle from the material, the conversation, or a clear default. Examples are font choice, or whether to use a bar chart for comparing amounts.

**How to ask.** Use the same format as superpowers' brainstorming skill: one question per message.

- **Ask one question per message.** If a topic needs more exploration, split it into several questions and ask them in turn.
- **Prefer multiple choice.** Open-ended is fine when options would be artificial (for example, "what's the exact budget figure?").
- **Lead with your recommendation.** Put the recommended option first, label it "(Recommended)", and give its reason (the book principle) and what changes if the user picks differently. Every other option must be a real alternative that would change the storyline.
- In Claude Code, prefer the `AskUserQuestion` tool with a single question per call. Otherwise use this plain-text form:

```
Q3 of ~6 — What question should the deck answer in the audience's mind?
a) (Recommended) "Should we approve $1.2M for the warehouse system?"
   Why: your notes describe a problem plus a costed fix, which is the classic
   "seeking approval" pattern. Its question is always "Should I approve?"
   If instead: b) gives a steps-based Key Line and no approval ask;
   c) gives a criteria-based Key Line.
b) "How do we fix the backlog?"
c) "Which of the three options should we choose?"
Reply with a letter, or edit an option.
```

Rules for the loop:

- Ask in dependency order, one question at a time: audience before the Question, the Question before the Answer, and the Answer before the Key Line. A later answer often changes an earlier one; say so when it does.
- If the request or material already settles something, don't ask it again. Reflect it back instead.
- Show a running count ("Q3 of ~6") so the user can see the loop will end.
- **Write back your understanding** after each group of questions (audience, then S-C-Q-A, then the Key Line). Give the emerging storyline in 3–5 lines, keep what the user said separate from your assumptions, and invite correction.
- Keep asking until the storyline passes the Phase 4 tests. Don't stop because the user seems impatient. Instead, offer an exit.
- **The exit.** If the user says "just go", "use your judgment", or similar, adopt every pending recommendation. Record each one in an **Assumptions** block at the top of `storyline.md`, and continue. Never stall.
- If an answer creates a contradiction, name it and ask again. For example: the Complication says costs are the problem, but the proposed Answer is about speed. Contradictions are the most valuable thing the loop surfaces.
- **Approval gate.** Present the governing thought and Key Line, then stop and wait for an explicit yes before starting Phase 5. Approving the audience or the Question doesn't approve the storyline.

## Workflow

### Phase 0: Triage the starting point

Look at what exists and classify it, because each kind needs a different first move:

| Starting point | First move |
|---|---|
| Bare topic or idea | Top-down. Go straight to audience, Question, and Answer questions. Expect the most questioning. |
| Rough notes or brain dump | Bottom-up. List every point, group the similar ones, and draw conclusions upward. Then confirm the Question. |
| Report, memo, or paper | Extract its governing thought and Key Line. It often has a buried conclusion, so move it to the top. |
| Data, spreadsheets, or analysis output | Find what the numbers *say*: one message per exhibit. Ask what decision the data serves. |
| Transcript or meeting notes | Pull out decisions, disagreements, and asks. The Complication usually hides in the disagreements. |
| Existing deck to fix | Rebuild its implied pyramid from the slide titles. Diagnose it with the Phase 4 tests. Show the before and after structure first. |
| Mixed | Combine these approaches. Material you don't need goes to an appendix, not the storyline. |

Read all supplied material fully before asking anything. Ask only what the material doesn't answer.

### Phase 1: Pin down the audience and the setting

Settle who the audience is, what they know, what they must do afterwards, whether the deck is presented live or read, the time or slide budget, and the format. Defaults and recommendations are in `question-bank.md` §1.

### Phase 2: Define the problem and the introduction (SCQA)

Read `references/introductions.md`. Establish, in this order:

1. **Situation.** A statement about the subject that the audience will accept without argument.
2. **Complication.** What happened in that situation that creates tension.
3. **Question.** The question the Complication raises. It is usually one of four: what should we do, how do we do it, is this the right solution, or why didn't it work.
4. **Answer.** The governing thought, written as one sentence with a verb, and specific enough that someone could disagree with it.

If the deck is analytical and the problem itself is fuzzy, use the problem-definition frame first: starting point, disturbing event, R1 (the undesired result), R2 (the desired result), and what has been tried so far. Then convert it to SCQA.

Match the request to a common pattern: directive, approval to spend, how-to, choosing among alternatives, proposal, or progress review. The pattern predicts the Key Line, so propose it as the recommendation.

### Phase 3: Build the pyramid

Read `references/pyramid-rules.md`.

- Take the new question the Answer raises (usually why, how, or which). Answer it with the Key Line: 2–5 points, inductive by preference, in a stated logical order (time, structure, or importance).
- Repeat the question-and-answer step one level down under each Key Line point. For a presentation, two levels below the governing thought is usually enough. Deeper material goes to an appendix.
- State every box as a full idea-sentence. "Three issues" isn't an idea. A specific claim about the issues is.
- Write the result to `storyline.md` using `assets/storyline-template.md`. Also write the machine-checkable `storyline.json`, whose format is described in `scripts/check_storyline.py --help`.

### Phase 4: Test the storyline (gate)

Run `python scripts/check_storyline.py storyline.json` and fix any errors. Then apply the judgment tests that no script can check:

- **Vertical.** Does each point summarize the points beneath it, and does it raise exactly the question they answer?
- **Horizontal.** Is each grouping the same kind of idea, MECE, and in a defensible order? For action groups: does their combined effect equal the parent? For situation groups: does the parent state the insight they share?
- **Introduction.** Does it contain only what the audience already accepts? Is there nothing new in the Situation, and nothing the audience already knows sitting in the body?
- **Governing thought.** Does it answer the Question directly? Would the audience's likely "so what?" be answered by the Key Line?
- **Deduction check.** Is any deductive chain longer than four steps, or could it be restated inductively? If so, restate it.

Show the user the pyramid as an indented outline (`check_storyline.py --outline`). Get explicit agreement on the governing thought and the Key Line before Phase 5. This is the last cheap moment to change direction.

### Phase 5: Storyboard

Read `references/slides.md`. Map the pyramid to slides:

- Opening: the Situation and Complication (one or two slides), then the governing thought together with the Key Line as the roadmap slide.
- For each Key Line point: a divider or summary slide, then one slide per support point.
- Close: a restatement of the governing thought and Key Line, then next steps or the ask.

Every slide gets an **action title**: the full-sentence point it proves, 15 words or fewer. Reading only the titles in order must reproduce the argument. For each exhibit slide, state the question it answers (components, item comparison, time series, frequency distribution, or correlation), pick the chart that fits, and sketch the data needed. Mark any data you don't have as `[DATA NEEDED: …]` rather than inventing numbers. Update `storyline.json` with the slides and rerun the checker.

### Phase 6: Script

Write speaker notes per slide. The notes carry transitions, context, and nuance. The slide carries only the point and its evidence. Write the opening (Situation → Complication → Question → Answer) in full, word for word. For read-ahead decks, move enough of the reasoning into the slide body that it stands alone, but still keep each slide to one idea.

### Phase 7: Render

Only now build the file. Delegate the mechanics:

- If a `pptx` skill is available, read its SKILL.md and follow it for .pptx creation (it covers pptxgenjs, charts, notes, and validation).
- If the user asked for another format (Google Slides, Keynote, HTML, reveal.js, Markdown/Marp), use that format's tooling. The storyline doesn't change.
- If no helper skill exists, use `pptxgenjs` (or `python-pptx`). Put action titles in the title placeholder, use native charts for exhibits, and write the script into speaker notes.

Presentation defaults: keep it mostly exhibits with few text slides, use at most about 30 words and 6 lines per text slide, and aim for type readable from the back of the room (≥24pt body on 16:9). Use a restrained palette and a single accent color that highlights the data point the title talks about.

### Phase 8: Final QA

- **Title-only read.** Read the action titles in order. Do they tell the full story without the bodies?
- **Evidence match.** Does each slide's chart or text actually show what its title claims?
- **Placeholders.** Are any `[DATA NEEDED]` markers left? List them for the user rather than filling them with invented numbers.
- **Render check.** Render the slides to images and check that there is no overflow and that nothing is illegible.

Deliver the deck together with `storyline.md`, which records the pyramid, the assumptions, and the open data needs, so the user can defend the logic in the room.

## Output files

- `storyline.md`: the human-readable pyramid, SCQA, assumptions, and open questions
- `storyline.json`: the structure used by the checker
- `storyboard.md`: one row per slide with number, type, action title, visual sketch, and pyramid reference
- The rendered deck (`deck.pptx` or the requested format), with speaker notes
