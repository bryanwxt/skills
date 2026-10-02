# Diagnostics: symptom → problem → fix

> Cross-cutting file. A quick index of the most common faults, arranged by where they show up in a document. Each chapter file has a fuller Diagnostics table (about 200 rows in total) for the long tail. Rule IDs point into the chapter files; `rules-and-checks.md` lists them all.

**Fix order:** repair the highest-level fault first. Rewording a section is wasted effort if the top point, the introduction, or the Key Line above it is wrong (PYR-10).

## The top of the document

| Symptom | Problem | Fix |
|---|---|---|
| The main point arrives in the last paragraph, or as a closing question ("Does that work for you?") | Ideas delivered in the order the writer discovered them | Put the summary first (PYR-3, PYR-6); `01` Procedure 4 |
| After the first paragraph the reader can't say what the document is about | No single governing thought, or it isn't stated first | PYR-6, BLD-2 |
| The opening is a topic label ("Re: the customer request", "This memo discusses…") | The top box has a Subject but no Answer | BLD-2, BLD-3 |
| The draft explains how something works when the reader asked whether to do it | The writer never identified the reader's Question | `02` Procedure A; BLD-3, BLD-6 |
| The top point doesn't answer the question the introduction raised | Introduction and pyramid built separately | BLD-6, DEF-21 |
| The writer has polished the prose for hours and reviewers still call it unclear | A structure problem treated as a style problem | PYR-1; rebuild with WF1 or WF2 |

## The introduction

| Symptom | Problem | Fix |
|---|---|---|
| "The purpose of this memo is to…" followed by a list of topics | No story; the reader's question is never identified | Rebuild as S-C-Q-A (INT-1, PYR-18) |
| The introduction asserts things the reader would dispute or has never heard | It informs instead of reminding | Move the claims into the body (INT-2, BLD-19) |
| A "Background" or "History" section in the body narrates events | Chronology placed in the pyramid | Fold the history into the Situation, or recast it as cause and effect (BLD-18, INT-14, INT-17) |
| The Situation is long and data-heavy | Opening Scene not kept to a sketch the reader can picture | DEF-4, DEF-5 |
| Each failed earlier attempt is presented as its own Complication | Layered history not folded into the Situation | DEF-15, DEF-16 |
| The intro asks "What should we do?" but the reader has already chosen a fix | Reader's position relative to a solution not established | DEF-13, DEF-14 |
| Options appear that the reader never raised, then get knocked down | Straw-man alternatives | DEF-17, DEF-18 |
| The introduction never previews the main points; the thinking emerges pages later | Key Line missing from the introduction | INT-11, BLD-14, PAG-3 |
| The introduction already contains causes or recommendations | Analysis material placed in the introduction | DEF-20 |
| Two questions open the document ("whether and how") | More than one opening Question | Fold one into the other (INT-20) |
| The introduction runs a page for a reader who already knows the story | Length set by document size, not reader need | INT-15, INT-16 |
| A funding request justified by "other benefits" | Extras used as the reason to act | PAT-6 |
| A progress review that lists problems with no proposed fixes | Problems without solutions | PAT-19 |

## The Key Line

| Symptom | Problem | Fix |
|---|---|---|
| Sections run Situation → Problems → Causes → Recommendations; the actions come last | Deductive Key Line; the reader relives the analysis | Rotate the worksheet so recommendations form the Key Line (DED-5, DED-8; `04` Procedure E) |
| Top-level sections titled "Findings", "Conclusions", "Recommendations" | Worksheet columns presented one at a time | DED-8, BLD-15 |
| Key Line reads premise → premise → "therefore" (restating the top) | Overstructured deduction | BLD-20, BLD-21; `02` Procedure E |
| "A fails, B fails, therefore C" | Choice justified by elimination | DEF-18 |
| Key Line points don't, together, answer the question the top point raises | Vertical Q/A broken | PYR-12, BLD-7 |
| Key Line noun mismatched ("steps" for fixing an existing system, "changes" for a new capability) | Noun doesn't fit the reader's situation | DEF-19 |

## Groupings

| Symptom | Problem | Fix |
|---|---|---|
| 8–12 bullets at one level | Beyond working memory; hidden subgroups | Regroup at 4–5 per level (PYR-5, ORD-8, ORD-29) |
| A list mixing reasons, steps, and problems | Not the same kind of idea | Plural-noun test; move misfits (PYR-8, DED-11) |
| Items could be shuffled with no loss | No order; the source of the grouping is unidentified | Impose time, structural, or degree order (ORD-3, ORD-4) |
| Some "steps" produce the outputs of others | Cause and effect at one level | Before = sibling, so that = child (ORD-9, SUM-11) |
| A step list turns into outcomes partway through | Actions mixed with results | ORD-11, ORD-12 |
| One item is plainly the consequence of the others | Effect sitting among its causes | Promote it (ORD-14) |
| One item covers all the others ("assess each area") | Different level of abstraction | ORD-21 |
| Parts overlap, or an obvious part has no home | Not MECE | ORD-15, ORD-17, ANL-5 |
| The first item of a ranked list isn't the strongest | Degree order inverted; unintended priority | ORD-25, ORD-26 |
| Three "indicators" that are successive effects of one cause | Deduction disguised as induction | DED-14 |
| True facts whose varying parts share nothing | News, not thinking | DED-17; `04` Procedure F |
| "Assumptions", "Methodology", or "Background" sections ahead of the main points | Questions answered before anyone asked them | PYR-13 |

