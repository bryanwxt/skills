# Skill blueprint

> How to turn `references/` into one or more Claude skills. This file holds design recommendations, not book content. Where it says what the book holds, it points to the reference file.

## 1. What the material supports

The book has three separable competencies. Each can be its own skill, or two can share one skill with a router.

| Candidate skill | Covers | Flows (`workflows.md`) | Reference files it needs |
|---|---|---|---|
| **A. Structuring documents**: write, restructure, or review memos, reports, emails, proposals, executive summaries, design docs | Parts One, Two, Four (page and prose) | WF1–WF4, WF7, WF8, WF-page | `01`–`06`, `10`, `12`, `rules-and-checks`, `diagnostics` |
| **B. Structuring problems**: define a business or technical problem, plan the analysis, build issue and hypothesis trees, write the proposal | Part Three, Appendix A, problem-related patterns in `03b` | WF5, WF5b, then WF8 for the write-up | `07`, `08`, `09`, `03b` (seven situations, proposals) |
| **C. Presentations** | Ch. 11, plus the pyramid and introductions | WF6 | `11`, `03`, `10` |

C already exists in this repo as `crafting-presentations`, which carries compressed paraphrases of this book. Its predecessor, `pyramid-deck`, was removed in `ac2d376`. Use this set to **audit** `crafting-presentations` rather than build another deck skill (see §7).

A and B have different triggers and almost no overlapping procedure, so keeping them as two skills makes discovery cleaner. If you want one skill, route on whether the analysis is already done: if it is, the job is writing (A); if it isn't, the job is problem solving (B).

## 2. Recommended shape for skill A

```
structuring-documents/
├── SKILL.md                      # < 500 words: core principle, router, output contract, quick reference, loading table
└── references/
    ├── pyramid-and-build.md      # condensed from 01 + 02 + 04 (~2.5k words)
    ├── introductions.md          # condensed from 03 + the pattern catalog at the top of 03b (~2.5k)
    ├── grouping-and-summaries.md # condensed from 05 + 06 (~2.5k)
    ├── page-and-prose.md         # condensed from 10 + 12 (~2k)
    ├── review-checklist.md       # Part 2 of rules-and-checks.md (~1.2k)
    └── diagnostics.md            # as is (~2k)
```

**Why condense.** The full reference set is about 134k words (roughly 175k tokens). Even one chapter file runs 4–16k words, which is too heavy to load mid-task. Keep this directory as the source of truth, and keep rule IDs in the condensed files (e.g. "(SUM-7)") so every condensed statement can be traced back and re-checked.

**SKILL.md outline**
1. *Overview:* structure before wording; a pyramid under one governing thought, delivered top-down.
2. *When to use / when not to:* key the exclusion to an observable predicate, such as "the text is a few sentences long" or "carries no conclusion, recommendation, or request" (eval S15).
3. *Router:* the table at the top of `workflows.md`, cut to A's flows.
4. *Output contract* (the recipe form; see §4): for build and restructure jobs, deliver in this order:
   1. the governing thought (one sentence);
   2. S-C-Q-A;
   3. the Key Line with its plural noun;
   4. the support skeleton;
   5. only then the prose, with the rule behind each structural change named in passing.
   For reviews, deliver findings ranked by pyramid level, each with a rule ID and fix, then the corrected skeleton.
5. *Quick reference:* Part 1 of `rules-and-checks.md`.
6. *Loading table:* §3 below.
7. *Common mistakes:* drawn from the baseline runs, not written in advance.

**Description (trigger-only, per writing-skills SDO), a draft to test:**
> Use when drafting, restructuring, or reviewing a memo, report, email, proposal, executive summary, or design doc meant to convey a conclusion or recommendation, or when a draft is described as unclear, rambling, too long, or burying the point.

**Skill B description draft:**
> Use when scoping or planning an analysis of a business or technical problem, building an issue tree, hypothesis tree, or driver tree, deciding what data to gather, or writing a consulting-style proposal or problem statement.

## 3. Loading map (phase → files)

