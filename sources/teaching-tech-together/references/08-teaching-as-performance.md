# Teaching as a Performance Art

> Source: Greg Wilson, *Teaching Tech Together* (2018), Ch. 8 "Teaching as a Performance Art" (§8.1–§8.5), appendix "Presentation Rubric". Licensed CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/); condensed and restructured for skill use, with quotations marked. Rule IDs use prefix `PRF`.

## When a skill needs this
- Reviewing a recording, transcript, or plan of someone's lecture, demo, or live-coding session, and producing structured feedback (2×2 grid or the Presentation Rubric).
- Coaching a new teacher on how to ask for, give, and absorb feedback on their teaching, or designing a peer-observation programme (lesson study).
- Planning or critiquing a live-coding segment: screen setup, pacing, handling mistakes, predictions, boilerplate.
- Running a teacher-training workshop session on delivery (the record-yourself exercise, the "tells" exercise, the bad/good live-coding critique).
- Building or pruning a feedback rubric for a teaching team.

## Key terms
| Term | Meaning (one line) |
|---|---|
| Jugyokenkyu | Japanese "lesson study": teachers routinely observe one another, discuss lessons afterward, and study curriculum together. |
| Lateral knowledge transfer | The audience learns Y (e.g. editor shortcuts) while the teacher sets out to teach X. |
| Demonstration lesson | One person teaches real students while other teachers observe. |
| Formative feedback/assessment | Feedback meant to show what is going well and what still needs work, not to grade. |
| 2×2 feedback grid | Rubric: rows "what went well" / "what can be improved", columns "content" / "presentation" (§8.2, Fig 8.2). |
| Compliment sandwich | Positive, then negative, then positive observation (§8.2). |
| Feedback translator | A third person who reads all feedback and gives the recipient a summary (§8.2). |
| Question budget | A rubric's total length stays fixed; adding a question means removing a less important one (§8.2). |
| Studio class | Learners solve small design problems and get immediate peer critique; the teacher critiques both the work and the critiques [Scho1984] (§8.2). |
| Tells | Nervous habits (pacing, hair-fiddling, fast high-pitched speech, rattling change) (§8.3). |
| Live coding | Teaching programming by writing code in front of learners as they follow along (§8.4). |
| Twitch coding | Learners, one by one, tell the teacher what to type next (§8.4). |
| Deliberate fumble | Making a known past mistake on purpose during a demo (§8.4). |
| Direct Instruction (DI) | Meticulous curriculum delivered through a prescribed script (§8.4). |
| PCK / TPACK | Pedagogical content knowledge; TPACK adds technology to the framework [Koeh3013] (Ch 8 intro). |

## Concepts

### Chapter framing (Ch 8 intro)
- Building on Chapter 7: effective teachers need content knowledge, general pedagogical knowledge, and pedagogical content knowledge (PCK). Adding technology (TPACK, [Koeh3013]) elaborates the framework but does not change the point: "it isn't enough to know the subject, or how to teach—you have to know how to teach that particular subject" (Ch 8 intro, citing [Maye2004]).
- Chapter focus: giving a lecture or live demonstration in front of a class. It is not the only way to teach but probably the most common, and the techniques transfer to other formats.
- Box "Teaching Tips": the CS Teaching Tips site collects PCK for teaching programming. Wilson hopes for future equivalents of misconception catalogues [Ojos2015], teacher-training materials [Hazz2014, Guzd2015a, Sent2018], and personal collections such as [Gelm2002].
- Learning objectives of the chapter: define jugyokenkyu and lateral knowledge transfer and relate them; describe and enact at least three techniques for giving and receiving feedback on teaching; explain at least two ways a rubric makes feedback more effective; describe live coding and its advantages for programming workshops; do and critique live coding.

### 8.1 Lesson Study
- Reformers have tried to find "born teachers" and weed out the rest. Wilson calls that assumption wrong: like any performance art, teaching improves through **practice and collaboration**.
- Jugyokenkyu ([Gree2014]) is "a bucket of practices": observing each other at work, discussing the lesson afterward, studying curriculum with colleagues. It is so pervasive in Japanese schools that it is effectively invisible.
- Japanese teacher training as a "teaching relay" ([Gree2014]): trainees first observe an assigned master teacher, then by the third week replace him. Each trainee plans five days of lessons in one subject, then each takes a day and must teach that day's lesson in *every* subject (the one they planned and the four they did not), in front of the master teacher. Afterward everyone (teacher, trainees, sometimes an outside observer) sits at a formal table to discuss what they saw.
- Scrutinising work to improve it is normal in sports and music. A professional musician will dissect half a dozen recordings of a song before performing it and expects feedback from peers in practice and after performances. The Japanese drew on Deming's ideas about continuous improvement in manufacturing.
- In most English-speaking countries continuous feedback isn't part of teaching culture: "what happens in the classroom stays in the classroom." Teachers rarely watch each other, so they can't borrow good ideas, and each one has to invent teaching alone, combining lesson plans, assignments, MOOCs, and education-school theory into actual lessons.
- **Writing up techniques and running demonstration lessons usually don't work** [Finc2007, Finc2012]: of 99 "change stories", teachers actively searched for new practices or materials in only 3 cases and consulted published material in only 8. Most changes happened locally, without outside sources, or through personal interaction with other educators.
- [Bark2015]: adoption is "not a 'rational action'" but an iterative series of decisions in a social context, relying on tradition, social cueing, and emotion or intuition. Faculty rarely base adoption on research findings, and "Positive student feedback is taken as strong evidence by faculty that they should continue a practice" (§8.1, quoting [Bark2015]).
- **Lateral knowledge transfer**: the audience learns Y as well as, or instead of, the X being taught. Example: a teacher demonstrates searching a text file for email addresses, and the audience comes away with new editor keyboard shortcuts. Jugyokenkyu maximises the chances of this happening *between teachers*.