## Summaries (the point above each grouping)

| Symptom | Problem | Fix |
|---|---|---|
| "There are three issues:", "Our findings are as follows:", "Key considerations" | Intellectually blank assertion | SUM-1; `06` P1 |
| Goal like "improve profits" over a list of actions | Effect too vague to judge sufficiency | SUM-8, SUM-15 |
| Steps like "strengthen effectiveness", "review processes", "address issues" | No end product; nobody could tell when it's done | SUM-7, SUM-9 |
| A workplan written as a list of questions | Questions substituted for end-product steps | SUM-10 |
| Columns of Tasks / Objectives / Benefits that repeat each other | Actions classified instead of structured | SUM-12, SUM-13 |
| The summary claims "will achieve" where the steps only enable | Overclaimed effect | SUM-14, SUM-15 |
| The parent asserts a cause or motive the items don't show | Inference exceeds the grouping | DED-12, DED-13 |
| The parent is so general any facts would fit ("represents an opportunity") | Summary pitched too high | DED-13 |
| Mixed positive and negative findings with an "overall, a mixed picture" hedge | Inductive leap not made, or the deductive "therefore" unfinished | SUM-25, SUM-26 |
| Polished, framework-sounding lists of "principles" or "characteristics" | Language masking the absence of a message | SUM-21, SUM-22 |

## Reasoning

| Symptom | Problem | Fix |
|---|---|---|
| A deductive chain of five or six steps with several "therefores" | Too long to summarize | At most four points and two "therefores" (DED-10) |
| The reader must hold a point from section 1 to understand section 4 | Deduction spread across sections | Push deduction down to paragraph level (DED-9) |
| A "therefore" drawn from two parallel facts | An inductive pair mistaken for deduction | DED-15 |
| A plausible cause reported as fact ("sales fell, so we're overpriced") | Abductive "possibly" treated as proven | ABD-4 |
| A test plan reads "change X and see what happens" | No keep/drop outcome defined in advance | ABD-9, ABD-8 |

## Problem-solving documents

| Symptom | Problem | Fix |
|---|---|---|
| The team is gathering "everything" before anyone can state the problem | Data-first analysis | Define the problem, then build a framework (DEF-1, ANL-1, ANL-15) |
| Recommendations can't be ranked; success is undefined | Vague R2 | Make R2 measurable (DEF-9, DEF-10) |
| A "Key Issues" section of open-ended, mixed questions | Issues list substituted for the analytical process | Yes/no issues mapped to a tree (ANL-18, ANL-19, ANL-21) |
| Hypotheses restate the client's goal or appear from nowhere | Causes not derived from the Opening Scene | ANL-2, ANL-14 |
| A decision tree or PERT chart offered as the analysis of why the problem exists | Planning chart confused with a diagnostic framework | ANL-3 |
| Fixes aimed downstream (repurchase) while upstream stages (targeting, awareness) are broken | Process order ignored | ANL-12 |

## On the page

| Symptom | Problem | Fix |
|---|---|---|
| TOC reads Introduction / Background / Findings / Conclusions / Recommendations | Headings name topics, not ideas | Idea headings; the TOC should summarize the argument (PAG-13, BLD-15) |
| A section with exactly one subsection | Heading added for looks | Merge or find the missing sibling (PAG-7) |
| Sibling headings in mixed grammatical forms | Ideas not recognized as the same kind | PAG-8 |
| Body text opens "This will…" referring back to the heading | Text depends on its heading | PAG-10 |
| A heading followed immediately by a subheading | Group not introduced | Add a point-plus-preview introduction (PAG-11, PAG-14) |
| "This chapter looked at A; the next looks at B" | Transition says what sections do, not what they say | PAG-27, PAG-29 |
| Ending: "This report has outlined our recommendations…" | Restatement conclusion | Delete, or give significance and a call to act (PAG-32) |
| Next Steps contain debatable actions | Argument smuggled outside the pyramid | Move to the body (PAG-33) |

## On screen

| Symptom | Problem | Fix |
|---|---|---|
| Slide titles are topics ("Q3 margins") | Captions, not statements | SCR-10, SCR-19 |
| Seven long bullets under a heading | List with no insight; visual recitation | SCR-2, SCR-9, SCR-11 |
| Presenter reads the slides, or says something different from them | Slides carry the script | SCR-3, SCR-6 |
| Mostly text slides | Exhibit/text balance inverted | About 90% exhibits (SCR-5) |
| Chart form chosen before its question (pie for change over time) | Form before message | SCR-18 |
| Slides built before the introduction is settled | No storyboard discipline | SCR-20, SCR-21 |

## In the prose

| Symptom | Problem | Fix |
|---|---|---|
| Five or more chained prepositional phrases in one sentence | No image; the reader loses the thread | Find the concrete nouns (PRO-8, PRO-11) |
| Abstract nouns everywhere, no concrete actor | Writer hasn't pictured who does what | PRO-4, PRO-8 |
| The sentence credits or blames the wrong thing | Misattribution hides the relationship | PRO-9 |
| A rewrite needs a specific the draft never gives | Writer's thinking incomplete | Placeholder plus a question to the author (PRO-10) |
