# Workflows: the book as executable flows

> Cross-cutting file. It strings the per-chapter procedures into end-to-end flows and says which file and rule IDs each step uses. The procedures themselves (with all their decision points) live in the chapter files; this file sequences them.

## Router: which flow?

| The user has / wants | Flow | Entry file |
|---|---|---|
| A topic and a reader, nothing written yet | **WF1 Build top-down** | `02-building-the-pyramid.md` Procedure A |
| Notes, findings, or a brain dump with no clear point | **WF2 Build bottom-up** | `02-building-the-pyramid.md` Procedure B |
| Someone's draft (memo, report, email, proposal) to fix | **WF3 Restructure a draft** | `01` Procedure 4, `02` Procedure B (closed universe) |
| A document to critique without rewriting | **WF4 Review** | `rules-and-checks.md` |
| A problem to analyze (report or proposal not yet possible) | **WF5 Problem to pyramid** | `07-defining-the-problem.md` P1 |
| A puzzle where nobody knows the mechanism | **WF5b Structureless problem** | `09-abduction.md` P1 |
| A presentation | **WF6 Pyramid to screen** | `11-pyramid-on-screen.md` P1 |
| Sentences or paragraphs that read as fog | **WF7 Pyramid to prose** | `12-pyramid-in-prose.md` P2 |
| Just the opening of a document | **WF8 Introduction only** | `03-introductions.md`, `03b-introduction-patterns.md` |

Two invariants hold for every flow:

1. **Structure before wording.** No prose, slides, or headings are drafted until the governing thought, the introduction (S-C-Q-A), and the Key Line exist and pass their checks (PYR-1, PYR-2, BLD-1, PRO-1).
2. **Fix from the top down.** An error high in the pyramid invalidates everything beneath it, so check and repair the top point and introduction before the Key Line, and the Key Line before its support.

---

## WF1 Build top-down

Use when the subject and reader are known. Source: `02` Procedure A.

| # | Step | Output | Gate (rules) |
|---|---|---|---|
| 1 | Name the Subject | Subject noun phrase | BLD-2, BLD-3 |
| 2 | Name the reader and the Question they want settled about the Subject | One question | PYR-17 |
| 3 | Write the Answer (or note "answerable") | Top sentence = Subject + Answer | PYR-6, BLD-2 |
| 4 | Situation: first uncontroversial statement about the Subject | 1 line | BLD-4, INT-4, INT-5 |
| 5 | Complication: what changed within it ("so what?") | 1 line | BLD-5, INT-8 |
| 6 | Recheck: C raises exactly Q; A answers Q. If not, change Q or C | Confirmed S-C-Q-A | BLD-6 |
| 7 | New Question raised by the Answer (Why? How? Which?) | 1 question | BLD-7, PYR-12 |
| 8 | Choose the Key Line form: inductive unless the answer is unexpected or the actions need explaining first | Form + plural noun | BLD-20, DED-5, DED-7 |
| 9 | Key Line points: each an instance of the plural noun; together they fully answer the New Question | 2–5 points | PYR-7, PYR-8, ORD-8 |
| 10 | Order the Key Line by its source (time / structure / degree) | Ordered points | PYR-9, ORD-3, ORD-4 |
| 11 | Repeat 7–10 down each leg until the reader would have no further question | Full pyramid | PYR-12 |
| 12 | Check every grouping: same kind, MECE, ordered, summary is not blank | Validated pyramid | ORD-31, SUM-1, SUM-4, SUM-29 |
| 13 | Pick the intro pattern and write the introduction, ending with the Key Line points | Intro text | INT-1, INT-11, PAT-1, BLD-14 |
| 14 | Render: page (WF-page), screen (WF6), prose (WF7) | Document | `10`, `11`, `12` |

Short documents may stop after step 10 and write; support emerges while drafting each section, but every grouping still gets the step-12 check afterwards (BLD-8, ORD-1).

## WF2 Build bottom-up

Use when the top is unclear. Source: `02` Procedure B, then `05` and `06`.

