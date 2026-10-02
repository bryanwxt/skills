# Workflows: the book as executable flows

> Cross-cutting file for Greg Wilson, *Teaching Tech Together* (2018), CC BY 4.0. It sequences the per-chapter procedures into end-to-end flows and says which file, procedure, and rule IDs each step uses. The procedures themselves, with their decision points, live in the chapter files.

## Router: which flow?

| The user wants to… | Flow | Entry point |
|---|---|---|
| Design a new lesson, course, workshop, or tutorial | **WF1 Backward design** | `06` P1 |
| Review or improve existing teaching material | **WF2 Lesson review** | this file, then `rules-and-checks.md` Part 2 |
| Write exercises, quizzes, or assessments | **WF3 Exercises and assessment** | `12` P1 |
| Prepare and run a live session or workshop | **WF4 Deliver a session** | `09` checklists |
| Get better at teaching, or give feedback on someone's teaching | **WF5 Improve teaching performance** | `08` P1–P3 |
| Teach programming specifically | **WF-PCK overlay** on WF1–WF4 | `07` P1 |
| Teach online: video, MOOC, flipped, hybrid | **WF6 Online** | `11` P1 |
| Help learners study better | **WF7 Learner self-regulation** | `05` P1 |
| Make teaching motivating, accessible, and inclusive | **WF8 Motivation and inclusion** | `10` P1–P5 |
| Start or grow a teaching group, recruit and keep volunteers, run meetings | **WF9 Community** | `13` P1 |
| Get support, find learners, or work with schools and other organizations | **WF10 Outreach and partnerships** | `14` P1, `15` P1 |

Three invariants hold across every flow:

1. **Learners, not content, come first.** Name who the teaching is for, concretely, before deciding anything else (WHY-1, LES-3, LES-5).
2. **Check understanding constantly.** Every 10–15 minutes, run a quick formative check whose result tells you what to do next (MOD-6, MOD-7). This is not justified by attention span (`02` Evidence).
3. **Prefer what the evidence supports, and say how strong it is.** Never design around debunked myths such as learning styles, the learning pyramid, the "geek gene", or far transfer (PCK-26, IND-3, MOT-15). Keep Wilson's hedges where he gives them (WHY-11, PCK-27).

---

## WF1 Backward design

