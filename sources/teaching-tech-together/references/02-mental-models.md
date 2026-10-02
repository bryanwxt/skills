# Building Mental Models

> Source: Greg Wilson, *Teaching Tech Together* (2018), Ch. 2 "Building Mental Models" (§2.1–§2.2). Licensed CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/); condensed and restructured for skill use, with quotations marked. Rule IDs use prefix `MOD`.

## When a skill needs this
- An exercise or quiz generator writes multiple-choice questions (MCQs) whose wrong answers diagnose specific misconceptions.
- A lesson-design assistant decides whether material should be a tutorial (for novices) or a manual (for competent practitioners), and sets how often to check understanding.
- A live-teaching assistant interprets a class vote (everyone right, one wrong answer dominant, answers split, a minority wrong) and recommends the next move.
- A teaching-feedback reviewer audits a lesson that lists facts or commands instead of building the concepts that make them meaningful.
- A course-design reviewer checks that formative assessments prepare learners for the summative exam.

## Key terms
| Term | Meaning (one line) |
|---|---|
| Mental model | "A simplified representation of the key elements and relationships of some problem domain that is good enough to support problem solving" (glossary). |
| Novice | Someone without a usable mental model of the domain, who reasons by analogy and guesswork (Ch 2 intro). |
| Competent practitioner | Someone who can "do normal tasks with normal effort under normal circumstances" with an everyday-good-enough model (Ch 2 intro). |
| Expert | Someone whose model includes the complexities and special cases, so they can handle the unusual and diagnose problems (Ch 2 intro; Ch 3). |
| Expertise reversal effect | Instruction that works for novices becomes ineffective for competent practitioners or experts, and vice versa [Kaly2003]. |
| Tutorial vs manual | A tutorial helps newcomers build a mental model; a manual helps competent practitioners fill gaps (Ch 2 intro). |
| Misconception (factual error / broken model / fundamental belief) | Novices' three kinds of wrong knowledge (§2.1). |
| Formative assessment | Assessment during a lesson that shapes the teaching; nobody passes or fails it (§2.1). |
| Summative assessment | Assessment at the end that tells whether the learning succeeded and the learner is ready to move on (§2.1). |
| Distractor | A wrong or less-than-best MCQ answer (§2.1). |
| Plausible distractor | A distractor that looks like it could be right (§2.1). |
| Diagnostic power | How much a wrong answer tells the teacher about that learner's misconception (§2.1). |
| Concept inventory | A validated MCQ instrument, built from large-scale interviews, that pinpoints specific misconceptions (§2.1 box). |
| Dreyfus model | Another name for the novice-to-expert progression used here (§2.2 exercise). |
| Four stages of competence | Unconscious incompetence, conscious incompetence, conscious competence, unconscious competence (§2.2 exercise). |

## Concepts

### Chapter 2 opening (unnumbered): novices, competent practitioners, experts
- **First task in teaching:** "figure out who your learners are and what they already know."
- **Origin.** Patricia Benner studied how nurses move from novice to expert [Benn2000] and identified **five stages** that most people go through "in a fairly consistent way." The hedges "most" and "fairly" are deliberate: people vary a lot, and "obsessing over how a few geniuses taught or learned isn't generally useful."
- **The book's three-stage simplification:**
  - **Novices** "don't know what they don't know." They have no usable mental model, so they reason by analogy and guesswork, borrowing pieces of models from superficially similar domains.
  - **Competent practitioners** have a model good enough for everyday purposes. It needn't be complete or accurate, just useful.
  - **Experts** have models that include the complexities and special cases, so they can handle out-of-the-ordinary situations and diagnose problems. Like competent practitioners, experts "know what they don't know and how to learn it" (more in Ch 3).
