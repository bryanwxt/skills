# Teaching Online

> Source: Greg Wilson, *Teaching Tech Together* (2018), Ch. 11 "Teaching Online" (§11 intro, §11.1–§11.5). Licensed CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/); condensed and restructured for skill use, with quotations marked. Rule IDs use prefix `ONL`.

## When a skill needs this
- Designing or reviewing an online, MOOC-style, or self-paced course: deadlines, synchronous vs. asynchronous activities, group structure, platform choice, code of conduct.
- Planning, scripting, or critiquing instructional videos and screencasts.
- Designing a flipped or hybrid class (online material plus live sessions, or several remote sites).
- Building or advising an online learning community: forums, peer grading, peer feedback, collaborative contests, live-streamed coding.
- Pushing back on ed-tech claims ("personalized learning will replace teachers", "MOOCs will fix education").

## Key terms
| Term | Meaning (one line) |
|---|---|
| Automated instruction | Teaching with recorded video plus automatically graded exercises (the chapter's focus). |
| Online vs. automated | Distinct things: live online teaching can resemble a small-group discussion; mass teaching requires automation. |
| MOOC | Massive Open Online Course; term coined by David Cormier in 2008. |
| Connectivism | Learning theory: knowledge is distributed; learning is finding, creating, and pruning connections (glossary). |
| cMOOC | MOOC following the original connectivist model. |
| xMOOC | MOOC with centralized, hub-and-spoke, instructor-defined control; also called a "MESS". |
| MESS | "Massively Enhanced Sage on the Stage": jokey name for an xMOOC. |
| Personalized learning | Automatically tailoring lessons to individuals; usually means skipping questions after correct answers. |
| Multiple paths | Several alternative explanations of a hard point, instead of accelerating one path. |
| Positive liberty | Being actually able to do something (e.g. be heard); from Isaiah Berlin. |
| Negative liberty | Absence of rules preventing you from doing something. |
| Throttling | Limiting contributions (e.g. one message per thread per day) to make room for others. |
| Direct Instruction | Teaching by precise delivery of a meticulously designed, tested script [Stoc2018]. |
| Screencast | Recorded video of a screen, often with narration; partly like live coding. |
| Refutation / Dialog video | Video styles that state and refute misconceptions, or present them as learner–tutor talk [Mull2007a]. |
| Flipped classroom | Learners watch recorded lessons on their own; class time is for discussion and problem sets [King1993]. |
| Public / social / private worlds | What the teacher does / peer-to-peer interaction / inside each learner's head [Nuth3007]. |
| Active / constructive / logistical / content-clarification posts | Forum question categories from [Vell2017]. |
| Co-opetition | A contest combining collaboration and competition, with all submissions open [Gull2004]. |
| Two-stage project | Solve individually, then improve the solution in pairs [Batt2018]. |
| Calibrated peer review | Learners grade samples and match the teacher's grades before grading peers (glossary). |
| Shareable feedback tags | Peer comments attached at specific code locations, shareable anonymously [Cumm2011]. |
| Physical vs. social presence | Sense of being somewhere vs. sense of being with others; social matters more [Ijss2000]. |
| Levels of presence | Realism, immersion, involvement, suspension of disbelief [Ijss2000]. |
| Real-time remote instruction | Learners co-located at 2–6 sites with helpers, teacher streaming in (§11.4; §C.2). |

## Concepts

### §11 Chapter objectives
After the chapter a teacher should be able to:
- explain why expectations for MOOCs were unrealistic;
- explain personalized learning and how the term is misused;
- describe key practices of successful automated courses;
- summarize at least four features that make instructional videos engaging.

### §11 (intro) Technology and teaching
- Epigraph (variously attributed): if you use robots to teach, you teach people to be robots.
- Technology has changed teaching many times:
  - **Blackboards** (early 1800s) let teachers share improvised examples with a whole class at once, combining low cost, low maintenance, reliability, ease of use, and flexibility.
  - Hand-held **video cameras** revolutionized athletics training.
  - **Tape recorders** did the same for music instruction a decade earlier.
- The Internet is "just the latest in a long series of attempts to use machines to teach" [Watt2014]. Every new medium, from the printing press through radio, TV, desktops, and mobile, produced "aggressive optimists" who believe education is broken and technology can fix it. Ed tech's strongest advocates often knew more "tech" than "ed", and were often driven more by profit than by improving learning.
- **"Online" ≠ "automated".**
  - Live online teaching can be like leading a small-group discussion.
  - Teaching hundreds at once requires standardized, automated assessment. The learner's experience is much the same whether the automation is software or teaching assistants following a tight rubric.
- Scope: this chapter covers automated instruction (recorded video plus auto-graded exercises) and ways of combining it with live teaching.

### §11.1 MOOCs
- **History.**
  - David Cormier coined "MOOC" in 2008 for a course by George Siemens and Stephen Downes, based on **connectivism**.
  - The term was quickly co-opted by hub-and-spoke courses: the instructor at the centre defines goals, and learners receive or replicate knowledge.
  - Now **cMOOC** means the connectivist kind and **xMOOC** the centralized kind (aka MESS).
- **Strengths:**
  - learners work when convenient;
  - wider course range, because the Internet brings courses next door and online courses usually have lower direct and indirect costs.

  About five years before the book, campus talk said MOOCs would revolutionize education, destroy it, or both.
- **Why MOOCs underdelivered** [Ubel2017]:
  1. Recorded content can't clear up individual **misconceptions** (Ch. 2). If a novice doesn't understand the explanation, there usually isn't another one.
  2. The automated assessment that makes them "massive" works well **only at the lower levels of Bloom's Taxonomy**.
  3. Learners carry far more of the burden of **staying focused**.
  4. Online impersonality can **demotivate and encourage uncivil behaviour**.
- **Quality studies:**
  - [Marg2015] examined 76 MOOCs: **lesson design quality was poor**, but organization and presentation were good.
  - [Kim2017] studied 30 popular online coding tutorials. They largely teach the same content the same way: **bottom-up**, from low-level concepts to high-level goals. Most require writing programs and give immediate but **very shallow feedback**. Few explain **when and why** concepts are useful (no transfer) or give guidance on common errors. Apart from rudimentary age-based differentiation, none personalize to prior experience or goals.
- **Personalized learning** (box).
  - To most ed-tech proponents it means adjusting pace or focus by performance, in practice skipping questions after several correct answers. That yields **modest improvements** (Wilson links a RAND brief).
  - Better: for topics many learners find hard, prepare **multiple alternative explanations**, "multiple paths forward" rather than accelerating one path. This takes much more design work, perhaps why it's less popular with the tech crowd.
  - Even if it works, effects will likely be smaller than advocates believe. A good teacher makes **0.1–0.15 standard deviations** of difference in end-of-year grade-school performance [Chet2014]. It is "simply unrealistic" to expect automation to beat that any time soon.
- **Pros of the web, each with a caveat:**
  1. *More lessons, more quickly*: if search engines index them, ISPs and governments don't block them, and truth isn't drowned in disinformation.
  2. *Better lessons*: unless learners are steered to second-rate material to redistribute wealth from have-nots to haves [McMi2017]. Scarcity raises perceived value, so as online education gets cheaper it will be seen as worth less.
  3. *Access to far more people*: only if learners have and can afford the technology, and aren't driven off by harassment or marginalized for not fitting the loudest group's norms. Most MOOC users come from secure, affluent backgrounds [Hansen2015].
  4. *Detailed insight into how learners work*: only for activities amenable to large-scale automated analysis, and only if learners don't object to ubiquitous surveillance or aren't powerful enough for objections to matter.
- **Practices that accentuate the positives** [Marg2015, Mill2016a, Nils2017]:
  1. **Make deadlines frequent and well-publicized, and enforce them**, so learners get into a work rhythm.
  2. **Keep synchronous all-class activities (e.g. live lectures) to a minimum**, to avoid scheduling conflicts.
  3. **Have learners contribute to collective knowledge**: shared notes (§9.7), classroom scribes, contributed problems for shared problem sets (§5.3).
  4. **Encourage or require small-group work with synchronous online activities** (e.g. a weekly online discussion) for engagement and motivation without big scheduling headaches. Appendix F (meetings) has tips for fair, productive discussions.
  5. **Create, publicize, and enforce a code of conduct**, so everyone can *actually*, not just theoretically, take part (§1.5).
  6. **Use many short lesson episodes rather than a few lecture-length chunks.** This minimizes cognitive load, gives many chances for formative assessment, and eases maintenance: re-recording a short video is often cheaper than patching a long one.
  7. **Use video to engage rather than to instruct**, since (disabilities aside) learners read faster than you talk. *Exception:* video is the best way to teach **verbs (actions)**. Short screencasts of using an editor or stepping through a debugger beat screenshots with text.
  8. **Identify and clear up misconceptions early** (Ch. 2). If data show struggles with part of a lesson, create alternative explanations and extra practice exercises.
- **Platform.**
  - Options: an all-in-one LMS (Moodle, Sakai), or an assembled stack: Slack or Zulip for chat; Google Hangouts or appear.in for video; WordPress, Google Docs, or a wiki for collaborative authoring.
  - Starting out: use whatever needs the **least installation and administration for you** and the **least extra learning for learners**. Wilson once ran a half-day class over group text messages because that was the only tool everyone knew.
  - **Most important: ask learners what they already use.** Normal people find IRC offputting. Requiring non-experts to submit GitHub pull requests to this book was "an unmitigated disaster", even with GitHub's online editor. You ask learners to learn a lot; the least you can do is learn their preferred tools.
- **Points for improvement** (box).
  - Show learners they learn *with* you, not just *from* you, by letting them **edit your course notes**: live during lectures (§9.7), or online via a wiki, Google Doc, or anything that lets you review changes.
  - Credit people for fixing mistakes, clarifying, adding examples, and writing exercises.
  - This doesn't reduce your workload but increases engagement and the lesson's lifetime (§6.3).
- **Making an online community a community.** Most books on this rest on personal experience. Exceptions:
  - [Krau2016] is evidence-based. It predates Twitter and Facebook's descent into "weaponized abuse and misinformation", but mostly still holds.
  - [Foge2005] is useful for the community of practice learners may hope to join.
- **Freedom to and freedom from** (box). Isaiah Berlin's "Two Concepts of Liberty" (1958) distinguishes positive liberty (ability to actually do something) from negative liberty (no rule stopping you). Unchecked online discussions give negative liberty but not positive liberty: many people can't actually be heard. **Remedy: throttling**, e.g. one message per learner per thread per day. People with something to say can say it, and space is cleared for others.
- **Cheating.**
  - Day-to-day dishonesty is no more common online than face to face [Beck2014].
  - The temptation to have someone else write the final exam, and the difficulty of detecting it, is one reason institutions resist crediting pure online classes.
  - Remote proctoring (webcam) is possible, but **read [Lang2013] first**: why and how learners cheat, and how to structure courses so they have no reason to.

### §11.2 Video
- The book says "a core element of cMOOCs" is recorded video lectures (see caveats; likely meant xMOOCs).
- **Direct Instruction** (precise delivery of a well-designed script) has repeatedly been shown effective [Stoc2018] (see Ch. 8), so recorded video *can* be effective. But DI scripts must be **designed, tested, and refined very carefully**, an investment many MOOC authors haven't made.
- **Cost of change.** Editing a web page or slide deck takes minutes. Even a small change to a short video takes an hour or more, so acting on feedback can be unsupportable.
- **Video needs activities.** [Koed2015] estimated the learning benefit from extra doing to be "more than six times" that of extra watching or reading.
- **Screencasts vs. slides.** For programming, screencasts offer some of live coding's advantages (§8.4). [Chen2009] gives tips for creating and critiquing screencasts.
- **Figure 11.1, "Patterns for Screencasting" (from [Chen2009]).** A concept map (see §3.1) whose nodes are patterns and whose labelled arrows are the goals linking them. Reconstructed edges:
  - *(entry)* "Prepare to start a screencast" → **Rehearsal Script**
  - Rehearsal Script —"Decide on screen area to focus"→ **Focused View**
  - Rehearsal Script —"Insert text without making typos"→ **Prepared Text**
  - Rehearsal Script —"Pace yourself for screencasting"→ **Slower Pace**
  - Rehearsal Script —"Make a succinct screencast"→ **Short & Sweet**
  - Slower Pace ↔ Short & Sweet: "Stick to time limits"
  - Prepared Text —"Allow time to read"→ **Silent Narration**
  - Slower Pace —"Record without audio"→ **Silent Narration**
  - Silent Narration —"Show keyboard entries"→ **Keyboard Focus**
  - Focused View —"Keep viewer focused"→ **Narrow Focus**
  - Focused View —"Show mouse interactions"→ **Mouse Focus**
  - Focused View —"Show keyboard interactions"→ **Keyboard Focus**
  - "Show mouse and keyboard interactions" → both **Mouse Focus** and **Keyboard Focus**
  - Narrow Focus —"Merge different screencasts"→ **Multiple Passes**
  - Short & Sweet —"Package into"→ **Chapter Tracks**
  - Multiple Passes —"Separate important actions"→ **Chapter Tracks**
  - Multiple Passes —"Bundle extra resources"→ **Bundled Resources**
  - Multiple Passes —"Add merited visual effects"→ **Embellishments**
  - Multiple Passes —"Add static content"→ **Picture Slides**
  - Bundled Resources —"Advertise resources"→ **Embellishments**
- **Engagement findings** [Guo2014], measured by how long learners watched MOOC videos:
  1. **Shorter videos are much more engaging. Keep videos no more than six minutes.**
  2. A **talking head superimposed on slides** is more engaging than voice-over slides alone.
  3. **Personal-feeling, informal videos** can be more engaging than high-quality studio recordings, so informal settings may work better for lower cost.
  4. **Drawing on a tablet** is more engaging than PowerPoint or code screencasts. It is unclear whether that is due to motion and informality, or to less text on screen.
  5. **Speaking fairly fast is OK if the teacher is enthusiastic.**
- **Limits of [Guo2014]:**
  - *Chicken-and-egg:* do learners find a style engaging because they're used to it (a feedback loop), or because of deeper cognitive processes?
  - *No learning outcomes measured.* Learner course evaluations don't correlate with learning [Star2014, Uttl2017]. It is plausible that people don't learn from what they don't watch, but unproven that they learn from what they do watch.
- **"I'm a little uncomfortable"** (box). [Guo2014] was ethics-approved, and learners almost certainly clicked "agree" somewhere. But at the conference where it appeared, "privacy" wasn't in the title or abstract of any of dozens of papers. Wilson: "Given a choice, I'd rather not know how engaged learners are than see privacy become obsolete."
- **Video styles** [Mull2007a]. 364 first-year physics learners were assigned online multimedia treatments of Newton's First and Second Laws in four styles:
  - **Exposition:** concise lecture-style presentation.
  - **Extended Exposition:** the same plus additional interesting information.
  - **Refutation:** exposition with common misconceptions explicitly stated and refuted.
  - **Dialog:** a learner–tutor discussion of the same material as Refutation.

  **Refutation and Dialog produced the greatest learning gains** compared with Exposition. Low-prior-knowledge learners benefited most, and high-prior-knowledge learners were not disadvantaged.

### §11.3 Flipped Classrooms
- In affluent societies almost all learning has an online component: official, or via peer back-channels and "surreptitious searches for answers to homework questions". Hybrids use the strengths of both modes:
  - *In class:* instant answers to questions, but slow feedback on coding exercises (sometimes days or weeks).
  - *Online:* slow answers to questions, but immediate feedback on auto-gradable coding.
- **Intersection vs. union.** Online exercises must be more detailed because they anticipate questions. In-person lessons start with the **intersection** of what everyone needs and expand on demand. Online lessons must include the **union** of what everyone needs, because the teacher isn't there to expand.
- **Flipped classroom** (most popular hybrid). Learners watch recordings alone; class time is for discussion and problem sets. Proposed in [King1993], popularized via peer instruction (§9.2), and intensively studied since.
- **[Camp2016]: online CS1 vs. in-person flipped CS1** (students self-selected):
  - Completing unmarked practice exercises correlated with exam scores in both.
  - Online students' completion rate of rehearsal exercises was significantly lower than in-person students' lecture attendance.
  - Perceived intrinsic value of the material mattered only in the flipped section, and only after controlling for prior programming experience.
  - Test anxiety and self-efficacy mattered only online.
  - The authors recommend **improving self-efficacy by increasing instructor presence online**.
- **Recording lectures** [Nord2017]. In most cases no negative consequences. Students don't skip lectures because recordings exist, or at least no more than usual. **Benefits are greatest for early-career students** and diminish as students mature.

### §11.4 Life Online
- **Three worlds in every classroom** [Nuth3007]: the **public** (what the teacher says and does), the **social** (peer-to-peer), and the **private** (inside each learner's head). The **social is usually most important**: learners pick up as much from peers as from formal instruction.
- **Therefore the key to effective online teaching is facilitating peer-to-peer interaction.** Courses almost always have a discussion forum.
- **Forum posts** [Vell2017] (395 CS2 students, two universities), four categories:
  - **Active:** help request that shows no reasoning, and nothing about what the student tried or knows.
  - **Constructive:** shows the student's reasoning or attempts at a solution.
  - **Logistical:** policies, schedules, submission, etc.
  - **Content clarification:** asks for more information without revealing the student's thinking.

  Findings:
  - Constructive and logistical questions dominated.
  - **Constructive questions correlated with grades.**
  - Students rarely ask more than one active question per course, and active questions don't correlate with grades.
  - Expectation-setting: "most won't" have lively online communities.
- **Procrastinators** [Mill2016a, summarized]. They are especially unlikely to join forums, and reduced participation correlates with worse grades. A likely reason: they hesitate to join a discussion already under way, fearing they'll look like newcomers, so they miss peer learning and motivation.
- **Co-opetition** (box).
  - [Gull2004] contest: a problem is posted with a correct but inefficient solution. The winner is whoever contributes most to improving the overall solution's performance. All submissions are open so people borrow ideas; the final solution is almost always a hybrid of many people's ideas.
  - [Batt2018] small-scale version in an intro class: stage 1, individual submission; stage 2, pairs create an improved solution to the same problem. Two-stage projects tended to improve understanding, and students enjoyed them.
- **Peer grading** [Pare2008, Kulk2013]. Student grades agreed with expert grades **as often as experts agreed with each other**. Simple steps reduced disagreement further: filtering out obviously unconsidered responses, and structuring rubrics. Collusion and bias are not significant factors (§5.3).
- **Shareable feedback tags** [Cumm2011]. Students attach tags at specific code locations, like code review, so the reader has no navigational cost. Students controlled whether to share work and feedback anonymously.
  - Tag clouds of feedback on their own work were useful, but tags were really meaningful only in context. "The greater the separation between action and feedback, the greater the cognitive load."
  - Unexpectedly, the best and worst students shared more than middling ones.
- **Trust, but educate** (box). Usually the validity of peer feedback is measured against expert grades, but **calibrated peer review** (§5.3) can be equally effective. Learners grade samples and compare with the teacher's grades, and may grade peers only once they align. Since critical reading is an effective way to learn, Wilson speculates about a future where learners use technology to *make* judgments rather than *be judged* by it.
- **Live-streamed coding** [Haar2017] has most of live coding's benefits (§8.4). Combined with collaborative note-taking (§9.7) it comes close to an in-class experience. Wilson expects more of it.
- **Presence** [Ijss2000]. Four levels:
  1. **realism** (we can't tell the difference);
  2. **immersion** (we forget the difference);
  3. **involvement** (engaged but aware);
  4. **suspension of disbelief** (we do most of the work).

  **Physical presence** (being somewhere) is distinct from **social presence** (being with others); the latter matters more for learning. One way to foster it is to bring everyday technology into class. [Deb2018]: in-class exercises with realtime feedback on mobile devices improved concept retention and engagement and reduced failure rates.
- **Hybrid presence** (box).
  - **Works:** real-time remote instruction. Learners are co-located at 2–6 sites with helpers present while the teacher streams in (§C.2). It scales, saves travel, and is less disruptive, especially for people with family responsibilities.
  - **Doesn't work:** one group in person plus one or more remote groups. "With the best will in the world", the local participants get far more attention.
- Online teaching is "still in its infancy". [Luxt2009] surveys peer-assessment tools, and [Broo2016] describes many discussion formats, but only a handful are widely known or used.
- Closing epigraph (William Gibson): future generations will find our real-world/online distinction quaint.

## Rules
- **ONL-1** — Treat ed-tech promises sceptically: don't expect automation or "personalized learning" to outperform a good teacher. *Why:* a long history of over-promising [Watt2014, Ubel2017]; adaptive skipping gives modest gains; teacher effect is 0.1–0.15 SD [Chet2014]. *Check:* claims in the plan are matched to evidence of learning, not engagement or hype. (§11 intro, §11.1)
- **ONL-2** — Decide explicitly whether the course is *online* (live, small-group possible) or *automated* (scale requiring standardized assessment), and design for that. *Why:* they're different, and automation at scale only assesses lower Bloom levels well. *Check:* the plan states the mode and which outcomes need human assessment. (§11 intro, §11.1)
- **ONL-3** — For topics many learners find hard, write several alternative explanations (multiple paths) rather than only adjusting pace. *Why:* recorded content can't otherwise address individual misconceptions; multiple paths beat acceleration. *Check:* hardest topics (from data or experience) each have at least two explanations. (§11.1)
- **ONL-4** — Set frequent, well-publicized deadlines and enforce them. *Why:* they create a work rhythm; online learners otherwise carry the full burden of focus. *Check:* a published calendar with regular deadlines and a stated enforcement policy. (§11.1)
- **ONL-5** — Minimize synchronous all-class activities, but put learners in small groups with a regular synchronous activity (e.g. a weekly online discussion). *Why:* avoids scheduling conflicts while keeping engagement and motivation. *Check:* there are no or few all-class live events, and every learner belongs to a small group with a scheduled meeting. (§11.1)
- **ONL-6** — Have learners build collective knowledge: shared or editable notes, scribes, contributed problems, credited fixes to course notes. *Why:* learning *with* you increases engagement and lesson lifetime (§9.7, §5.3, §6.3). *Check:* there is a mechanism and a credit policy for learner contributions. (§11.1)
- **ONL-7** — Create, publicize, and enforce a code of conduct for online spaces. *Why:* so everyone can actually, not just theoretically, take part; online impersonality encourages incivility. *Check:* the CoC is linked from every discussion space and an enforcer is named. (§11.1)
- **ONL-8** — Throttle discussion where a few voices dominate (e.g. one message per learner per thread per day). *Why:* gives positive liberty (being heard), not just negative liberty. *Check:* the forum rules include a participation limit or equivalent. (§11.1)
- **ONL-9** — Chunk content into many short episodes; keep each video to six minutes or less. *Why:* lower cognitive load, more formative-assessment points, cheaper maintenance [Guo2014]. *Check:* list video durations; flag any over six minutes. (§11.1, §11.2)
- **ONL-10** — Use video to engage, not to deliver text-like content; use short screencasts to teach actions ("verbs"). *Why:* learners read faster than you talk; video is best for showing how to do things. *Check:* each video either shows a procedure or builds engagement; explanatory content is also in text. (§11.1)
- **ONL-11** — Use learner data to find misconceptions early, and respond with alternative explanations and extra exercises. *Why:* recorded content can't otherwise clear misconceptions (Ch. 2). *Check:* there is a plan for which data are reviewed, when, and what gets added. (§11.1)
- **ONL-12** — Choose the platform learners already use and that needs the least setup on both sides; never impose expert tools (IRC, pull requests) on non-experts. *Why:* Wilson's PR-based contributions were "an unmitigated disaster"; learners are already learning a lot. *Check:* learners were asked about their tools, and setup steps are counted. (§11.1)
- **ONL-13** — Before investing in proctoring, restructure the course to remove reasons to cheat. *Why:* everyday online cheating is no more common [Beck2014]; course design drives cheating [Lang2013]. *Check:* high-stakes single exams are minimized and assessments are aligned with outcomes. (§11.1)
- **ONL-14** — Pair every video with something learners *do*. *Why:* doing is estimated to be more than six times as beneficial as extra watching or reading [Koed2015]. *Check:* every video is followed by an exercise or activity. (§11.2)
- **ONL-15** — Budget for scripting, testing, and refining a video before recording, and expect edits to be expensive. *Why:* Direct Instruction works only with carefully refined scripts [Stoc2018]; even small video changes take an hour or more. *Check:* the script was trialled (e.g. delivered live) before recording; short videos keep re-recording cheap. (§11.2)
- **ONL-16** — Produce videos for engagement: a talking head over slides; informal, personal settings over studio polish; tablet drawing where suitable; an enthusiastic delivery (fairly fast speech is OK). *Why:* [Guo2014] engagement findings. *Caveat:* engagement isn't learning, and the effects may be habit. *Check:* style choices are listed and learning is measured separately. (§11.2)
- **ONL-17** — In instructional video, state common misconceptions and refute them explicitly, or use a learner–tutor dialogue, rather than plain exposition. *Why:* Refutation and Dialog gave the greatest gains, mostly for novices, without hurting experts [Mull2007a]. *Check:* the script names at least one misconception and refutes it. (§11.2)
- **ONL-18** — Make screencasts with the [Chen2009] patterns: rehearsal script, focused or narrow view, prepared text (no live typos), slower pace, short and sweet, silent narration where useful, visible mouse and keyboard actions, multiple passes, chapter tracks, bundled resources, merited embellishments only. *Why:* a pattern language of screencasting tips. *Check:* T2 checklist. (§11.2)
- **ONL-19** — Write online materials to cover the *union* of what learners need (anticipate questions); in person, start from the *intersection* and expand on demand. *Why:* no teacher is present online to expand. *Check:* online exercises include hints or FAQs for anticipated questions. (§11.3)
- **ONL-20** — In flipped or online courses, increase visible instructor presence to raise learners' self-efficacy. *Why:* self-efficacy and test anxiety mattered only for online learners [Camp2016]. *Check:* scheduled instructor touchpoints (videos, forum replies, office hours) are planned. (§11.3)
- **ONL-21** — Provide lecture recordings; don't withhold them for fear of absence. *Why:* no attendance drop on average; biggest benefit for early-career students [Nord2017]. *Check:* the recording policy is stated. (§11.3)
- **ONL-22** — Design online courses around peer-to-peer interaction, and set realistic expectations for forum activity. *Why:* the social world matters most [Nuth3007]; most course forums won't be lively [Vell2017]. *Check:* structured peer activities exist beyond "there's a forum". (§11.4)
- **ONL-23** — Encourage constructive questions (show your reasoning and attempts). *Why:* constructive questions correlate with grades; active (no-reasoning) ones don't [Vell2017]. *Check:* the forum guidelines or template ask posters to share what they tried and think. (§11.4)
- **ONL-24** — Draw procrastinators and late-joiners into discussions early, and make joining late feel normal. *Why:* fear of being a newcomer in an ongoing thread keeps them out, correlating with worse grades [Mill2016a]. *Check:* there are early required posts, fresh threads per unit, or explicit welcomes for late joiners. (§11.4)
- **ONL-25** — Use collaborative or two-stage formats (open co-opetition contests; individual then paired rework). *Why:* hybrid solutions emerge [Gull2004]; two-stage projects improved understanding and enjoyment [Batt2018]. *Check:* at least one project has a collaborative second stage. (§11.4)
- **ONL-26** — Use peer grading with structured rubrics, filter unconsidered responses, and calibrate graders first. *Why:* peer grades match experts as often as experts match each other [Pare2008, Kulk2013]; calibrated peer review is as valid (§5.3). *Check:* rubric, filtering step, and calibration samples exist. (§11.4)
- **ONL-27** — Attach feedback at the exact location it concerns (in-line, code-review style), not in detached summaries. *Why:* separation between action and feedback raises cognitive load; tags are meaningful only in context [Cumm2011]. *Check:* the feedback tool supports location-anchored comments. (§11.4)
- **ONL-28** — Consider live-streamed coding with collaborative notes to approximate in-class experience. *Why:* it keeps live coding's benefits [Haar2017]. *Check:* if streaming, a shared-notes doc is set up. (§11.4)
- **ONL-29** — Foster social presence over physical realism, e.g. bring learners' everyday devices into exercises with realtime feedback. *Why:* social presence matters more [Ijss2000]; mobile realtime exercises improved retention and reduced failure [Deb2018]. *Check:* the plan names how learners will feel "with others". (§11.4)
- **ONL-30** — For hybrid delivery, make *all* groups remote (co-located sites with local helpers); never mix one in-person group with remote groups. *Why:* local participants inevitably get far more attention. *Check:* the delivery topology has no privileged in-room group. (§11.4)
- **ONL-31** — Weigh learner privacy before collecting engagement analytics. *Why:* Wilson would "rather not know how engaged learners are than see privacy become obsolete"; insight depends on surveillance learners may not be able to refuse. *Check:* the data collected are justified, disclosed, and minimal. (§11.1, §11.2; Wilson's stated preference)

## Procedures

### P1. Designing an automated or online course (ONL-2 to 14, 19)
1. Decide the mode: live online, automated, or flipped/hybrid. If automated at scale, list the outcomes above Bloom's lower levels that will need human or peer assessment.
2. Ask learners which tools they already use; pick the lowest-setup platform (all-in-one LMS vs. assembled chat, video, and docs).
3. Chunk content into short episodes (videos of six minutes or less), each followed by an exercise.
4. Write material for the *union* of needs: anticipate questions and add hints.
5. Set a frequent deadline calendar; publicize and enforce it.
6. Minimize all-class live events; form small groups with a weekly synchronous discussion.
7. Publish the code of conduct; consider throttling rules for forums.
8. Add collective-knowledge mechanisms (editable notes, contributed problems) with credit.
9. Plan peer interaction: forum guidelines asking for constructive questions; early posting; peer review with calibration.
10. Instrument for misconceptions (with privacy in mind). Schedule reviews; when a topic shows trouble, add alternative explanations and exercises.
11. Design assessments to remove incentives to cheat before considering proctoring.

### P2. Making an instructional video or screencast (ONL-9, 10, 14 to 18)
1. Decide whether video is the right medium: is this a *verb* (an action to show) or for engagement? If it's mainly explanation, also provide text.
2. Write a rehearsal script. Trial it (e.g. live) and refine; editing later is expensive.
3. Include at least one common misconception, stated and refuted, or present it as a learner–tutor dialogue.
4. Plan for six minutes or less; split longer content into chapter tracks.
5. Set up: choose the screen area (focused or narrow view); enlarge it; prepare text to paste so you don't make typos; plan a slower pace.
6. Record. Consider recording silently and narrating afterwards. Show mouse and keyboard actions visibly. Talking head over slides or tablet drawing; informal setting is fine; be enthusiastic.
7. Edit: merge multiple passes; separate important actions into chapters; add only merited visual effects; add static picture slides where useful; bundle and advertise extra resources (code files, transcripts).
8. Accessibility: narrate on-screen action, and provide code as text and captions (see `10-motivation-and-inclusion.md` MOT-20).
9. Attach a follow-up activity.
10. Measure learning, not just watch-time.

### P3. Setting up a flipped class (ONL-19 to 21)
1. Move exposition to short recorded pieces, each with a practice exercise (unmarked practice still correlates with exam scores).
2. Use class time for discussion, problem sets, and peer instruction (§9.2).
3. Add instructor presence online (short personal videos, forum replies) for self-efficacy.
4. Record live sessions and share them.

### P4. Running hybrid or remote delivery (ONL-28 to 30)
1. Prefer co-located learner groups at 2–6 sites, each with a local helper; the teacher streams in.
2. Never mix a single in-room group with remote groups.
3. Use live-streamed coding plus a shared collaborative notes document.
4. Bring learners' own devices into realtime exercises to build social presence.

## Diagnostics
| Symptom (in a lesson, class, or community) | Underlying problem | Fix (rule IDs) |
|---|---|---|
| High enrolment, low completion; learners drift | No rhythm; learner carries all focus burden | ONL-4, ONL-5, ONL-20 |
| Novices stuck on the same point, no way forward | Single explanation can't address misconceptions | ONL-3, ONL-11, ONL-17 |
| Course only assesses recall | Automated assessment limited to low Bloom levels | ONL-2, ONL-26 |
| Long lecture videos, low watch-through | Videos too long or instructing instead of engaging | ONL-9, ONL-10, ONL-16 |
| Learners watch but can't do | No activities paired with video | ONL-14 |
| Video errors persist because fixing is costly | Long videos; unrefined script | ONL-9, ONL-15 |
| Screencasts hard to follow (typos, tiny text, invisible clicks) | Screencast patterns ignored | ONL-18 |
| Forum dominated by a few loud voices; harassment | No code of conduct; negative liberty only | ONL-7, ONL-8 |
| Forum posts are "it doesn't work, help" | Active questions; no norm of showing reasoning | ONL-23 |
| Late joiners never post | Newcomer aversion among procrastinators | ONL-24 |
| Learners refuse to use course tools | Expert tools imposed (IRC, PRs) | ONL-12 |
| Remote participants feel second-class | Mixed in-person/remote format | ONL-30 |
| Online learners anxious and low self-efficacy | Little instructor presence | ONL-20 |
| Course designed around engagement analytics | Engagement ≠ learning; privacy cost | ONL-16, ONL-31 |
| Demand for webcam proctoring | Course incentivizes cheating | ONL-13 |
| Peer grades distrusted | No rubric, filtering, or calibration | ONL-26 |
| Feedback ignored or misunderstood | Feedback detached from code location | ONL-27 |

## Templates and checklists

### T1. Online course design checklist (§11.1 practices plus platform guidance)
```
[ ] Frequent, well-publicized, enforced deadlines
[ ] Minimal synchronous all-class activities
[ ] Learners contribute to collective knowledge (shared notes / scribes / problem sets), with credit
[ ] Small groups with a regular synchronous activity (e.g., weekly online discussion)
[ ] Code of conduct created, publicized, enforced
[ ] Many short episodes (videos of six minutes or less), each with formative assessment
[ ] Video used to engage or to show actions ("verbs"), not as a text substitute
[ ] Misconceptions identified early from data -> alternative explanations + extra exercises
[ ] Platform = what learners already use; least setup for teacher and learners
[ ] Materials cover the union of needs (anticipated questions)
[ ] Instructor presence planned (self-efficacy)
[ ] Lecture recordings provided
[ ] Forum norms: show reasoning; welcome late joiners; throttling if needed
[ ] Peer grading uses rubric + filtering + calibration
[ ] Assessment designed to remove cheating incentives before proctoring
[ ] Analytics collected only as justified; privacy considered
```

### T2. Screencast checklist (patterns of Fig 11.1, [Chen2009])
```
Before recording
[ ] Rehearsal Script written and rehearsed
[ ] Focused View: screen area chosen; Narrow Focus to keep viewer on task
[ ] Prepared Text ready to insert (no live typos); allow time to read it
[ ] Slower Pace planned; Short & Sweet: stick to time limits
Recording
[ ] Silent Narration option: record without audio, narrate after
[ ] Mouse Focus / Keyboard Focus: mouse and keyboard interactions visible
[ ] Multiple Passes: merge different takes
After recording
[ ] Chapter Tracks: package into chapters; separate important actions
[ ] Bundled Resources: extra files bundled and advertised
[ ] Embellishments: only merited visual effects
[ ] Picture Slides: static content added where helpful
```

### T3. Video style decision (§11.2)
| Goal | Use | Evidence |
|---|---|---|
| Show how to do an action | Short screencast | §11.1 ("verbs") |
| Address a known misconception | Refutation or Dialog style | [Mull2007a] |
| Maximize engagement | ≤6 min, talking head + slides, informal, tablet drawing, enthusiastic | [Guo2014] (engagement only) |
| Convey reference or explanatory text | Text (learners read faster than you talk) | §11.1 |

### T4. Forum post categories and a constructive-question prompt ([Vell2017])
```
Categories: Active (no reasoning shown) | Constructive (reasoning/attempts shown) |
            Logistical (policies, schedule, submission) | Content clarification (asks for info, no own thinking)
Prompt for posters (to encourage Constructive):
  What are you trying to do?
  What did you try, and what happened?
  What do you think is going wrong, and why?
```

### T5. Web pros and caveats (§11.1), for evaluating ed-tech proposals
| Claimed benefit | Caveat to check |
|---|---|
| More lessons, faster | Indexed? Not blocked? Not drowned in disinformation? |
| Better lessons | Not steering have-nots to second-rate material [McMi2017]? Cheapness lowers perceived value |
| Access to more people | Learners have and can afford the tech? Not driven off by harassment? MOOC users mostly affluent [Hansen2015] |
| Insight into learners | Only for auto-analysable work; relies on surveillance learners may be unable to refuse |

### T6. Peer grading setup (§11.4, §5.3)
```
1. Structured rubric
2. Calibration: graders score samples; compare to teacher; start grading peers once aligned
3. Filter obviously unconsidered responses
4. Feedback anchored at specific code locations; learner controls anonymous sharing
```

## Examples
- **Blackboards, video cameras, tape recorders** (§11 intro). Earlier technologies genuinely transformed teaching because they were cheap, reliable, and flexible. Lesson: judge new tech on such properties, not on hype.
- **Group text messages** (§11.1). Wilson ran a half-day class over group SMS because everyone already knew it. Lesson: the learners' familiar tool beats the "right" tool.
- **GitHub PRs for this book** (§11.1). Asking non-experts to submit pull requests was "an unmitigated disaster". Lesson: don't impose expert workflows.
- **Coding tutorials** [Kim2017] (§11.1). 30 tutorials: bottom-up, shallow feedback, no transfer, no personalization. Lesson: a checklist of what online lessons usually miss.
- **Physics video styles** [Mull2007a] (§11.2). Refutation and Dialog beat Exposition. Lesson: name and refute misconceptions in video.
- **Online vs. flipped CS1** [Camp2016] (§11.3). Self-efficacy mattered online only. Lesson: increase instructor presence.
- **Co-opetition contest** [Gull2004] and **two-stage projects** [Batt2018] (§11.4). Open, borrowing-friendly competition produced hybrid solutions; individual-then-pair rework improved understanding.
- **Real-time remote instruction** (§11.4, §C.2). Wilson taught 2–6 co-located sites with helpers successfully; mixed in-room plus remote failed to treat remote learners equally.

## Evidence and caveats
- **MOOC disappointment:** [Ubel2017] is a brief article. [Marg2015] (76 MOOCs: poor lesson design, good organization). [Kim2017] (30 tutorials).
- **Personalized learning:** "modest improvements" (RAND brief linked). Teacher effect 0.1–0.15 SD [Chet2014]. The claim that automation won't beat this soon is Wilson's judgement.
- **MOOC users mostly affluent:** [Hansen2015].
- **Cheating no more common online:** [Beck2014].
- **Direct Instruction effective:** [Stoc2018] meta-analysis.
- **Doing > watching ("more than six times"):** [Koed2015], presented as an estimate.
- **Video engagement:** [Guo2014]. Explicitly limited by Wilson: engagement measured as watch time; possible habituation loop; no learning outcomes; course evaluations don't track learning [Star2014, Uttl2017]. The tablet-drawing finding has unclear cause. The bibliography annotation summarizes [Guo2014] as "talking heads are more engaging than tablet drawings", while the text says tablet drawing beats PowerPoint or code screencasts. These compare different pairs, so there's no direct contradiction, but don't over-rank tablet drawing.
- **Refutation and Dialog:** [Mull2007a], 364 physics learners. Presented as a solid finding.
- **Flipped classroom:** [King1993] origin; [Camp2016] is a self-selected comparison (students *chose* online).
- **Recordings don't reduce attendance:** [Nord2017] (a preprint, psyarxiv).
- **Social world matters most:** [Nuth3007] (Nuthall, 2007; the key has a typo year).
- **Forum categories:** [Vell2017], 395 CS2 students.
- **Peer grading ≈ expert grading:** [Pare2008, Kulk2013]. Collusion and bias not significant (§5.3).
- **Feedback tags:** [Cumm2011].
- **Presence:** [Ijss2000] is conceptual. [Deb2018] mobile realtime exercises improved retention and engagement and reduced failure.
- **Wilson's stated opinions:** prefers privacy over engagement data; online teaching is "in its infancy"; expects more live streaming. The intersection-vs-union observation is from his own experience ("I find").
- **Possible text errors:**
  - "A core element of cMOOCs is their reliance on recorded video lectures": by §11.1's own definitions, this describes xMOOCs.
  - The intro says "the next chapter" will combine automated and live teaching, but that material is §11.3–§11.4 in this chapter; Ch. 12 is Exercise Types.

## Practice exercises
- **Give Feedback on a Bad Screencast** (whole class, 20 min). Watch a provided screencast; give feedback on a 2×2 of positive/negative × content/presentation; each person adds one non-duplicate point to a shared grid; compare with the checklist in Appendix J.
- **Two-Way Video** (pairs, 10 min). Record a 2–3 minute video of yourself doing something; swap and watch each other's at 4× speed; note what's hard to follow or missed.
- **Viewpoints** (individual, 10 min). Using [Irib2009]'s disciplinary lenses on online-community success (Business: loyalty, brand, extrinsic motivation; Psychology: sense of community, intrinsic motivation; Sociology: group identity, physical community, social capital, collective action; CS: technical implementation), identify your closest and most distant perspective.
- **Helping or Harming** (small groups, 30 min). Read Susan Dynarski's NYT article on schools moving students who fail in-person courses into online ones; propose 2–3 compensating measures with per-student cost estimates; compare across groups; estimate the teaching positions cut to fund the top ideas for 100 students; decide as a class whether it's a net benefit. Wilson notes that budgeting exercises reveal who is serious about change.

## Cross-references
- `01-introduction-and-motivation-to-teach.md`: Code of Conduct (§1.5).
- `02-mental-models.md`: misconceptions, and why recorded content can't clear them.
- `03-expertise-and-memory.md`: concept maps (Fig 11.1 is one).
- `04-cognitive-load.md`: short episodes; feedback separation raises load.
- `05-individual-learning.md`: peer assessment, calibrated peer review, contributed problem sets (§5.3).
- `06-lesson-design.md`: Bloom's taxonomy; lesson lifetime and maintenance (§6.3).
- `08-teaching-as-performance.md`: live coding (§8.4); Direct Instruction.
- `09-in-the-classroom.md`: peer instruction (§9.2); collaborative note-taking (§9.7).
- `10-motivation-and-inclusion.md`: retention drivers that are hard to replicate online; online demotivation [Ford2016]; video accessibility; Code of Conduct template.
- `12-exercise-types.md`: auto-gradable exercise types; auto-grading feedback.
- `13-building-community.md`: online communities, meetings (Appendix F), real-time remote instruction (§C.2).

## Source map
| Book section | Covered under |
|---|---|
| §11 objectives, intro (history, online vs automated) | Concepts §11 intro; ONL-1, ONL-2 |
| §11.1 MOOCs (cMOOC/xMOOC, failures, [Marg2015], [Kim2017]) | Concepts §11.1; ONL-1 to ONL-3 |
| §11.1 box "Personalized Learning" | Concepts; ONL-1, ONL-3 |
| §11.1 pros and cons of the web | Concepts; T5; ONL-31 |
| §11.1 practices list | ONL-4 to ONL-11; T1; P1 |
| §11.1 platform choice | ONL-12 |
| §11.1 box "Points for Improvement" | ONL-6 |
| §11.1 community ([Krau2016], [Foge2005]) | Concepts §11.1 |
| §11.1 box "Freedom To and Freedom From" | ONL-8 |
| §11.1 cheating | ONL-13 |
| §11.2 Video (DI, cost, [Koed2015]) | ONL-14, ONL-15 |
| §11.2 Fig 11.1 [Chen2009] | Concepts §11.2; ONL-18; T2; P2 |
| §11.2 [Guo2014] and limits | ONL-9, ONL-16; Evidence |
| §11.2 box "I'm a Little Uncomfortable" | ONL-31 |
| §11.2 [Mull2007a] | ONL-17; T3 |
| §11.3 Flipped Classrooms | Concepts §11.3; ONL-19 to ONL-21; P3 |
| §11.4 Life Online ([Nuth3007], [Vell2017], [Mill2016a]) | ONL-22 to ONL-24; T4 |
| §11.4 box "Co-opetition" | ONL-25 |
| §11.4 peer grading, tags, box "Trust, but Educate" | ONL-26, ONL-27; T6 |
| §11.4 streaming, presence, box "Hybrid Presence" | ONL-28 to ONL-30; P4 |
| §11.5 Exercises | Practice exercises |