### 8.2 Giving and Getting Feedback on Teaching
- "Observing someone helps you; giving them feedback helps them" (§8.2). Receiving feedback is hard, especially negative feedback.
- Figure 8.1 ("Feedback Feelings", © Deathbulge 2013; described, not reproduced): a three-panel cartoon. A character is surrounded by many speech bubbles of praise and one saying they can be a jerk sometimes. Over the panels the praise fades while that one criticism stays vivid, until the character lies awake in bed at night with only the criticism still clear. The point: one negative remark can outweigh many positive ones.
- Feedback is easier to give and receive when both sides **share ground rules and expectations**. This matters most when people come from different backgrounds or cultures with different norms about what may be said.

**Getting better feedback on your own teaching:**
1. **Initiate feedback.** Asking for it beats receiving it unwillingly.
2. **Choose your own questions.** Ask for specific feedback. "What do you think?" is much harder to answer than "What is one thing I could have done as a teacher to make this lesson more effective?" or "If you could pick one thing from the lesson to go over again, what would it be?" (§8.2). Directed feedback also helps you: it is better to fix one thing at a time than to change everything and hope; focusing on a chosen area raises the odds you will see progress.
3. **Use a feedback translator.** Someone else reads all the feedback and summarises it. "It sounds like most people are following, so you could speed up" is easier to hear than several notes saying "this is too slow" or "this is boring" (§8.2).
4. **Be kind to yourself.** Write down what you thought of your own performance *before* reading others' feedback, then compare. This calibrates your self-assessment. Common example: people believe they say "um" and "err" constantly when the audience doesn't notice; hearing this once lets them rescale their self-judgement next time.

**Giving better feedback to others:**
1. **Balance positive and negative.** A common method is the compliment sandwich (positive, negative, positive), "though this can get tiresome after a while" (§8.2).
2. **Organise feedback with a rubric.** People are more comfortable giving and receiving feedback when they understand the social rules for what may be said and how. A facilitator can transcribe items into a shared document or onto a whiteboard during discussion.

**Rubrics:**
- The simplest is the **2×2 grid** (Figure 8.2, "Teaching Rubric"): the vertical axis is "what went well" vs "what can be improved", the horizontal axis is "content" (what was said) vs "presentation" (how it was said). Observers write comments on sticky notes while watching, then post them into the matching quadrant of a grid drawn on a whiteboard.
- A more detailed rubric for 5–10 minute videos of programming instruction is the **Presentation Rubric** appendix (reproduced below). A rubric that detailed is best presented as a **checklist ordered roughly as items will be used** (introduction questions before conclusion questions).
- Box "Question Budgets": rubrics grow as people think of things to add. Keep the total length constant, so anyone adding a question must name a less important one to remove.
- Further reading: [Gorm2014] for making peer-to-peer feedback routine; [Gawa2011] on the value of having a coach.
- However it is collected, peer feedback is **formative**: it helps people see what they do well and what still needs work.
- These guidelines cover **peer-to-peer feedback on delivery**. Feedback from *learners* should be "as close to continuous as you can make it", and you should prompt for questions and reflections as well as positives and negatives (§8.2).
- Box "Studio Classes": architecture schools run studio classes in which students solve small design problems and get feedback from peers on the spot. They work best when the teacher critiques both the designs *and the peer critiques*, so participants learn how to give and get feedback as well as how to design [Scho1984]. Music master classes serve a similar purpose.

### 8.3 How to Practice Performance
- The best way to improve in-person delivery is to **watch yourself do it**. The method below is borrowed from Warren Code at the University of British Columbia.
- Procedure: groups of three; rotate roles (teacher, audience, videographer); each teacher gets **two minutes** to explain one key idea from their teaching or other work as if to a class of high-school students; the audience is attentive; the videographer records on a phone or other handheld device. After everyone has taught, the group watches all three videos together and everyone gives feedback on all three, **including their own**. Then the videos are **deleted** (many people are uncomfortable with images of themselves appearing online). Finally, return to the main group and add feedback to a shared 2×2 grid (positive/negative × content/presentation).
- Conditions for success:
  - **Record all three, then watch all three.** With teach-review-teach-review the last person runs out of time; reviewing after all the teaching also puts some distance between teaching and reviewing, "which makes the exercise slightly less excruciating" (§8.3).
  - **Tell people at the start of the class** that they will teach something, so they have time to choose a topic. Telling them further in advance can backfire because some will fret about how much to prepare.
  - **Separate groups physically** to cut audio cross-talk: in practice 2–3 groups per normal classroom, the rest in breakout spaces, lounges, offices, or (once) a janitor's storage closet.
  - **People must give feedback on themselves** as well as others, so they can calibrate their self-impressions against others'. Most people are harder on themselves than others are, and they need to see this.