- **What a mental model is:** a simplified representation of the most important parts of a domain, good enough for problem solving. Example: ball-and-spring molecules. Atoms aren't balls and bonds aren't springs, but the model helps people reason about compounds and reactions. A more sophisticated model, a nucleus with orbiting electrons, is "wrong, but useful" too.
- **A sign of being a novice:** what they say is "not even wrong." Example: believing that a program typed character by character differs from an identical one that was copied and pasted.
- **Don't make novices uncomfortable for this.** Until they have a better model, borrowing (inappropriately) from other subjects is the best they can do (pointer to Ch 10).
- **Facts without a model backfire.** Presenting novices with a pile of facts is counter-productive because they have nowhere to put them. Too many facts too soon can even reinforce the incorrect model they have cobbled together. In [Mull2007a], a study of science video instruction, students who watched clear, well-illustrated videos believed they were learning but didn't engage deeply enough to notice that the content contradicted their prior beliefs. Presenting common misconceptions alongside the correct concepts increased learning, because it increased the mental effort students spent while watching.
- **Goal with novices:** help them build a mental model "so that they have somewhere to put facts."
- **Example, the Unix shell lesson:** Software Carpentry teaches fifteen commands in three hours (one every twelve minutes). That looks "glacially slow" until you see that the real content is the concepts: paths, history, tab completion, wildcards, pipes, command-line arguments and redirection. Without those concepts the commands make no sense. With them, learners can quickly assemble a repertoire of commands.
- **Tutorials vs manuals.** A **tutorial** helps newcomers build a mental model. A **manual** helps competent practitioners fill gaps. Tutorials frustrate competent practitioners because they are slow and state the obvious (obvious only to the practitioner). Manuals frustrate novices with jargon and missing explanations. This is the **expertise reversal effect** [Kaly2003], "another reason you have to decide early on who your lessons are meant for."
- **"A Handful of Exceptions" box:** Kernighan et al.'s trilogy [Kern1978, Kern1983, Kern1988] worked as good tutorials and good manuals at once, which is part of why Unix and C became popular. Ray and Ray on Unix [Ray2014] and Fehily on SQL [Fehi2008] also manage it. Wilson admits he doesn't know how they do it.

