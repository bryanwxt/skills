# Skill blueprint

> How to turn `references/` into one or more Claude skills. This file holds design recommendations, not book content; where it describes the book, it points to the reference file.

## 1. What the material supports

The book has four separable jobs. Each could be its own skill, or two can share a skill behind a router.

| Candidate skill | Covers | Flows (`workflows.md`) | Reference files it needs |
|---|---|---|---|
| **A. Designing lessons and exercises**: lessons, courses, workshops, tutorials, quizzes, exercises, auto-graders | Ch 2–7, 10 (design side), 12 | WF1, WF2, WF3, WF-PCK, WF8 | `02`–`07`, `10`, `12`, `rules-and-checks` A and C |
| **B. Delivering teaching**: preparing and running sessions, live coding, co-teaching, feedback on teaching, online and hybrid delivery | Ch 8, 9, 11 | WF4, WF5, WF6 | `08`, `09`, `11`, `rules-and-checks` B and D |
| **C. Supporting learners**: study strategies, time management, peer assessment | Ch 5 | WF7 | `05` |
| **D. Running a teaching organization**: community, volunteers, meetings, marketing, partnerships | Ch 13–15, appendices C and F | WF9, WF10 | `13`, `14`, `15` |

**Relationship to existing skills in this repo:**

- **`crafting-presentations`** (on `main`) already draws on this book for its Teach track. `references/02b-lesson-design.md` encodes the backward-design steps: personas, scope, concept map, objectives, summative and formative checks, episodes, and an overview written last.
  - Use this set to audit it against WF1 and Part 2A of `rules-and-checks.md`. Check specifically: Bloom's first four levels for intro material (LES-14), diagnostic distractors (MOD-8), worked and faded examples (COG-5, COG-6), and quick useful wins first (MOT-6).
  - Its rehearse/deliver phase can also be checked against `08`: live coding (PRF-16 to PRF-29) and record-and-review (PRF-13).
- **`teaching-tech`** was a standalone Wilson skill, removed from `main` in `ac2d376`. It is still in git history, with references for learning science, lesson design, delivery, exercises, inclusion, online, PCK, community, and a question bank, plus template assets.
  - If you rebuild a teaching skill, start from that skill's shape and refresh its references from this set. Its assets map onto templates here: event checklists, rubrics, pre-assessment, lesson-design template, MCQ item, persona, and code of conduct.

**Recommendation:** fold A into `crafting-presentations`' Teach track rather than adding a new skill, since the triggers overlap ("workshop", "training", "tutorial"). Add D as a separate skill only if you actually need organizer support; its triggers ("volunteers", "coding club", "partnerships", "cold email") don't overlap with A or B. Fold B's live-coding and feedback material into the deck skill's deliver phase. C fits best as a reference that A loads, not as a skill of its own.

## 2. Recommended shape (if built as a standalone teaching skill)

```
designing-tech-lessons/
├── SKILL.md                   # < 500 words: core principle, router, output contract, quick reference, loading table
└── references/
    ├── learning-science.md    # condensed from 02 + 03 + 04 + 05 (~3k words)
    ├── lesson-design.md       # condensed from 06 with the T1 template (~2k)
    ├── programming-pck.md     # condensed from 07 with its T1–T7 cards (~2k)
    ├── exercises.md           # the 12 catalog + per-type templates (~2.5k)
    ├── motivation-inclusion.md# condensed from 10 with its checklists (~2k)
    ├── delivery.md            # condensed from 08 + 09 with checklists and rubric (~3k)
    ├── online.md              # condensed from 11 (~1.5k)
    └── review-checklists.md   # Part 2 of rules-and-checks.md
```

The full set is about 130k words and the chapter files run 4.5–12k words each, too heavy to load mid-task. Keep this directory as the source of truth and keep rule IDs in the condensed text, so every statement traces back.

**Output contract for a design job** (a recipe form; see §4). Deliver in this order:
1. Personas
2. Objectives
3. Summative exercise
4. Outline of episodes, each ending in a formative check
5. Content only after that

