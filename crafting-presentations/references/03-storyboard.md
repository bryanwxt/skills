# Phase 3: Storyboard

The storyboard turns the approved storyline into a slide-by-slide plan: one row per slide, giving its **action title**, what the slide shows, what the speaker says, and how long it takes. It is sometimes called a ghost deck. The storyboard has no finished visuals or real numbers yet.

## Mapping the storyline to slides

**Decide / Inform / Talk (pyramid):**
1. **Title slide.** Its subtitle is the governing thought or the question.
2. **Introduction** on 1–3 slides: Situation, then Complication. The Question is often spoken rather than shown. For executives, use the **Direct** order (A-S-C): the Answer + Key Line slide comes right after the title, and the introduction follows it briefly or is spoken.
3. **Answer + Key Line** on one text slide: the governing thought and its 3–5 points. This is the 30-second slide. It replaces the agenda.
4. **For each Key Line point:**
   - optionally, a divider slide stating the point, which is useful in longer decks;
   - one slide per support point, each a **sentence title over an exhibit** (chart, table, or diagram).
5. **Close:** the decision or ask (Decide), the implications and next steps (Inform), or the take-home action (Talk). The close adds perspective or calls for action. It never just repeats the deck.
6. **Appendix / backup:** detail, methodology, and anticipated Q&A.

**Teach (lesson design):** slides follow the episodes.
- **Opening** (10–30 seconds): who you are, what learners will be able to do, the prerequisites, and the code of conduct if relevant.
- **Per episode:**
  - a **model** slide (diagram or analogy);
  - **demo cue** slides that say "switch to terminal"; the code lives in the demo, not on slides;
  - a **check** slide (an MCQ, "predict the output", or the exercise brief);
  - a **debrief** slide.
- **Minute-card slides** before breaks.
- **Closing** (10–30 seconds): recap the objectives as things learners can now do, where to get help, and next steps.

## Action titles

Every title is a **full sentence with a verb** that states the slide's single point. Aim for 15 words or fewer.

**Exceptions:** a slide whose job is to ask or instruct gets a title that *is* the question or the instruction. Examples: "What happens to the source data when you refresh?" on a check slide, "Your turn: total sales by region (8 min)" on an exercise slide, "Watch: build the pivot from a raw export" on a demo slide. Every model, explanation, and evidence slide still states its point.

| Topic title (fails) | Action title (passes) |
|---|---|
| Q2 churn | Churn doubled after we dropped annual discounts |
| Root causes | Two of the three churn drivers are pricing changes we chose |
| Warehouse returns | One carrier accounts for 60% of damaged returns |
| Indexing lessons (talk) | Index for the queries you run, not the columns you have |
| Pivot tables (teach) | A pivot table summarises rows without changing the source |
| Next steps | Approve the pilot in two regions by March 1 |

Titles at the same level are **grammatically parallel**.

**Talk:** the Key Line titles are the **lessons**, written as advice the audience can use, with your team's result as the evidence. For example: "Index for the queries you run (our p95 fell from 2s to 80ms)", not "We added composite indexes". Titles that report what you did drift the talk back into chronology.

**Title test:** read the titles in order, with nothing else. A reader who sees only the titles should get the whole argument or lesson. If a title could fit on any deck ("Overview", "Next steps", "Summary"), rewrite it.

## Choosing the exhibit

First decide **what question** the chart answers. Then write the answer as the title. Then choose the form.

| The slide asks… | Form |
|---|---|
| What are the parts, or how does it work? | Structure or process diagram |
| How do the amounts compare with each other or the whole? | Bar chart (ranked), or stacked bar / waterfall |
| How has it changed over time? | Line chart or column chart |
| How are items spread out? | Histogram |
| How do two things relate? | Scatter plot |

Aim for about 90% exhibit slides and 10% text slides. Text slides are for structure (introduction, Key Line, dividers) and key groups (the recommendations, the ask). A text slide holds about 6 lines or 30 words at most, and the lines are statements, not captions.

**One idea per slide.** A slide that needs two titles is two slides.

## Timing

Most talks need about 1–2 minutes per exhibit slide, and a text slide takes about 30–60 seconds. Workshops follow the episode clock, not a slide count.

Add up the durations and compare the total with the brief's talk time, after taking out the Q&A slot. If it runs over, **cut support points, never Key Line points**, or move them to the appendix. Mark 2–3 slides as candidates to cut on the day.

## Output: `storyboard.md`

Use `assets/storyboard-template.md`. Then run the title test, and show the user **the titles in sequence** as the review surface.

**Gate:** the user approves the title sequence. Changes at this stage cost one sentence each. After Phase 4 they cost a whole slide.