| Phase | Load | Not needed |
|---|---|---|
| Finding the governing thought and Key Line | `01`, `02` (Procedures A–C), `04` (Procedure D) | `10`–`12` |
| Writing the introduction | `03`; the catalog and decision table at the top of `03b`; one pattern card | the rest of `03b` |
| Checking groupings and summaries | `05` (P1, P2), `06` (P1–P4) | `07`–`09` |
| Problem definition | `07` (P1–P3) | `10`–`12` |
| Analysis plan | `08` (P1, the matching framework procedure, P8) | `03`, `10` |
| Unknown mechanism | `09` | — |
| Formatting the page | `10` (P1–P5) | `07`–`09` |
| Slides | `11` | `07`–`09` |
| Sentence clarity | `12` | everything else |
| Review | `rules-and-checks.md` Part 2, `diagnostics.md` | chapter files unless a finding needs detail |

## 4. Guidance form per expected failure

Following writing-skills' "match the form to the failure". These are hypotheses until the baseline runs in `eval-scenarios.md` confirm the failures.

| Expected failure | Type | Form that should bind | Scenario |
|---|---|---|---|
| Answer buried; analysis order kept | Wrong shape | Output contract: governing thought first, skeleton before prose | S1, S2 |
| Category headings, blank summaries | Omitted element | Required slot: every heading and summary is a full-sentence claim; the template has no "Background" or "Findings" slot | S3, S5 |
| Vague, flat action lists | Omitted element | Template slot per action: end product (+ owner if known); at most five per level | S4 |
| Inventing missing specifics | Wrong shape | Required placeholder slot: `[? which resources]` plus a question to the author | S14 |
| Framework imposed on trivial messages | Conditional | Observable predicate (length; no conclusion or request) | S15 |
| Skipping structure under time pressure | Discipline | Prohibition plus rationalization table, only if baseline runs show it | S16 |
| Straw-man alternatives, wrong reader question | Wrong shape | Recipe step: "locate the reader's position (DEF-13) before writing Q" | S7, S8 |

## 5. Elicitation: what to ask, with defaults

The book's load-bearing unknowns, in dependency order. Ask one at a time, each with a recommended answer and the reason for it (the questioning style the removed `pyramid-deck` used, and superpowers' brainstorming uses). Don't ask what the material already settles.

| # | Question | Why it's load-bearing | Default if the user says "just go" |
|---|---|---|---|
| 1 | Who is the reader, and what do they already know about this? | Everything in the introduction must be known to them (INT-2) | The person the user names, assumed to know the background but not the analysis |
| 2 | What question do they need answered? | The top point must answer it (PYR-17); only one question per document (INT-20) | Inferred from the request; stated back for confirmation |
| 3 | Have they already acted toward a solution? | Sets which of the seven situations applies, and so the Question (DEF-13, DEF-14) | No action taken yet (Case 1) |
| 4 | What result do they want, in measurable terms? | Options are judged against R2 (PAT-12, DEF-9) | Ask; if unknown, make "define R2" the first step |
| 5 | Did they raise alternatives themselves? | Alternatives appear only if they did (DEF-17, PAT-9) | No: argue for the recommendation directly |
| 6 | Form and length (memo, report, deck; read alone or discussed)? | Chooses the page device (PAG-1, `10` P2) | Memo with underlined Key Line points if short; headings if long |
| 7 | Tone (standard, direct, concerned, aggressive)? | Sets the written order of S-C-Q-A (INT-10) | Standard; direct for senior readers who asked a direct question |

## 6. Decisions the book leaves open

The readers found these tensions inside the book. A skill must pick one reading and state it, or agents will oscillate between them.

