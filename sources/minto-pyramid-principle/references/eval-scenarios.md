# Eval scenarios

> Cross-cutting file. Candidate scenarios for testing a skill built from this material, following the RED → GREEN → REFACTOR cycle in superpowers' writing-skills: run each scenario **without** the skill first, record what the agent actually does, and write guidance only for failures you observe. The "expected baseline failure" column is a prediction from the reference readers, not an observation; confirm it before writing guidance. Fixtures are invented for testing and are not taken from the book.

## How to read a scenario

- **Type:** application (can it apply the technique?), recognition (does it spot the fault?), counter-example (does it hold back when the technique doesn't apply?), pressure (does it hold under a competing instruction?), trigger (does the skill load?).
- **Pass criteria** are observable in the output, so a script can flag them and a human can confirm. Read every flagged run, since automated counts overstate both passes and failures.
- **Form of fix** follows writing-skills' "match the form to the failure": shape failures get a recipe or output contract, omissions get a required slot, and discipline failures get prohibitions plus a rationalization table.

## Scenarios

### S1 Buried answer (application)
- **Fixture:** a 350-word memo to a COO that walks through an inventory investigation in discovery order: what the team looked at, three findings, two causes, and finally a recommendation to consolidate two warehouses, ending "Let me know your thoughts."
- **Prompt:** "Tighten up this memo before I send it."
- **Expected baseline failure:** polishes the sentences and keeps the order; the recommendation stays last.
- **Pass:** the recommendation is the first or second sentence; the opening is a short S-C-(Q)-A; the Key Line is the recommendation's reasons or steps; findings sit under the points they support; the changes are explained with the principle behind them.
- **Rules:** PYR-3, PYR-6, DED-5, DED-8, INT-1, BLD-14. **Form:** output contract (governing thought first, skeleton before prose).

### S2 Describing instead of answering (application)
- **Fixture:** a request from a VP: "Should we fund the caching layer the platform team proposed?", plus the team's design notes.
- **Prompt:** "Draft the reply."
- **Expected baseline failure:** explains how the caching layer works and lists pros and cons; no yes/no answer up top.
- **Pass:** the top sentence answers the funding question; the Key Line gives the reasons; the design detail appears only where a reason needs it.
- **Rules:** PYR-17, BLD-3, BLD-6, PAT-5.

### S3 Category headings (recognition + application)
- **Fixture:** a 3-page report outline with sections Background / Findings / Analysis / Recommendations / Next Steps.
- **Prompt:** "Review the structure of this report."
- **Expected baseline failure:** accepts the headings; comments on content or length.
- **Pass:** flags the headings as topics rather than ideas; proposes idea headings that, read alone, summarize the argument; moves background into the introduction; checks that Next Steps holds only self-evident actions.
- **Rules:** BLD-15, INT-13, INT-14, PAG-13, PAG-33.

### S4 Flat, vague action plan (application)
- **Fixture:** notes listing 11 actions: "improve onboarding", "strengthen vendor relationships", "review pricing", "hire 2 SDRs", "launch referral program", "fix churn", "update website", "train CSMs", "build dashboard", "tackle support backlog", "revisit roadmap".
- **Prompt:** "Turn these notes into an action plan for the leadership offsite."
- **Expected baseline failure:** keeps 10+ bullets at one level, perhaps with category headers; vague verbs survive; the goal is "drive growth".
- **Pass:** at most five groups per level; each action worded as an end product someone could hold; groups formed by the effect they produce, summarized by that effect specifically; the before/so-that split separates levels; items that can't be visualized are flagged for the author.
- **Rules:** ORD-8, SUM-7, SUM-8, SUM-9, SUM-11, SUM-14.

### S5 Blank summaries and overreaching inferences (recognition)
- **Fixture:** a findings slide titled "Key findings" with five true but loosely related facts about a product launch, plus a draft summary claiming "customers fundamentally distrust our brand".
- **Prompt:** "Is this summary right?"
- **Expected baseline failure:** accepts or lightly rewords the summary; doesn't test it against the items.
- **Pass:** names the blank title; checks whether the items share a subject, predicate, or judgment; narrows the inference to what these items alone support, or says they are news with no common inference.
- **Rules:** SUM-1, SUM-20, SUM-22, DED-12, DED-13, DED-17.

### S6 Introduction that informs (application)
- **Fixture:** a draft opening paragraph that launches into new survey data and a contested claim, under a "Background" heading, for a reader who commissioned the survey.
- **Prompt:** "Rewrite the opening."
- **Expected baseline failure:** keeps the new data and the heading; makes it read more smoothly.
- **Pass:** the opening contains only what the reader already knows (they commissioned the survey); new data moves into the body; one Question is raised and answered; no "Background" heading; for a long document, the Key Line points are listed after the main point.
- **Rules:** INT-1, INT-2, INT-11, INT-14, BLD-19.

### S7 Wrong question for the reader's position (application)
- **Fixture:** a brief: the client has already chosen vendor B and asks for help rolling it out.
- **Prompt:** "Write the introduction to our proposal."
- **Expected baseline failure:** frames the question as "which vendor should you choose?" and reopens the comparison.
- **Pass:** the Question is how to implement B; the Key Line is steps; no vendor comparison in the Key Line.
- **Rules:** DEF-13, DEF-14, PAT-3, PAT-9.

### S8 Straw-man alternatives (recognition + application)
- **Fixture:** a recommendation memo structured "Option A fails because… Option B fails because… so we recommend C", where the reader never asked about A or B.
- **Prompt:** "Make this more persuasive."
- **Expected baseline failure:** strengthens the knock-downs.
- **Pass:** restructures around why C reaches the desired result (R2); drops or relegates A and B (an appendix chart if the reader insists); if R2 is undefined, defines it first.
- **Rules:** DEF-17, DEF-18, PAT-12, PAT-13.

### S9 Data-first analysis plan (application)
- **Fixture:** "Monthly churn rose from 2.1% to 3.4% over two quarters."
- **Prompt:** "Plan the analysis."
- **Expected baseline failure:** a list of data to pull and dashboards to build, then "identify drivers".
- **Pass:** problem definition first (Opening Scene, Disturbing Event if known, R1, measurable R2); a MECE diagnostic framework derived from how customers flow through the product; each branch as a yes/no question with the data that answers it; tests ordered by ease of elimination and likelihood.
- **Rules:** DEF-2, DEF-9, ANL-1, ANL-5, ANL-6, ANL-7, ANL-16.

### S10 Unverified cause (recognition)
- **Fixture:** "We raised prices 8% in March and sales fell 12% in Q2. Write up the cause for the board."
- **Expected baseline failure:** states the price rise as the cause.
- **Pass:** presents the price rise as a hypothesis; names competing structural causes; proposes a test with a keep/drop outcome decided in advance; matches certainty words to the reasoning mode.
- **Rules:** ABD-2, ABD-4, ABD-8, ABD-9.

### S11 "Key Issues" list (recognition)
- **Fixture:** a proposal section "Key Issues" with eight open-ended, overlapping questions, one off-topic.
- **Prompt:** "Review this section."
- **Pass:** recasts issues as yes/no questions; maps each to a branch of a MECE tree; drops the orphan; names the gaps; suggests presenting the analytical process instead of an issues list.
- **Rules:** ANL-18, ANL-19, ANL-21.

### S12 Deck from a report (application)
- **Fixture:** the restructured memo from S1, expanded to a 6-page report.
- **Prompt:** "Make a 10-slide deck for the exec meeting."
- **Expected baseline failure:** topic titles ("Inventory overview"), dense bullet slides, transitions on slides.
- **Pass:** an introduction written first; a storyboard covering S, C, main point, Key Line, and one level below; every title a statement; mostly exhibits, each with its question named before its chart form; transitions in the speaker script.
- **Rules:** SCR-5, SCR-10, SCR-18, SCR-20, SCR-21, SCR-6.

### S13 Ending (recognition)
- **Fixture:** a report ending "In conclusion, this report has outlined our findings and recommendations", followed by Next Steps that include "adopt a new pricing strategy".
- **Pass:** removes or replaces the restating conclusion; moves the debatable step into the body; keeps only self-evident immediate actions in Next Steps.
- **Rules:** PAG-32, PAG-33.

### S14 Opaque sentence (application)
- **Fixture:** "The area of improvement of the deployment of resources in support of the realization of objectives at the level of the regions requires attention in terms of prioritization."
- **Prompt:** "Make this clear."
- **Expected baseline failure:** swaps synonyms and shortens the sentence while keeping the abstractions.
- **Pass:** identifies the concrete actors and objects, states one relationship with a concrete subject and active verb, and flags the missing specifics (which resources, which objectives) as questions rather than inventing them.
- **Rules:** PRO-8, PRO-9, PRO-10.

### S15 Over-application (counter-example)
- **Prompts:** "Reply to Sam that 3pm Thursday works." / "Write a two-line Slack update saying the deploy finished." / "Fix the typo in paragraph 2."
- **Expected baseline failure (with the skill):** imposes S-C-Q-A scaffolding, headings, or a restructure on a one-line message.
- **Pass:** a direct, short reply; no framework vocabulary; at most a one-line note if a real structural problem is visible.
- **Form:** a conditional keyed to an observable predicate (e.g. the text is a few sentences long, or carries no conclusion or recommendation), not an exemption clause.

### S16 Competing instruction (pressure)
- **Prompt:** "Just fix the grammar in this memo, I'm sending it in five minutes. Don't restructure anything." (Fixture: the S1 memo.)
- **Decision for the skill author:** the book gives no guidance here. A reasonable target: obey the instruction, fix the grammar, and add one sentence noting that the recommendation is buried at the end, offering to move it up.
- **Pass (if that target is chosen):** grammar fixed, structure untouched, a single-sentence offer, and no lecture.

## Trigger tests

| Should load | Should not load |
|---|---|
| "Restructure this memo, it rambles" | "Fix the typo in line 3" |
| "Write an exec summary of these findings" | "Write a poem about autumn" |
| "My report isn't landing with the VP, can you help?" | "Translate this paragraph into Spanish" |
| "Build an issue tree for why churn rose" | "What time zone is Singapore in?" |
| "Help me write a proposal to a new client" | "Reply 'sounds good' to Sam" |
| "Turn these notes into a recommendation" | "Write unit tests for this function" |
| "Storyline for my board deck" (if the skill covers decks; otherwise the deck skill) | "Summarize this article for me" (borderline; decide and test) |
| "Review the structure of this design doc" | "Rename these variables" |
