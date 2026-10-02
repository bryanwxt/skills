# In the Classroom

> Source: Greg Wilson, *Teaching Tech Together* (2018), Ch. 9 "In the Classroom" (§9.1–§9.13), appendices "Checklists for Events" and "Pre-Assessment Questionnaire". Licensed CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/); condensed and restructured for skill use, with quotations marked. Rule IDs use prefix `CLS`.

## When a skill needs this
- Planning the logistics and run-sheet of a programming workshop: setup instructions, room layout, sticky notes, shared notes, breaks, end-of-day feedback, event checklists.
- Designing in-class activities: peer-instruction questions, pair programming, think-pair-share, starter code, prediction prompts.
- Advising co-teachers and helpers on how to split work and behave while the other person teaches.
- Writing or reviewing a pre-workshop questionnaire, and planning for mixed abilities and false beginners.
- Handling a Code of Conduct incident during a class, or deciding how many new teaching techniques to introduce.

## Key terms
| Term | Meaning (one line) |
|---|---|
| Individual tutoring / 2-sigma | One-to-one mastery tutoring beats lecture by two standard deviations [Bloo1984] (Ch 9 intro). |
| Peer instruction | Brief intro → misconception-probing MCQ → vote → discuss in small groups if split → re-vote [Mazu1996] (§9.2). |
| Hypercorrection | Being confidently wrong, then learning why, makes the correction stick (§5.1, §9.2). |
| Co-teaching | Two teachers working together in the same classroom (§9.3). |
| Team teaching / Teach and assist / Alternative / Teach and observe / Parallel / Station teaching | The six co-teaching models from [Frie2016] (§9.3). |
| Helper | A non-teaching person who gives in-class technical support (§9.3). |
| Summative vs formative assessment | End-of-course judgement vs feedback that shapes instruction; learners assume all tests are summative (§9.4). |
| Dunning-Kruger effect | The less people know, the less accurately they estimate their knowledge [Krug1999] (§9.4). |
| False beginner | Has studied the subject before: same pre-test score (intercept) as beginners, much faster progress (slope) (§9.5). |
| Preparatory privilege | Advantage from a background that better prepares one for a learning task [Marg2010] (§9.5). |
| Pair programming (driver / navigator) | Two people, one computer; driver types, navigator comments; switch roles (§9.6). |
| Collaborative (shared) notes | A class-wide live document (Etherpad, Google Docs) for notes, code, data, and answers (§9.7). |
| Status flags | Two coloured sticky notes: one for "done, check me", one for "need help" (§9.8.1). |
| Minute cards | Before a break, one positive and one negative/question note, clustered by teachers (§9.8.3). |
| Never a blank page | Novices start exercises from existing code, never from an empty screen (§9.9). |
| One up, one down | End-of-day round: alternately one positive and one negative point, no repeats (§9.11). |
| Think-pair-share | Think alone and jot notes → explain in pairs and merge → a few pairs present (§9.11). |
| Free-range learner | Learner outside institutional classrooms with mandated curriculum (glossary). |

## Concepts

### Chapter framing (Ch 9 intro)
- Objectives: describe how to handle a Code of Conduct violation; explain the benefits and drawbacks of co-teaching; explain why teachers should not introduce new pedagogical practices in a short workshop; name, describe, and enact four teaching practices suited to programming workshops for adults, with a pedagogical justification for each.
- Ch 8 covered practising in-class teaching and live coding. This chapter covers other practices that have helped in programming classes.
- **Set expectations**: the best known method is individual tutoring. [Bloo1984] found one-to-one tutoring with mastery-learning techniques produced results two standard deviations better than conventional lecture, i.e. better than 98% of lectured students. One teacher per student is impossibly expensive, and "despite the hype, artificial intelligence isn't going to take the place of human instructors any time soon" (Ch 9 intro, written in 2018). **Every method is an attempt to get as much of the value of individual attention as possible, at scale.**

### 9.1 Enforce the Code of Conduct
- Every workshop should have and enforce a Code of Conduct (Ch 1; appendix "Code of Conduct", covered in `10-motivation-and-inclusion.md`).
- A teacher who believes someone has violated it may **warn them, ask them to apologise, and/or expel them**, depending on severity and on whether the violation seems intentional.
- Whatever you do:
  - **Do it in front of witnesses.** Most people tone down language and hostility in front of an audience, and a witness prevents later disputes about who said what.
  - **If you expel someone, tell the rest of the class and explain why.** This stops exaggerated rumours and signals clearly that you are serious about a safe, respectful class.
  - **Contact the class host as soon as you can** and describe what happened.
- "A Code of Conduct is meaningless without procedures for reporting violations and enforcing its rules" (§9.1). Enforcing is unpleasant, but reporting can be a much greater burden for people who have been targets.

### 9.2 Peer Instruction
- Problem: a teacher can say only one thing at a time, so how can she clear up many different misconceptions quickly? The best solution so far is **peer instruction**, created by Eric Mazur at Harvard [Mazu1996]. It has been studied extensively, including in programming [Crou2001, Port2013], and [Port2016] found students value it "even at first contact" (§9.2).
- It is "essentially a way to provide one-to-one mentorship in a scalable way" (§9.2), interleaving formative assessment with student discussion:
  1. Brief introduction to the topic.
  2. A multiple-choice question that **probes for misconceptions** rather than simple factual knowledge.
  3. All students vote.
  4. All right → move on.
  5. All the same wrong answer → address that specific misconception.
  6. A mix of right and wrong → several minutes of discussion in small groups (typically 2–4), then reconvene and re-vote.