### 2.1 Are People Learning?
- **Clearing away wrong knowledge is part of model-building.** Mark Twain: "It ain't what you don't know that gets you into trouble. It's what you know for sure that just ain't so."
- **The three categories of novice misconceptions:**
  - **Factual errors**, e.g., believing Vancouver is the capital of British Columbia (it's Victoria). They are easy to correct, but "getting the facts right is not enough on its own."
  - **Broken models**, e.g., believing motion and acceleration must point the same way. *Treatment:* have novices reason through examples that expose the contradictions.
  - **Fundamental beliefs**, e.g., "the world is only a few thousand years old" or "some kinds of people are just naturally better at programming than others" [Guzd2015b, Pati2016]. These are broken models too, but they are often tied to the learner's social identity, so "they resist evidence and reason."
- **Formative assessment.** Teaching works best when teachers identify and clear up misconceptions *during* the lesson. "Formative" means the assessment forms or shapes the teaching. Learners don't pass or fail. It tells teacher and learner how both are doing and what to focus on next. Examples: a music teacher asks a learner to play a scale very slowly to check her breathing; a web-design teacher asks a learner to resize the images on a page to see whether the CSS explanation made sense.
- **Summative assessment** comes at the end of a lesson and tells whether the learner understood and is ready to move on. Chef analogy: the chef tasting while cooking is formative; the guests tasting the served dish is summative.
- **What a formative assessment needs:** it must be **quick** (so it doesn't break the flow of the lesson) and give a **clear result** (so it works with groups as well as individuals).
- **MCQs.** These are probably the most widely used formative assessment. Many teachers think little of them, but well-designed ones reveal much more than whether someone knows a fact. Example from teaching multi-digit addition [Ojos2015]: "What is 37 + 15?" with options 52 / 42 / 412 / 43.
  - **52** is correct.
  - **42**: the learner throws away the carry completely.
  - **412**: the learner treats each column as a separate problem, unconnected to its neighbours.
  - **43**: the learner knows a 1 must be carried but carries it back into the column it came from.
  - Each wrong answer is a **plausible distractor with diagnostic power**: it looks right, and it tells you what to explain next to *that* learner.
- **Where to find plausible distractors:**
  1. Questions learners asked, or problems they had, the last time you taught the subject.
  2. If you haven't taught it before: your own misconceptions, colleagues' experiences, and the history of the field. "If everyone misunderstood your subject in some way fifty years ago, the odds are that a lot of your learners will still misunderstand it that way today."
  3. Open-ended questions in class to collect misconceptions about material for a later class.
  4. Q&A sites such as Quora or Stack Overflow, to see what confuses people learning the subject elsewhere.
- **Other quick, unambiguous formats:** Parsons Problems (Ch 4) and matching problems (§12.3). Short-answer questions also work: answers of 2–5 words leave few enough plausible answers for scalable assessment [Mill2016a].
- **Writing formative assessments pays off even if you never use them.** It forces you to think about learners' mental models and how they might be broken, "to put yourself into your learners' heads."
- **Cadence:** "use something that takes a minute or two every 10–15 minutes" to make sure learners are learning. Then if many have fallen behind, only a short stretch needs repeating. This rhythm is **not** based on an attention limit: [Wils2007] found little support for the often-repeated claim that students can only pay attention for 10–15 minutes. **Online** (Ch 11), check in much more often to keep learners engaged.
  - *Note for the coordinator:* the brief mentions "1-in-4 / 1-in-10" timing heuristics. They don't appear in Ch 2 of this edition. The only cadence given is "a minute or two every 10–15 minutes."
- **Preemptive use:** start a class with an MCQ. If everyone answers correctly, skip the explanation they don't need. This also shows you respect learners' time, which helps motivation (Ch 10).
- **Reading the results:**
  - **Majority picks the same wrong answer:** go back and correct the misconception that distractor points to.
  - **Answers roughly evenly split across several options:** learners are probably guessing. Back up and re-explain the idea *in a different way*.
  - **Most are right, a few are wrong:** decide whether to spend time catching up the minority or keep the majority engaged. "No matter how hard you work or what teaching practices you use, you won't always be able to give everyone what they need; it's your responsibility as a teacher to make the call."
- **"Concept Inventories" box.**
  - The **Force Concept Inventory** [Hest1992] assesses basic Newtonian mechanics. Its creators interviewed many respondents, correlated misconceptions with patterns of right and wrong answers, and refined the questions until the tool could pinpoint specific misconceptions. Researchers then use it to measure how well changes in teaching work [Hake1998].
  - Computing: Tew and others developed and validated a language-independent introductory programming assessment [Tew2011], which was replicated in [Park2016]. [Hamo2017] is developing a recursion concept inventory.
  - *Caveats:* such tools are very costly to build, and students' ability to search for answers online is "an ever-increasing threat to their validity."
- **Running MCQs smoothly:**
  - Give learners coloured or numbered cards so everyone answers at once, instead of raising hands in turn.
  - Include an "I have no idea" option.
  - Encourage learners to talk to their neighbours for a few seconds before answering.
  - §9.2 describes an evidence-based method built on these ideas (peer instruction).
- **"Humor" box:** joke options such as "my nose!" (common on MCQs for younger students) give no insight into misconceptions, and most people don't find them funny, "especially on re-reading."
- **Alignment with summative assessment:** formative assessments should prepare learners for the summative one. "No one should ever encounter a question on an exam that the teaching did not prepare them for." New *kinds* of problems on an exam are fine only if learners have already practised tackling novel problems and received feedback on that practice.

## Rules
- **MOD-1** — Decide early who a lesson is for (novice, competent practitioner or expert) and write it as a tutorial or a manual accordingly. *Why:* the expertise reversal effect [Kaly2003]: tutorials frustrate competent practitioners and manuals frustrate novices. *Check:* the lesson states its audience level, and its pace, jargon and explanation depth match it. (Ch 2 intro)
- **MOD-2** — For novices, teach the concepts that organize the facts before or alongside the facts themselves. Don't present a pile of facts. *Why:* novices have no model to put facts in, and too many facts too soon can reinforce a wrong model [Mull2007a]. *Check:* for each list of commands or facts, the lesson names the underlying concepts it serves, as in the Unix-shell example (paths, pipes, wildcards...). (Ch 2 intro)
- **MOD-3** — Present common misconceptions explicitly alongside the correct concept. *Why:* in [Mull2007a] this increased the mental effort learners spent and increased learning. Clear explanations alone gave an illusion of learning. *Check:* the material contains at least one "you might think X, but actually Y" for each key idea. (Ch 2 intro)
- **MOD-4** — Don't make novices feel foolish for "not even wrong" reasoning by analogy. *Why:* until they have a better model it is the best they can do (Ch 10). *Check:* the feedback scripts for wrong answers are non-judgmental and redirect to the model. (Ch 2 intro)
- **MOD-5** — Match the correction to the type of misconception: state the fact for factual errors; walk through contradiction-exposing examples for broken models; expect resistance, and don't rely on evidence alone, for identity-linked fundamental beliefs. *Why:* the three categories respond differently (§2.1). *Check:* each anticipated misconception is labelled with its type and its treatment. (§2.1)
- **MOD-6** — Use formative assessment throughout every lesson, and make each check quick and its result clear. *Why:* identifying and clearing up misconceptions during the lesson is when teaching is most effective. Quick, clear checks keep the flow and scale to groups. *Check:* every formative item takes about 1–2 minutes and has an unambiguous answer. (§2.1)
- **MOD-7** — Insert a 1–2 minute check roughly every 10–15 minutes in person, and much more often online. *Why:* if many learners have fallen behind, only a short stretch needs repeating. This is a practical rhythm, **not** an attention-span limit [Wils2007]. *Check:* the lesson timeline has no stretch longer than about 15 minutes without a check (shorter online). Reject any justification that cites a "10-minute attention span." (§2.1)
- **MOD-8** — Make every MCQ distractor plausible and diagnostic. Each wrong answer should correspond to one specific, named misconception. *Why:* then a learner's choice tells you what to explain next to them (37 + 15 example, [Ojos2015]). *Check:* every distractor has a written misconception attached, and none is "obviously wrong." (§2.1)
- **MOD-9** — Source distractors from real learner errors: past learners' questions and problems, your own and colleagues' misconceptions, the field's historical misunderstandings, open-ended questions asked in earlier classes, and Q&A sites. *Why:* plausibility comes from errors people actually make. *Check:* each distractor's source is identifiable. (§2.1)
- **MOD-10** — Don't put joke options in MCQs. *Why:* they reveal no misconception and most people don't find them funny. *Check:* no option is deliberately absurd. (§2.1)
- **MOD-11** — Act on class MCQ results by pattern. If the majority picks one wrong answer, fix that misconception. If answers are split, re-explain differently. If everyone is right, move on or skip ahead. If a minority is wrong, make an explicit call between catching them up and keeping the majority engaged. *Why:* each pattern signals a different state of understanding (§2.1). *Check:* the teaching plan or assistant output names which pattern occurred and the matching action. (§2.1)
- **MOD-12** — Make sure formative assessments prepare learners for the summative assessment. Never examine what the teaching didn't prepare learners for. If an exam includes novel problems, give practice and feedback on novel problems first. *Why:* fairness and alignment (§2.1). *Check:* map each exam question to a formative exercise of the same kind; any unmapped "novel problem" item needs a prior novel-problem practice. (§2.1)
- **MOD-13** — Use a preemptive check at the start of a topic and skip material the class already knows. *Why:* it saves time and shows respect for learners' time, which helps motivation (Ch 10). *Check:* the lesson has an opening check with a planned skip branch. (§2.1)
- **MOD-14** — Collect answers simultaneously (coloured or numbered cards), offer an "I have no idea" option, and allow a few seconds of neighbour discussion before answering. *Why:* this keeps the flow, and it avoids the hand-raising-in-turn problem and forced guessing. *Check:* the MCQ delivery plan specifies a simultaneous response mechanism and includes "I have no idea." (§2.1)
- **MOD-15** — Use other quick, unambiguous formats where MCQs don't fit: Parsons Problems, matching problems, or 2–5-word short answers. *Why:* they are equally quick to mark, and short answers keep the space of plausible answers small enough to scale [Mill2016a]. *Check:* each free-text formative item has an expected answer of 2–5 words. (§2.1)
- **MOD-16** — Write formative assessments as a design exercise even if you won't use them in class. *Why:* it forces you to model learners' broken mental models. *Check:* the lesson design includes the drafted checks with their misconception notes. (§2.1)
- **MOD-17** — Prefer validated concept inventories (FCI, the language-independent CS1 assessment) to measure the effect of teaching changes where they exist. Treat them as costly to build and vulnerable to online answer lookup. *Why:* a validated instrument can pinpoint misconceptions and measure the effect of a change [Hest1992, Hake1998, Tew2011]. *Check:* any claim that a teaching change "worked" names its instrument and acknowledges validity threats. (§2.1)

## Procedures

### P1: Write a diagnostic multiple-choice question
1. Pick one concept the lesson has just taught. Write a question stem that requires *thinking through* the concept, not recalling a phrase.
2. List the misconceptions learners have shown or are likely to have (MOD-9 sources). Classify each as a factual error or a broken model (MOD-5).
3. For each of 2–4 misconceptions, work the problem *as a learner holding that misconception would* and record the answer it produces. That answer is the distractor (as in the 37 + 15 example: drop the carry → 42; columns independent → 412; carry back into the same column → 43).
4. Check plausibility: would a learner with that misconception confidently choose it? Delete any option that is obviously wrong or a joke (MOD-10).
5. Check uniqueness: each distractor should map to exactly one misconception, so the response is unambiguous.
6. Optionally add "I have no idea" (MOD-14).
7. Write the remediation for each distractor ahead of time: what you will explain if the majority picks it.
8. Peer-test: give it to a colleague. Is it ambiguous? Are the misconceptions plausible? Do the distractors really test for them? Are likely misconceptions missing? (the §2.2 exercise questions)

### P2: Run and interpret an in-class formative check
1. Pose the question. Learners answer simultaneously with cards or a similar mechanism. Optionally allow a few seconds of neighbour discussion first (MOD-14; §9.2 for peer instruction).
2. Tally the answers.
3. Decide:
   - **Almost all correct** → move on. If this was a preemptive check, skip the planned explanation (MOD-13).
   - **Majority on one distractor** → address the misconception linked to that distractor.
   - **Evenly split** → learners are guessing. Re-explain the idea in a *different* way, not the same explanation again.
   - **Most correct, a few wrong** → make an explicit call: help the minority (e.g., one-on-one later, or a helper) or keep the majority engaged. Accept that you can't serve everyone every time.
4. Plan the next check 10–15 minutes later (sooner online).

### P3: Plan formative checks for a lesson
1. Split the lesson into segments of at most about 10–15 minutes of instruction, shorter for online teaching.
2. End each segment with a 1–2 minute check (MCQ, Parsons, matching, or short answer) whose result is clear.
3. Optionally open with a preemptive check.
4. Map every summative item back to a formative check of the same kind (MOD-12). Add novel-problem practice if the exam has novel problems.

### P4: Decide tutorial vs manual
1. Identify the audience's stage: do they have a usable model (competent or expert) or not (novice)?
2. Novice → tutorial: build the model, introduce few concepts slowly, avoid jargon, explain everything, and check often.
3. Competent practitioner → manual: organize for gap-filling and lookup, and don't re-explain the basics.
4. A mixed audience → expect frustration on both sides (expertise reversal). Pick one primary audience, or produce both forms. Writing both at once is rarely achieved (the Kernighan / Ray / Fehily exceptions).

## Diagnostics
| Symptom (in a lesson, class, or community) | Underlying problem | Fix (rule IDs) |
|---|---|---|
| The lesson is a list of commands or API calls, and learners forget them immediately | Facts presented without a model to hold them | MOD-2 |
| Learners report "that was clear" but fail transfer questions | Illusion of learning; prior misconceptions never confronted [Mull2007a] | MOD-3, MOD-6 |
| Experienced attendees are bored and novices are lost in the same session | Expertise reversal; audience not chosen | MOD-1, P4 |
| A learner says copy-pasted code "works differently" from typed code | Novice reasoning by analogy ("not even wrong") | MOD-4, MOD-2 |
| The teacher only finds out at the exam that half the class didn't get it | No formative assessment, or checks too far apart | MOD-6, MOD-7, P3 |
| MCQ results say nothing about what to re-teach | Distractors aren't diagnostic (random or joke options) | MOD-8, MOD-10, P1 |
| Votes are spread evenly across all options | Learners are guessing | MOD-11: re-explain differently |
| Most of the class picks the same wrong option | A shared misconception | MOD-11: target that distractor's misconception |
| Some learners don't answer when hands are raised | Social exposure and turn-taking slow things down | MOD-14 |
| A learner insists "some people just can't code" despite evidence | A fundamental belief tied to identity | MOD-5 (expect resistance); see `10-motivation-and-inclusion.md` |
| Exam questions surprise learners | Formative and summative assessments are misaligned | MOD-12 |
| A justification cites a "10-minute attention span" | A myth [Wils2007] | MOD-7 |

## Templates and checklists

**Diagnostic MCQ template:**
```
Concept tested:
Stem:
A) <correct answer>
B) <distractor>  -> misconception: <...>  -> if majority picks: <remediation>
C) <distractor>  -> misconception: <...>  -> if majority picks: <remediation>
D) <distractor>  -> misconception: <...>  -> if majority picks: <remediation>
E) I have no idea   (optional)
Source of each misconception: past learners / own / colleagues / history of field / Q&A sites
```

**MCQ review checklist (from §2.1 and the §2.2 exercise):**
- [ ] Is the question unambiguous?
- [ ] Is each misconception plausible?
- [ ] Does each distractor actually test for its misconception?
- [ ] Are any likely misconceptions *not* tested for?
- [ ] Are there no joke or absurd options?
- [ ] Can it be answered in a minute or two with a clear result?

**Class-vote decision table:**
| Result pattern | Interpretation | Action |
|---|---|---|
| Nearly all correct | Understood (or already known) | Move on; skip ahead if this was a preemptive check |
| Majority on one wrong answer | A shared misconception | Address that distractor's misconception |
| Evenly split | Guessing | Re-explain in a different way |
| Most right, a few wrong | Mixed | Teacher's call: help the minority vs keep the majority engaged |

**Formative assessment requirements:** quick to administer; clear result; usable with groups; about 1–2 min; every 10–15 min in person, more often online.

## Examples
- **37 + 15 MCQ** [Ojos2015]. Distractors 42, 412 and 43 each identify a distinct carrying error, so the teacher knows exactly what to explain to each child (§2.1).
- **Unix shell lesson.** Fifteen commands in three hours looks slow, but the target is the seven concepts (paths, history, tab completion, wildcards, pipes, command-line arguments, redirection). With those, learners pick up commands quickly. *Lesson:* teach the model, not the list (Ch 2 intro).
- **Ball-and-spring and orbiting-electron atoms** are "wrong, but useful" models that support reasoning (Ch 2 intro).
- **Music scale / web image resize.** Small diagnostic tasks embedded in practice reveal whether the explanation landed (§2.1).
- **Chef tasting vs guests tasting:** the formative/summative distinction (§2.1).
- **Ice in a bathtub** (§2.2 exercise; Figure 2.1 shows a block of ice floating in a tub filled to the rim with water). Does the water overflow, drop, or stay the same when the ice melts? It stays the same: the ice displaces its own weight in water, so the meltwater exactly fills the "hole." Working out why builds a model of weight, volume and density [Epst2002]. *Lesson:* a good formative question makes people think through a model.
- **Kernighan trilogy, Ray & Ray, Fehily:** rare books that work both as tutorials and as manuals (Ch 2 intro box).

## Evidence and caveats
- **Benner's stages** [Benn2000] are followed by "most" people in a "fairly" consistent way. The three-stage version is the book's own simplification.
- **[Mull2007a]:** clear videos alone produced an illusion of learning. Including misconceptions increased mental effort and learning.
- **[Kaly2003]:** the expertise reversal effect.
- **[Wils2007]:** little support for the "10–15 minute attention span" claim. **Treat the attention-span claim as debunked.** The 10–15 minute check-in rhythm is pragmatic, not physiological.
- **[Mill2016a]:** short answers of 2–5 words allow scalable assessment.
- **[Hest1992], [Hake1998]:** the Force Concept Inventory, and its use to compare teaching methods.
- **[Tew2011], [Park2016], [Hamo2017]:** computing concept inventories, the last still in development. Building them is very costly, and online searching increasingly threatens their validity.
- **[Guzd2015b], [Pati2016]:** "some people are naturally better at programming" is listed as a *fundamental-belief misconception*. Per its bibliography entry, [Pati2016] reports evidence that CS grades are not bimodal. **Record the "natural programmer" idea as debunked.**
- **[Tedr2008]** (exercise): three traditions of computing (mathematical, scientific, engineering), offered as alternative mental models of the discipline, not as findings.
- Wilson says MCQs are often looked down on but are powerful *when well designed*. The value depends on distractor quality.

## Practice exercises
- **Your Mental Models** — describe one mental model you use at work in a few sentences, give a partner feedback, have a few people share with the group, then discuss whether "mental model" can be defined precisely or is useful because it is fuzzy. Think-pair-share / 15 min.
- **Symptoms of Being a Novice** — discuss what someone does or says that marks them as a novice in a domain. Whole class / 5 min.
- **Modelling Novice Mental Models** — write an MCQ on a topic you teach, explain what misconception each distractor diagnoses, then swap with a partner and critique it (ambiguity, plausibility, whether the distractors test the misconceptions, untested misconceptions). Pairs / 20 min.
- **Other Kinds of Formative Assessment** — using the ice-in-bathtub problem as a model, describe another formative assessment you have seen or used and how it tells both teacher and learner where they are and what to do next. Whole class / 20 min.
- **A Different Progression** — using the four stages of competence (unconscious incompetence → conscious incompetence → conscious competence → unconscious competence), name one subject where you are at each stage, the stage most of your learners are at, and the stage you want to get them to. Individual / 15 min.
- **What Kind of Book Is This?** — decide whether the book's main chapters are a tutorial or a manual, the same for the appendices, and why. Small groups / 5 min.
- **What Kind of Computing?** — decide which of [Tedr2008]'s three traditions (mathematical: programs as correct or incorrect algorithms; scientific: programs as models of information processes; engineering: programs as built objects judged by effectiveness and reliability) matches your model of computing, or describe your own. Individual / 10 min.

## Cross-references
- `01-introduction-and-motivation-to-teach.md` — who the learners are; pre-assessment.
- `03-expertise-and-memory.md` — experts in depth, the expert blind spot, concept maps as a way to see mental models.
- `04-cognitive-load.md` — Parsons Problems as quick formative assessment.
- `06-lesson-design.md` — backward design: summative first, then formative, then content; learner personas (§6.1).
- `09-in-the-classroom.md` — peer instruction (§9.2), which builds on simultaneous MCQ voting; pre-assessment (§9.4).
- `10-motivation-and-inclusion.md` — not making novices uncomfortable; respecting learners' time; fixed vs growth mindset.
- `11-teaching-online.md` — checking in more often online.
- `12-exercise-types.md` — matching problems (§12.3) and other formats.

## Source map
| Book section | Covered under |
|---|---|
| Ch 2 intro (Benner; novice/competent/expert; mental model; Mull2007a; Unix shell; tutorials vs manuals; expertise reversal; "A Handful of Exceptions") | Concepts › Ch 2 opening; MOD-1–MOD-4; P4 |
| §2.1 Misconception types | Concepts › 2.1; MOD-5 |
| §2.1 Formative vs summative | Concepts › 2.1; MOD-6, MOD-12 |
| §2.1 MCQs, distractors, diagnostic power | Concepts › 2.1; MOD-8, MOD-9, MOD-16; P1; MCQ template |
| §2.1 Other formats, cadence, preemptive use, interpreting results | MOD-7, MOD-11, MOD-13, MOD-15; P2, P3 |
| §2.1 "Concept Inventories" box | Concepts › 2.1; MOD-17; Evidence |
| §2.1 Card voting, "I have no idea", neighbour talk | MOD-14 |
| §2.1 "Humor" box | MOD-10 |
| §2.1 Formative prepares for summative | MOD-12 |
| §2.2 Exercises (incl. Figure 2.1, Dreyfus / four stages, [Tedr2008]) | Practice exercises; Examples |
