---
name: crafting-presentations
description: 'Use when asked to create, outline, restructure, or review a presentation, slide deck, talk, pitch, exec briefing, status update, decision memo presented to a group, conference talk, workshop, training session, tutorial, onboarding session, or lecture — before drafting any slide, outline, or speaker notes. Based on Minto''s "The Pyramid Principle" and Wilson''s "Teaching Tech Together".'
---

# Crafting Presentations

A presentation is built like software: intent, then design, then build, then verify. The **storyline is the spec**. Slides are the implementation. Skipping to slides is writing code before you know what it should do.

**Two ideas carry the whole skill:**
- **Arguments go top-down** (Minto). One governing thought, stated first. Everything below it answers the question the level above raised. Groups are MECE, one kind of idea each, and in a deliberate order. Every slide title is a sentence stating the slide's point.
- **Lessons go backward** (Wilson). Decide what learners will be able to *do*, write the checks that prove it, then write just enough material to get from one check to the next.

## Classify first, and say it out loud

Before your first question, name the type and scale, e.g. "This is a **Decide** presentation, full scale: I'll agree a brief, then a storyline, then a slide-by-slide storyboard before building anything." The user can override you.

| Type | The audience leaves able to… | Signals | Structure engine |
|---|---|---|---|
| **Decide** | say yes/no, approve, choose | budget, ask, recommend, pitch, proposal, choose between | Pyramid, actions on the Key Line |
| **Inform** | know what happened and what it means | status, update, findings, results, review, QBR | Pyramid (progress-review pattern) |
| **Teach** | *do* something they couldn't before | workshop, training, tutorial, onboarding, course, lab | Backward lesson design + a pyramid per explanation |
| **Talk** | carry away one idea and act on it | conference, meetup, keynote, lightning talk, "how we did X" | Pyramid for the message, teaching techniques for engagement |

When a request has two types (a "talk that teaches", a "training that needs sign-off"), pick the one that sets the success test. If it's unclear, take the heavier process (Teach > Decide > Talk > Inform).

**Scale:** a request is **quick** if any of these hold: the talk slot is 10 minutes or less, it needs 7 slides or fewer, or the user is under time pressure. Quick scale runs Phases 1–3 as **one message**: a terse brief with `[ASSUMED]` tags, the storyline, and the title sequence. That message ends with one approval question. Nothing is written to files. **Full** scale covers everything else: written artifacts and every gate.

<HARD-GATE>
Do not write slide content, bullets, speaker notes, or files in any deck format until the user has **seen** the storyline (Phase 2) and replied. Approving a topic, an agenda, or the brief does not approve the storyline.
- If the user says "just make the slides", use the quick-scale single message. One reply from them saves a rewrite.
- Any go-ahead that comes after they have seen the storyline counts as approval, including "just build it" or "whatever you think". Build it, and list your open assumptions at the top of the deck.
- The gate is **showing** the storyline before building. It is not about extracting answers to questions.
</HARD-GATE>

## Phases

Make a todo for each phase. Read each phase's reference file **when you enter that phase**, not before.

| # | Phase | Reference | Output | Gate |
|---|---|---|---|---|
| 1 | **Brief**: audience, purpose, the one question, constraints | `references/01-brief.md` | `brief.md` (template in `assets/`) | User confirms the brief |
| 2 | **Storyline**: Decide/Inform/Talk use the pyramid; Teach uses the lesson design | `references/02a-pyramid.md` or `references/02b-lesson-design.md` | `storyline.md` | **User approves the storyline (HARD GATE)** |
| 3 | **Storyboard**: one row per slide with its action title, visual, and timing | `references/03-storyboard.md` | `storyboard.md` (template in `assets/`) | User approves the titles read in sequence |
| 4 | **Build**: slide content, exhibits, speaker notes, handouts | `references/04-build.md` | the deck in the chosen format | — |
| 5 | **Review**: a fresh-eyes check against the type's checklist | `references/05-review.md` | review findings, then the fixes | Every blocking finding fixed |
| 6 | **Rehearse and deliver**: timing, Q&A prep, room and logistics | `references/06-rehearse-deliver.md` | rehearsal kit | — |

**Where artifacts go:** `presentations/YYYY-MM-DD-<slug>/` in the working directory, unless the user or project says otherwise. For quick scale, keep them in chat.

**Format handoff (Phase 4):** use whatever the user asked for. For .pptx, load the `pptx` skill. For a web page, use an Artifact (and `dataviz` for charts). Otherwise produce Markdown. The format skill decides *how* to render the deck. This skill decides *what* each slide says, and its storyboard is the source of truth.

## The tests that catch most bad decks

Run these at every phase, not just in review:

1. **Title test:** read only the slide titles, in order. They should tell the whole argument or lesson, and every one should be a full sentence with a verb. Check, exercise and demo slides are the exception: their title is the question or the instruction itself. "Q2 churn" fails; "Churn doubled after we dropped annual discounts" passes.
2. **30-second test:** could the audience state the main point and the 3–5 supporting points within 30 seconds of the opening?
3. **So-what test:** no summary is "blank", like "4 causes", "several challenges", "key learnings", or "…for three reasons". Every summary states the insight or the effect. The Key Line slide's title is the governing thought itself, never "N reasons why".
4. **Evidence test:** every title claims only what the evidence on or behind that slide shows. "8% of revenue, 30% of tickets" does not prove "costs more than it earns". Either weaken the claim or add `[NEEDS DATA]`. The numbers (dates, costs, counts) must match across every slide and the notes.
5. **Plural-noun test:** every group can be labelled with one plural noun (reasons, steps, risks), is mutually exclusive and collectively exhaustive (MECE), holds 3–5 items, and has an order you can name.
6. **Do-test (Teach):** every objective uses a measurable verb, and every 10–15 minutes there is a check where learners *do* something.

## Red Flags: stop and go back a phase

| Thought | Reality |
|---|---|
| "The user gave me the content, so I'll lay it out" | Content ≠ structure. The order they told you is the order they thought of it, not the order the audience needs. Build the pyramid. |
| "I'll follow the chronology: what we did, then what happened" | That reports activity. Lead with what you found or what you recommend, and put the history in the introduction. |
| "Topic titles are cleaner" | A topic title hides the point, so each viewer invents their own. Write the sentence. |
| "An agenda slide covers the structure" | An agenda lists topics. The Key Line states ideas. |
| "It's a workshop, so I'll write the lecture and add labs" | That's content first. Write the objectives and checks first, then the material to get between them. |
| "They're busy, I'll skip the brief" | Then the brief is a single message of labelled assumptions. It's shorter, not skipped. |
| "I'll get feedback on the finished deck" | Rewriting 20 finished slides costs more than rewriting 5 storyline sentences. Get approval at the storyline gate. |
| "Review is overkill, I checked as I went" | You can't see your own blind spots. Review uses fresh eyes (Phase 5). |

*Paraphrased from Barbara Minto, "The Pyramid Principle" (3rd ed.), and Greg Wilson, "Teaching Tech Together". The process shape follows Superpowers © Jesse Vincent (MIT).*
