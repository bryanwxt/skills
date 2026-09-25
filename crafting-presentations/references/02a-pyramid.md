# Phase 2a: Storyline as a Pyramid (Decide, Inform, Talk)

The storyline is a pyramid:
- **Governing thought**: one sentence, the answer to the brief's question.
- **Introduction**: Situation, then Complication, then the Question.
- **Key Line**: 3–5 points, each a full-sentence idea.
- **Support**: one level of points under each Key Line point, with the evidence named.

Write it as indented text in `storyline.md`. It is the spec for the deck.

## The three rules

1. **Vertical.** Each point summarises the points grouped below it. Each point raises a question (Why? How? How do you know?), and the row below answers exactly that question. Never answer a question before it has been raised.
2. **Same kind.** Every group can be labelled with one plural noun: reasons, steps, causes, risks, options.
3. **Ordered.** Every group has a nameable order, and there are only four:
   - **Time**: steps or cause→effect. The summary is the effect.
   - **Structure**: the parts of a whole, which must be mutually exclusive and collectively exhaustive (MECE).
   - **Degree**: ranked, strongest first.
   - **Argument**: deductive.

If you can't name the order, the group is wrong or the thinking isn't finished. Fix the structure before writing any words for the slides.

## Build it top-down (try first)

1. Write the **Subject**.
2. Write the reader's **Question**, taken from the brief.
3. Write the **Answer**, even as a hypothesis. This is the governing thought.
4. Write the **Situation**: a statement the audience already knows and accepts, anchored in a time and place.
5. Write the **Complication**: what changed, and why it raises the Question. It is not necessarily a problem.
6. **Recheck.** Does the Complication lead straight to the Question? If not, change one of them.
7. Ask what new question the Answer raises (usually Why? or How?). Answer it with 3–5 points and name their plural noun.
8. Repeat one level down.

## Build it bottom-up (when the answer is unclear)

1. List every point the user wants to make.
2. Sort them: problems vs solutions, causes vs effects. Draw the cause→effect arrows.
3. Group points of the same kind. More than 5 in a group means some belong together at a lower level.
4. Draw the conclusion each group implies (see "So what?" below).
5. Work back up to the governing thought and the introduction.

Judge the action points first. They are easier to test than the situation points.

## Inductive vs deductive

- **Inductive group**: parallel points of one kind, with an inference drawn from what they share. **Put this on the Key Line.** What goes on the Key Line depends on the Question:
  - "What should we do?" or "How?": **actions**, each with its evidence underneath.
  - "Should you approve / is it right?": **reasons** to say yes (see Seeking funds). The actions go in the support, or on the ask slide.
- **Deductive group**: a statement, then a comment on it, then "therefore". Keep it to 4 points or fewer. Use it on the Key Line only when the answer is surprising and the audience needs the reasoning before they'll accept it. Otherwise push deduction down to the support level.
- A "findings → conclusions → recommendations" Key Line makes the audience relive your analysis before the payoff. Rotate it 90°: recommendations on top, each backed by its own findings.
- **Cause chains dressed as lists.** "Low productivity, high overtime, high prices" is a chain, not three parallel reasons.

## "So what?": no blank summaries

"There are 4 causes", "We recommend 3 changes", "Key challenges": each of these names a category and says nothing. Replace it:
- **For actions, state the effect.** Ask: "If they do these, what do they get that they wouldn't otherwise have?" Word each action as an end product you could hold, with a measure: "Switch damaged-goods returns to carrier B in all regions by Nov 30", not "Improve returns handling."
- **For situations, state what the similarity implies.** Find what the points share, then make the inductive leap. "Two of the three churn drivers are pricing changes we chose" is an insight; "three drivers" is not.
- **Test the summary.** Could each point below be derived from it? Does it say something about *these* points and *only* these?

Carry forward the brief's evidence gaps as `[NEEDS DATA: …]`. Don't upgrade a hunch into a claim.

## Introduction patterns

| Pattern | Situation | Complication | Question → Key Line |
|---|---|---|---|
| **Seeking funds / approval** | We have problem P | Fixing it costs $N | Should you approve? The reasons are: it can't wait · this is the best fix · the cost is covered by savings or avoided loss · other benefits |
| **Choosing among options** | We must do X | We have options A, B, C (only if the audience already knows them) | Which one? Structure around the criteria ("C is fastest, cheapest, least risky"). **Never** "A is bad, B is bad, so C". |
| **Explaining how / change** | Here is the current process | It doesn't work, or we're not set up for X | How do we change it? Draw the before and after. The differences are the Key Line. |
| **Directive** | We want to do X | We need you to do Y | How do I do Y? The Key Line is steps with owners and dates. |
| **Progress review / status** | You asked us to do X, or we committed to X | We've now done it (or it slipped) | What did you find / where are we? The Key Line is findings stated as ideas. |
| **Recurring review (monthly/QBR)** | The standing metrics the audience tracks | The one or two things that moved and matter this period | What changed, and what does it mean for us? The governing thought is the period's headline. The Key Line holds the 2–4 things that matter. The full scorecard is one fixed-layout slide, same each period, placed after the Key Line or in the appendix. It is not the structure of the deck. |
| **Talk / "how we did X"** | The world the audience recognises | A tension they share | How do you solve it? The Key Line is the transferable lessons, **not** the chronology of what we did. |

The introduction **reminds; it doesn't inform**. It covers only what the audience knows or will accept, runs 1–3 slides or 2–3 short paragraphs, and has no exhibits. History and background go here, never in the body. The body holds only ideas.

Tone variants: Standard is S-C-A. Direct (answer first, for executives) is A-S-C. Concerned is C-S-A. Always *think* it from S.

## Talks: the extra steps

A conference talk's pyramid still has one governing thought. It should be a claim the audience can take home, like "Most slow queries are missing the index their access pattern needs", not "Our database journey". Build the Key Line from the **lessons**, ordered by degree (biggest win first) or by time (the order the audience should apply them). The chronology of what you did becomes the concrete example under each lesson. Engagement comes from techniques in `02b-lesson-design.md`: open with a concrete story, ask the audience to predict before you reveal, give an early usable win, state a common misconception and then refute it, and end with a "Monday morning" action.

## Output: `storyline.md`

```
Governing thought: <one sentence answering the Question>
S: <…>  C: <…>  Q: <…>
Key Line (<plural noun>, <order>, inductive|deductive):
  1. <full-sentence idea>
     - <support idea> — evidence: <source | [NEEDS DATA]>
  2. …
Anticipated objections → where they're answered: <…>
```

Run the **30-second test**: say the governing thought and the Key Line aloud. If it takes longer than 30 seconds, or doesn't hang together, restructure.

**Gate (HARD):** show the storyline and ask for approval or changes. No slide content until the user says yes.