**Output contract for a review:** findings ranked by impact, each with a rule ID and a fix, then a revised outline.

**Draft description for skill A (trigger-only):**
> Use when designing, planning, or reviewing a lesson, course, workshop, tutorial, or training for learners of a technical skill, or when writing exercises, quizzes, or assessments for one.

**Draft description for skill D:**
> Use when starting, growing, or running a volunteer teaching group, coding club, or community of practice: recruiting or retaining volunteers, governance, meetings, marketing, cold outreach, or partnering with schools or companies.

## 3. Loading map

| Phase | Load | Not needed |
|---|---|---|
| Who and why | `01` P1, `06` P3 | `13`–`15` |
| Objectives and outline | `06` P1–P2, `03` P1 (concept map) | `08`, `11` |
| Formative checks / MCQs | `02` P1–P3 | `13`–`15` |
| Explanations and examples | `04` P1–P3, `05` P3 (ADEPT), `03` P4 (blind spot) | `13`–`15` |
| Programming content | `07` P1–P4, T1–T7 | `13`–`15` |
| Exercises | `12` catalog, P1–P3 | `08`, `13`–`15` |
| Motivation / inclusion pass | `10` P1–P5, T1–T4 | `07` |
| Session prep and delivery | `09` P1–P9 and checklists, `08` P4 | `06`, `13`–`15` |
| Feedback on teaching | `08` P1–P3, P5, rubric | `07`, `12` |
| Online | `11` | `09` checklists |
| Community / outreach | `13`, `14`, `15` | `02`–`07`, `12` |
| Review | `rules-and-checks.md` Part 2, `diagnostics.md` | chapter files unless a finding needs detail |

## 4. Guidance form per expected failure

These are hypotheses until the baseline runs in `eval-scenarios.md` confirm them.

| Expected failure | Type | Form that should bind | Scenario |
|---|---|---|---|
| Writes content first, adds exercises last | Wrong shape | Output contract: personas → objectives → summative → outline of checks → content | S1 |
| Vague objectives, MCQs with no rationale for distractors | Omitted element | Required slots: verb + performance + condition per objective; a "misconception this detects" column per distractor | S2, S3 |
| Blank-page novice exercises | Omitted element | Template slot per exercise: type (from the catalog) + scaffold | S4 |
| "Just…", skipped steps | Wrong shape | Recipe step: blind-spot sweep before output | S5 |
| Accepts debunked premises (VAK) | Premise | Conditional: if the request rests on a debunked claim, say so in one line and offer the evidence-based alternative | S6 |
| Overloads a workshop with new techniques | Discipline | Explicit cap (CLS-41) + rationalization table, only if baseline runs show the failure | S11 |
| Lesson plan when the user wanted an answer | Conditional | Observable predicate: the user is designing, delivering, or evaluating teaching | S18 |

## 5. Elicitation: what to ask, with defaults

Ask one question at a time, each with a recommended answer, and only when the answer would change the design.

| # | Question | Why it's load-bearing | Default |
|---|---|---|---|
| 1 | Who are the learners: background, prior knowledge, what they want, constraints? | Everything is designed for them (LES-3, LES-5) | Write two personas from the request and confirm them |
| 2 | What should they be able to *do* afterwards? | Backward design starts here (LES-1) | Infer one summative task and confirm it |
| 3 | Setting: one-off workshop or course; length; in person, online, or hybrid; class size; helpers? | Sets the episode count, innovation budget, and online rules (LES-8, CLS-41, ONL-30) | One-day in-person workshop with helpers |
| 4 | Their tools and environment? | Setup pain is a top demotivator (MOT-11, CLS-29) | Learners' own laptops, all three operating systems |
| 5 | Are novices, mixed, or practitioners expected? | Tutorial vs manual; expertise reversal (MOD-1) | Novices |
| 6 | Any accessibility needs known? | Baseline accommodations come regardless (MOT-18) | Baseline accommodations only |

