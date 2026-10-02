# Introduction and Motivation to Teach

> Source: Greg Wilson, *Teaching Tech Together* (2018), Ch. 1 "Introduction" (§1.1–§1.7) and Ch. 16 "Why I Teach" (unnumbered). Licensed CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/); condensed and restructured for skill use, with quotations marked. Rule IDs use prefix `WHY`.

## When a skill needs this
- A workshop planner or lesson-design assistant has to frame who a teaching effort is for, and why, before it designs anything. Use it to draft the opening "who are you / why teach" pre-assessment.
- A community-building advisor sets up a new volunteer teaching group and needs the code-of-conduct rationale, including the reply to "isn't this censorship?".
- A teaching-feedback reviewer checks whether a course pitch justifies programming only by "jobs of the future" and ignores other reasons to learn.
- Any skill that has to place a user among the book's intended readers (end-user teachers), or point a user to further reading.
- A skill writing a motivational close, mission statement or "why we teach" page for a teaching community.

## Key terms
| Term | Meaning (one line) |
|---|---|
| End-user teacher | Someone who teaches often but not as their main job, has little or no pedagogy background, and may work outside institutional classrooms (glossary). |
| Free-range learner | Someone learning outside an institutional classroom with required homework and a mandated curriculum (glossary). |
| Novice / competent practitioner / expert | The book's three-stage simplification of Benner's model: no usable mental model / a model good enough for everyday work / a dense model that handles exceptions. Detailed in `02-mental-models.md`. |
| Code of Conduct | A published statement of expected behaviour and consequences that everyone in a class must abide by (§1.5; template in appendix "Code of Conduct"). |
| Pre-assessment | Questions learners answer before a class so the teacher knows who they are and how to help (§1.7, §9.4). |
| Community of practice | A self-perpetuating group of people who share and develop a craft (glossary). It is the subject of the book's fourth part. |

## Concepts

### Chapter 1 opening (unnumbered): what the book is and what it assumes
- **Problem.** Hundreds of grassroots groups teach programming, web design, robotics and similar skills to free-range learners outside traditional classrooms. They exist so that people don't have to learn alone, yet "their founders and instructors are often teaching themselves how to teach" (Ch 1 intro).
- **Premise.** Wilson's analogy: knowing a few basic facts about germs and nutrition helps you stay healthy. In the same way, knowing a little psychology, instructional design, inclusivity and community organization makes you a more effective teacher. The book "presents evidence-based practices you can use right now, explains why we believe they are true, and points you at other resources" (Ch 1 intro).
- **The four parts:** (1) how people learn; (2) how to design lessons that work; (3) how to deliver those lessons; (4) how to grow a community of practice around teaching.
- **The book follows its own advice.** It opens with short, engaging, actionable ideas to motivate further reading (Ch 10). It includes many exercises to reinforce learning (Ch 2). It publishes its original design (appendix "Design Notes", Appendix M) as a worked example of a lesson design.
- **"This Book Belongs to Everyone".** The book is a community resource. Parts were first written for the Software Carpentry instructor training program, which had run several hundred times over the previous six years. All of it may be freely redistributed under CC BY 4.0. Contributions of every size, from errata to new chapters, are handled the way Wikipedia edits or open-source patches are. Every contributor is credited in each new release (Appendix C; code of conduct in §C.1).
- **What the book believes, as Ch 1 states it.** Ch 1 has no numbered list of assumptions. Its commitments are stated through the text:
  - teaching can be improved with evidence-based practice;
  - people construct knowledge rather than absorb it. Wilson names Papert [Pape1993] as the strongest influence on his teaching (§1.2);
  - mutual respect, enforced by a code of conduct, is the most important lesson of his thirty years of teaching (§1.5);
  - education should give people the power to decide what jobs exist and to make sure those jobs are worth doing, not just prepare them for "the jobs of the future" (§1.4);
  - teaching is a way of making the world better (Ch 16).
  - Reader prerequisites are listed elsewhere: the appendix "Design Notes" says some exercises assume readers can loop over a list, use if-else, and write and call a simple function (owned by `06-lesson-design.md`).