1. **List** every point, one line each. Split into action ideas (things to do) and situation ideas (things that are so) (BLD-11, SUM-5).
2. **Actions first.** Reword each as an end product you could hold (SUM-7). For each pair ask *before* (siblings) or *so that* (child) (SUM-11). Cluster by the effect they produce (`06` P3).
3. **Situations next.** Reduce each to bare subject/predicate (SUM-21). Draw cause→effect arrows; mark missing links (BLD-12). Group the like-kind statements by shared subject, predicate, or judgment (SUM-20).
4. **Order** each cluster by its source (`05` P2).
5. **Summarize** each cluster: actions → the direct effect, stated as an end product (SUM-14); situations → the inference their similarity implies (SUM-3). Reject blank assertions (SUM-1).
6. **Conclude.** If one top point emerges, it is the candidate Answer. If several structures are possible, choose by working out the introduction for this reader (BLD-13).
7. **Hand off to WF1 from step 4**: run S-C-Q-A against the candidate Answer, then validate the Key Line top-down.

## WF3 Restructure someone else's draft

1. **Treat the draft as a closed universe**: clarify what it says, don't judge or add content (BLD-10).
2. **Strip** it to one line per point, in its current order (`01` Procedure 4).
3. **Find the buried answer.** It is usually near the end: a recommendation, a request, or a closing question.
4. **Reconstruct the introduction**: what does the reader already know (S), what changed (C), what do they need answered (Q)? If the draft is a problem-solving document, reconstruct the problem definition first (`07` P4).
5. **Run WF2 steps 2–6** on the remaining points.
6. **Relocate misplaced material**: history and background into the Situation (BLD-18); new or disputable claims out of the introduction (BLD-19); "Assumptions", "Methodology", and "Background" sections that answer questions nobody has asked yet move down to the point that raises them (PYR-13).
7. **Deliver** the restructured skeleton first (top point, intro, Key Line, support), then the rewritten text, naming the rule behind each change so the author learns it.

## WF4 Review

Run the passes in `rules-and-checks.md` in order (top point → introduction → Key Line → groupings → summaries → reasoning → presentation → prose). Report findings ranked by pyramid level, highest first, because higher-level faults cascade. Each finding names: where, the symptom, the rule ID, and the fix. Close with the corrected skeleton when the top two levels are wrong; line edits are pointless until those are fixed.

## WF5 Problem to pyramid

Use for analytical reports, proposals, and consulting-style work. Source: Part Three.

1. **Define the problem** (`07` P1): Opening Scene → Disturbing Event → R1 → R2, then any solution layers already tried. R2 must be measurable; if it isn't, the first task is to establish it (DEF-9, DEF-10).
2. **Locate the reader** (`07` P2): have they acted toward a solution? Map to one of the seven situations and take its Question (DEF-13, DEF-14).
3. **Structure the analysis before gathering data** (`08` P1): pick a diagnostic framework from the Opening Scene (physical, financial/task, activity, classification/choice/sequential), make each level MECE, turn each branch into a yes/no question, and plan the data that answers it (ANL-1, ANL-5, ANL-6, ANL-14, ANL-16).
4. **Gather and test**; prune excluded branches; if nothing confirms, recheck the framework's foundations or the problem definition (ANL-13).
5. **Generate solutions** with a logic tree rooted in the action objective; weigh payoff against risk (ANL-17).
6. **Convert to an introduction** (`07` P3): read the framework left to right and down; the last thing the reader knows is the Complication; earlier failed solutions fold into the Situation; alternatives appear only if the reader raised them (DEF-15 to DEF-17).
7. **Form the pyramid** (`08` P8): top = the answer to Q; Key Line = chosen actions (report) or analytical steps (proposal), named "changes" or "steps" as appropriate (DEF-19); support = confirmed causes and evidence. Validate each grouping against its tree (ANL-18).
8. **Never argue by eliminating alternatives**; show that the choice reaches R2 (DEF-18).