- The exercise is often greeted with groans, but participants consistently rate it among the most valuable parts of workshops based on these notes. It also prepares people for co-teaching (§9.3): partners give each other informal feedback more easily after practice and with a shared rubric.
- Box "Tells": everyone has nervous habits (talking faster and higher, playing with hair, cracking knuckles, pacing, looking at shoes, rattling change when you don't know an answer). They are often less noticeable than you think, but you should know yours. You can't eliminate tells, and trying makes you obsess. Instead **displace** them, e.g. train yourself to scrunch your toes inside your shoes instead of cracking your knuckles.

### 8.4 Live Coding
- Epigraph: "Teaching is theater, not cinema." (Neal Davis, §8.4)
- Live coding means the teacher writes code in front of the class, instead of using slides, as learners follow along. Wilson says it "completely changed the way I teach programming" (§8.4). Why it beats slides:
  1. Watching a program being written is more compelling than paging through slides of fragments of the same code.
  2. It lets teachers respond to "what if?" questions. A slide deck is a railway track; live coding lets you go off-road and follow learners' interests.
  3. It enables lateral knowledge transfer: learners pick up more than we realised we were teaching by watching how we work.
  4. It slows the teacher down: typing, she can go only about twice as fast as learners rather than ten-fold as with slides.
  5. It keeps short-term-memory load down because the teacher feels how much they are throwing at learners (slides and copy-paste don't give that signal).
  6. Learners see the teacher's mistakes and how to diagnose and fix them. Novices will spend most of their time doing this, yet most textbooks leave it out.
  7. Seeing the teacher make mistakes shows it's all right to make them. People model their teachers' behaviour: an unembarrassed teacher makes learners comfortable too.
- Thinking aloud while coding takes a bit of practice; most teachers then report it is no harder than talking around slides. "Research seems to back up its effectiveness" [Rubi2013, Haar2017] (§8.4). [Rubi2013] reports live coding is as good as or better than static code examples; [Haar2017] is an early look at live-streamed coding.

**Embrace your mistakes**
- Epigraph: "The typos are the pedagogy." (Emily Jane McTavish, §8.4)
- The **most important rule** of live coding: embrace your mistakes. You will make some however well you prepare, so think through them with the audience. Data are scarce, but professional programmers spend roughly 25–60% of their time debugging and novices much more (§7.2), yet textbooks and tutorials spend little time on diagnosis and correction. Talking aloud as you find and fix what went wrong gives learners a toolbox for their own errors.
- This contradicts [Kran2015], who says material should be "absolutely mastered" before class and that fixing a broken example in front of the group will "lose all but the diehards quickly." Wilson's counter-evidence is Software Carpentry and similar experience: watching the teacher make mistakes motivates most students, because it gives them permission to be imperfect.
- Box "Deliberate Fumbles": once you have given a lesson several times you will mostly make only basic typos (which can still be informative). Remembering past mistakes and making them on purpose often feels forced, unless the mistake and its correction is the main point of the lesson. A better option is **twitch coding**: ask learners one by one what to type next. This is "pretty much guaranteed to get you into the weeds" (§8.4).

**Ask for predictions**
- Ask, e.g., "What is going to happen when I run this code?" Then either show them, or write down the first few suggestions, have the class vote on the most likely, and run the code. This keeps attention on task and practises reasoning about code behaviour, a useful skill in itself. (See also §9.11 "Have Learners Make Predictions", [Mill2013].)

**Take it slow**
- For every command, word of code, menu item, or button: say out loud what you are doing while you do it, then point to the command and its output and go through it a second time. This slows you down and lets learners copy you or catch up even when they are looking at their own screens.
- **Don't copy and paste code**: it "practically guarantees that you'll race ahead of your learners" (§8.4).
- If you use tab completion, say so out loud the first few times, e.g. "Let's use turtle dot 'r' 'i' and tab to get 'right'" (§8.4).
- If output scrolls your typed command out of view, scroll back up. If that's impractical, run the command again or paste the last command(s) into the shared notes.

**Be seen and heard**
- If you are physically able to stand for a couple of hours, stand: sitting hides you from the back rows. Tell organisers in advance so they can arrange a high table, standing desk, or lectern.
- Standing or sitting, move around as much as reasonable (go to the screen to point, draw on the board). Movement makes teaching less monotonous and pulls learners' attention from their screens to you.
- Use a microphone even if your voice is good, especially if the room has one: it saves your voice and helps people with hearing difficulties.

**Mirror your learners' environment**
- Your customised prompt, colour scheme, and shortcuts aren't on learners' machines. Create an environment like theirs, e.g. a bare-bones separate user account on your laptop, or a teaching-only account on online services such as Scratch or GitHub.

**Use the screen wisely**
- Enlarge the font a lot so the back row can read it. You will often be down to 60–70 columns and 20–30 rows, "using a 21st Century supercomputer to emulate an early-1980s VT100 terminal" (§8.4).
- Maximise the window, then ask everyone for thumbs-up or thumbs-down on readability.
- Use a **black font on a lightly tinted background**, not light-on-dark; a light tint glares less than pure white.
- Lighting: the room shouldn't be fully dark, and no lights should be directly on or above the screen. Reposition tables if needed so everyone can see.
- If the bottom of the projection is at or below learners' head height, the back rows can't see the lower part. Raise the bottom of your windows, accepting even less typing space.
- If you can get a second projector and screen, use it: code on one, output or behaviour on the other. It may need its own computer and a helper to drive it.
- In a console (e.g. Unix shell), **say when you enter an in-console text editor and when you return to the prompt.** Novices haven't seen one window "take on multiple personalities" and get confused, especially when it also hosts an interactive interpreter (§8.4).
- Box "Accessibility Aids Help Everyone": cursor highlighters (Mouseposé for Mac, PointerFocus for Windows) and screen-recording tools such as Camtasia that echo invisible keys (Tab, Control-J) as you type. They take practice but are extremely helpful for more advanced tools.

**Double devices**
- Some teachers use two devices: a laptop on the projector for learners, and a tablet beside it showing their own notes and the learners' shared notes (§9.7). This is more reliable than flipping between virtual desktops. Printouts of the lesson remain "the most reliable backup technology" (§8.4).

**Use diagrams**
- Diagrams are almost always a good idea. Prepared diagrams on screen are common (Wilson often keeps a slide deck of diagrams in the background while live coding), but sketching on the whiteboard lets you build a diagram step by step, which helps retention (§4.1) and allows improvisation.

**Avoid distractions**
- Turn off notifications (social media, email, etc.). They distract you and learners and can show messages you'd rather others not see. Frequent teachers may want a second computer account with no email or similar tools set up.

**Improvise after you know the material**
- The first time you teach a lesson, stick fairly closely to the plan you drew up or borrowed. Resist showing a neat trick or alternative: there's a fair chance you'll hit something unexpected that you then have to explain.
- Once familiar, you can and should improvise based on learners' backgrounds, their questions, and what you find most interesting. Analogy: the first few times you play a new song you stick to the sheet music, then put your own stamp on it.
- If you want to use something outside the material, run through it beforehand exactly as planned, on the computer you will teach on. Cautionary example: installing several hundred megabytes of updates over high-school WiFi in front of increasingly bored 16-year-olds.
- Box "Direct Instruction": DI uses meticulous curriculum design and a prescribed script, closer to an actor reciting lines than to the improvisation recommended here. [Stoc2018], a meta-analysis, finds a statistically significant positive effect, although DI is sometimes criticised as mechanical. Wilson still prefers improvisation because DI needs far more up-front investment than most free-range learning groups can afford.

**Face the screen, occasionally**
- Facing the screen is fine for a few seconds, e.g. while walking through code statement by statement or drawing a diagram, and a brief look can lower anxiety by giving you a break from being looked at. Don't do it for longer.
- Rule of thumb: "treat the screen as one of your learners" (§8.4). If it would be uncomfortable to stare at a person that long, turn around and face the audience.

**Drawbacks**
- Going too slowly: either poor typing (fix: typing practice) or too much time checking notes for what to type next (fix: break the lesson into very short pieces so you only ever have to remember one small next step).
- Typing imports, class headers, and other boilerplate raises learners' **extraneous cognitive load** (Ch 4). If you do much of it, that may be all they remember, so give yourself and learners **skeleton code** to start from (§9.9).

## Rules
- **PRF-1**: Build teaching skill through practice and collaboration (observe colleagues, be observed, discuss afterward), not by assuming some people are born teachers. *Why:* jugyokenkyu [Gree2014]; improvement in sports and music works the same way. *Check:* Does the training plan include peer observation plus a structured debrief, not just materials? (§8.1)
- **PRF-2**: Spread a teaching practice through personal interaction and observation, not by publishing write-ups or staging demonstration lessons alone. *Why:* only 3 of 99 change stories involved active searching and 8 involved published material [Finc2007, Finc2012]; adoption is social, not rational [Bark2015]. *Check:* Does the dissemination plan put teachers in the room with the practice, or in conversation with someone who uses it? (§8.1)
- **PRF-3**: Ask for feedback on your teaching yourself rather than waiting for it. *Why:* feedback you requested is easier to accept than feedback received unwillingly. *Check:* Did the teacher set up the feedback request before or after the session? (§8.2)
- **PRF-4**: Ask specific feedback questions about one thing you have chosen to work on. *Why:* "What do you think?" is hard to answer; fixing one thing at a time makes progress visible. *Check:* Is each feedback prompt specific, such as "one thing I could have done to make this more effective"? (§8.2)
- **PRF-5**: Have a feedback translator summarise raw feedback before the teacher reads it. *Why:* a summary ("most are following, you could speed up") is easier to hear and act on than a pile of "too slow/boring" notes. *Check:* Is raw learner feedback clustered and rephrased before delivery? (§8.2)
- **PRF-6**: Write down your own assessment before reading others', then compare. *Why:* most people are harder on themselves (e.g. imagined "ums"), and comparing calibrates self-judgement. *Check:* Does the review process capture self-assessment first? (§8.2, §8.3)
- **PRF-7**: Balance positive and negative points when giving feedback. *Why:* negative feedback lands hard (Fig 8.1). The compliment sandwich is one method but gets tiresome. *Check:* Does each feedback set include both what went well and what could improve? (§8.2)
- **PRF-8**: Organise feedback on teaching with a shared rubric; the default is the 2×2 grid (went well / can be improved × content / presentation). *Why:* shared social rules make feedback more comfortable to give and receive, and a facilitator can collate items. *Check:* Is every feedback item placed in a quadrant or tied to a rubric item? (§8.2)
- **PRF-9**: Present a detailed rubric as a checklist ordered as the items will be used (opening first, closing last). *Why:* it matches the flow of the observed lesson. *Check:* Does the rubric's order follow the lesson's timeline? (§8.2)
- **PRF-10**: Hold rubrics to a question budget: to add an item, remove a less important one. *Why:* rubrics grow without limit otherwise. *Check:* Is the rubric the same length as the last version? (§8.2)
- **PRF-11**: Keep peer feedback on delivery formative, and collect feedback from learners as close to continuously as possible, prompting for questions and reflections as well as positives and negatives. *Why:* the goal is to show what is working and what to work on, not to grade. *Check:* Is there an in-lesson channel for learner feedback, not just an end-of-course form? (§8.2)
- **PRF-12**: When running peer critique (studio or master-class style), critique the critiques as well as the work. *Why:* participants learn to give and get feedback as well as the subject [Scho1984]. *Check:* Does the facilitator comment on the quality of peer feedback? (§8.2)
- **PRF-13**: Practise delivery by recording short teaching and reviewing it in threes: record all three before reviewing any, include self-feedback, delete recordings afterward, and pool points in a shared 2×2 grid. *Why:* watching yourself is the best way to improve, and the ordering protects time and eases discomfort. *Check:* Does the session plan follow the record-all-then-review-all order and provide for deletion? (§8.3)
- **PRF-14**: Tell trainees at the start of the session, not days ahead, that they will teach a short piece, and physically separate recording groups. *Why:* advance notice causes over-preparation and fretting; cross-talk ruins audio. *Check:* Is the announcement timed at session start, with one group per space (2–3 per room)? (§8.3)
- **PRF-15**: Find out your tells and displace them rather than trying to eliminate them. *Why:* elimination is impossible and leads to obsessing. *Check:* Has the teacher named a replacement habit (e.g. scrunching toes)? (§8.3)
- **PRF-16**: Teach programming by live coding rather than walking through code on slides. *Why:* it is more compelling, responsive to "what if?", enables lateral transfer, slows the teacher, keeps load down, and models debugging and the acceptability of errors [Rubi2013, Haar2017]. *Check:* Is code built up in front of learners rather than revealed slide by slide? (§8.4)
- **PRF-17**: Embrace mistakes made during live coding: diagnose and fix them aloud. Prefer twitch coding to forced deliberate fumbles. *Why:* debugging dominates novices' time but is missing from textbooks, and visible mistakes give learners permission to err. *Check:* When an error occurs, does the teacher narrate the diagnosis instead of silently fixing it or skipping ahead? (§8.4)
- **PRF-18**: Ask learners to predict what code will do before running it, optionally collecting several predictions and taking a class vote. *Why:* it keeps attention on task and practises reasoning about code [Mill2013]. *Check:* Are there prediction prompts at run points in the plan? (§8.4, §9.11)
- **PRF-19**: Narrate every action, point at command and output and go over it a second time, never copy-paste code, say tab completion aloud at first, and re-display output that scrolled away. *Why:* this lets learners keep up and copy you. *Check:* Does the script contain any paste-in blocks? Is there a "say, then point" beat for each command? (§8.4)
- **PRF-20**: Be visible and audible: stand if able, move around, use a microphone. *Why:* sitting hides you from the back rows, movement draws attention, and a mic saves your voice and helps people with hearing difficulties. *Check:* Has the organiser been asked for a lectern or standing desk and a mic? (§8.4)
- **PRF-21**: Teach from an environment that mirrors learners' (default prompt, colours, shortcuts), e.g. a separate bare-bones account. *Why:* learners don't have your customisations. *Check:* Would a learner's screen look the same as yours? (§8.4)
- **PRF-22**: Make the screen readable from the back: large font, maximised window, a thumbs-up/down readability check, dark text on a lightly tinted background, suitable lighting, windows raised above head height, a second screen if available, and accessibility aids for cursor and keystrokes. *Why:* learners can't follow code they can't see. *Check:* Was the room tested from the back row before class? (§8.4)
- **PRF-23**: Announce every mode switch in a console (entering or leaving an editor or interpreter). *Why:* novices are confused by one window with "multiple personalities". *Check:* Is each mode change marked in the script? (§8.4)
- **PRF-24**: Keep your notes and the shared notes on a second device, and carry printouts as backup. *Why:* more reliable than flipping virtual desktops. *Check:* Is the projected screen free of notes windows? (§8.4)
- **PRF-25**: Use diagrams, preferably sketched step by step on the board as you go. *Why:* incremental building aids retention (§4.1) and allows improvisation. *Check:* Does the plan mark where diagrams are drawn? (§8.4)
- **PRF-26**: Turn off notifications, or teach from an account with no email or social tools. *Why:* pop-ups distract everyone and can expose private messages. *Check:* Has a do-not-disturb or teaching account been set up? (§8.4)
- **PRF-27**: Stick to the lesson plan the first time you teach it; improvise only once familiar, and rehearse any off-plan material on the teaching machine beforehand. *Why:* untested detours hit unexpected problems you then have to explain. *Check:* Is this a first delivery? If so, are there unplanned "neat tricks"? (§8.4)
- **PRF-28**: Face the screen only for a few seconds at a time; treat it like a learner you wouldn't stare at. *Why:* the audience loses connection with you. *Check:* In a recording, are there long stretches with the teacher's back to the class? (§8.4)
- **PRF-29**: Keep live-coding pace up with typing practice and very small lesson steps, and supply skeleton code instead of typing boilerplate live. *Why:* slowness loses learners, and boilerplate adds extraneous load that may become all they remember (Ch 4, §9.9). *Check:* Does the demo spend time typing imports, headers, or setup? (§8.4)

## Procedures

### P1. Record-and-review delivery practice (Warren Code / UBC method, §8.3)
1. At the **start** of the session, tell participants they will each teach a two-minute piece; let them pick a key idea from their own teaching or work.
2. Form groups of three. Send groups to separate spaces (at most 2–3 per normal classroom; use breakout rooms, lounges, offices).
3. Round 1: A teaches (2 min, pitched at high-school students), B is the attentive audience, C records on a phone. Rotate so each person plays each role. **Do not review between rounds.**
4. When all three are recorded, the group watches all three videos together.
5. Each person gives feedback on all three videos, including their own (write your self-assessment first, PRF-6).
6. Delete the videos.
7. Return to the main group; each group adds points to a shared 2×2 grid (positive/negative × content/presentation). Optionally take one point per participant, no duplicates, without saying who made it or whom it's about (see exercise "Practice Giving Feedback").
8. Decision point: if time is short, cut the video count rather than switching to teach-review-teach-review.

### P2. 2×2 grid feedback session (§8.2, §8.5)
1. Draw the grid: rows "what went well" / "what can be improved"; columns "content" / "presentation".
2. Observers write one comment per sticky note while watching.
3. After the demo, observers post notes in the matching quadrant (or add to a shared-notes table).
4. Optionally go round: each person adds one point not already on the grid.
5. A facilitator transcribes and clusters items. For the teacher, act as feedback translator (PRF-5): summarise themes in one or two sentences.
6. Discuss: what did others see that you missed? Where do you strongly agree or disagree?

### P3. Asking for feedback on your own teaching (§8.2)
1. Pick the one thing you are working on.
2. Before the session, write a specific question (e.g. "What is one thing I could have done to make this lesson more effective?" / "If you could pick one thing from the lesson to go over again, what would it be?").
3. After the session, write your self-assessment before reading any responses.
4. Have someone else read and summarise the responses for you.
5. Compare the summary with your self-assessment; adjust your calibration (e.g. "ums" nobody noticed).
6. Choose one change for next time.

### P4. Planning and running a live-coding segment (§8.4)
1. **Before:** set up a learner-like account (PRF-21); turn off notifications (PRF-26); prepare skeleton code for boilerplate (PRF-29); break the lesson into very small steps; rehearse any off-plan material on the teaching machine (PRF-27); plan prediction points (PRF-18); plan diagrams (PRF-25); arrange a lectern or standing desk, a mic, and a second screen or tablet if possible (PRF-20, PRF-24).
2. **In the room:** maximise the window, enlarge the font, use dark text on a light tint, check lighting, raise the window above head-height line, and ask for thumbs-up/down from the back (PRF-22).
3. **Each step:** say what you'll type → type it (no paste) → run → point at command and output and go over it again (PRF-19). At chosen points, ask "What will happen when I run this?" and optionally vote (PRF-18).
4. **On an error:** stop, think aloud, diagnose with the class, fix, and explain the fix (PRF-17).
5. **Mode switches:** announce "now I'm in the editor" / "back at the shell prompt" (PRF-23).
6. **Output scrolls away:** scroll back, re-run, or paste the command into shared notes.
7. **Facing:** glance at the screen briefly, then turn back to the audience (PRF-28).
8. **Experienced teacher, few natural errors?** Use twitch coding (learners dictate the next line) rather than staged fumbles.
9. **First delivery of this lesson?** Stay on plan. Later deliveries: improvise from learner questions and interests.

### P5. Building or maintaining a teaching rubric (§8.2, Presentation Rubric)
1. Start from the Presentation Rubric below (or the 2×2 grid for informal use).
2. Order items in the sequence they occur in a talk.
3. Use response columns Yes / Iffy / No / N/A; use "exists" gate items so that sections not used are N/A.
4. Apply the question budget: any addition requires a removal (PRF-10).

## Diagnostics
| Symptom (in a lesson, class, or community) | Underlying problem | Fix (rule IDs) |
|---|---|---|
| Teacher asks "Any feedback?" and gets vague or no answers | Unfocused question | PRF-3, PRF-4 |
| Teacher is crushed by one negative comment despite much praise | Unfiltered raw feedback; negativity bias (Fig 8.1) | PRF-5, PRF-6, PRF-7 |
| Teacher believes they say "um" constantly / rates self far below observers | Uncalibrated self-assessment | PRF-6, PRF-13 |
| Peer feedback is awkward, personal, or overly polite | No shared rubric or ground rules | PRF-8, PRF-12 |
| Team rubric keeps growing and nobody completes it | No question budget | PRF-10 |
| Good practices published by the department aren't adopted | Relying on write-ups or demo lessons | PRF-1, PRF-2 |
| Recording exercise overruns; last person never reviewed | Teach-review interleaving | PRF-13 |
| Trainees arrive anxious with over-prepared mini-lectures | Announced too far ahead | PRF-14 |
| Learners fall behind during a code demo | Pasting code, typing too fast, not narrating | PRF-19, PRF-29 |
| Back rows can't read code; glare | Font, colours, lighting, screen height | PRF-22 |
| Learners lost after teacher opens vim/nano or a REPL in the same window | Unannounced mode change | PRF-23 |
| Learners baffled by teacher's prompt, aliases, shortcuts | Customised environment | PRF-21 |
| Teacher hides an error and restarts, or skips it | Treating mistakes as failures | PRF-17 |
| Demo of a "neat extra trick" derails the session | Improvising before mastering material; unrehearsed | PRF-27 |
| Learners remember only the imports and boilerplate | Extraneous load from live boilerplate | PRF-29 |
| Teacher talks to the screen for minutes | Facing the screen too long | PRF-28 |
| Email or chat pop-ups appear on the projector | Notifications on | PRF-26 |
| Experienced teacher's demo is too slick; learners never see debugging | No natural mistakes left | PRF-17 (twitch coding) |

## Templates and checklists

### Feedback request prompts (§8.2)
```
- "What is one thing I could have done as a teacher to make this lesson more effective?"
- "If you could pick one thing from the lesson to go over again, what would it be?"
```

### 2×2 teaching feedback grid (§8.2, Figure 8.2)
| | Content (what was said) | Presentation (how it was said) |
|---|---|---|
| **What went well** | | |
| **What can be improved** | | |

### Live-coding pre-flight checklist (condensed from §8.4)
```
[ ] Learner-like account / environment (no custom prompt, theme, shortcuts)
[ ] Notifications off (or teaching-only account)
[ ] Font enlarged; window maximised; dark text on lightly tinted background
[ ] Readability thumbs-up/down from the back row
[ ] Room not fully dark; no light on/above screen; tables give everyone a view
[ ] Window bottom raised above learners' head height if needed
[ ] Second projector/screen (and helper to drive it) if available
[ ] Tablet/second device with notes and shared notes; printed backup
[ ] Mic; standing desk / lectern arranged with organisers
[ ] Cursor highlighter / keystroke echo tool if teaching advanced tools
[ ] Skeleton code ready for boilerplate
[ ] Lesson broken into very small steps
[ ] Prediction points marked
[ ] Diagrams planned (prepared or to sketch)
[ ] Any off-plan material rehearsed on this machine, on this network
```

### Presentation Rubric (appendix "Presentation Rubric", every item kept)
Designed for 5–10 minute recordings of people teaching with slides, live coding, or both; "use it as a starting point for creating a rubric of your own." Mark each item: Yes / Iffy / No / N/A.

| Section | Item | Yes | Iffy | No | N/A |
|---|---|---|---|---|---|
| **Opening** | Exists (use N/A for other responses if not) | ○ | ○ | ○ | ○ |
| | Good length (10–30 seconds) | ○ | ○ | ○ | ○ |
| | Introduces self | ○ | ○ | ○ | ○ |
| | Introduces topics to be covered | ○ | ○ | ○ | ○ |
| | Describes prerequisites | ○ | ○ | ○ | ○ |
| **Content** | Clear goal/narrative arc | ○ | ○ | ○ | ○ |
| | Inclusive language | ○ | ○ | ○ | ○ |
| | Authentic tasks/examples | ○ | ○ | ○ | ○ |
| | Teaches best practices/uses idiomatic code | ○ | ○ | ○ | ○ |
| | Steers a path between the Scylla of jargon and the Charybdis of over-simplification | ○ | ○ | ○ | ○ |
| **Delivery** | Clear, intelligible voice (use "Iffy" or "No" for strong accent) | ○ | ○ | ○ | ○ |
| | Rhythm: not too fast or too slow, no long pauses or self-interruption, not obviously reading from a script | ○ | ○ | ○ | ○ |
| | Self-assured: does not stray into the icky tarpit of uncertainty or the dungheap of condescension | ○ | ○ | ○ | ○ |
| **Slides** | Exist (use N/A for other responses if not) | ○ | ○ | ○ | ○ |
| | Slides and speech complement one another (dual coding) | ○ | ○ | ○ | ○ |
| | Readable fonts and colors/no overwhelming slabs of text | ○ | ○ | ○ | ○ |
| | Frequent change (something happens on screen at least every 30 seconds) | ○ | ○ | ○ | ○ |
| | Good use of graphics | ○ | ○ | ○ | ○ |
| **Live Coding** | Used (use N/A for other responses if not) | ○ | ○ | ○ | ○ |
| | Code and speech complement one another (i.e., instructor doesn't just read code aloud) | ○ | ○ | ○ | ○ |
| | Readable fonts and colors/right amount of code on the screen at a time | ○ | ○ | ○ | ○ |
| | Proficient use of tools | ○ | ○ | ○ | ○ |
| | Highlights key features of code | ○ | ○ | ○ | ○ |
| | Dissects errors | ○ | ○ | ○ | ○ |
| **Closing** | Exists (use N/A for other responses if it doesn't) | ○ | ○ | ○ | ○ |
| | Good length (10–30 seconds) | ○ | ○ | ○ | ○ |
| | Summarizes key points | ○ | ○ | ○ | ○ |
| | Outlines next steps | ○ | ○ | ○ | ○ |
| **Overall** | Points clearly connected/logical flow | ○ | ○ | ○ | ○ |
| | Make the topic interesting (i.e., not boring) | ○ | ○ | ○ | ○ |
| | Knowledgeable | ○ | ○ | ○ | ○ |

Total: 31 items in 7 sections. Each "Exists/Exist/Used" item is a gate: if the answer is No, mark the rest of that section N/A.

> **Skill note:** A feedback-reviewer skill can emit this table filled in, plus a 2×2 grid summary, plus one "focus next time" item (PRF-4). The "strong accent" note under *Delivery* is the book's wording. A skill may want to flag it for the user, since it could conflict with the inclusivity goals in Ch 10; the book itself does not discuss that tension.

## Examples
- **Japanese teaching relay** ([Gree2014], §8.1): trainees observe a master teacher, then by week three take over, each planning one subject for five days but teaching all five subjects on their day, then join a formal group debrief → lesson: improvement comes from observed practice plus structured discussion.
- **Musician analogy** (§8.1): a professional dissects half a dozen recordings of a song before performing and expects peer feedback → teaching lacks this culture in most English-speaking countries.
- **Email-search lesson** (§8.1): teacher shows regex search for addresses; audience learns editor shortcuts → lateral knowledge transfer, which jugyokenkyu harnesses between teachers.
- **"Too slow/boring" notes** (§8.2): a translator reframes them as "most are following, so you could speed up" → summaries are easier to act on.
- **"Um" and "err"** (§8.2): teachers think they say them constantly; audiences don't notice → calibrate with self-assessment before feedback.
- **Janitor's closet** (§8.3): recording groups were once placed in a storage closet to avoid audio cross-talk → physical separation matters.
- **Groans then praise** (§8.3): the recording exercise is dreaded but consistently rated among the most valuable parts of workshops.
- **Turtle tab completion** (§8.4): "turtle dot 'r' 'i' and tab to get 'right'" → narrate shortcuts.
- **VT100** (§8.4): readable fonts reduce you to 60–70 × 20–30 characters → plan for very little screen space.
- **High-school WiFi** (§8.4): installing hundreds of megabytes of updates in front of bored 16-year-olds → rehearse off-plan material on the real machine.
- **Wilson's background diagrams** (§8.4): he keeps a slide deck of diagrams behind his live-coding session, and also sketches on the board.
- **Software Carpentry vs [Kran2015]** (§8.4): Krantz says to master material so you never fix a broken example in front of the class; Software Carpentry feedback says watching the teacher err motivates most students.

## Evidence and caveats
- **Born teachers**: Wilson calls the assumption that some people are born teachers wrong; practice and collaboration are the keys (§8.1). This is argued from [Gree2014] and analogy, not from a cited effect size.
- **Dissemination**: [Finc2007, Finc2012]: of 99 change stories, 3 involved active searching for new practices and 8 involved published material; most change was local or through personal interaction. [Bark2015]: adoption is social, intuitive, and driven by student feedback rather than research.
- **Live coding effectiveness**: "research seems to back up its effectiveness" [Rubi2013, Haar2017] (§8.4). That is a hedged claim: [Rubi2013] found live coding as good as or better than static examples; [Haar2017] is "an early look" at live-streaming.
- **Time spent debugging**: "data is hard to come by"; professionals spend 25–60% of their time debugging, novices more (§8.4, §7.2).
- **Mistakes motivate**: supported by Software Carpentry workshop feedback (practitioner experience), contrary to [Kran2015]'s opinion-based advice.
- **Direct Instruction**: [Stoc2018] meta-analysis finds a statistically significant positive effect. Wilson prefers improvisation on cost grounds (DI's up-front investment), not on evidence of better outcomes. This is a stated preference that runs against the cited evidence.
- **Compliment sandwich**: offered as "a common method", with the caveat that it gets tiresome.
- **Recording exercise value**: evidence is participant ratings in Wilson's workshops ("consistently rate it as one of the most valuable parts").
- **Studio classes**: most effective when the teacher critiques both designs and peer critiques [Scho1984].
- **Tells**: often less noticeable than you think. Advice to displace rather than eliminate is practitioner guidance.
- **Coaching**: [Gawa2011] describes the value of a coach across fields. **Peer feedback practices**: [Gorm2014].
- **TPACK** [Koeh3013] refines PCK; Wilson treats it as not changing the core point [Maye2004].

## Practice exercises
- **Give Feedback on Bad Teaching** (whole class, 20 min): watch a video of bad teaching; give feedback organised as positive/negative × content/presentation; each person adds one non-duplicate point to a shared 2×2 grid; discuss what others saw that you missed and where you strongly agree or disagree.
- **Practice Giving Feedback** (small groups, 45 min): run the three-person record-and-review process (P1); the teacher then adds one point per participant to a 2×2 grid with no duplicates; participants don't say whether a point was by them, about them, or neither. Goal: get comfortable with feedback and build consensus on what to look for.
- **The Bad and the Good** (whole class, 20 min): watch a poor and a good live-coding video (they assume learners know shell variables, `head`, and the data files) and summarise both on a 2×2 grid.
- **See Then Do** (pairs, 30 min): live code 3–4 min of a lesson to a fellow trainee, then swap; don't record (hard to capture person and screen with a handheld); give 2×2-style feedback; explain beforehand what you're teaching and the assumed prior knowledge. Debrief: how did live coding feel versus lecturing? What mistakes happened and how were they handled? Talk and type at once or alternate? How often did you point at the screen or highlight with the mouse? What will you do differently?
- **Tells** (small groups, 15 min): privately note what you think your tells are; teach a 3–5 minute lesson; ask the audience how you betray nervousness; compare lists.
- **Teaching Tips** (small groups, 15 min): go through the CS Teaching Tips site's tip sheets and classify each tip as "use all the time" / "use occasionally" / "never use"; discuss where your practice differs from peers' and any tips you strongly disagree with or think ineffective.

> **Skill note:** The book links specific videos for the bad-teaching, bad/good live-coding, and (in Ch 9) pair-programming exercises. The URLs are not in the source text. A workshop-planner skill should ask the user for substitute recordings.

## Cross-references
- `07-programming-pck.md`: PCK framework this chapter builds on; novice debugging time (§7.2); why learner satisfaction is a poor proxy for learning (§7.5).
- `04-cognitive-load.md`: extraneous load from boilerplate; building diagrams step by step (§4.1).
- `05-individual-learning.md`: elaboration; hypercorrection.
- `09-in-the-classroom.md`: co-teaching (§9.3), shared notes (§9.7), sticky notes and minute cards (§9.8), skeleton/starter code (§9.9), predictions (§9.11), limiting innovation (§9.12).
- `10-motivation-and-inclusion.md`: inclusive language (rubric item), code of conduct.
- `11-teaching-online.md`: live coding and feedback in online settings.
- `13-building-community.md`: peer observation as community practice.
- `bibliography.md`: full citations for the keys above.

## Source map
| Book section | Covered under |
|---|---|
| Ch 8 intro, objectives, box "Teaching Tips" | Concepts > Chapter framing |
| §8.1 Lesson Study | Concepts §8.1; PRF-1, PRF-2; Examples |
| §8.2 Giving and Getting Feedback on Teaching (Fig 8.1, Fig 8.2, boxes "Question Budgets", "Studio Classes") | Concepts §8.2; PRF-3 to PRF-12; P2, P3, P5; Templates (prompts, 2×2 grid) |
| §8.3 How to Practice Performance (box "Tells") | Concepts §8.3; PRF-13 to PRF-15; P1 |
| §8.4 Live Coding (all subsections; boxes "Deliberate Fumbles", "Accessibility Aids Help Everyone", "Direct Instruction") | Concepts §8.4; PRF-16 to PRF-29; P4; Templates (pre-flight checklist) |
| §8.5 Exercises | Practice exercises |
| Appendix "Presentation Rubric" | Templates > Presentation Rubric; P5 |