### 1.1 Who You Are
- Wilson applies his own method (§6.1, learner personas) to the book. All four target readers are **end-user teachers**: teaching isn't their main job, they have little or no pedagogy background, and they may work outside institutional classrooms.
- **The four personas:**
  - **Emily** trained as a librarian and now works as a web designer and project manager at a small consultancy. She helps run web-design classes for women entering tech as a second career. She is recruiting colleagues to run more classes with her lessons and wants to learn how to grow a volunteer teaching organization. *How she will use the book:* a weekly online reading group with her volunteers.
  - **Moshe** is a professional programmer whose two teenagers' school offers no programming. He volunteers to run a monthly after-school club. He presents to colleagues often but has never designed a lesson. He wants to build lessons collaboratively and may turn them into a self-paced online course. *Use:* part of the book in a two-day weekend workshop, the rest on his own.
  - **Samira** is a robotics undergraduate considering full-time teaching. She wants to help run weekend workshops for undergraduate women, but has never taught a whole class and is uncomfortable teaching things she isn't an expert in. She wants to learn about education to decide whether it's for her. *Use:* a one-semester undergraduate course with assignments, a project and a final exam.
  - **Gene** (they/them) is a CS professor in operating systems who has taught undergraduates for six years and believes "there has to be a better way". The campus teaching centre only trains staff to post assignments and grades in the learning management system, so Gene wants to know what else to ask for. *Use:* reading alone in the office or while commuting.
- **What the personas have in common:** varied technical backgrounds and some teaching experience, but no formal training in teaching, lesson design or community organization. Most work with free-range learners and focus on teenagers and adults, not children. All have limited time and resources.
- Other ways people have used the material are in §C.2. That discussion sits in an appendix because it depends on ideas introduced later in the book.

### 1.2 What to Read Instead
- **In a hurry:** [Brow2018], "Ten quick tips for teaching programming" (PLoS Computational Biology), freely available online.
- **Also recommended:**
  - The Carpentries instructor training. Most of the first half of the book was developed for it.
  - [Lang2016] *Small Teaching* and [Hust2012] *Teaching What You Don't Know*: short, approachable, and they connect things you can do now to the research behind them.
  - [Majo2015] (catalogue of about 100 exercise types), [Broo2016] (50 ways to get groups discussing productively), [Berg2012] (pedagogical patterns) and [Rice2018] (why and how to give learners breaks in class). Wilson thinks these make more sense once Huston or Lang has given you a framework.
  - [DeBr2015], which teaches what is true about education by explaining what isn't, and [Dida2016], which grounds learning theory in cognitive psychology.
  - [Pape1993] *Mindstorms*: "an inspiring vision of how computers could change education."
  - [Gree2014], [McMi2017], [Watt2014]: why forty years of education reform have failed, how for-profit colleges exploit and worsen inequality, and how technology has repeatedly failed to revolutionize education.
  - [Guzd2015a], [Hazz2014], [Sent2018]: academically oriented books on teaching computing.
  - [Brow2007], [Mann2015]: on changing systems and organizations, "because you can't teach computing well without changing the system in which we teach, and you can't do that on your own."
- **The most formative book for Wilson** is [Pape1993]. Papert's central argument: people don't absorb knowledge; they (re-)construct it for themselves, and computers are a new and powerful tool for helping them do that. Wilson points to Andy Ko's summary of Papert and to [Craw2010] *Shop Class as Soulcraft* as a companion.

### 1.3 History
- In the late 1980s Wilson taught too fast, used too much jargon, and had no idea how much his learners understood. He improved slowly, "stumbling around in a darkened room."
- In 2010 he rebooted **Software Carpentry**, which teaches basic computing skills to researchers. The name "carpentry" set it apart from software engineering: "the digital equivalent of painting a bathroom, not building the Channel Tunnel."
- He found Mark Guzdial's blog and *How Learning Works* [Ambr2010], which led him to [Hust2012, Lemo2014, Lang2016]. These showed him how to build and deliver better lessons in less time and with less effort.
- He began applying these ideas in 2012. The results were "everything I'd hoped for", so he started training others. That grew into a programme taught by dozens of trainers to more than a thousand people on six continents. He has since run it for people who teach programming to children, for librarians, and for women re-entering the workforce or changing careers. All of these experiences feed into the book.

