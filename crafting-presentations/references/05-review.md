# Phase 5: Review

A fresh-eyes review against the checklists below. If you can dispatch subagents, send the prompt in `assets/reviewer-prompt.md` to a new agent, along with the paths to `brief.md`, `storyline.md`, `storyboard.md` and the deck. Otherwise run the checklist yourself and quote the failing text for each finding.

Findings come in two levels:
- **Blocking**: the audience would misunderstand, or not reach the outcome.
- **Polish**: everything else.

Fix every blocking finding, update the storyboard if the structure changed, and re-run the failed checks. Then report to the user in three parts:
- the results, including any polish items you chose not to fix;
- **every open assumption**;
- a **data-to-gather list**: each `[NEEDS DATA]` item with its likely source and the slide(s) it affects.

## All types

1. **No drift.** Slide titles match the storyboard, and the Key Line matches the storyline. Every date, cost and count is identical everywhere it appears: slides, notes, appendix, and handouts.
2. **One question, one answer.** The deck answers the brief's question, and the governing thought appears within the first 3 slides.
3. **Title test.** Read in order, the titles tell the whole story. Every title is a full sentence with a verb. No title is generic ("Overview", "Summary", "Next steps").
4. **30-second test.** The main point and the Key Line (or the objectives) are stated up front.
5. **Introduction reminds, not informs.** It is short, has no exhibits, and contains no new claims. History lives here and nowhere else.
6. **Groups pass the plural-noun test.** They are MECE, 3–5 items each, never a lone sub-point, and each has a nameable order.
7. **No blank summaries.** Every summary states an insight or an effect.
8. **Actions are end products** with owners, dates, and measures where relevant.
9. **Evidence.** Every claim has support on its slide or in the appendix. Every `[NEEDS DATA]` is still visible and listed for the user. No invented numbers.
10. **One idea per slide.** Text slides are ≤ ~30 words. Charts answer one question, and the title states the answer.
11. **Say ≠ show.** The notes add to the slide rather than repeating it. Transitions link content.
12. **Legibility and accessibility.** Type is large enough, meaning never relies on colour alone, and the text or code shown is also available as real text.
13. **Timing** fits the brief's slot, with Q&A reserved and cut candidates marked.
14. **The close** asks for the decision or states the take-home action. It is not a recap slide or a bare "Questions?".

## Decide: add

- The ask is explicit, on its own slide, with options the audience can say yes or no to (and a fallback).
- The Key Line carries actions (inductive), unless the answer is surprising.
- Alternatives are judged against criteria or R2, not dismissed by elimination.
- The cost of doing nothing is quantified, or marked `[NEEDS DATA]`.

## Inform: add

- Findings are stated as ideas ("Returns from one carrier caused 60% of refunds"), not activities ("We analysed refunds").
- Implications are stated. What does this mean for the audience?

## Talk: add

- The governing thought is a transferable claim, not "our journey".
- The Key Line is made of lessons, and the chronology appears only as examples. The Key Line **titles** read as advice to the audience, not as reports of what the team did.
- The answer to "what should I do first?" is the same on the opening, Key Line, and closing slides.
- The opening hooks with something concrete within 30 seconds, and the close gives an action for Monday.
- There is at least one moment where the audience predicts or thinks before the reveal.

## Teach: add

- Personas exist, and the novice-vs-competent choice is explicit.
- Every objective uses a measurable verb, and each one is covered by a check. No check exists without an objective.
- There is a check every 10–15 minutes. Each MCQ's distractors map to named misconceptions, and "I don't know" is an option.
- The first activity is a quick, useful win on authentic data.
- There are worked examples before exercises, and no blank pages.
- Each chunk introduces ≤ ~5 new concepts, and jargon is defined before use.
- Skills are taught by live demo, and slides don't carry code walkthroughs.
- Minute cards before breaks, a feedback activity at the end, and a 10–15% time buffer.
- The setup instructions, the check command, and the helper plan exist.
- **Walk the exercises in order** as a learner would, from a fresh setup. Every step names a real UI element or command. No exercise depends on a step that isn't taught. Nothing collides across learners or with the instructor's demo. The take-home action uses only what was taught.
- The language avoids "just", mockery of learners' tools, and talk of innate talent.