### WF5b Structureless problem

If the outcome is unexplained because the structure producing it is unknown, hidden, or contradicted, switch to scientific abduction (`09` P3): state the mismatch, list the assumptions, generate one hypothesis per structural component plus analogies, derive a necessary consequence of each, design a test with a keep/drop verdict decided in advance, iterate. Label conclusions by their certainty (ABD-2, ABD-4, ABD-9).

## WF6 Pyramid to screen

Source: `11` P1–P4. Requires a finished pyramid from WF1, WF2, or WF5.

1. Write the introduction word for word; confirm the question it raises fits this audience (SCR-20).
2. Storyboard frames for the S and C worth showing, the main point, each Key Line point, and each point one level below (SCR-21).
3. Head every frame with a statement of its point, never a caption (SCR-10, SCR-24).
4. Mark each frame text or exhibit; aim for about 90% exhibits, using text only for structure and emphasis (SCR-5).
5. For each exhibit: decide its question (elements, comparison, change, distribution, co-relation), title it with the answer, then choose the chart form (SCR-18, SCR-19).
6. Text slides: one idea, about 6 lines / 30 words, relationships laid out visually rather than as bullets (SCR-9, SCR-11, SCR-15).
7. Script the spoken words, including all transitions, which never go on slides (SCR-6, SCR-23).
8. Rehearse (SCR-25).

## WF-page Pyramid to page

Source: `10` P1–P6.

1. Choose the form by length and audience (PAG-1).
2. Choose the device: underlined Key Line points for short memos; indented display for one parallel group; hierarchical headings for reports; decimal numbering only alongside worded headings; dot-dash for progress reviews (`10` P2).
3. Map pyramid levels to formatting levels; headings state ideas, cut to essence, parallel within a group, never one of a kind, never stacked without text (PAG-4, PAG-7 to PAG-13).
4. Open every Key Line section with a mini S-C-Q story or a backward reference, then preview its supporting points (PAG-26 to PAG-30).
5. End with Next Steps if the immediate actions are self-evident; otherwise no conclusion unless it adds significance and a push to act (PAG-32, PAG-33).

## WF7 Pyramid to prose

Source: `12` P1–P3.

1. Make sure the point and its place in the pyramid are settled (PRO-1).
2. Picture the relationship the sentence must convey; sketch it as shapes and arrows if needed (PRO-4, PRO-7).
3. Write the sentence as a copy of the picture: concrete nouns as actors, the relationship as the verb (PRO-5).
4. For an opaque sentence: break it into phrases, keep the concrete nouns, draw how they relate, check that the right noun is acting, write one plain sentence, and mark any missing specifics for the author rather than inventing them (PRO-8 to PRO-10).

## WF8 Introduction only

Source: `03`, `03b`, `07` P2–P3.

1. Identify the reader and what they already know and accept.
2. Identify which of the four question families the document answers (what to do / whether to go ahead / how / why; PAT-1, catalog in `03b`), or, for problem-solving documents, which of the seven reader situations applies (DEF-14). Exactly one opening Question per document (INT-20); if it won't surface, reason backward from the body (INT-21).
3. Write S (known, uncontroversial, about the subject), C (the next development, also known; not necessarily a problem), Q (explicit or implied, but always written down privately), A (the top point). The introduction reminds; it never informs, and carries no proof or exhibits (INT-1 to INT-9, INT-22, BLD-19).
4. Choose the written order for tone (standard, direct, concerned, aggressive), never dropping an element; the thinking order always starts at the Situation (INT-10, BLD-16).
5. Long document: end with the Key Line points listed after the main point (INT-11). Short document: skip the list and make each point the underlined topic sentence of its paragraph (INT-12). Give each Key Line section its own mini S-C-Q introduction (INT-18, PAG-26). Blend background into the story; never a "Background" section (INT-14, INT-17).
6. Length: just enough for writer and reader to stand in the same place, set by the reader's needs and the subject's demands, not the document's length (INT-15, INT-16).