### 1.4 Why Learn to Program?
- **The common argument:** future jobs require programming. Evidence offered: [Scaf2017] found that non-developers who program earn more than comparable workers who don't.
- **Wilson's caveat:** as Benjamin Doxtdator has pointed out, many such claims rest on shaky ground. Even if they were true, "education shouldn't prepare people for the jobs of the future: it should give them the power to decide what kinds of jobs there are, and to ensure that those jobs are worth doing" (§1.4).
- **Mark Guzdial's reasons to learn to program** (verbatim list, §1.4):
  1. "To understand our world."
  2. "To study and understand processes."
  3. "To be able to ask questions about the influences on their lives."
  4. "To use an important new form of literacy."
  5. "To have a new way to learn art, music, science, and mathematics."
  6. "As a job skill."
  7. "To use computers better."
  8. "As a medium in which to learn problem-solving."
- Wilson's motivation: if enough people understand how to make technology work for them, we can build a society that values and rewards all of these reasons (links to Ch 16).

### 1.5 Have a Code of Conduct
- "The most important thing I've learned about teaching in the last thirty years is how important it is for everyone to treat everyone else with respect, both in and out of class" (§1.5).
- **Instruction:** if you use this material in any way, adopt a Code of Conduct like the one in the appendix "Code of Conduct" (Appendix D) and require everyone in your classes to abide by it.
- **What a code can and can't do:** it can't stop people being offensive, any more than laws against theft stop stealing. It can make expectations and consequences clear. More importantly, having one tells people that there are rules and that they can expect a friendly learning experience.
- **Answer to free-speech objections:** a code of conduct isn't an infringement of free speech. People have a right to say what they think, but not wherever and whenever they want. "If they want to make someone feel unwelcome, they can go and find their own space in which to do it" (§1.5).
- Enforcement and the full code text are covered in `10-motivation-and-inclusion.md`.

### 1.6 Acknowledgments
- Many contributors are thanked by name, and Lukas Blakk is credited for the cover. Wilson takes responsibility for any remaining mistakes.
- **"Breaking the Law" box:** much of the cited research was publicly funded but sits behind paywalls. Wilson estimates he broke the law about 250 times downloading papers from sites like Sci-Hub. He asks researchers to publish in open-access venues or post copies on open preprint servers.

### 1.7 Exercises (framing)
- Every chapter ends with exercises that give a suggested format and a typical in-person duration. Most work in other formats. Solo readers can still do many of the "group" exercises, and any of them can take longer than suggested.
- **The Ch 1 exercises double as pre-assessment questions (§9.4).** Have learners answer them a few days before a class or workshop to get a much clearer idea of who they are and how best to help them.

### Chapter 16: Why I Teach
- **Wilson's original answer to University of Toronto students:** at their age he thought universities taught people how to learn; in grad school he thought they were about research; in his forties he realized "what we're really teaching you is how to take over the world, because you're going to have to whether you want to or not."
  - His parents' generation no longer runs the world; his own generation passes the laws, sets interest rates and makes life-and-death decisions in hospitals ("we are the grownups"). In about twenty years the students will be in charge.
  - **That is the reason for the design of hard coursework:** problems whose answers can't be "cribbed from last year's notes", and situations where students must decide what needs doing now, what can wait, and what can be ignored. If they don't learn these things now, they won't be ready when they must.
- **The fuller reason.** He doesn't want people to improve the world so he can retire in comfort. He wants them to do it because it is "the greatest adventure of our time." His examples of progress: 150 years ago most societies practised slavery; 100 years ago his grandmother wasn't legally a person in Canada; 50 years ago most people lived under totalitarian rule; in the year he was born, judges still ordered electroshock therapy to "cure" homosexuals. We have many more choices than our grandparents did.
- **Progress isn't automatic.** It comes from millions of people making millions of small decisions. Everyday choices (which brand to buy, which insult to shout) are political because each one picks one vision of the world over another.
- **Orwell.** Wilson quotes Orwell's "Why I Write" (1947): every line of Orwell's serious work since 1936 was written against totalitarianism, and "It is simply a question of which side one takes." His conclusion: "Replace 'writing' with 'teaching' and you'll have the reason I do what I do." The world "gets better because people make it better: penny by penny, vote by vote, and one lesson at a time."
- **Closing maxim (Ch 16, verbatim):** "Start where you are. / Use what you have. / Help who you can."