Source: `06` P1 (Lesson Design Template) with T1, worked example E1 (the book's own design notes).

| # | Step | Output | Rules / procedures |
|---|---|---|---|
| 1 | Brainstorm the problems learners will solve, the misconceptions to address, and what is out of scope; agree with co-designers | Scope notes | LES-2, MEM-10 |
| 2 | Write 2–3 learner personas (five parts; "wants" in the learner's own words); reuse a shared set where one exists | Personas | LES-3, LES-4, `06` P3 |
| 3 | Record prerequisites beyond what the personas imply | Prerequisite list | LES-6 |
| 4 | Draw a concept map of the content; separate *what* from *in what order*; count new items per chunk | Concept map, chunk list | MEM-5 to MEM-8, `03` P1 |
| 5 | Choose what to teach first: quick to master and immediately useful; defer hard, low-use fundamentals | Ordered topics | MOT-6, `10` P2 (Figure 10.1 grid) |
| 6 | Write 1–2 full summative exercises with solutions, plus point-form ones | Summative assessments | LES-1, LES-7, `12` P1 |
| 7 | Write formative assessments and order them into an outline: 3–4 episodes per hour, a check every 10–15 minutes | Outline of checks | LES-8, MOD-7, `02` P3 |
| 8 | Write only enough content to get learners from one check to the next | Lesson content | LES-9 |
| 9 | Apply load and motivation design: worked → faded examples, Parsons problems, labelled subgoals, authentic tasks, no `foo`/`bar` | Revised content | COG-5, COG-6, COG-11, COG-12, MOT-7, MOT-8 |
| 10 | Write the course overview last: pitch, about six objectives, prerequisites. Objectives are one sentence each, with a measurable verb, at the right Bloom level (first four levels for intro courses) | Overview | LES-10, LES-13, LES-14, `06` P2 |
| 11 | Accessibility and inclusivity pass | Fix list | `10` P4, P5 |
| 12 | Plan for maintenance: cheap to update, small remixable pieces | Maintenance notes | LES-19, LES-20 |

Iterate freely, but keep the design notes in canonical order (LES-11). Backward design is not teaching to the test (LES-12).

## WF2 Lesson review

Run these audits on existing material, highest impact first. Report each finding with its rule ID and fix.

1. **Who and why.** Are the intended learners named, and do the lesson's reasons match theirs? (WHY-1, WHY-7, LES-5)
2. **Objectives.** Are they measurable and at the right level? (LES-13, LES-14)
3. **Formative checks.** Is there a check every 10–15 minutes, with diagnostic distractors? (MOD-6 to MOD-11)
4. **Expert blind spot.** Look for "just", explanations ordered by deep principle, and skipped steps. (MEM-1 to MEM-4, MOT-11; `03` P4)
5. **Cognitive load.** Check for split attention, decorative graphics, too much new content per step, and no worked examples. (`04` P4, P6)
6. **Motivation.** Check for authentic tasks, early wins, and demotivators. (`10` P1, P3)
7. **Accessibility and inclusion.** (`10` P4, P5)
8. **Programming specifics, if relevant.** Does the lesson show process, debugging, prediction, and tracing? Does it target known misconceptions? (PCK-1, PCK-5, PCK-8, PCK-9, PCK-12)
9. **Exercises.** Are the formats right, are they piloted, and are time estimates realistic? (`12` T2, EXR-28, EXR-29)
10. **Maintainability.** (LES-19)

## WF3 Exercises and assessment

1. Decide what you are assessing, and at which Bloom level (LES-13, LES-14).
2. Pick the exercise type from the catalog in `12` (EXR-1). For novices, prefer fill-in-the-blanks and Parsons problems over a blank page (EXR-7, CLS-27).
3. Write it with the type's recipe (`12` P2):
   - **MCQ:** every distractor maps to one real misconception, and there are no joke options (MOD-8 to MOD-10, EXR-2; `02` P1).
   - **Tracing:** answers are free entry, using a variables-by-lines table (EXR-9, EXR-10).
   - **Novice Parsons problems:** no distractor lines (EXR-8).
   - **Faded series:** ends in a blank solution (COG-6; `04` P1).
4. If auto-grading: provide a public mini test suite, never reject correct code that differs from yours, give actionable messages, and don't reveal expected outputs (`12` P3, EXR-4, EXR-19 to EXR-24).
5. If peers grade: use a rubric of observable behaviours and calibrate reviewers against the instructor first (IND-24 to IND-26, ONL-26, EXR-26).
6. Time it: count the time lost to "simple" failures, and pilot it on a colleague (EXR-28, EXR-29).

## WF4 Deliver a session

**Before**
- Run the event checklists: scheduling, setup, start, end, and the travel kit (`09` Checklists for Events, CLS-42).
- Send the pre-assessment. Ask how easy specific tasks would be, never for a 1–5 self-rating, and follow up with non-responders (CLS-13, CLS-14; `09` Pre-Assessment Questionnaire).
- Advertise the level with a topic list and sample exercises (CLS-15).
- Send a setup page and reminder email for all operating systems (CLS-29; `09` P7).
- Co-teachers agree a teaching model, hand signals, and who covers what (CLS-7 to CLS-11; `09` P3).

**During**
- Open with introductions that convey both competence and approachability, and state the Code of Conduct (CLS-31, WHY-3).
- Live-code rather than showing slides of code: narrate, use small steps, embrace mistakes, and ask learners to predict output (PRF-16 to PRF-29, PCK-8; `08` P4).
- Every 10–15 minutes, run a formative check, or peer instruction for misconceptions (MOD-7; CLS-5, CLS-6; `09` P2).
- Use sticky notes for status, pair programming with rotation, and shared notes. Don't touch learners' keyboards (`09` P5, P6; CLS-20, CLS-22, CLS-34).
- Repeat each question before answering it (CLS-35).
- Handle Code of Conduct violations by severity, in front of witnesses, and report them (`09` P1).

**After**
- Collect minute cards and one-up/one-down feedback, cluster them, and act on them (CLS-26, CLS-36; `09` P8).
- Co-teachers debrief (CLS-12).

**Constraint:** limit innovation. In a short workshop, add at most one new technique (CLS-41; `09` P9).

## WF5 Improve teaching performance

1. Practise with record-in-threes: record, review, give yourself feedback, then delete the recordings (`08` P1, PRF-13, PRF-14).
2. Ask for feedback yourself, with specific questions about the one thing you're working on, and write a self-assessment before reading it (PRF-3, PRF-4, PRF-6; `08` P3).
3. Structure the feedback with the 2×2 grid (went well / can improve × content / presentation) or the Presentation Rubric (PRF-8, PRF-9; `08` P2, P5).
4. Identify your nervous tells and displace them rather than trying to eliminate them (PRF-15).
5. Make the improvement social: lesson study, peer observation, and spreading practices by personal contact (PRF-1, PRF-2).

Learner satisfaction does not measure learning (PCK-16, `09` Kirkpatrick levels).

## WF-PCK overlay: teaching programming

Apply on top of WF1–WF4 (`07` P1–P4):

- **Show process.** Write code outside-in, in small steps with frequent feedback, and model debugging (PCK-1 to PCK-5).
- **Teach programming plans and the roles of variables** (PCK-4; `07` T3).
- **Make learners predict and trace.** Have them predict before running code and trace values beside variable names (PCK-8, PCK-9; `07` P2).
- **Teach testing as finding bugs** (PCK-10).
- **Target the known misconceptions**, such as the superbug (the belief that the computer understands intent) and spreadsheet-style variables. Prioritize errors by measured frequency (PCK-11 to PCK-13; `07` T1, T2).
- **Never call syntax simple** (PCK-14).
- **Use an explicit notional machine**, introduced incrementally (PCK-25; `07` P4).
- **Choose tools deliberately.** Use blocks for children; for adults, introduce procedural code before classes. Research doesn't settle typed vs. untyped languages (PCK-17 to PCK-19; `07` T6).
- **Favour the interventions with the largest measured effect:** media computation, group work, and CS0 (PCK-23; `07` T5).

## WF6 Online

1. Decide whether the course is online-with-humans or automated. Automation assesses only the lower Bloom levels well (ONL-1, ONL-2; `11` P1).
2. Use many short episodes. Keep videos to six minutes or less, and pair each one with an activity (ONL-9, ONL-14).
3. Use video to engage or to show actions, and text to explain. State misconceptions on screen and refute them (ONL-10, ONL-16, ONL-17; `11` P2, T2).
4. Set frequent, enforced deadlines, and hold weekly synchronous small-group sessions (ONL-4, ONL-5).
5. Build social presence: instructor presence, peer interaction, and a code of conduct (ONL-7, ONL-20, ONL-22, ONL-29).
6. Hybrid delivery: make every site remote with local helpers. Never run one in-room group plus remote attendees (ONL-30; `11` P4).
7. Flipped classroom: online materials cover everything; in-person time starts from the common core (ONL-19 to ONL-21; `11` P3).

## WF7 Learner self-regulation

Teach the six strategies by name: spaced practice, retrieval practice, interleaving, elaboration, concrete examples, and dual coding (IND-1 to IND-19; `05` P1–P3). Teach time management: no all-nighters, 30–60-minute uninterrupted blocks, and habits rather than willpower (IND-20 to IND-23; `05` P6). Use calibrated peer assessment and the Teamwork Rubric (IND-24 to IND-28; `05` P4, P5). Promise near transfer, never far transfer (IND-3).

## WF8 Motivation and inclusion

1. Run the motivation audit: self-determination theory (competence, autonomy, relatedness), authentic tasks, and early wins (`10` P1, P2; MOT-1, MOT-6, MOT-7).
2. Sweep for demotivators: contempt, tool-bashing, deep dives, bluffing, "just", installation pain, and "natural programmer" talk (`10` P3, T1; MOT-11, MOT-15, MOT-27).
3. Accessibility pass: involve disabled people, prepare baseline accommodations in advance, and make easy fixes first (`10` P4, T3; MOT-17 to MOT-20).
4. Inclusivity plan: a Code of Conduct, group signup, Lee's five practices, structural explanations of under-representation, and no deficit model (`10` P5, T4, T7; MOT-21 to MOT-26).
5. Impostor syndrome: share your own mistakes, live-code, and invite questions (`10` P6; MOT-14, COM-22).

## WF9 Community

1. Decide whether to found a new group or join an existing one. Learn first, then do (COM-1 to COM-7; `13` P1).
2. Recruit: end each class with how learners can help, ask recruits for a small favour first, and put newcomers in group activities (COM-9 to COM-12; `13` P2).
3. Retain: ask what people want and can do, offer many ways to contribute, recognize contributions, and make space for others (COM-14 to COM-18; `13` P3).
4. Retire members with the checklist (COM-13; `13` P4).
5. Govern: formal and accountable power, no early constitution, competent board members, a democracy when you formalize, and planned succession (COM-23 to COM-28; `13` P5).
6. Meetings and post mortems (COM-29 to COM-42; `13` P6–P8).

## WF10 Outreach and partnerships

1. Work out what you are really offering, and to whom. Write a persona and an elevator pitch for each stakeholder (MKT-1 to MKT-7; `14` P1, P2).
2. Brand and findability: lead with stories and positioning, and keep website essentials on the first screen (MKT-8 to MKT-14; `14` P3).
3. Cold contact: a specific point of connection; state the benefit, the offer, your credibility, and the terms; keep it short and plain; expect 10–15% conversion (MKT-15 to MKT-20; `14` P4).
4. Partners: listen to what they believe they need first. Address faculty fears and time costs rather than citing research. Change incrementally inside their framework, and change your own goals to fit (PTN-1 to PTN-13; `15` P1–P4).
