# Phase 4: Build

Build from the approved storyboard, one slide per row. **The storyboard is the source of truth.** If a slide won't work, change the storyboard first and tell the user. Don't let the deck drift away from the storyboard without anyone noticing.

## Format handoff

| User wants | Do |
|---|---|
| .pptx / PowerPoint / Keynote import | Load the `pptx` skill for rendering. Put speaker notes in the notes field. |
| A web page / shareable link | Build an Artifact, and load `dataviz` before drawing charts. |
| Google Slides, or unspecified | Markdown: one `## <action title>` per slide, the body underneath, and `Notes:` after it. |
| A pre-read document instead of a talk | The same pyramid, rendered as a memo. Headings are the Key Line, and the Key Line points are set out in the first paragraph. |

## Slide rules

- **The title is the storyboard's action title, word for word** (or better, with the storyboard updated to match).
- **Show, then say.** The slide shows the stark point. The speaker supplies the sentences, the transitions, and the "why". Never put the same text on screen as in the script: people waste effort cross-checking the two. The exception is when the audience needs to read along, e.g. non-native speakers or a code snippet.
- **Text slides:** about 6 lines or 30 words at most, parallel statements, simple words, rounded numbers ($4.9M, not $4,876,987).
- **Exhibits:**
  - One message per chart, and the message is the title.
  - Highlight the data point that carries the message and grey out the rest.
  - Labels sit on the thing they label, not in a legend.
  - A decorative image doesn't help anyone learn; use instructive visuals only.
- **Complex diagrams:** at most 1–2 per talk. Build them up piece by piece (animation builds or successive slides) while you narrate.
- **Pace:** something should change on screen at least every 30 seconds or so. Use builds, not walls of text.
- **Legibility:** at least about 24pt body text for rooms. The rule of 32: the farthest viewer's distance in feet ÷ 32 = the minimum letter height in inches. Dark text on a light background. Never use colour alone to carry meaning.
- **Placeholders stay visible.** `[NEEDS DATA: …]` stays in the deck until the user fills it. Never fabricate a number to make a chart look finished.

## Teach-specific

- **Live demos teach skills.** Slides say "Demo: …" plus the goal of the demo. The code itself lives in a script file for the presenter.
- **Check slides** show the MCQ with its lettered options. The options' misconception mapping goes in the speaker notes, not on the slide. Include an "I don't know" option.
- **Exercise slides** state the task, a time box, the finish signal (e.g. a green sticky note), and a stretch goal for learners who finish fast.
- **Handouts:**
  - a one-page cheat sheet with task → steps, and symptom → cause → fix;
  - the setup instructions;
  - starter code, so no learner faces a blank page.
- **Language:**
  - Don't say "just", "simply", or "obviously".
  - Don't mock learners' tools (Excel, Windows).
  - Use diverse names in examples.
  - Never imply that talent is innate.

## Speaker notes, for every slide

1. **Transition in:** link to the previous slide's *content*, not its container ("so if onboarding is where customers stall…", not "next section").
2. **The point**, in one sentence.
3. **The talking points** behind the evidence: 2–4 bullets, not a script to read aloud.
4. **Timing** mark.
5. **Teach slides also get:** the expected wrong answers, and what to do about each vote pattern.

## Deck-level extras

- **Appendix:** backup slides for the anticipated objections from the storyline, the methodology, and the full data.
- **Pre-read or handout version** (if needed): the slides alone won't stand alone, which is correct. Add a one-page memo version of the pyramid instead of cramming text onto slides.

When the build is done, go to Phase 5. Don't present the deck as finished before the review.
