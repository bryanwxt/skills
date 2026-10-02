# A Lesson Design Process

> Source: Greg Wilson, *Teaching Tech Together* (2018), Ch. 6 "A Lesson Design Process" (§6 intro, §6.1–§6.4), appendices "Lesson Design Template" and "Design Notes". Licensed CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/); condensed and restructured for skill use, with quotations marked. Rule IDs use prefix `LES`.

## When a skill needs this
- Designing a new lesson, workshop, or course from scratch (backward design: scope, personas, exercises, outline, overview).
- Reviewing or rewriting learning objectives so they are single-sentence, verb-led, assessable, and pitched at the right Bloom/Fink level.
- Writing or critiquing learner personas for a target audience.
- Auditing an existing lesson for maintainability, or producing the design notes that let someone else maintain it.
- Generating teacher-training activities on lesson design (personas, objectives, subtracting complexity, PRIMM, CRA, lesson-evaluation dimensions).

## Key terms
| Term | Meaning (one line) |
|---|---|
| Backward design | Glossary: "An instructional design method that works backwards from a summative assessment to formative assessments and thence to lesson content." Also called *understanding by design*. |
| Test-driven development (TDD) | Writing tests first to fix what "done" means, then just enough code to pass them, then cleaning up; the analogy for backward design. |
| Teaching to the test | Focusing on getting learners to pass externally set summative tests that drive teacher pay and promotion, rather than on learning. Not the same as backward design. |
| Learner persona | Glossary: a brief description of a typical target learner: general background, what they already know, what they want to do, how the lesson will help them, special needs. |
| Learning objective | What a lesson strives to achieve; written as one sentence with a measurable or verifiable verb and criteria for acceptable performance. |
| Learning outcome | What a lesson actually achieves, i.e. what learners take away. |
| Formative assessment | Assessment during a lesson that tells learner and teacher whether learning is on track. |
| Summative assessment | Assessment at the end that tells whether the desired learning took place; compares outcomes with objectives. |
| Bloom's Taxonomy | Six-level *hierarchical* classification of understanding. Revised form (Ch 6, [Ande2001]): remembering, understanding, applying, analyzing, evaluating, creating. (The book's glossary lists the original 1956 names: knowledge, comprehension, application, analysis, synthesis, evaluation.) |
| Fink's Taxonomy | Six *complementary* (non-hierarchical) categories of learning defined by the change in the learner: foundational knowledge, application, integration, human dimension, caring, learning how to learn [Fink2013]. |
| Maintainable lesson | One that is cheaper to update than to replace (§6.3). |
| Episode | A chunk of teaching that gets learners from one formative assessment to the next; 3–4 per classroom hour. |
| Choral explanations | Caulfield's idea: sites like Stack Overflow succeed by offering many answers per question, each suited to a slightly different questioner (§6.3). |
| Inessential weirdness | Betsy Leondar-Wright's term for unnecessary group habits that alienate non-members (§6.4 exercise). |
| PRIMM | Predict, Run, Investigate, Modify, Make: a sequence for introducing new computing ideas (§6.4 exercise). |
| Concrete-Representational-Abstract (CRA) | Introducing ideas by physical manipulation, then images, then symbols; mainly used with younger learners (§6.4 exercise). |

## Concepts

### §6 (introduction) — Why backward design
- **The usual (forward) process** Wilson describes: someone asks you to teach a topic you have not thought about in years; you write slides explaining what you know; after two or three weeks you invent an assignment based on what you have taught so far; you repeat that several times; you stay up late writing a final exam and promise to be more organized next time.
- **TDD as the model.** Programmers using TDD write tests first, then just enough code to pass, then clean up. TDD works because:
  - writing tests forces you to state exactly what you are trying to accomplish and what "done" looks like ("it's easy to be vague when using a human language … much harder to be vague in Python or R");
  - it reduces endless polishing;
  - it reduces confirmation bias: someone who has not yet written the program tests it more objectively than someone who has just spent hours on it and "really, really wants to be done".
- **Backward design** applies the same idea to lessons. Developed independently in [Wigg2005, Bigg2011, Fink2013] and summarized in [McTi2013]. Simplified steps (§6 intro):
  1. **Brainstorm** a rough idea of what to cover, how, what problems or misconceptions to expect, and what is *not* included. You may also draw concept maps here.
  2. **Create or recycle learner personas** to work out who you are teaching and what will appeal to them. (This can come first, before brainstorming.)
  3. **Create formative assessments** that let learners practise what they are learning and tell both sides whether they are progressing and where to focus.
  4. **Order the formative assessments** by complexity and dependency to produce a course outline.
  5. **Write just enough** to get learners from one formative assessment to the next. Each classroom hour then has three or four such episodes.
- **What it buys you:** teaching stays focused on its objectives, and learners never meet anything on the final exam that the course did not prepare them for.
- **Not "teaching to the test".** In backward design teachers set goals to help design the lesson, and "may never actually give the final exam that they wrote". In teaching to the test, an external authority sets assessment criteria for all learners regardless of their situation, and the results affect teachers' pay and promotion. That gives teachers an incentive to focus on passing rather than learning.
- **Box "Measure…And Then?":** [Gree2014] argues that a focus on measurement appeals to those who set the tests, but is unlikely to improve outcomes unless teachers also get support to improve based on the results. That support is often missing because large organizations value uniformity over productivity [Scot1998]. Wilson returns to this in Chapter 8.
- **Iterative in practice, sequential on paper.** Lesson design is almost never done in sequence: you may change what you want to teach while writing an MCQ, or rethink the audience once you have an outline. Still, the notes you leave behind should present things in the order above, because that makes it easier for whoever uses or maintains the lesson to retrace your thinking. The same "rewriting of history" is useful in software design and other fields [Parn1986] (bib: "a rational design process is less important than looking as though you had").
- The book's own design notes (appendix "Design Notes", called Appendix M in the text) were produced this way; Wilson says the finished book matches the plan "pretty closely", with a few things added, dropped, or rearranged.