## 6. Decisions the book leaves open

The readers found these tensions. A skill must choose a stance and state it.

| # | Tension | Where | Recommendation |
|---|---|---|---|
| 1 | Working memory is 7±2 [Mill1956] or 4±1 [Dida2016]; the two-store model is "useful but superseded" | `03` | Design for small chunks (about 4–5 new items) and cite neither number as exact |
| 2 | Check every 10–15 minutes, but explicitly *not* because of attention span [Wils2007] | `02` | Keep the cadence; never justify it by attention span |
| 3 | Strong guidance for novices (Ch 4, [Kirs2006]) vs productive failure (Ch 10) and the softened anti-inquiry stance ([Kaly2015], [Kirs2018]) | `04`, `10` | Guidance first for novices; productive failure only as a deliberate, scaffolded exception (COG-21, MOT-13) |
| 4 | Scripted Direct Instruction shows a significant effect [Stoc2018], but Wilson prefers improvisation on cost grounds | `08` | Report both; let the user's context decide |
| 5 | Two-stage exams helped homogeneous groups, not heterogeneous ones [Cao2017b], vs mixed-ability pairing elsewhere | `05`, `09` | Use homogeneous groups for two-stage exams; pairing advice stands for exercises |
| 6 | Learner satisfaction doesn't measure learning, yet adoption by faculty is driven by student feedback [Bark2015] | `07`, `09`, `15` | Measure learning for evaluation; use satisfaction only as an adoption lever |
| 7 | Shared notes on laptops are recommended, though handwriting beats laptop notes [Muel2014], and limiting innovation takes precedence in one-off sessions | `09` | Shared notes for multi-session courses; skip them in first-time one-day workshops |
| 8 | "Never a blank page", but starter code can add extraneous load | `09`, `04` | Starter code without boilerplate |
| 9 | Parsons distractors: harder but no better [Harm2016] vs equal to code-writing [Eric2017] | `12`, `04` | No distractors for novices; treat them as a cost elsewhere |
| 10 | Stereotype threat and growth mindset are hedged as weakly supported | `10` | Use the practices, but don't oversell the theory (MOT-16) |
| 11 | The Presentation Rubric marks a strong accent as Iffy/No, which sits uneasily with the inclusivity chapter | `08` | Drop or reword the accent item ("Was speech intelligible to this audience?") |
| 12 | Bloom's level names: 1956 (glossary) vs 2001 revision (Ch 6) | `06` | Use the 2001 names |
| 13 | Checklists: the evidence is "more nuanced" [Urba2014], but Wilson's group uses them | `09` | Use them as memory aids, not as proof of quality |
| 14 | New-to-CS teachers seemed as effective [Hu2017] vs the emphasis on PCK | `15`, `07` | PCK helps; it isn't a precondition for teaching |

**Source quirks to know about:**
- The EPUB has a systematic word swap: "exercise" was printed where "challenge" or "problem" is meant, e.g. "hearing exercises". The files flag each instance.
- Some citation keys are mistyped in the book itself (`Rich3017`, `Spoh2985`, `Koeh3013`, `Kuch3011`, `Nath3003`). They are kept as printed because they match the bibliography.
- There are a few garbled sentences and wrong section pointers; each file's *Evidence and caveats* or *Source map* records them.

**Dated material to modernize** (none of it changes a principle):
- 2018 tools: Etherpad, IRC, and early-MOOC platforms.
- The "jobs of the future" framing.
- Online-meeting tooling.
- The evidence base itself, which ends in 2018, so newer research isn't reflected.

## 7. Licensing

The book is CC BY 4.0, so this set may be published, provided:
- attribution is kept (each file opens with it);
- the license is linked;
- changes are indicated (each file says it is condensed and restructured).

Exception: Figure 8.1 (© Deathbulge) and Figure 7.3 (a third-party Scratch screenshot) are described only, and must stay that way in derived skills.