- Why it works: group discussion forces students to clarify their thinking, which can expose gaps in reasoning (the book cites a video from Avanti's learning centre in Kanpur). Re-polling tells the teacher whether to move on or explain further. A final round of explanation and discussion after the correct answer is revealed gives one more chance to consolidate.
- **Is it just follow-the-leader?** [Smit2009] followed the first question with a second, answered individually. Peer discussion really does improve understanding, "even when none of the students in a discussion group originally knew the correct answer" (§9.2).
- Box "Taking a Stand": learners must **vote publicly** so they can't later change their minds and rationalise ("I just misread the question"). Much of the value comes from **hypercorrection**: having their answer be wrong and thinking through why (§5.1).

### 9.3 Teach Together
- **Co-teaching** is any situation where two teachers work in the same classroom. [Frie2016] describes six models:
  - **Team teaching**: both deliver a single stream of content in tandem, taking turns like musicians taking solos.
  - **Teach and assist**: A teaches; B moves around helping struggling students.
  - **Alternative teaching**: A gives a small set of students more intensive or specialised instruction; B delivers the general lesson to the main group.
  - **Teach and observe**: A teaches; B observes students, collecting data on their understanding to plan future lessons.
  - **Parallel teaching**: the class is split into two equal groups; both teachers present the same material simultaneously.
  - **Station teaching**: students in small groups rotate through stations or activities; both teachers supervise where needed.
- All models create more opportunities for **lateral knowledge transfer** than teaching alone. **Team teaching is particularly good for day-long workshops**: it rests each teacher's voice and reduces the risk that by day's end they are so tired they snap at students or fumble at the keyboard.
- Box "Helping": people uncomfortable teaching can still provide in-class technical support: help with setup and installation, answer technical questions during exercises, watch the room for people needing help, and monitor shared notes (§9.7), answering there or reminding the instructor at breaks. Helpers may be teachers-in-training (Teacher B in teach-and-assist), the host institution's technical support staff, alumni, or **advanced learners** who already know the material. Using advanced learners is "doubly effective": they understand peers' problems and it stops them getting bored (§9.3).
- **Rules for co-teaching partners:**
  - Spend 2–3 minutes before each class confirming who teaches what. With time for advance preparation, draw a concept map together.
  - Use that time to agree hand signals: "You're going too fast", "speak up", "that learner needs help", "It's time for a bathroom break" (§9.3).
  - Each person teaches at least 10–15 minutes at a stretch; more frequent switching distracts students.
  - The non-teaching partner must not interrupt, offer corrections, elaborations, or amusing personal anecdotes, or otherwise distract. **Exception:** leading questions can help, especially if learners seem unsure.
  - Before starting, each person checks what their partner will teach next and does not present any of it.
  - The non-teaching partner stays engaged (not on email): monitor shared notes, watch for strugglers, jot feedback for the partner at the next break. "Anything that contributes to the lesson is better than anything that doesn't" (§9.3).
  - Most importantly, after class take a few minutes to congratulate or commiserate with each other. Shared misery is lessened and shared joy increased.
- (Ch 8 §8.3 notes that the record-yourself exercise and a shared rubric make co-teachers' informal mutual feedback easier.)

### 9.4 Assess Prior Knowledge
- The more you know about learners beforehand, the more you can help them. In a formal school system, infer incoming knowledge from what the prerequisites *actually* cover. In free-range settings learners vary much more, so consider a short advance survey or questionnaire.
- **Risk 1: scaring people off.** School trains people to treat all assessment as summative: anything exam-like is something to pass, not a way to shape instruction. Answering "I don't know" to a handful of questions may make them conclude the class is too advanced, "you might scare off many of the people you most want to help" (§9.4).
- **Risk 2: self-assessment is unreliable** because of the Dunning-Kruger effect [Krug1999]: the less people know, the less accurate their self-estimate. Conversely, competent people may underrate themselves because they regard their competence as normal.
- So **don't ask people to rate their knowledge 1–5**. Ask how easily they could complete specific tasks. That can still scare people, so use something non-intimidating like the Pre-Assessment Questionnaire appendix (below), and **follow up with non-responders** to find out why they didn't respond.

### 9.5 Plan for Mixed Abilities
- With widely varying prior knowledge you can easily end up with a third of the class lost and a third bored. Strategies:
  - **Communicate the level clearly before sign-up**: list topics covered and show a few example exercises learners will be asked to do.
  - **Provide extra self-paced exercises** so advanced learners don't finish early and get bored.
  - **Ask advanced learners to help their neighbours.** They learn from answering, because it forces them to think in new ways.
  - **Watch for learners falling behind and intervene early**, before they become frustrated and give up.
- Most important: **accept that no single lesson can meet everyone's needs**. Slowing down for 2 strugglers fails the other 38; a few minutes on an advanced topic for one bored learner makes the rest feel left out.
- Box "False Beginners": a false beginner has studied the subject before and is learning it again. They may be indistinguishable from absolute beginners on pre-tests but move much faster: "their intercept is the same, but their slope is very different" (§9.5). They are common in free-range programming classes (e.g. a child who took Scratch two years ago has a mental model of loops and conditionals but tests poorly because it isn't fresh). All the strategies above apply.
- Being a false beginner is an example of **preparatory privilege** [Marg2010], often the result of a home secure and affluent enough to have several computers and parents familiar with them. "Whether or not this is fair depends on what you choose to include in your assessment" (§9.5).

### 9.6 Pair Programming
- Two programmers share one computer: the **driver** types, the **navigator** comments and suggests; they switch roles several times per hour.
- Effective in professional work [Hann2009] and as a teaching method. Benefits include higher success rates in introductory courses, better software, and greater student confidence in their solutions, with evidence that **students from underrepresented groups benefit even more** [McDo2006, Hank2011, Port2013, Cele2018]. Partners help each other during practicals, clarify each other's misconceptions when the solution is presented, and discuss shared interests at breaks. Wilson finds it especially helpful in mixed-ability classes, "since pairs are likely to be more homogeneous than individuals" (§9.6).
- How to run it:
  - **Pair everyone**, not just strugglers, so no one feels singled out.
  - Have people **sit in new places regularly** (new partners).
  - **Switch roles three or four times per hour** so the stronger personality doesn't dominate.
  - Use **flat (dinner-style) seating**, not banked (theatre-style): it supports pairing and lets helpers reach learners.
  - **Demonstrate** what pairing looks like, so people understand the navigator isn't supposed to just sit and watch.
  - Tell learners about [Lewi2015]: in a Grade 6 class, pairs focused on finishing the task as fast as possible were less fair in sharing.
- Box "Switching Partners": teachers disagree about requiring regular partner changes. For: new insights, new friends. Against: moving computers and power adapters several times a day is disruptive, and pairing can be uncomfortable for introverts. Evidence: [Hann2010] found only weak correlation between the "Big Five" personality traits and pair-programming performance; the earlier [Wall2009] found pairs whose members differed in a trait communicated more.

### 9.7 Take Notes…Together?
- Note-taking improves retention [Aike1975, Boha2011]. It is real-time **elaboration** (§5.1): organising and reflecting on material as it arrives raises the chance it reaches long-term memory in usable form. [Boha2011]: the gain is greatest at deeper levels of understanding.
- Experience and some recent research suggest **collaborative** note-taking is also effective [Ornd2015, Yang2015], even though note-taking on a computer is generally less effective than pen and paper [Muel2014].
- First-timers sometimes find it distracting ("one more thing" to watch). Arguments for it:
  - People compare what they think they heard with what others heard, filling gaps and correcting misconceptions immediately.
  - Advanced learners get something useful to do (leading the note-taking) instead of checking social media, which keeps them engaged and frees less advanced learners to focus on the new material. It also helps the whole class, because "boredom is infectious" (§9.7): when a few people check out, those around them follow.
  - Learner-written notes are usually more useful than teacher-prepared notes, because learners record what they actually found new rather than what the teacher predicted would be new.
  - Glancing at the notes shows the teacher when the class missed or misunderstood something important.
- Tools: **Etherpad** (easy to see who wrote what) or **Google Docs** (scales better, allows images). Either way, classes also use it to share code snippets and small datasets, and learners paste their work in to show teachers.
- **Name-list trick**: when you want everyone to answer a question or contribute a solution, paste a list of everyone's names into the doc. This stops everyone editing the same few lines at once.
- Wilson's view: benefits outweigh costs. **But** if you work with a group only once, follow §9.12 and stick to what they're used to.

### 9.8 Sticky Notes
- Wilson's favourite tool, valued for "versatility, portability, stickability, foldability, and subtle yet alluring aroma" (§9.8, citing [Ward2015]).

#### 9.8.1 As Status Flags
- Give each learner two notes of different colours (e.g. orange and green). They can be held up for votes, but their main use is as **status flags**: green on the laptop = "done, please check"; orange = "I have a problem, need help".
- Better than raised hands because it is **more discreet** (so people actually do it), they **can keep working** while flagged, and the teacher sees the **state of the whole class** at a glance from the front.

#### 9.8.2 To Distribute Attention
- Each learner writes their name on a note and sticks it on their laptop. Each time the teacher calls on them or answers their question, the note comes down. When all are down, everyone puts theirs back up.
- This shows the teacher whom they haven't spoken with recently, avoiding the unconscious trap of interacting only with the most extroverted learners. It also shows learners that attention is distributed fairly, so being called on doesn't feel like being picked on.

#### 9.8.3 As Minute Cards
- Before each break, learners spend a minute writing one positive thing on the green note (e.g. something learned that will be useful) and on the red note one thing that was too fast, too slow, confusing, or irrelevant, or a question not yet answered or something still confusing.
- During the break, teachers review and cluster the notes. In a few minutes they see what learners enjoy, what confuses them, what problems they're having, and what questions are unanswered.

### 9.9 Never a Blank Page
- Three ways to structure a workshop: **independent exercises**, a **single extended example** developed in stages, or a **mix**.
  - Independent exercises: people who fall behind can re-synchronise easily, and developers can add, remove, or rearrange material at will.
  - Extended example: shows how the pieces fit together, giving more opportunity to **integrate** knowledge.
- Whichever you choose, **novices should never start an exercise from a blank page or screen**: they find it intimidating or bewildering. Instead ask them to add a few lines to, or modify, the example you've built through live coding, or paste starter code into the shared notes for them to extend.
- Modifying existing code gives structure and is closer to real-life work.
- **Caveat:** starter code can *increase* cognitive load if learners try to understand all of it first. Java's `public static void main()` or a block of Python imports may make sense to you but is extraneous load to them (Ch 4).

### 9.10 Setting Up Your Learners
- Adult learners say it matters to them to **leave with their own computers set up for real work**. So Wilson "strongly recommend[s]" being prepared to teach on **Linux, macOS, and Windows**, even though requiring one platform would be simpler (§9.10).
- Put **detailed setup instructions for all three** on the class website, and **email a reminder a couple of days before** the workshop.
- Some people will still arrive without the right software (no time, or setup problems). **Have everyone run a simple command on arrival and show a teacher the result**; helpers and other learners assist those in trouble.
- Box "Common Denominators": with mixed operating systems, avoid OS-specific features and **point out any you do use** (e.g. shell command options differ between macOS and Linux; Windows "minimize window" controls and behaviour differ).
- **Virtual machines / Docker** can reduce installation problems but bring their own: older or smaller machines are too slow; learners struggle switching between two sets of shortcuts (e.g. copy/paste); even competent practitioners get confused about what is happening where.
- **Browser-based tools** avoid installation, but make the class dependent on institutional WiFi (of highly variable quality) and don't satisfy adults' wish to leave with a working machine. Wilson notes this matters less as cloud-native development tools (e.g. Glitch) spread.

### 9.11 Other Teaching Practices
"None of the smaller practices described below are essential, but all will improve lesson delivery" (§9.11). Like chess and marriage, success in teaching is often slow, steady progress.

- **Start with introductions.** Teachers give a brief intro conveying their capacity to teach the material, accessibility and approachability, desire for student success, and enthusiasm. Tailor it to the learners' level: show competence without seeming too advanced, and show you can relate to them. Keep showing interest in their progress and enthusiasm for the topics throughout. Learners introduce themselves too, preferably out loud; at minimum everyone adds their name to the shared notes. It's good for everyone at a site to know who's in the group; this can be done during setup before the start.
- **Set up your own environment.** As well as the software and network access to the note-taking tool, have water, tea, or coffee. It keeps your throat lubricated, but its real purpose is an **excuse to pause for a couple of seconds and think** when asked a hard question or when you lose your place. Bring whiteboard pens and other travel-kit items (appendix "Checklists for Events").
- **Avoid homework in all-day formats.** People who've programmed all day are tired; homework makes them start the next day tired too.
- **Don't touch the learner's keyboard.** Fixing it yourself can seem like magic even if you narrate. Talk them through it instead: slower, but more likely to stick.
- **Repeat the question** before answering: it checks you understood, lets people who didn't hear catch it, and matters especially for recordings and broadcasts (the mic usually doesn't pick up the audience). It also gives you a chance to redirect to something you're more comfortable answering "if need be…" (§9.11).
- **One up, one down.** At the end of each day, learners alternately give one positive and one negative point about the day, **without repeating** anything already said. The rule forces people to say things they otherwise wouldn't: "once all the 'safe' feedback has been given, participants will start saying what they really think" (§9.11). Minute cards are anonymous and one-up-one-down is not; each has strengths and weaknesses, and using both aims to get the best of both.
- **Have learners make predictions.** People learn more from demonstrations if asked to predict what will happen [Mill2013]. This fits live coding naturally: after changing a few lines, ask someone what will happen when it runs. (See §8.4.)
- **Setting up tables.** If you control the layout, use **flat (dinner-style) seating**, not banked (theatre-style), so you can reach learners and they can pair (the text cites §9.5; the pairing material is §9.6). In-floor power outlets avoid cords across the floor (safer) but are rare. Ensure seats have good back support (people sit for long periods) and an unobstructed view of the screen.
- **Cough drops.** Talking all day irritates the epithelial cells of the larynx and pharynx: you get hoarse and more vulnerable to infection (part of why people catch colds after teaching). Keep your throat lined by using cough drops "early and often" (§9.11). Good ones also mask coffee breath.
- **Think-pair-share.** Each person thinks individually and jots notes; pairs explain their ideas to each other and possibly merge them or pick the more interesting ones; a few pairs present to the whole group. It works because, paraphrasing Oscar Wilde's Lady Windermere, people often can't know what they think until they hear themselves say it. Pairing gives insight into one's own thinking and forces gaps and contradictions to be resolved before facing the larger group.
- **Morning, noon, and night.** [Smar2018]: students whose classes and work are scheduled out of line with their natural body clocks do worse (a morning person in night classes, or vice versa). Usually impossible to accommodate in small groups, but larger ones should **stagger start times**, which also helps people with childcare and other time constraints.
- **Humor.** Use sparingly. Written jokes get less funny with each re-reading; spontaneous humour works better but can go wrong, since a joke among friends may be a serious political issue to your audience. Never make jokes at the expense of any group, or of anyone except possibly yourself.

### 9.12 Limit Innovation
- Each technique in this chapter improves classes, but **don't adopt them all at once**. It may even be best to use none, especially when you're with the learners only briefly.
- Reason: every new practice adds cognitive load. Learners must absorb the content *and* learn a new way to learn.
- Repeated contact: introduce **one new technique every few lessons**. One-day workshop: be **conservative**.

### 9.13 Exercises
(Summarised under Practice exercises below; two of them introduce frameworks summarised here.)
- **Credibility** [Fink2013]: teachers are credible to learners through **competence** (knowledge of the subject, shown by explaining complex ideas or referencing others' work), **trustworthiness** (having the student's best interests in mind, shown by individualised feedback, rational explanations of grading, and treating all students the same), and **dynamism** (excitement about the subject; Ch 8).
- **Four levels of training evaluation** [Kirk1994]: **Reaction** (how learners felt), **Learning** (how much they learned), **Behavior** (how much they changed their behaviour), **Results** (how those changes affected their output or their group's).
- **Objections and counter-objections** (premise from §7.5: learners' answers on whether a class was useful don't correlate with how much they learned): four proposals and their rebuttals.
  - Ask whether they'd recommend it to friends → no more meaningful than asking how they feel.
  - Exam at the end → end-of-day knowledge poorly predicts recall two or three months later, and any final exam changes the class's feel because school conditions learners to see exams as high-stakes.
  - Exam two or three months later → practically impossible with free-range learners, and skewed because those who got little out of it are less likely to take part.
  - Check whether they keep using what they learned → how, since "installing spyware on learners' computers is frowned upon" (§9.13)?

## Rules
- **CLS-1**: Respond to a Code of Conduct violation in proportion to its severity and apparent intent: warn, request an apology, and/or expel. *Why:* a code is meaningless without enforcement, and reporting already burdens targets. *Check:* Does the incident plan name a graded set of responses? (§9.1)
- **CLS-2**: Act on Code of Conduct violations in front of witnesses. *Why:* people tone down hostility before an audience, and a witness prevents later conflicting claims about who said what. *Check:* Does the plan require a second person present? (§9.1)
- **CLS-3**: If you expel someone, tell the class you did so and why. *Why:* it prevents exaggerated rumours and signals that safety is taken seriously. *Check:* Does the plan include a class announcement? (§9.1)
- **CLS-4**: Report any incident to the class host as soon as possible. *Why:* the host must know, and it supports the reporting and enforcement procedure. *Check:* Is a host contact listed in the run-sheet? (§9.1)
- **CLS-5**: Use peer instruction: a brief intro, then an MCQ that probes misconceptions (not recall), a vote, and branching (all right: move on; all the same wrong answer: address it; mixed: 2–4-person discussion and re-vote), then a final explanation. *Why:* it scales one-to-one mentoring; discussion improves understanding even when no one in the group knew the answer [Mazu1996, Crou2001, Port2013, Port2016, Smit2009]. *Check:* Does each question's wrong answers map to known misconceptions? Is the branching decided by the vote? (§9.2)
- **CLS-6**: Make the first peer-instruction vote public and committed. *Why:* it prevents after-the-fact rationalising and triggers hypercorrection (§5.1). *Check:* Are votes visible (hands, cards, sticky notes) before discussion? (§9.2)
- **CLS-7**: Choose an explicit co-teaching model, and use team teaching for day-long workshops. *Why:* co-teaching adds lateral transfer; team teaching rests voices and prevents end-of-day snapping and fumbling. *Check:* Does the plan name the model and the handover points? (§9.3)
- **CLS-8**: Recruit helpers (trainee teachers, host tech staff, alumni, advanced learners) for setup, exercise support, room-watching, and monitoring shared notes. *Why:* it extends individual attention; advanced learners also stay engaged. *Check:* Is there a helper-to-learner plan with assigned duties? (§9.3)
- **CLS-9**: Co-teachers spend 2–3 minutes before each class confirming who teaches what and agreeing hand signals (too fast, speak up, learner needs help, bathroom break). *Why:* it avoids overlap and allows silent coordination. *Check:* Does the run-sheet have a pre-class sync slot and a signal list? (§9.3)
- **CLS-10**: Each co-teacher teaches for at least 10–15 minutes per stretch, and does not present material the partner will cover next. *Why:* frequent interleaving distracts students, and pre-empting the partner causes repetition. *Check:* Are any segments shorter than 10 minutes? Have teachers checked each other's next segments? (§9.3)
- **CLS-11**: The non-teaching partner never interrupts, corrects, elaborates, or adds anecdotes (leading questions excepted) and stays engaged: monitor notes, spot strugglers, note feedback. *Why:* interruptions distract and undermine; engagement adds value. *Check:* What is the off-duty teacher assigned to do? (§9.3)
- **CLS-12**: Co-teachers debrief together after each class. *Why:* shared misery lessens and shared joy grows; it sustains the partnership. *Check:* Is there a post-class debrief slot? (§9.3)
- **CLS-13**: Assess prior knowledge of free-range learners in advance with questions about how easily they could do specific tasks, never 1–5 self-ratings, phrased so they don't intimidate. *Why:* learners treat tests as summative and may drop out; self-ratings are distorted by Dunning-Kruger [Krug1999]. *Check:* Does any question ask for a numeric self-rating or look like an exam? (§9.4)
- **CLS-14**: Follow up with people who don't answer the pre-assessment, to find out why. *Why:* non-response may mean the survey scared them off. *Check:* Is a follow-up step scheduled? (§9.4)
- **CLS-15**: Advertise the workshop's level before sign-up by listing topics and showing sample exercises. *Why:* it reduces the lost-third/bored-third split. *Check:* Does the sign-up page contain topics and at least a few example exercises? (§9.5)
- **CLS-16**: Provide extra self-paced exercises for fast finishers, and ask advanced learners to help neighbours. *Why:* it prevents boredom, and explaining deepens their own understanding. *Check:* Does every section have stretch exercises? (§9.5)
- **CLS-17**: Watch for learners falling behind and intervene early. *Why:* it catches them before frustration makes them give up. *Check:* Is there a mechanism (status flags, helpers) to spot strugglers? (§9.5, §9.8.1)
- **CLS-18**: Accept that one lesson can't fit everyone: don't slow the whole class for a few, or go deep on side topics for one. *Why:* it serves the majority. *Check:* Are individual needs handled through helpers or extra exercises, not whole-class pace changes? (§9.5)
- **CLS-19**: Expect false beginners and don't take pre-test scores as fixed level; treat their head start as preparatory privilege when designing assessment. *Why:* same intercept, steeper slope; fairness depends on what you assess [Marg2010]. *Check:* Does the plan anticipate fast movers who scored as beginners? (§9.5)
- **CLS-20**: When pairing, pair everyone, switch driver/navigator three or four times an hour, rotate seats regularly, demonstrate active navigating, and warn that speed-focused pairs share less fairly. *Why:* avoids singling out strugglers or letting one personality dominate [Lewi2015]; pairing improves success, confidence, and equity [McDo2006, Hank2011, Port2013, Cele2018]. *Check:* Does the plan include a pairing demo and timed role switches? (§9.6)
- **CLS-21**: Use flat (dinner-style) seating with good back support, clear sightlines, and safe power, wherever you control the room. *Why:* it supports pairing and lets helpers reach learners. *Check:* Has the room layout been confirmed with the host? (§9.6, §9.11)
- **CLS-22**: Run a shared-notes document (Etherpad or Google Docs) for notes, code snippets, data, and learner work, and glance at it while teaching. *Why:* it fills gaps, engages advanced learners, yields notes on what was actually new, and reveals misunderstandings [Ornd2015, Yang2015]. *Check:* Is the doc created and linked before the event? Is someone assigned to monitor it? (§9.7)
- **CLS-23**: When everyone must answer in the shared doc, paste a list of all names first. *Why:* it prevents edit collisions on the same lines. *Check:* Does the exercise prompt include a name list? (§9.7)
- **CLS-24**: Give each learner two coloured sticky notes and use them as status flags (done / need help). *Why:* discreet, lets learners keep working, and shows class state at a glance. *Check:* Are sticky notes on the event checklist and explained at the start? (§9.8.1)
- **CLS-25**: Use name sticky notes to spread your attention evenly: take a note down when you interact with that learner, reset when all are down. *Why:* avoids favouring extroverts; being called on doesn't feel like being picked on. *Check:* Can the teacher name who hasn't been engaged yet? (§9.8.2)
- **CLS-26**: Collect minute cards (one positive, one negative/question) before each break, and cluster them during the break. *Why:* fast, anonymous, continuous formative feedback. *Check:* Does each break in the schedule have a minute-card slot and a review task? (§9.8.3)
- **CLS-27**: Never start novices on an exercise with a blank page: have them extend live-coded code or starter code, keeping starter code free of unexplained boilerplate. *Why:* blank pages intimidate; modifying is realistic; but starter code can add extraneous load. *Check:* Does each exercise ship with a starting point? How much of it is boilerplate learners can't yet read? (§9.9)
- **CLS-28**: Choose deliberately between independent exercises (easy re-sync, easy to edit) and a single extended example (integration), or mix them. *Why:* each has distinct benefits. *Check:* Does the design state which and why? (§9.9)
- **CLS-29**: Support Linux, macOS, and Windows: post per-platform setup instructions, send a reminder email a couple of days before, and check setup on arrival with a simple command, with helpers fixing failures. *Why:* adults want to leave with a working machine, and some will always arrive unprepared. *Check:* Are all three platforms covered, and is there a check command in the opening run-sheet? (§9.10)
- **CLS-30**: Avoid OS-specific features with mixed platforms, or point them out. Weigh VMs/Docker (slow machines, shortcut confusion) and browser-based tools (WiFi dependence, no working local setup) before adopting them. *Why:* each option has costs. *Check:* Does the plan record the setup approach and its known failure modes? (§9.10)
- **CLS-31**: Open with teacher introductions that convey competence (pitched at learners' level), approachability, desire for their success, and enthusiasm; have learners introduce themselves (at least names in the shared notes). *Why:* builds credibility and group awareness [Fink2013]. *Check:* Is there an intro slot for both teachers and learners? (§9.11, §9.13)
- **CLS-32**: Keep a drink at hand (and cough drops) to buy thinking time and protect your voice. *Why:* a sip is a natural pause; cough drops keep the throat lined against hoarseness and infection. *Check:* Are these on the travel kit list? (§9.11)
- **CLS-33**: Don't set homework in all-day formats. *Why:* tired learners start the next day tired. *Check:* Is there any after-hours assignment in a multi-day full-day schedule? (§9.11)
- **CLS-34**: Don't touch the learner's keyboard; talk them through the fix. *Why:* fixing it yourself looks like magic and doesn't stick. *Check:* Are helpers briefed on hands-off support? (§9.11)
- **CLS-35**: Repeat each audience question before answering. *Why:* confirms understanding, lets everyone (and recordings) hear it, and allows redirection. *Check:* In a recording, are questions audible or repeated? (§9.11)
- **CLS-36**: End each day with one-up-one-down (alternating positive and negative, no repeats), alongside anonymous minute cards. *Why:* the no-repeat rule surfaces candid feedback after the "safe" points are used up; the two modes complement each other. *Check:* Does the day end with a feedback round? (§9.11)
- **CLS-37**: Ask learners to predict outcomes before demonstrations. *Why:* people learn more from demonstrations when they predict first [Mill2013]. *Check:* Are prediction prompts placed before runs? (§9.11, §8.4)
- **CLS-38**: Use think-pair-share for open questions: think alone and note, explain in pairs and merge, a few pairs present. *Why:* people discover what they think by saying it; pairs resolve gaps before facing the group. *Check:* Do discussion prompts have the three phases? (§9.11)
- **CLS-39**: For larger groups, stagger start times to fit different body clocks and caregiving constraints. *Why:* misaligned schedules lower performance [Smar2018]. *Check:* Does a large event offer more than one start time? (§9.11)
- **CLS-40**: Use humour sparingly and never at the expense of any group or person other than yourself. *Why:* jokes can land as serious political issues for some learners. *Check:* Do scripted jokes target anyone? (§9.11)
- **CLS-41**: Limit innovation: in short workshops stay with familiar practices; with repeated contact add at most one new technique every few lessons. *Why:* each new practice adds cognitive load, because learners must learn a new way to learn. *Check:* How many techniques new to these learners does the plan introduce in one session? (§9.12, §9.7)
- **CLS-42**: Run events from checklists (scheduling, setup, start, end, travel kit) that your group customises and maintains. *Why:* useful, especially for onboarding new instructors, though the research is "more nuanced" [Gawa2007, Avel2013, Urba2014]. *Check:* Is there a checklist, and was it updated after the last event? (appendix "Checklists for Events")

## Procedures

### P1. Handling a Code of Conduct violation (§9.1)
1. Judge severity and whether it seemed intentional.
2. Choose a response: warn → request apology → expel (escalate with severity).
3. Act with a witness present (co-teacher, helper, host).
4. If expelling: tell the class that someone was expelled and why (without exaggeration).
5. Contact the host as soon as possible with a description of what happened.
6. Record the incident per your group's reporting procedure.

### P2. Peer instruction cycle (§9.2)
1. Give a brief introduction to the topic.
2. Pose an MCQ whose distractors each reflect a specific misconception.
3. Everyone votes publicly (hands, coloured sticky notes, cards) and commits.
4. Branch:
   - All correct → move on.
   - All the same wrong answer → address that misconception directly.
   - Mixed → groups of 2–4 discuss for several minutes, then re-vote.
5. After the re-vote, reveal and explain the correct answer, with a final round of discussion.
6. Optional check (after [Smit2009]): ask a second, similar question answered individually to confirm real understanding.

### P3. Co-teaching a session (§9.3)
1. Before class (2–3 min): confirm who teaches what, agree hand signals, and (if time) draw a concept map together.
2. Each teacher reviews what the other will teach next and avoids covering it.
3. Teach in stretches of at least 10–15 min.
4. Off-duty teacher: no interruptions (leading questions only), monitor shared notes, watch strugglers, note feedback.
5. At breaks: exchange feedback (the 2×2 grid from Ch 8 helps).
6. After class: congratulate or commiserate.

### P4. Pre-assessing learners (§9.4)
1. Formal setting? Infer from what prerequisites actually covered. Free-range? Send a short questionnaire.
2. Write questions about how easily they could do concrete tasks (not 1–5 self-ratings), with graded, non-judgemental options (see template).
3. Include a motivation question ("Why do you want to take this…?").
4. Keep it short and non-exam-like.
5. Follow up with non-responders.
6. Use the results to adjust level and examples, add stretch exercises, and plan helper placement; watch for false beginners.

### P5. Pair programming in class (§9.6)
1. Arrange flat seating.
2. Demonstrate pairing, showing an active navigator.
3. Put everyone in pairs.
4. Mention [Lewi2015]: racing to finish makes sharing less fair.
5. Signal role switches three or four times per hour.
6. Periodically reseat people (decide based on room logistics and introvert comfort, per "Switching Partners").

### P6. Using sticky notes (§9.8)
1. Hand out two colours per learner at the start (on the event checklist).
2. Explain status-flag meanings: green = done/check me; orange/red = need help.
3. Optionally use name notes to track attention: remove on interaction, reset when all are down.
4. Before each break: one minute of writing, positive on green, negative/question on red.
5. During the break, teachers cluster the notes into what's enjoyed, what's confusing, problems, and unanswered questions.
6. After the break, address the clusters.

### P7. Getting learners set up (§9.10)
1. Choose an approach: native install on all three OSes (default), VM/Docker, or browser-based. Note the trade-offs.
2. Publish detailed per-OS instructions on the workshop site.
3. Email a reminder a couple of days before.
4. On arrival, everyone runs a simple check command and shows a teacher the result.
5. Helpers and other learners fix failures.
6. During teaching, avoid or flag OS-specific behaviour.

### P8. End-of-day feedback (§9.8.3, §9.11)
1. Collect minute cards (anonymous) before breaks during the day.
2. At day's end, run one-up-one-down: go round alternating one positive and one negative point, no repeats allowed.
3. Teachers review both sources and adjust tomorrow's plan.

### P9. Deciding how many new practices to use (§9.12)
1. Count the practices in the plan that these learners haven't met before.
2. One-off or short workshop → be conservative: keep only those essential to the lesson (and for shared notes, stick to what the group already uses).
3. Repeated contact → add one new technique every few lessons.

## Diagnostics
| Symptom (in a lesson, class, or community) | Underlying problem | Fix (rule IDs) |
|---|---|---|
| Rumours spread after a learner was removed | Expulsion not explained to the class | CLS-3 |
| Dispute afterwards over what was said in a CoC incident | No witness | CLS-2, CLS-4 |
| Peer-instruction discussion goes nowhere; question was trivial recall | MCQ doesn't probe misconceptions | CLS-5 |
| Learners claim they "misread the question" after the reveal | Private or uncommitted voting | CLS-6 |
| Co-teachers talk over or correct each other mid-lesson | No rules for the off-duty teacher | CLS-11 |
| Second teacher repeats what the first just covered, or pre-empts the next segment | No pre-class sync or look-ahead | CLS-9, CLS-10 |
| Teachers exhausted and snappy by late afternoon | Solo teaching all day | CLS-7 |
| Few sign-ups or drop-off after the pre-survey | Survey felt like an exam | CLS-13, CLS-14 |
| Survey shows everyone "4/5" yet many are lost | Self-rating plus Dunning-Kruger | CLS-13 |
| A third of the class lost, a third bored | Mixed abilities unmanaged | CLS-15, CLS-16, CLS-17, CLS-18 |
| "Beginners" racing ahead after an hour | False beginners | CLS-19, CLS-16 |
| One partner types the whole session; the other watches | No role switching or navigator demo | CLS-20 |
| Only struggling learners paired, and they feel singled out | Selective pairing | CLS-20 |
| Helpers can't reach learners; pairs can't share screens | Theatre-style seating | CLS-21 |
| Everyone overwrites the same lines in the shared doc | No name list | CLS-23 |
| Advanced learners on social media, boredom spreading | Nothing for them to do | CLS-16, CLS-22, CLS-8 |
| Learners stuck silently, unwilling to raise hands | No discreet help signal | CLS-24 |
| Teacher only ever answers the same few vocal learners | Unequal attention | CLS-25 |
| Teacher learns of confusion only at the end-of-course survey | No continuous feedback | CLS-26, CLS-36 |
| Novices freeze at the start of an exercise | Blank page | CLS-27 |
| Learners stall reading starter code full of imports | Starter code adds extraneous load | CLS-27 |
| First hour lost to installation problems | No pre-workshop instructions, reminder, or arrival check | CLS-29 |
| macOS users' commands fail where Linux users' work | OS-specific options not flagged | CLS-30 |
| Learner can't reproduce a fix the helper typed | Helper touched the keyboard | CLS-34 |
| Recording has answers without questions | Questions not repeated | CLS-35 |
| End-of-day feedback is all bland praise | No no-repeat alternating round | CLS-36 |
| Day-2 learners tired and behind | Homework after an all-day session | CLS-33 |
| Joke offends part of the room | Humour at a group's expense | CLS-40 |
| One-day workshop feels chaotic: learners juggling notes doc, flags, pairing, clickers | Too many new practices at once | CLS-41 |
| Teacher hoarse by afternoon or sick after the workshop | No voice care | CLS-32, CLS-7 |

## Templates and checklists

### Checklists for Events (appendix "Checklists for Events", every item kept)
Preamble: [Gawa2007] popularised checklists as life-saving; recent studies are "more nuanced" [Avel2013, Urba2014], but Wilson's group still finds them useful, especially when bringing new instructors onto a team. These are used before, during, and after instructor-training events and adapt easily to end-learner workshops. "We recommend that every group build and maintain its own checklists customized for its instructors' and learners' needs."

**Scheduling the Event**
```
[ ] Decide if it will be in person, online for one site, or online for several sites.
[ ] Talk through expectations with the host(s) and make sure that everyone agrees on who is covering travel costs.
[ ] Determine who is allowed to take part: is the event open to all comers, restricted to members of one organization, or something in between?
[ ] Arrange instructors.
[ ] Arrange space, including breakout rooms if needed.
[ ] Choose dates. If it is in person, book travel.
[ ] Get names and email addresses of attendees from host(s).
[ ] Make sure they are added to the registration system.
```

**Setting Up**
```
[ ] Set up a web page with details on the workshop, including date, location, and a list of what participants need to bring.
[ ] Check whether any attendees have special needs.
[ ] If the workshop is online, test the video conferencing link.
[ ] Make sure attendees will all have network access.
[ ] Create an Etherpad or Google Doc for shared notes.
[ ] Email attendees a welcome message that includes a link to the workshop home page, background readings, and a description of any prerequisite tasks.
```

**At the Start of the Event**
```
[ ] Remind everyone of the code of conduct.
[ ] Collect attendance.
[ ] Distribute sticky notes.
[ ] Collect any relevant online account IDs.
```

**At the End of the Event**
```
[ ] Update attendance records. Be sure to also record who participated as an instructor or helper.
[ ] Administer a post-workshop survey.
[ ] Update the course notes and/or checklists.
```

**Travel Kit** ("a few things instructors take with them when they travel to teach")
```
[ ] sticky notes
[ ] cough drops
[ ] comfortable shoes
[ ] a small notepad
[ ] a spare power adapter
[ ] a spare shirt
[ ] deodorant
[ ] a variety of video adapters
[ ] laptop stickers
[ ] a toothbrush or some mouthwash
[ ] a granola bar or some other emergency snack
[ ] Eno or some other antacid (because road food)
[ ] business cards
[ ] a printed copy of the notes, or a tablet or other device
[ ] an insulated cup for tea/coffee
[ ] spare glasses/contacts
[ ] a notebook and pen
[ ] a portable WiFi hub (in case the room's network isn't working)
[ ] extra whiteboard markers
[ ] a laser pointer
[ ] a packet of wet wipes (because spills happen)
[ ] USB drives with installers for various operating systems
[ ] running shoes, a bathing suit, a yoga mat, or whatever else you exercise in or with
```

> **Skill note:** Ch 9 practices that a workshop-planner skill could add to a customised version (the book recommends customising): setup instructions for three OSes plus a reminder email a couple of days before (§9.10); an on-arrival setup check command (§9.10); a co-teacher sync and hand signals (§9.3); flat seating confirmed with the host (§9.11); helpers recruited (§9.3); minute-card slots before breaks and a one-up-one-down round at day's end (§9.8.3, §9.11); a follow-up for pre-assessment non-responders (§9.4). These additions are derived from the chapter text, not part of the appendix.

### Pre-Assessment Questionnaire (appendix "Pre-Assessment Questionnaire", every item kept)
Designed to gauge prior knowledge for an introductory **JavaScript** workshop; "You can use it as a starting point for creating a rubric of your own."

```
1. Which of these best describes your previous experience with programming in general?
   ( ) I have none.
   ( ) I have written a few lines now and again.
   ( ) I have written programs for my own use that are a couple of pages long.
   ( ) I have written and maintained larger pieces of software.

2. Which of these best describes your previous experience with programming in JavaScript?
   ( ) I have none.
   ( ) I have written a few lines now and again.
   ( ) I have written programs for my own use that are a couple of pages long.
   ( ) I have written and maintained larger pieces of software.

3. Which of these best describes how easily you could write JavaScript to find the largest number in a list?
   ( ) I wouldn't know where to start.
   ( ) I could struggle through by trial and error with a lot of web searches.
   ( ) I could do it quickly with little or no use of external help.

4. Which of these best describes how easily you could write JavaScript to capitalize all of the titles in a web page?
   ( ) I wouldn't know where to start.
   ( ) I could struggle through by trial and error with a lot of web searches.
   ( ) I could do it quickly with little or no use of external help.

5. Why do you want to take this training course?
   (free text)
```

Design pattern behind it (from §9.4): two experience questions (general, then language-specific) on a four-step scale of concrete descriptions of past work; two task-ease questions on a three-step scale, from a simple core task to a domain-applied task; one open motivation question. No numeric self-ratings, no right/wrong answers.

> **Skill note:** To adapt the questionnaire to another language or domain, keep the structure and swap the language name and the two tasks: one small algorithmic task and one task applied to the learners' domain. Pair it with CLS-14 (follow up non-responders).

### Co-teaching hand signals (§9.3)
```
- "You're going too fast"
- "Speak up"
- "That learner needs help"
- "It's time for a bathroom break"
```

### Peer-instruction decision table (§9.2)
| First vote result | Action |
|---|---|
| All correct | Move on |
| All the same wrong answer | Address that specific misconception |
| Mix of right and wrong | 2–4-person discussion (several minutes) → re-vote → explain |

### Minute card prompt (§9.8.3)
```
GREEN: One thing you've learned that you think will be useful.
RED:   One thing that was too fast, too slow, confusing, or irrelevant
       — or a question that hasn't been answered yet.
```

### Kirkpatrick evaluation levels (§9.13, [Kirk1994])
| Level | Question |
|---|---|
| Reaction | How did the learners feel about the training? |
| Learning | How much did they actually learn? |
| Behavior | How much have they changed their behavior as a result? |
| Results | How have those changes in behavior affected their output or the output of their group? |

### Teacher credibility (§9.13, [Fink2013])
| Dimension | Shown by |
|---|---|
| Competence | Explaining complex ideas; referencing others' work |
| Trustworthiness | Individualised feedback; rational explanation of grading; treating all students the same |
| Dynamism | Excitement about the subject |

## Examples
- **Bloom's 2-sigma** (Ch 9 intro): tutored students beat 98% of lectured students → every classroom technique is a way of approximating individual attention at scale.
- **Avanti learning centre, Kanpur** (§9.2): a video shows group discussion improving understanding in peer instruction.
- **"Vote like Jane"** (§9.2): the worry that re-vote gains are just copying the class star; [Smit2009] ruled it out with an individual follow-up question.
- **Advanced learners as helpers** (§9.3): advanced learners used as helpers both understand peers' problems and stay engaged.
- **Loops** (§9.3): the co-teacher understands how pleased you are to have helped someone understand loops better than anyone else could → debrief together.
- **2 of 40** (§9.5): slowing down for 2 strugglers fails the other 38.
- **Scratch child** (§9.5): a child who did Scratch two years ago scores like a beginner but progresses fast → false beginner, preparatory privilege.
- **Grade 6 pairs** ([Lewi2015], §9.6): speed-focused pairs shared less fairly.
- **Infectious boredom** (§9.7): a few people updating Facebook profiles leads neighbours to check out → give advanced learners note-taking duty.
- **Java `public static void main()` / Python imports** (§9.9): sensible to the teacher, extraneous load to novices.
- **Docker confusion** (§9.10): VMs bring slowness, dual shortcut sets, and "where is this happening?" confusion, even for competent practitioners.
- **Glitch** (§9.10): cloud-native development tools reduce the need to leave with a locally configured machine.
- **Lady Windermere** (§9.11): people often don't know what they think until they hear themselves say it → think-pair-share.

## Evidence and caveats
- **Individual tutoring** [Bloo1984]: +2 standard deviations over lecture (better than 98% of lectured students). Wilson's 2018 aside that AI won't replace instructors "any time soon" is opinion.
- **Peer instruction**: extensively studied [Mazu1996, Crou2001, Port2013]; students value it at first contact and it improves outcomes [Port2016]; discussion gains are real, not copying, even when no group member initially knew the answer [Smit2009]. Public voting's value rests on hypercorrection (§5.1).
- **Co-teaching**: models from [Frie2016]. Benefits (lateral transfer, voice rest, less fatigue) are argued from experience, not measured.
- **Pre-assessment**: risk of scaring off learners is Wilson's experience-based caution. Dunning-Kruger [Krug1999] is cited for self-assessment unreliability.
- **Pair programming**: effective professionally [Hann2009]; in education higher success, better software, more confidence, with extra benefit for underrepresented groups [McDo2006, Hank2011 (some evidence it particularly helps women; notes scheduling and partner-compatibility problems), Port2013, Cele2018 (same learning gains as side-by-side programming, higher satisfaction)]. Equity risk when pairs race [Lewi2015]. Partner switching: opinions are mixed; personality-performance correlation is weak [Hann2010]; differing traits mean more communication [Wall2009]. "Pairs are more homogeneous than individuals" is Wilson's experience.
- **Note-taking**: improves retention [Aike1975, Boha2011]. Collaborative notes: "our experience, and some recent research" [Ornd2015, Yang2015] (hedged). Counter-evidence acknowledged: laptop note-taking is generally worse than pen and paper [Muel2014]. Learners at first may find shared notes distracting.
- **Sticky notes** [Ward2015] is a stationery book cited playfully; the sticky-note practices rest on practitioner experience.
- **Predictions**: [Mill2013] (physics lecture demonstrations).
- **Body clocks**: [Smar2018] (3.4 million LMS logins; "social jet lag" correlates with lower performance).
- **Checklists**: [Gawa2007] popularised them; [Avel2013] and [Urba2014] are "more nuanced" ([Urba2014] found no significant effect of surgical checklists on outcomes in Ontario). Wilson still finds them useful.
- **Learner satisfaction is not learning** (§7.5, used in §9.13): don't rely on "was this useful?" Every alternative (recommend to friends, final exam, delayed exam, usage tracking) has an objection; the book leaves it as an open exercise.
- **Limit innovation** (§9.12): the reasoning is cognitive load; no study is cited.
- **Starter code** (§9.9): helpful structure but a possible source of extraneous load. Both sides stated, with no resolution beyond judgement.
- **Collaborative notes vs limiting innovation**: the benefits outweigh the costs in Wilson's experience, but in a one-off session defer to §9.12.

## Practice exercises
- **Create a Questionnaire** (individual, 20 min): using the Pre-Assessment Questionnaire as a template, write a short questionnaire for a class of your own. What do you most want to know about their background?
- **One of Your Own** (whole class, 15 min): think of a teaching practice not yet described; present to a partner, hear theirs, choose one to present to the group (itself a think-pair-share).
- **May I Drive?** (pairs, 10 min): swap computers with a partner, ideally one on a different OS, and do a simple programming exercise. How frustrating is it, and what does it show about novices' experience?
- **Pairing** (pairs, 15 min): watch a pair-programming video, then pair with a partner, switching driver/navigator every few minutes. How long does it take to find a working rhythm?
- **Compare Notes** (small groups of 3–4, 15 min): compare the notes each person took on this material. What did you find noteworthy that others missed, and vice versa? What did you understand differently?
- **Credibility** (individual, 15 min): using [Fink2013]'s competence/trustworthiness/dynamism, describe one thing you do in each category and one thing you don't but should.
- **Measuring Effectiveness** (individual, 15 min): for each of [Kirk1994]'s four levels (reaction, learning, behavior, results), what do you do now to evaluate your teaching, and what could you do?
- **Objections and Counter-Objections** (think-pair-share, 15 min): answer the objections to four evaluation proposals (recommend to friends; end exam; exam 2–3 months later; track continued use) alone, swap with a partner, then share your best counter-argument with the class.

## Cross-references
- `08-teaching-as-performance.md`: live coding, predictions in live coding, the 2×2 grid, the record-yourself exercise as preparation for co-teaching, skeleton code.
- `10-motivation-and-inclusion.md`: Code of Conduct appendix and why it matters; inclusive humour.
- `05-individual-learning.md`: elaboration (note-taking), hypercorrection (public voting).
- `04-cognitive-load.md`: extraneous load from starter code; why limiting innovation helps.
- `07-programming-pck.md`: novice debugging; learner satisfaction vs learning (§7.5).
- `06-lesson-design.md`: concept maps (co-teacher prep); designing exercises and the extended-example structure.
- `12-exercise-types.md`: MCQs with plausible distractors for peer instruction.
- `11-teaching-online.md`: online and multi-site variants of these practices.
- `13-building-community.md`: helpers and instructor-training pipeline.
- `bibliography.md`: full citations.

## Source map
| Book section | Covered under |
|---|---|
| Ch 9 intro (objectives, [Bloo1984]) | Concepts > Chapter framing; Evidence |
| §9.1 Enforce the Code of Conduct | Concepts §9.1; CLS-1 to CLS-4; P1 |
| §9.2 Peer Instruction (box "Taking a Stand") | Concepts §9.2; CLS-5, CLS-6; P2; decision table |
| §9.3 Teach Together (box "Helping") | Concepts §9.3; CLS-7 to CLS-12; P3; hand signals |
| §9.4 Assess Prior Knowledge | Concepts §9.4; CLS-13, CLS-14; P4 |
| §9.5 Plan for Mixed Abilities (box "False Beginners") | Concepts §9.5; CLS-15 to CLS-19 |
| §9.6 Pair Programming (box "Switching Partners") | Concepts §9.6; CLS-20, CLS-21; P5 |
| §9.7 Take Notes…Together? | Concepts §9.7; CLS-22, CLS-23 |
| §9.8 Sticky Notes (§9.8.1–§9.8.3) | Concepts §9.8; CLS-24 to CLS-26; P6; minute-card prompt |
| §9.9 Never a Blank Page | Concepts §9.9; CLS-27, CLS-28 |
| §9.10 Setting Up Your Learners (box "Common Denominators") | Concepts §9.10; CLS-29, CLS-30; P7 |
| §9.11 Other Teaching Practices (all 13 subsections) | Concepts §9.11; CLS-21, CLS-31 to CLS-40; P8 |
| §9.12 Limit Innovation | Concepts §9.12; CLS-41; P9 |
| §9.13 Exercises | Concepts §9.13; Practice exercises; Kirkpatrick and credibility tables |
| Appendix "Checklists for Events" | Templates > Checklists for Events; CLS-42 |
| Appendix "Pre-Assessment Questionnaire" | Templates > Pre-Assessment Questionnaire; P4 |