### §6.1 Learner Personas
- Write **two or three** personas to work out who the audience is. The technique comes from user interface designers, who write short profiles of typical users.
- **Five parts:**
  1. the person's general background;
  2. what they already know;
  3. what *they* think they want to do (as opposed to what someone who already understands the subject thinks they need);
  4. how the course will help them;
  5. any special needs they might have.
  The parts can be rearranged to read more naturally, as in the personas of §1.1.
- **Worked persona (weekend workshop for college students), Jorge:**
  1. Background: just moved from Costa Rica to Canada to study agricultural engineering; joined the college soccer team; looking forward to learning ice hockey.
  2. Prior knowledge: beyond Excel, Word, and the Internet, his biggest computing experience is helping his sister build a WordPress site for the family business.
  3. What he wants: he measures soil properties with a handheld device that sends text-format logs to his computer. Now he opens each file in Excel, crops the first and last points, and calculates an average.
  4. How the workshop helps: it will show him how to write a small Python program to read the data, select the right values from each file, and calculate the statistics.
  5. Special needs: reads English well, but sometimes struggles to follow spoken conversation, especially with a lot of new jargon.
- **Box "A Gentle Reminder": "you are not your learners."** You may be younger (if teaching seniors) or wealthier (able to download videos without giving up a meal to pay for bandwidth), and you almost certainly know more about technology. Don't assume you know what they need or will understand: ask them, and listen to the answer. "It's only fair that learning should go both ways."
- **Shared persona sets.** Rather than write new personas for each lesson, teachers commonly create and share a handful covering everyone they are likely to teach, then pick a few for each piece of material. The names then become design shorthand: "Would Jorge understand why we're doing this?", "What installation problems would Jorge face?"
- **Either order works.** You can brainstorm the content and then decide whom you are helping, or pick an audience and brainstorm their needs. Either way, [Guzd2016] advises:
  - Connect to what learners know.
  - Keep cognitive load low.
  - Use authentic tasks (§10.1).
  - Be generative and productive.
  - Test your ideas rather than trusting your instincts.
- **One size won't fit all.** [Alha2018] reported better learning outcomes and student satisfaction in a course for students from varied academic backgrounds that let them choose among domain-related assignments. It is extra work to set up and grade, but manageable if the projects are open-ended (so they can be reused) and the load is shared with other teachers (§6.3). Building courses for science students around topics as diverse as music, data science, and cell biology also improves outcomes [Pete2017, Dahl2018, Ritz2018].

### §6.2 Learning Objectives
- Formative and summative assessments help teachers decide what to teach. To communicate that to learners and other teachers, a course description should also have **learning objectives**, so everyone shares the same understanding of what a lesson should accomplish.
- **Vagueness example, "understand Git".** It could mean any of the following, each needing a very different lesson:
  - learners can describe three scenarios where version control like Git beats file-sharing tools like Dropbox, and two where it is worse;
  - learners can commit a changed file to a Git repository using a desktop GUI tool;
  - learners can explain what a detached HEAD is and recover from it using command-line operations.
- **Box "Objectives vs. Outcomes":** "A learning objective is what a lesson strives to achieve. A learning outcome is what it actually achieves." Summative assessment compares the two.
- **Definition (§6.2):** "A learning objective is a single sentence describing how a learner will demonstrate what they have learned once they have successfully completed a lesson." It has a measurable or verifiable verb that says what the learner will do, and it specifies the criteria for acceptable performance. This may feel restrictive at first, but it gives clear guidelines for both teaching and assessment, and learners appreciate clear expectations.
- **Improving a poor objective, step by step:**
  1. "The learner will be given opportunities to learn good programming practices." Describes the lesson's *content*, not the attributes of successful students.
  2. "The learner will have a better appreciation for good programming practices." No active verb, no level of learning, and the subject has no context and is not specific.
  3. "The learner will understand how to program in R." Starts with an active verb, but doesn't define the level of learning, and the subject is still too vague to assess.
  4. "The learner will write one-page data analysis scripts to read, filter, summarize, and print results for tabular data using R and R Studio." Active verb, defined level of learning, and enough context that outcomes can be assessed.
- **Bloom's Taxonomy.** First published in 1956 and revised at the turn of the century [Ande2001], it is the most widely used framework for discussing levels of understanding. The revised form has six hierarchical categories:

  | Level | Definition (§6.2) | Typical verbs |
  |---|---|---|
  | Remembering | Exhibit memory of previously learned material by recalling facts, terms, basic concepts, and answers. | recognize, list, describe, name, find |
  | Understanding | Demonstrate understanding of facts and ideas by organizing, comparing, translating, interpreting, giving descriptions, and stating main ideas. | interpret, summarize, paraphrase, classify, explain |
  | Applying | Solve new problems by applying acquired knowledge, facts, techniques and rules in a different way. | build, identify, use, plan, select |
  | Analyzing | Examine and break information into parts by identifying motives or causes; make inferences and find evidence to support generalizations. | compare, contrast, simplify |
  | Evaluating | Present and defend opinions by making judgments about information, validity of ideas, or quality of work based on a set of criteria. | check, choose, critique, prove, rate |
  | Creating | Compile information together in a different way by combining elements in a new pattern or proposing alternative solutions. | design, construct, improve, adapt, maximize, solve |

- **Caveat on Bloom's:** [Masa2018] found that even experienced educators have trouble agreeing on how to classify a question or idea by Bloom's levels. Most introductory programming material fits the **first four levels**. Only after mastering it can learners start evaluating and creating. Willingham: people can't think without something to think about [Will2010].
- **Fink's Taxonomy** [Fink2013] defines learning by the change it is meant to produce in the learner. It also has six categories, but they are **complementary, not hierarchical**:

  | Category | Meaning (§6.2) | Typical verbs |
  |---|---|---|
  | Foundational Knowledge | understanding and remembering information and ideas | remember, understand, identify |
  | Application | skills, critical thinking, managing projects | use, solve, calculate, create |
  | Integration | connecting ideas, learning experiences, and real life | connect, relate, compare |
  | Human Dimension | learning about oneself and others | come to see themselves as, understand others in terms of, decide to become |
  | Caring | developing new feelings, interests, and values | get excited about, be ready to, value |
  | Learning How to Learn | becoming a better student | identify source of information for, frame useful questions about |