## Rules
- **WHY-1** — Before designing or adapting material, name your intended learners concretely, for example with short personas that cover background, current situation, goals and how they will use the material. *Why:* Wilson begins his own book this way (§1.1, applying §6.1). Readers differ in time, setting and need. *Check:* the plan names at least one learner with background, constraints, goal and delivery format, not just "beginners". (§1.1)
- **WHY-2** — Treat time and resources as limited for both teachers and learners, and design for volunteers and free-range learners where that is the audience. *Why:* all the target readers "have limited time and resources" and most teach outside institutions. *Check:* the plan fits the stated time budget and doesn't assume institutional support such as TAs, an LMS or mandatory attendance unless it exists. (§1.1)
- **WHY-3** — Adopt a code of conduct and require every participant to abide by it, in and out of class. *Why:* Wilson calls respect "the most important thing I've learned about teaching in the last thirty years". A code makes expectations and consequences clear and signals a friendly environment. *Check:* the event plan links a code of conduct and says how participants agree to it. (§1.5)
- **WHY-4** — Don't claim a code of conduct prevents bad behaviour. Present it as setting expectations and consequences. *Why:* like laws against theft, it can't stop offences. *Check:* the wording promises clarity and consequences, not prevention. (§1.5)
- **WHY-5** — Answer "free speech" objections to a code by separating the right to speak from a right to speak anywhere, any time. *Why:* this is the argument Wilson gives. *Check:* a drafted response states that the class space has rules and that people who want to exclude others can find their own space. (§1.5)
- **WHY-6** — Justify learning to program with several reasons (understanding the world and processes, questioning influences, literacy, learning other subjects, using computers better, problem-solving) and not only "jobs of the future". *Why:* job-market claims rest on shaky ground, and education should empower people to shape which jobs exist. *Check:* course or pitch copy names at least one non-vocational reason that matches its audience. (§1.4)
- **WHY-7** — Check that your reasons for teaching match your learners' reasons, and adjust content where they don't. *Why:* the §1.7 "Why Learn to Program?" exercise asks how off-diagonal items change what you teach. *Check:* the plan records the learners' motivations and where they differ from the teacher's. (§1.4, §1.7)
- **WHY-8** — Send reflective questions (best and worst class, what, whom and why you teach, how you will know you're teaching well) a few days before an event as pre-assessment. *Why:* the answers give "a much clearer idea of who they are and how best you can help them." *Check:* a pre-event questionnaire exists and is due days before the event, not at the start of it. (§1.7, §9.4)
- **WHY-9** — Make teaching materials follow the teaching advice they contain: open with short, engaging, actionable ideas, include reinforcing exercises, and publish the design. *Why:* the book does this deliberately (Ch 1 intro, citing Ch 10, Ch 2, Appendix M). *Check:* the material opens with something actionable, has exercises, and its design rationale is available. (Ch 1 intro)
- **WHY-10** — Release teaching materials under an open licence and accept community contributions with credit. *Why:* the book is a community resource under CC BY 4.0, handled like Wikipedia or open-source patches, and every contributor is credited. *Check:* the material has a licence, a contribution route and a credits list. (Ch 1 intro)
- **WHY-11** — Ground practice in evidence and say why you believe it, pointing learners to further resources. *Why:* that is the book's stated method ("explains why we believe they are true"). *Check:* each recommended practice cites its reason or source. (Ch 1 intro, §1.2)
- **WHY-12** — Give learners problems that can't be copied from last year's notes, and situations where they must triage what to do now, later or never. *Why:* they will soon run the world and must practise judgment now (Ch 16). *Check:* the assessments include novel problems and prioritization, with practice beforehand (see MOD-12). (Ch 16)
- **WHY-13** — Begin with what you have. Don't wait for ideal conditions: "Start where you are. Use what you have. Help who you can." *Why:* the world improves "one lesson at a time." *Check:* advice to a hesitant would-be teacher points to a concrete first step within their current means. (Ch 16)

## Procedures

### P1: Frame a new teaching effort (who, why, what)
1. Write two to four learner personas (WHY-1). For each, record background, current job or situation, what they want to teach or learn and why, constraints (time, money, institution), and how they will engage (reading group, weekend workshop, semester course, self-study). Use the §1.1 personas as models.
2. Classify each persona's teaching context: institutional or free-range; children, teenagers or adults; volunteer or paid.
3. List the reasons for learning from §1.4. Ask the learners, or estimate, how important each is to them and to you (the 3 × 3 grid exercise). Note the misaligned items.
4. Decision: if the learners' top reasons are non-vocational (understanding, art, science, literacy), choose examples and projects in those domains instead of job-skill framing (WHY-6, WHY-7).
5. Adopt a code of conduct (WHY-3) and decide how participants will see and accept it.
6. Send the §1.7 questions as pre-assessment a few days ahead (WHY-8). Read the answers before finalizing content.

### P2: Respond to a challenge to the code of conduct
1. Acknowledge that people have a right to say what they think.
2. State that this right doesn't extend to every place and time. This class is a space with rules.
3. State what the code does: it makes expectations and consequences clear and promises a friendly learning experience. It doesn't claim to prevent all offence.
4. If someone wants to make others feel unwelcome, they can find their own space (§1.5). For enforcement steps, see `10-motivation-and-inclusion.md`.

### P3: Choose further reading for a user
1. A user in a hurry gets [Brow2018].
2. A user who wants a practical framework gets [Lang2016] or [Hust2012] first, then the activity catalogues [Majo2015], [Broo2016], [Berg2012], [Rice2018].
3. A user who wants the cognitive science gets [Dida2016], then [DeBr2015] for myths.
4. A user interested in vision or reform gets [Pape1993] (plus [Craw2010]), then [Gree2014], [McMi2017], [Watt2014].
5. A user teaching computing academically gets [Guzd2015a], [Hazz2014], [Sent2018].
6. A user trying to change an organization gets [Brow2007], [Mann2015].

## Diagnostics
| Symptom (in a lesson, class, or community) | Underlying problem | Fix (rule IDs) |
|---|---|---|
| The plan says "for beginners" with no further detail | No concrete learner model | Write personas (WHY-1) |
| A volunteer workshop is designed like a semester course (long homework, assumed LMS) | Mismatch with the end-user-teacher or free-range context | WHY-2, WHY-1 |
| No code of conduct, or it is buried and never mentioned | Expectations and consequences unclear; newcomers can't expect a friendly space | WHY-3 |
| Organizers claim the code "prevents harassment" | Overpromising; credibility suffers when incidents happen | WHY-4 |
| Pushback that the code "limits free speech" goes unanswered | No prepared rationale | WHY-5, P2 |
| The course pitch is all about "jobs of the future" | Narrow, shaky justification that may not match learners' motives | WHY-6, WHY-7 |
| The teacher's passion and the learners' goals diverge (e.g., the teacher loves theory, learners want to make art) | Misaligned reasons | WHY-7 (3 × 3 grid) |
| The teacher learns who the audience is only on the day | No pre-assessment | WHY-8 |
| A would-be teacher keeps postponing until they "know enough" | Waiting for ideal conditions | WHY-13 |

## Templates and checklists

**Learner persona frame (modelled on §1.1):**
```
Name:
Background / training:
Current role:
Teaching or learning context (who, where, institutional or free-range, age group):
What they want and why:
Constraints (time, resources, experience, discomforts):
How they will use the material (reading group / workshop + self-study / course / solo):
```

**Pre-assessment questions (§1.7, usable verbatim):**
```
Highs and Lows
- What is the best class or workshop you ever took? What made it so good?
- What was the worst one? What made it so bad?

Know Thyself
- What do you most want to teach?
- Who do you most want to teach?
- Why do you want to teach?
- How will you know if you're teaching well?

Starting Points
- What do you most want to learn about teaching and learning?
- What is one specific thing you believe is true about teaching and learning?
```

**Reasons-alignment grid (§1.7, "Why Learn to Program?"):**
```
3 x 3 grid. X axis = importance to you (low/medium/high).
            Y axis = importance to your learners (low/medium/high).
Place each of Guzdial's 8 reasons (§1.4) in one cell.
- Diagonal = aligned. Off-diagonal corners = misaligned.
- Ask: how does this change what you teach?
```

**Code-of-conduct checklist (§1.5):**
- [ ] A code like the appendix "Code of Conduct" has been adopted.
- [ ] Every participant is required to abide by it, in and out of class.
- [ ] The wording states expectations and consequences.
- [ ] A free-speech response is prepared (P2).

## Examples
- **Software Carpentry's name.** Researchers needed basic computing skills, not software engineering, so Wilson chose "carpentry": "painting a bathroom, not building the Channel Tunnel." *Lesson:* naming scope precisely tells learners what they are getting (§1.3).
- **Wilson's early teaching.** He went too fast, used too much jargon and couldn't tell what learners understood. Reading research-based books (2010–2012) made his lessons better and cheaper to produce. *Lesson:* evidence-based practice saves teacher effort as well as helping learners (§1.3).
- **The four personas** (Emily, Moshe, Samira, Gene) each come with a different use of the book. *Lesson:* the same material serves very different delivery formats (§1.1).
- **"Breaking the Law."** About 250 illegal paper downloads were needed to write a book about publicly funded research. *Lesson:* publish research openly (§1.6).
- **The Toronto answer.** "We're teaching you how to take over the world" explains why coursework uses uncribbable problems and triage (Ch 16).

## Evidence and caveats
- [Scaf2017]: non-developer workers who program (or use spreadsheets) earn more than comparable workers who don't. Wilson cites it as the usual jobs argument, then notes (via Doxtdator) that many such claims are "built on shaky ground" (§1.4).
- The book's practices are presented as evidence-based, but Ch 1 itself is mostly framing, history and values. Its strongest empirical claim is the success of the Software Carpentry training, reported as Wilson's experience ("everything I'd hoped for") and not as a controlled study (§1.3).
- The claim that respect and a code of conduct matter most is Wilson's judgment from thirty years of teaching, not a cited finding (§1.5).
- Benner's five-stage progression, which underpins the novice/competent/expert distinction, holds for "most" people in a "fairly" consistent way. Wilson stresses human variability and warns against obsessing over how a few geniuses learned (Ch 2 intro; see `02-mental-models.md`).

## Practice exercises
- **Highs and Lows** — each person writes brief answers about the best and worst class or workshop they ever took and why, then shares them (in shared online notes if available, §9.7). Whole class / 5 min.
- **Know Thyself** — each person answers what, whom and why they want to teach, and how they will know they're teaching well, shares, and keeps the answers to revisit. Whole class / 5 min.
- **Starting Points** — each person writes what they most want to learn about teaching and one specific thing they believe is true about it, shares, and keeps the answers. Individual / 5 min.
- **Why Learn to Program?** — each person places Guzdial's eight reasons on a 3 × 3 grid (importance to me × importance to my learners), then identifies aligned (diagonal) and misaligned (off-diagonal) reasons and how that changes what they teach. Individual / 20 min.
- *(All four can be sent as pre-assessment a few days before a class, §1.7.)*

## Cross-references
- `02-mental-models.md` — the novice / competent practitioner / expert distinction and the expertise reversal effect.
- `03-expertise-and-memory.md` — the expert blind spot, relevant to Samira's worry about teaching outside her expertise.
- `06-lesson-design.md` — learner personas (§6.1) and the book's own design notes (appendix "Design Notes": scope, prerequisites).
- `09-in-the-classroom.md` — pre-assessment (§9.4) and shared online notes (§9.7).
- `10-motivation-and-inclusion.md` — motivation (Ch 10) and the full Code of Conduct appendix with enforcement.
- `13-building-community.md` — growing a volunteer teaching organization (Emily's goal), and the appendix on joining the book's community.

## Source map
| Book section | Covered under |
|---|---|
| Ch 1 intro (four parts; "This Book Belongs to Everyone") | Concepts › Chapter 1 opening; WHY-9, WHY-10, WHY-11 |
| §1.1 Who You Are | Concepts › 1.1; WHY-1, WHY-2; P1; persona template |
| §1.2 What to Read Instead | Concepts › 1.2; P3 |
| §1.3 History | Concepts › 1.3; Examples |
| §1.4 Why Learn to Program? | Concepts › 1.4; WHY-6, WHY-7 |
| §1.5 Have a Code of Conduct | Concepts › 1.5; WHY-3, WHY-4, WHY-5; P2 |
| §1.6 Acknowledgments ("Breaking the Law") | Concepts › 1.6; Examples |
| §1.7 Exercises | Concepts › 1.7; WHY-8; Practice exercises; pre-assessment template |
| Ch 16 Why I Teach | Concepts › Chapter 16; WHY-12, WHY-13 |