| # | Tension | Where | Recommendation |
|---|---|---|---|
| 1 | Group size: about seven (Ch. 1, memory limit) vs four or five (Ch. 1 regrouping advice, Ch. 6) vs at most five inductive and four deductive (Ch. 10) | `01`, `05`, `10` | 2–5 per grouping; flag 6+ |
| 2 | "Two relationships" (deductive/inductive) vs "four orders" | `01`, `04`, `05` | Every grouping is deductive or inductive; inductive groupings take time, structural, or degree order. Already reconciled in `01` and `05` |
| 3 | Rule numbering shifts between chapters ("the second rule" vs rule 3) | `05` nuances | Cite rule IDs, never ordinal rule numbers |
| 4 | The story has three elements (S, C, Solution; p. 48) vs four (S, C, Q, A) | `03` | Use S-C-Q-A; Q may be implicit but is always written down privately (INT-22) |
| 5 | The four standard questions are listed differently in three places ("why not?" vs "why did it happen?") | `03`, `03b` reconciliation table | Use the `03b` reconciled list |
| 6 | Ch. 7 warns against wording action steps as questions, yet one rewrite frames its top point as "whether we can…" | `06` (Skill note) | Steps are never questions; a proposal's top point may frame a yes/no decision |
| 7 | Analytical issues must be yes/no, but introduction Questions are often open "how?" questions | `08`, `03` | Apply yes/no only to analytical issues; never force an introduction's Question into yes/no |
| 8 | Avoid deduction at the Key Line, but the Hertz example and Case 6 (strategy) use it | `04`, `07` | Allow a deductive Key Line only under DED-7's two conditions; at most four points |
| 9 | "Alternatives always go in the Complication", yet Exhibit 36 places one at the end of the Situation | `07` nuances | Follow the rule (DEF-17); treat the exhibit as loose |
| 10 | Introductions "remind, not inform", but directives and wide-audience pieces plant the question, and Appendix B lets an uninformed reader "see" a possible problem | `03`, `03b` | Remind by default; plant only for directives, wide audiences, and readers unaware of the problem, and still assert nothing contestable |
| 11 | Relaxed precision: Ch. 7 allows a looser summary when the reasoning is known to be valid | `06` | Allow it in reviews only for low-level groupings; never at the top or the Key Line |
| 12 | "Never only one heading" is relaxed for dot-dash outlines | `10` | Keep the strict rule except for dot-dash progress reviews |
| 13 | The book's own heading-marker and numbering examples are inconsistent | `10` uncertain readings | Pick one house style (e.g. 1 → 1.1 → a → dash) and state it |
| 14 | Exhibit 19 is captioned "problem analysis is always deductive", but the text credits induction and abduction | `04` | The *presentation* of analysis (wrong → cause → fix) is deductive; the reasoning mixes all three |

**Dated material to modernize** (none of it changes a principle):
- Overhead-projector slide guidance, and the Rule of 32 (feet/inches) for projected text; screen-shared and read-ahead decks need their own legibility rule.
- Underlining for emphasis, which is bold today.
- The 1990s consulting setting, where "client" can usually be read as "stakeholder" or "decision maker".

## 7. Relationship to the existing skills in this repo

- **`crafting-presentations`** (`references/01-brief.md`, `02a-pyramid.md`, `03-storyboard.md`, `05-review.md`) paraphrases the book's core in compressed form: the pyramid rules, building top-down and bottom-up, deduction vs induction, blank summaries, introduction patterns, and storyboarding. The removed `pyramid-deck` covered the same ground; its references are in git history before `ac2d376`. To audit `crafting-presentations`, run a few of the deck-relevant rules against its text: one question per deck (INT-20); alternatives only if the audience raised them (DEF-17, DEF-18); end-product wording for action points (SUM-7); question before chart form (SCR-18); no restating conclusion (PAG-32); text slides as relationship diagrams (SCR-15).
- **The superpowers lenses** (`software-design`, `clean-python`, `data-intensive`) suggest another option: a writing lens that applies skill A's output contract to the documents superpowers already produces (brainstorming's spec, the plan, PR descriptions), built around stock superpowers like the others. Superpowers prescribes those documents' headings, so such a lens would govern the order and wording inside them (governing thought first, idea headings, no blank summaries) rather than replace them.

## 8. Provenance and licensing

- Everything in `references/` is paraphrased, with page citations. A checker compared every file with the book's text layer, and no run of ten or more words matches, apart from chapter and subsection titles. Book examples are reduced to their structure or replaced with invented examples of the same shape; invented examples are marked as Skill notes.
- *The Minto Pyramid Principle* is copyrighted. Whether to commit or publish these notes in a public repo is your call. If you publish skills built from them, ship the condensed references, as the existing skills do, not this full set.