- **Fink-based example, introductory HTML/CSS course.** "By the end of this course, learners will be able to:"
  1. Explain the difference between markup and presentation, what CSS properties are, and how CSS selectors work.
  2. Write and style a web page using common tags and CSS properties.
  3. Compare and contrast authoring with HTML and CSS to authoring with desktop publishing tools.
  4. Identify issues in sample web pages that would make them difficult for the visually impaired to interact with, and provide appropriate corrections.
  5. Explain the role that JavaScript plays in styling web pages and want to learn more about how to use it.

> **Skill note:** The book does not label each HTML/CSS objective with its Fink category. A plausible reading: 1 = foundational knowledge, 2 = application, 3 = integration, 4 = human dimension (understanding others' needs) plus application, 5 = foundational knowledge plus caring ("want to learn more"). Classifying these by Bloom's level is a §6.4 exercise, so treat any labelling as open to discussion. [Masa2018] shows experts disagree too.

### §6.3 Maintainability
- **Definition:** a lesson is maintainable "if it's cheaper to update it than to replace it." Three factors decide this:
  1. **How well the design is documented.** If the maintainer doesn't know or remember what the lesson is meant to achieve, or why topics come in a particular order, updating takes longer. Capturing those decisions is one reason to use the backward design process.
  2. **How easily collaborators can work together technically.** Teachers usually email PowerPoint files or use shared drives. Google Docs and wikis are a big improvement, since many people can edit and comment on the same document. Version control such as GitHub is a further advance: any number of people work independently, then merge changes in a controlled, reviewable way. But version control has a long, steep learning curve and still doesn't handle common office formats.
  3. **How willing people are to collaborate.** This is the most important factor in practice. The tools for a "Wikipedia for lessons" have existed for twenty years, but most teachers still don't write and share lessons that way, even though commons-based lesson development and maintenance works very well (§13.4 and §C.3).
- **Why teachers don't use sharing sites:** [Leak2017] interviewed 17 computer science teachers and found mostly operational reasons. Teachers said sites need:
  - landing pages that ask "what is your current role?" and "what course and grade level are you interested in?";
  - all resources displayed in context, since visitors may be new teachers still connecting the dots;
  - anonymous posting on discussion forums, to reduce the fear of looking foolish in front of peers.
- **Remix, not co-author (tentative).** Teachers don't collaborate at scale, but they do remix: they find others' material online or in textbooks and rework it. So the root problem may be a flawed analogy. Lesson development may be less like writing a Wikipedia article or open source software and "perhaps … more like sampling in music."
- If so, whole lessons may be the wrong unit for sharing, and collaboration might take hold on smaller pieces. This fits Caulfield's theory of **choral explanations**: Stack Overflow succeeds because each question gets a chorus of answers, each best for a slightly different questioner. "If Caulfield is right," tomorrow's lessons may include guided tours of community-curated Q&A repositories for learners at very different levels. (Wilson frames this as speculation.)

### §6.4 Exercises
Summarized under **Practice exercises** below. Several introduce design techniques found nowhere else in the chapter (subtracting complexity, inessential weirdness, PRIMM, [Mart2017] lesson dimensions, CRA). These are captured in **Procedures** and **Templates and checklists**.

### Appendix "Lesson Design Template"
- **Why a template:** "Designing a good course is as hard as designing good software." The template:
  - lays out a step-by-step progression so you know what to think about in what order;
  - provides **spaced deliverables**, so you can re-scope or redirect without too many unpleasant surprises;
  - wastes no effort, because everything from Step 2 onward goes into the final course;
  - makes you write sample exercises early, so you can check that everything you want students to do actually works.
- It is backward design [Wigg2005, Bigg2011, Fink2013], slimmed down by removing steps about curriculum guidelines and institutional requirements.
- Steps are described in increasing detail, but the process "is always iterative": you will often revise earlier work after answering a later question or finding your plan won't work as expected.
- The five steps and deliverables are in **Procedures**, P1.

### Appendix "Design Notes"
The book's own backward-design record (the text calls it Appendix M). It shows every stage of the template applied to *Teaching Tech Together*. It is reproduced in condensed form under **Examples**, E1.

## Rules
- **LES-1** — Design backward: write the assessments (what learners will do) before writing explanatory content. *Why:* like TDD, this forces a precise definition of "done", limits endless polishing, avoids confirmation bias, and stops learners meeting exam material they weren't prepared for [Wigg2005, Bigg2011, Fink2013, McTi2013]. *Check:* do concrete exercises or assessments exist, and was the content clearly derived from them, or were slides written first and exercises bolted on? (§6 intro; Template)
- **LES-2** — Start with a brainstorm that states the problems learners will solve, expected misconceptions, and what is explicitly out of scope, and agree it with colleagues. *Why:* a couple of hours here "can save days of rework later on." *Check:* does the design record answer at least 3–4 brainstorm questions, always including "what problems will learners learn to solve?", plus an out-of-scope list? (§6 intro; Template Step 1)
- **LES-3** — Name the audience with two or three learner personas, each with all five parts (background, prior knowledge, what *they* think they want, how the course helps, special needs). *Why:* "beginner" and "expert" mean different things to different people, and many factors besides prior knowledge decide fit. *Check:* every persona has all five parts; part 3 is in the learner's terms, not the expert's. (§6.1; Template Step 2)
- **LES-4** — Prefer a shared, reusable persona set over new personas for each lesson, and use persona names as design shorthand. *Why:* it saves effort and gives teachers a common vocabulary ("Would Jorge understand why we're doing this?"). *Check:* does the lesson reference existing team personas where they exist? (§6.1; Template Step 2 says "preferably")
- **LES-5** — Don't assume you know what learners need: ask them, and listen. *Why:* "you are not your learners." You probably differ in age, wealth, and above all technical knowledge. *Check:* is there evidence of learner input (surveys, interviews, pre-assessment) rather than only the designer's assumptions? (§6.1)
- **LES-6** — Record prerequisite skills or knowledge beyond what the personas state. *Why:* personas describe people; a course also needs explicit entry requirements. *Check:* is there a prerequisites list consistent with the chosen personas? (Template Step 2, Step 5)
- **LES-7** — Write 1–2 fully described end-of-course exercises, with worked solutions and example code, before outlining. Add brief outlines of 1–2 exercises per lecture hour. *Why:* concrete endpoints firm up vague goals, show how fast you expect learners to progress, and expose technical requirements early. *Check:* full exercises have runnable solutions; about half a dozen point-form exercises exist; each targets one skill the major exercises need. (Template Step 3)
- **LES-8** — Build the outline by ordering formative assessments by complexity and dependency. Use one major bullet per hour and 3–4 minor bullets (episodes) per hour. *Why:* the outline then follows what learners must be able to do, and each episode is "just enough" to reach the next check. *Check:* does every episode end in a formative assessment? Are there 3–4 per hour? Are datasets consolidated? (§6 intro steps 4–5; Template Step 4)
- **LES-9** — Write only enough content to get learners from one formative assessment to the next. *Why:* this keeps teaching focused on its objectives. *Check:* flag content that no exercise depends on. (§6 intro step 5)
- **LES-10** — Write the course overview (one-paragraph pitch, about six learning objectives, prerequisites) *last*. *Why:* writing it earlier usually wastes effort, because material gets added, cut, or moved. *Check:* the overview's objectives match the final exercises, not an early wish list. (Template Step 5)
- **LES-11** — Keep design notes in the canonical order (brainstorm → audience → exercises → outline → overview) even though the real process looped. *Why:* maintainers can retrace your reasoning; this is "faking" a rational process as in [Parn1986]. *Check:* does a design-notes document exist, ordered this way, recording *why* topics are in this order? (§6 intro; §6.3)
- **LES-12** — Don't confuse backward design with teaching to the test. Write the summative assessment as a design aid, which you may never give. *Why:* teaching to the test serves externally imposed metrics tied to pay and promotion, not learning; measurement without support for improvement rarely helps [Gree2014, Scot1998]. *Check:* is the assessment there to clarify goals and help learners, or to game an external metric? (§6 intro)
- **LES-13** — Write each learning objective as one sentence describing what the *learner* will do, with a measurable or verifiable active verb, a defined level of learning, and enough context or criteria to assess it. *Why:* this gives clear guidance for teaching and assessment, and learners appreciate clear expectations. *Check:* reject objectives that describe content ("will be given opportunities"), use non-observable verbs ("appreciate", "understand"), or name too vague a subject ("program in R"). (§6.2)
- **LES-14** — Choose objective verbs from Bloom's levels, and keep introductory material at the first four (remember, understand, apply, analyze). Expect evaluate/create only after mastery. *Why:* people can't think without something to think about [Will2010]. Most intro programming fits the first four levels. *Check:* does an intro lesson demand "design" or "critique" before learners have the foundations? (§6.2)
- **LES-15** — Use Fink's categories to add objectives that Bloom's misses: integration with real life, human dimension, caring, and learning how to learn. *Why:* Fink defines learning by the change in the learner, and its categories are complementary, not a ladder [Fink2013]. *Check:* does the objective set include at least one non-cognitive goal where the course aims for one (e.g. "want to learn more", accessibility awareness)? (§6.2)
- **LES-16** — Treat objectives and outcomes as distinct, and use summative assessment to compare them. *Why:* what a lesson aims at and what learners take away differ. *Check:* is there a way to measure each objective's outcome? (§6.2)
- **LES-17** — Apply [Guzd2016]'s five principles when matching material to an audience: connect to what learners know, keep cognitive load low, use authentic tasks, be generative and productive, and test ideas rather than trust instincts. *Check:* for each principle, point to where the design meets it. (§6.1)
- **LES-18** — Where audiences vary, offer a choice of domain-related assignments or domain-themed courses. Keep projects open-ended and share grading with other teachers. *Why:* [Alha2018] found better outcomes and satisfaction with choice; domain contexts (music, data science, cell biology) improve outcomes [Pete2017, Dahl2018, Ritz2018]. *Check:* is there at least one domain-relevant option per major persona? Is the extra grading load sustainable? (§6.1)
- **LES-19** — Build lessons to be cheaper to update than to replace: document the design, use tools that let many people edit and review, and cultivate willingness to collaborate (the most important factor). *Why:* someone will have to maintain the lesson. *Check:* is the design documented, is the material in a collaboratively editable or versioned format, and do others actually contribute? (§6.3)
- **LES-20** — When building a lesson-sharing resource, design for how teachers actually share. Ask role and course/grade level on landing; show resources in context; allow anonymous forum posts; support remixing of small pieces. *Why:* [Leak2017]'s barriers were mostly operational. Teachers remix rather than co-author, so smaller units may share better (tentative: the "sampling in music" and choral-explanations ideas are offered as possibilities). *Check:* compare the site or repository against these features. (§6.3)

## Procedures

### P1. Backward lesson design (Lesson Design Template, executable form)
Run the steps in order of increasing detail. **Loop back whenever a later step reveals something an earlier one missed**: the template says this happens repeatedly.

1. **Brainstorm (Step 1).** Write point-form answers to 3–4 of these questions (more if helpful), *always* including a couple of answers to the first:
   - What problem(s) will students learn how to solve?
   - What concepts and techniques will students learn?
   - What technologies, packages, or functions will students use?
   - What terms or jargon will you define?
   - What analogies will you use to explain concepts?
   - What heuristics will help students understand things?
   - What mistakes or misconceptions do you expect?
   - What datasets will you use?
   Optionally draw concept maps (§6 intro), and list what is out of scope (Design Notes practice).
   **Deliverable:** a rough scope for the course, agreed with colleagues.
   *Decision point:* if colleagues' answers diverge, resolve the scope before going on.
2. **Who is this course for? (Step 2).** Create learner personas (§6.1), or preferably pick from a shared set. Decide which personas the course targets and how it will help each. Note prerequisite skills or knowledge beyond what the personas state. (This step may come before Step 1.)
   **Deliverable:** brief summaries of whom the course will help and how.
3. **What will learners do along the way? (Step 3).** Write full descriptions of 1–2 exercises learners will be able to do near the end, with solutions and example code, so you can check that the software can do everything you need. Then list the skills those exercises require, and write a brief point-form exercise targeting each, at 1–2 per lecture hour.
   **Deliverable:** 1–2 fully explained exercises plus about half a dozen point-form exercise outlines.
   *Decision point:* if a solution exposes a missing tool, dataset, or prerequisite, return to Step 1 or 2.
4. **How are concepts connected? (Step 4).** Put the exercises in a logical order (by complexity and dependency). Derive a point-form outline: one major bullet per hour of work, 3–4 minor bullets for that hour's episodes. Consolidate the datasets the formative assessments use. Expect to change assessments so they build on each other, and to find things you forgot.
   **Deliverable:** a course outline.
5. **Write content (§6 intro step 5).** For each episode, write just enough material to get learners from the previous formative assessment to the next.
6. **Course overview (Step 5).** Write (a) a one-paragraph description, i.e. "a sales pitch to students"; (b) about half a dozen learning objectives (use P2); (c) a summary of prerequisites.
   **Deliverable:** course description, learning objectives, and prerequisites.
7. **Write up the design notes** in the order above, whatever order you actually worked in (LES-11). Use the Design Notes appendix (E1) as the model.

### P2. Write and check a learning objective
1. Start from a concrete exercise (P1 Step 3): what will the learner *do* to show they have learned it?
2. Write one sentence: "Learners will [measurable or verifiable verb] [specific object] [in what context, with what tools, to what standard]."
3. Pick the verb from the Bloom's table at the intended level. For intro material, stay within remember/understand/apply/analyze unless foundations are already mastered. Where the goal is affective, integrative, or metacognitive, use Fink's verbs instead.
4. Run the four failure checks from the §6.2 progression:
   - Does it describe content or opportunities rather than learner performance? Rewrite.
   - Is the verb non-observable ("appreciate", "understand", "know")? Replace it.
   - Is the level of learning undefined? Add scope (e.g. "one-page scripts").
   - Is the subject too vague to assess ("program in R")? Add context (data, tools, operations).
5. Ask: could two teachers write very different lessons from it (the "understand Git" test)? If so, it is still too vague.
6. Confirm a summative assessment exists that can compare the outcome with this objective.

### P3. Write a learner persona
1. Pick a realistic typical learner and give them a name.
2. Write five short points: general background; what they already know (be concrete about tools used); what they think they want to do, in their own terms and tied to a real task; how this course will help them do it; special needs (language, accessibility, bandwidth, schedule, etc.).
3. Optionally rewrite the points as flowing prose (as in §1.1).
4. Check against "you are not your learners". Where possible, validate the persona with real learners.
5. Add it to the team's shared persona set, and refer to it by name in design discussions.

### P4. Build a programming lesson by subtracting complexity (§6.4 exercise technique)
1. Write the complete program or web page learners should be able to create at the end.
2. Remove the most complex part you want them to write. That becomes the **last** exercise.
3. Remove the next most complex part you want them to write. That becomes the **penultimate** exercise. Repeat.
4. Whatever remains that you don't want them to write (e.g. importing libraries, loading data) becomes the **starter code**.
5. Count the parts and name the key idea each introduces. Those are your episodes.

### P5. PRIMM sequence for introducing a computing idea (§6.4 exercise)
1. **Predict** a program's behaviour or output.
2. **Run** it to see what it actually does.
3. **Investigate** why (e.g. step through it in a debugger, or draw the flow of control).
4. **Modify** it or its inputs.
5. **Make** something similar from scratch.

### P6. Concrete-Representational-Abstract (CRA) (§6.4 exercise; mainly younger learners)
1. **Concrete:** physically manipulate objects to solve the problem (e.g. pile blocks to add).
2. **Representational:** use images that stand for those objects.
3. **Abstract:** use numbers or symbols.
Worked activity: write 2, 7, 5, 10, 6 on sticky notes; simulate a loop that finds the largest by looking at each in turn (concrete); sketch and label the process (representational); write instructions someone else could follow (abstract); compare with a partner.

## Diagnostics
| Symptom | Underlying problem | Fix (rule IDs) |
|---|---|---|
| Slides written first; assignments invented weeks in; exam written the night before | Forward design | LES-1, LES-7, LES-8 |
| Exam contains material the course never prepared learners for | Assessments not derived from or aligned with content | LES-1, LES-8 |
| Objective says "understand X" or "appreciate X" | Non-observable verb, no level, vague subject | LES-13, P2 |
| Objective says "learners will be given opportunities to…" | Describes content, not learner performance | LES-13 |
| Intro course objectives ask learners to "design" or "critique" from day one | Bloom's level too high for novices | LES-14 |
| Course has only cognitive objectives, though the designer wants learners to care or keep learning | Fink's dimensions missing | LES-15 |
| Audience given as "beginners" with no further detail | No personas, so "beginner" is ambiguous | LES-3, P3 |
| Persona's "wants" are what the expert thinks they should learn | Persona part 3 written from the expert's view | LES-3, LES-5 |
| Designer assumes learners have fast bandwidth, the same jargon, or the same OS habits | Designer projects themselves onto learners | LES-5; see the inessential weirdness exercise |
| Each lesson invents new personas; team discussions talk past each other | No shared persona set | LES-4 |
| Learners hit installation or tool failures mid-course | Exercises not solved early with real code | LES-7 |
| Hour-long block has no checkpoints, or 10 tiny ones | Episode granularity wrong | LES-8, LES-9 |
| Course description and objectives rewritten many times | Overview written too early | LES-10 |
| New maintainer can't tell why topics are ordered as they are | Design rationale not captured | LES-11, LES-19 |
| Lesson is cheaper to rewrite than to update | Poor documentation, poor tooling, or no collaboration culture | LES-19 |
| Teachers download from a sharing site but never contribute | Operational barriers; wrong sharing granularity | LES-20 |
| Mixed-background class disengaged by one-size assignments | No domain choice | LES-18 |
| Assessment exists only to hit an externally set metric | Teaching to the test | LES-12 |

## Templates and checklists

### T1. Lesson design document skeleton (from the Lesson Design Template)
```markdown
# <Course title> — Design Notes

## 1. Brainstorming  (deliverable: rough scope agreed with colleagues)
- What problems will learners learn how to solve?   <- always answer
- What is out of scope?
- What concepts and techniques will learners encounter?
- What technologies, packages, or functions will they use?
- What terms or jargon will be defined?
- What analogies will be used?
- What heuristics will help?
- What mistakes or misconceptions do we expect?
- What datasets will be used?
- In what contexts will this material be used? (primary / secondary)

## 2. Intended audience  (deliverable: who the course helps and how)
- Persona A: background / knows / wants / how course helps / special needs
- Persona B: ...
- Common elements across personas:
- Learning context for each persona:
- Prerequisites beyond the personas:

## 3. Exercises  (deliverable: 1–2 full exercises + ~6 point-form outlines)
- Full exercise 1: description + solution + example code
- Full exercise 2: ...
- Point-form exercises (1–2 per lecture hour, one per required skill):

## 4. Outline  (deliverable: course outline)
- Hour 1: <major topic>
  - episode 1 -> formative assessment
  - episode 2 -> formative assessment
  - episode 3 -> formative assessment
- Hour 2: ...
- Consolidated datasets:

## 5. Course overview  (deliverable; write last)
- Brief description (one-paragraph pitch to learners):
- Learning objectives (~6, "Learners will be able to…"):
- Prerequisites:
```

### T2. Learner persona card
```text
Name:
1. General background:
2. What they already know:
3. What THEY think they want to do (their words, their real task):
4. How this course will help them:
5. Special needs (language, accessibility, bandwidth, time, devices…):
```

### T3. Learning objective checklist
- [ ] One sentence.
- [ ] Subject is the learner, and describes what they will *do*, not what the lesson contains.
- [ ] Measurable or verifiable active verb (Bloom's or Fink's table).
- [ ] Level of learning defined.
- [ ] Context and criteria for acceptable performance stated (data, tools, scope).
- [ ] Specific enough that two teachers would build similar lessons from it ("understand Git" test).
- [ ] Level suits the audience (intro: Bloom's levels 1–4).
- [ ] A summative assessment can compare the outcome with it.

### T4. Lesson-evaluation dimensions [Mart2017] (rate each low / medium / high / not applicable)
| Dimension | Question |
|---|---|
| Closed vs. open | Is there a well-defined path and endpoint, or are learners exploring? |
| Cultural relevance | How well is the task connected to things learners do outside class? |
| Recognition | How easily can the learner share the product of their work? |
| Space to play | (Wilson: "seems to overlap closed vs. open") |
| Driver shift | How often are learners in control of the learning experience? (Tight "see then do" cycles score highly.) |
| Risk reward | To what extent is taking risks rewarded or recognized? |
| Grouping | Is learning individual, in pairs, or in larger groups? |
| Session shape | Theater-style classroom, dinner seating, free space, public space, etc. |

### T5. Maintainability audit (§6.3)
- [ ] Design notes exist and explain what the lesson should achieve and why topics are ordered as they are.
- [ ] Material is in a format many people can edit, comment on, and merge (collaborative docs or version control), with the learning curve weighed.
- [ ] People other than the author have actually contributed or remixed.
- [ ] Pieces are small enough to remix independently.

### T6. Guzdial's five checks [Guzd2016]
Connect to what learners know · keep cognitive load low · use authentic tasks · be generative and productive · test ideas rather than trust instincts.

## Examples

### E1. The book's own design (appendix "Design Notes"), a full worked run of P1
**Brainstorming.**
- *Problems learners will solve:* how people learn and what that implies for teaching (educational psychology, cognitive load, study skills); how to design and deliver instruction in computing skills (backward curriculum design, some computing PCK); how to deliver lessons (teaching as a performance art, live coding, motivation and demotivation, automation); how to grow a teaching community (community organization and marketing).
- *Out of scope:* teaching children or people with special learning needs (much applies, but they have different or extra needs); rigorously assessing the impact of training (informal self-assessment only, no publishable educational research); designing whole degree programmes or extended curricula (much applies, but large-scale design has extra needs).
- *Concepts and techniques:* 7 ± 2 and chunking; authentic tasks with tangible artifacts; Bloom's, Fink's, and Piaget's development stage theory; branding; cognitive development from novice to competent to expert; cognitive load; collaborative lesson development; concept mapping; assessments with diagnostic power; Dunning-Kruger effect; expert blind spot; externalized cognition; fixed vs. growth mindset (and critiques); formative vs. summative assessment; governance models of community organizations; inquiry-based learning (and critiques); intrinsic vs. extrinsic motivation; jugyokenkyu (lesson study); learner personas; legitimate peripheral participation in a community of practice; live coding; PCK and TPACK; peer instruction; reflective (deliberate) practice; backward design; stereotype threat (and critiques); working vs. persistent memory.
- *Expected mistakes or misconceptions (that learners hold):* children and adults learn the same way; computing education should be for and about computer science; programming skill is innate; student evaluations of courses indicate learning outcomes; teaching ability is innate; the best way to teach is to throw people in at the deep end; the best way to teach is to use "real" tools from the start; visual-auditory-kinesthetic (VAK) learning styles are real; women don't like programming or have less innate aptitude; getting a (better) job is the main reason to learn to program.
- *Contexts:* primary, an intensive weekend workshop for people in tech who want to volunteer with grassroots get-into-coding initiatives. Secondary, self-study or guided study by such people, and a one-semester undergraduate course for CS majors interested in education.

**Intended audience (personas).**
- *Emily:* trained as a librarian, now a web designer and project manager at a small consultancy. In her spare time she helps run web design classes for women entering tech as a second career. She is recruiting colleagues to run more classes using her lessons and wants to know how to grow a volunteer teaching organization.
- *Moshe:* professional programmer with two teenagers whose school has no programming classes. He has volunteered to run a monthly after-school club. He presents often to colleagues but has never designed lessons. He wants to build effective lessons collaboratively and turn them into a self-paced online course.
- *Samira:* robotics undergraduate considering full-time teaching. She wants to help teach weekend workshops for undergraduate women, but has never taught a whole class and is uncomfortable teaching things she isn't an expert in. She wants to learn about education to decide whether it's for her.
- *Gene* (referred to as "they"): CS professor in operating systems, teaching undergraduates for six years, increasingly sure there's a better way. Their university's teaching center only trains people on the learning management system, so they want to know what else to ask for.
- *Common elements:* varied technical backgrounds; may or may not have teaching experience; no formal training in teaching, lesson design, or community organization; more often teaching in free-range settings than in institutional classrooms with required homework, exams, and mandated curriculum; focused on teens and adults rather than children; limited time and resources (volunteers, or teaching is a secondary duty).
- *Learning contexts:* Emily, a weekly online reading group with her volunteers. Moshe, part of the book in a two-day weekend workshop and the rest alone. Samira, a one-semester undergraduate course with assignments, a project, and a final exam. Gene, reading alone in the office or while commuting.

**Exercises (formative; "the finished book will include others as well").** Learners will:
1. Create MCQs whose incorrect answers have diagnostic power.
2. Give feedback on a recorded teaching episode and compare their points with expert feedback.
3. Create a Parsons Problem.
4. Create a short debugging exercise.
5. Create a short execution-tracing exercise.
6. Explain their personal motivation for teaching.
7. Explain their community of practice's aims and conventions.
8. Explain the difference between an oversight board and a governance board.
9. Design an hour-long lesson using backward design.
10. Describe the pros and cons of standardized testing.
11. Create learner personas for their intended students.
12. Write and critique learning objectives for an hour-long lesson.
13. Write and critique a short value proposition for a class they intend to offer.
14. Teach a short lesson using live coding and critique a recording of it.
15. Create a short video lesson and critique it.
16. Construct a short series of faded examples that illustrate a problem-solving pattern in programming.
17. Describe ways in which they differ from their intended learners.
18. Create and critique an elevator pitch for a course they intend to teach.
19. Write a "cold call" email to solicit support for what they intend to teach.
20. Create a concept map for a topic they intend to teach.
21. Explain six strategies students can use to learn more effectively.
22. Analyze and critique the accessibility of a short online lesson.
23. Analyze and critique the inclusivity of a short lesson.
24. Create and critique a non-programming exercise for a programming class.
25. Describe the relative merits of block-based and text-based environments for introductory programming classes for adults.
26. Create a one-to-one matching exercise.
27. Create a diagram-labelling exercise.
28. Write and submit an improvement or extension to an existing lesson and review a peer's submission.
29. Describe the pros and cons of collaborative note-taking.
30. Describe the pros and cons of gamification in online learning.
31. Create and critique a short questionnaire for assessing learners' prior knowledge.
32. Conduct a demonstration lesson using peer instruction.
33. Describe ways computing is unwelcoming to or unaccepting of people from diverse backgrounds.
34. Demonstrate several ways to distribute an instructor's attention fairly through a class.
35. Describe the pros and cons of in-person, automated, and hybrid teaching strategies.
36. Write and critique automated tests for a short programming exercise.

**Outline.** Each major section takes 2–3 weeks in a conventional classroom, or one full day (in less detail) in an intensive workshop.
- Introduction
- Learning: Building Mental Models; Expertise and Memory; Cognitive Load; Effective Learning
- Designing: A Lesson Design Process; Pedagogical Content Knowledge
- Delivering: Teaching as a Performance Art; Live Coding; Motivation and Demotivation; Automation; Hybrid Models
- Organizing: Awareness; Operations; Building Community

**Course overview.**
- *Brief description:* "Teaching isn't magic: good teachers are simply people who have learned how to design lessons to achieve concrete goals, how to get and use feedback from learners, and how to work well with other teachers." The book shows how to do this, introduces research on why some things work and others don't, and is aimed mainly at people in tech with no formal teaching training who want to help adults learn to create web sites, write programs, and analyze data, though the ideas apply to other groups.
- *Learning objectives:* "Learners will be able to…"
  1. Explain the cognitive changes as people go from novice to competent to expert, and how best to teach each group.
  2. Explain how to design, construct, and maintain lessons in a systematic, collaborative way.
  3. Design exercises to help correct key misconceptions learners have about computing.
  4. Summarize key elements of PCK related to computing and other technical skills.
  5. Compare and contrast teaching with other performance arts, and take part in structured critiques of live teaching.
  6. Compare and contrast interactive teaching, automated teaching, and hybrid models.
  7. Describe factors that motivate or demotivate adult learners, and how to take them into account when teaching.
  8. Describe ways members of different groups are made to feel unwelcome or excluded in computing, and what can make computing more inclusive.
  9. Explain the purpose and value of their teaching and of their community of practice.
  10. Be a productive member of a community of teaching practice.
- *Prerequisites:* some exercises assume a little programming. Readers should know how to loop over a list, act using if-else, and write and call a simple function.

> **Skill note:** In E1 the published outline differs from the final book (e.g. "Live Coding", "Automation", "Hybrid Models", "Awareness", "Operations" became or merged into other chapters such as Teaching Online, Marketing, and Partnerships). This illustrates Wilson's point that design is iterative and things get "added, dropped, or rearranged". The E1 personas are prose, not five-part lists, and they fold "how the course helps" into the learning-context list. The plan has 10 objectives, against the template's "half a dozen", and several use verbs ("explain", "be a productive member") that a strict P2 check would push to sharpen. An agent can use this as a critique exercise.

### E2. Persona "Jorge" (§6.1)
Situation: a weekend workshop for college students. Done: a five-part persona tying the course to Jorge's real task (averaging soil-sensor logs he currently processes by hand in Excel), and naming a special need (spoken jargon). Lesson: a concrete persona turns abstract audience talk into checkable questions ("What installation problems would Jorge face?").

### E3. "Understand Git" (§6.2)
Situation: a vague objective. Done: three concrete readings (compare Git with Dropbox; commit via GUI; recover from a detached HEAD on the command line). Lesson: vague objectives hide what are really different lessons.

### E4. Poor objective → good objective (§6.2)
"Given opportunities to learn good programming practices" → "better appreciation for…" → "understand how to program in R" → "write one-page data analysis scripts to read, filter, summarize, and print results for tabular data using R and R Studio." Lesson: each step fixes one defect: content vs. learner, active verb, level, context.

### E5. HTML/CSS objectives based on Fink (§6.2)
Five objectives spanning explanation, production, comparison with desktop publishing, accessibility correction, and "want to learn more" about JavaScript. Lesson: one course can mix cognitive, integrative, human, and affective goals.

## Evidence and caveats
- **Backward design** was developed independently by [Wigg2005] (Understanding by Design), [Bigg2011] (Teaching for Quality Learning at University), and [Fink2013] (Creating Significant Learning Experiences), and summarized in [McTi2013]. Wilson presents it as better than forward design by analogy with TDD. He does not cite a controlled comparison.
- **Measurement without support:** [Gree2014] says focusing on measurement rarely improves outcomes unless teachers get help to improve. [Scot1998] says large organizations prefer uniformity over productivity.
- **Faking a rational process:** [Parn1986].
- **Persona guidance:** [Guzd2016] (bib: principles for choosing a programming language for newcomers; Wilson applies them to lesson design).
- **Assignment choice and domain context:** [Alha2018] better outcomes and satisfaction; [Pete2017] music, [Dahl2018] data science, [Ritz2018] molecular or cell biology contexts improve outcomes.
- **Bloom's reliability:** [Masa2018], even experienced educators disagree on classifying items. Bloom's revision: [Ande2001]. "Can't think without something to think about": [Will2010].
- **Fink's Taxonomy:** [Fink2013].
- **Resource-sharing sites:** [Leak2017], interviews with 17 CS teachers; barriers mostly operational.
- **Hedged ideas:** "lesson development as sampling in music" (introduced with "perhaps") and choral explanations ("If Caulfield is right") are speculative.
- **Commons-based development "actually works very well":** Wilson's claim, pointing to §13.4 and appendix §C.3 for evidence.
- Bloom's levels are hierarchical; Fink's are not. Don't treat Fink's as a ladder.

## Practice exercises
- **Create Learner Personas** — create a five-point persona describing one of your typical learners. Small groups, 30 min.
- **Classify Learning Objectives** — classify the §6.2 HTML/CSS objectives by Bloom's level, then compare with a partner, discussing agreements and disagreements. Pairs, 10 min.
- **Write Learning Objectives** — write objectives for something you teach using Bloom's, then critique and improve them with a partner. Pairs, 20 min.
- **Write More Learning Objectives** — the same using Fink's Taxonomy. Pairs, 20 min.
- **Building Lessons by Subtracting Complexity** — take a target program or page, work backward to break it into parts (P4), count them, and name the key idea of each. Individual, 20 min.
- **Inessential Weirdness** — read Leondar-Wright's and Harihareswara's pieces (examples include disparaging remarks about Windows, cryptically named command-line tools, and the command line itself), list the inessential weirdnesses your learners might meet, and decide how many you can avoid. Individual, 15 min.
- **PRIMM** — outline a short lesson on something recently taught, following Predict–Run–Investigate–Modify–Make (P5). Individual, 15 min.
- **Evaluating Lessons** — rate recent lessons on [Mart2017]'s eight dimensions (T4) as low, medium, high, or n/a, and pick the two dimensions that matter most to you as teacher and as learner. Pairs, 20 min.
- **Concrete-Representational-Abstract** — sticky-note find-the-maximum loop through the concrete, representational, and abstract stages, then compare with a partner (P6). Pairs, 15 min.

## Cross-references
- `01-introduction-and-motivation-to-teach.md`: the §1.1 personas (the five-part persona in prose form).
- `02-mental-models.md`: concept maps for brainstorming; formative assessment, MCQs, and diagnostic power.
- `03-expertise-and-memory.md`: expert blind spot (why "you are not your learners").
- `04-cognitive-load.md`: "keep cognitive load low"; Parsons Problems; faded examples.
- `07-programming-pck.md`: what to put in the brainstorm's "mistakes or misconceptions" and "concepts" lists for programming lessons; PRIMM-style predict-then-run.
- `08-teaching-as-performance.md`: [Gree2014] and lesson study; live coding.
- `09-in-the-classroom.md`: pre-assessment questionnaires to validate personas.
- `10-motivation-and-inclusion.md`: authentic tasks (§10.1); inessential weirdness and inclusivity.
- `12-exercise-types.md`: exercise formats for formative assessments.
- `13-building-community.md`: commons-based lesson development (§13.4, §C.3).

## Source map
| Book section | Covered under |
|---|---|
| §6 intro (forward vs. backward design, TDD, teaching to the test, "Measure…And Then?", Parn1986) | Concepts §6 intro; LES-1, LES-8, LES-9, LES-11, LES-12; P1 |
| §6.1 Learner Personas | Concepts §6.1; LES-3, LES-4, LES-5, LES-17, LES-18; P3; T2; E2 |
| §6.2 Learning Objectives | Concepts §6.2; LES-13 to LES-16; P2; T3; E3, E4, E5 |
| §6.3 Maintainability | Concepts §6.3; LES-19, LES-20; T5 |
| §6.4 Exercises | Practice exercises; P4, P5, P6; T4 |
| Appendix "Lesson Design Template" (Steps 1–5, Reminder) | Concepts; LES-2, LES-6, LES-7, LES-10; P1; T1 |
| Appendix "Design Notes" | Examples E1 |
