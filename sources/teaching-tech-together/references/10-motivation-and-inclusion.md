# Motivation, Demotivation, Accessibility, and Inclusion

> Source: Greg Wilson, *Teaching Tech Together* (2018), Ch. 10 "Motivation and Demotivation" (§10 intro, §10.1–§10.5), appendix "Code of Conduct". Licensed CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/); condensed and restructured for skill use, with quotations marked. Rule IDs use prefix `MOT`.

## When a skill needs this
- Reviewing a lesson, workshop plan, or slide deck for things that will demotivate or exclude learners (wording, examples, setup steps, classroom behaviour).
- Choosing what to teach first in a curriculum, or replacing toy examples with authentic tasks.
- Writing an accessibility or inclusivity checklist for an event or for online materials.
- Drafting or adopting a Code of Conduct for a class, workshop, or online course.
- Coaching a teacher on handling impostor syndrome (their own or learners'), "geek gene" talk, or deficit-model thinking.

## Key terms
| Term | Meaning (one line) |
|---|---|
| Extrinsic motivation | Doing something to earn a reward or avoid punishment (book glossary). |
| Intrinsic motivation | Doing something because it is personally rewarding; we learn best this way [Wlod2017]. |
| Self-determination theory | Says intrinsic motivation is driven by competence, autonomy, and relatedness (§10 intro). |
| Competence / Autonomy / Relatedness | Knowing what you're doing / controlling your own destiny / feeling connected to others. |
| Constructive alignment | Approach in [Bigg2011] that brings learning activities and learning outcomes into line with each other. |
| Authentic task | Something learners believe they would actually do in real life; glossary adds: learners construct their own answers, using real tools and data. |
| Media computation | Georgia Tech approach where first programs manipulate images, sound, and so on [Guzd2013]. |
| Learned helplessness | After repeated negative feedback they can't change, people stop trying to change even what they could. |
| Productive failure | Deliberately giving learners problems they can't yet solve, so they must acquire new knowledge [Kapu2016]. |
| Impostor syndrome | Believing you aren't good enough and your successes are flukes, and fearing you'll be found out. |
| Stereotype threat | Anxiety about confirming a negative stereotype of your group, which lowers performance [Stee2011]. |
| Fixed / growth mindset | Belief that ability is innate / belief that ability is learned and improvable (Dweck). |
| Geek gene | The folk belief that some people are natural programmers; refuted by [Pati2016]. |
| Accessibility | Equal access to lessons and exercises for people with disabilities. |
| *Nihil de nobis, sine nobis* | "Nothing for us without us": involve disabled people in decisions. |
| Curb-cut effect | Accommodations made for disabled people end up helping everyone (§10.3 box "It Helps Everyone"). |
| Inclusivity | A policy of including people who might otherwise be excluded or marginalized. |
| Community representation | Highlighting learners' social identities, histories, and community networks in computing activities [Lach3018]. |
| Computational integration | Using ideas from the learner's community in computing, e.g. reverse-engineering indigenous designs [Lach3018]. |
| Spoons | Christine Miserandino's metaphor for the limited daily energy of people with chronic illness. |
| Deficit model | Belief that under-represented groups lack something and so are responsible for not getting ahead. |
| Leaky pipeline | A metaphor the book says to stop using [Mill2015]. |
| Preparatory privilege | Advantage from a background that better prepares you for a learning task (glossary; §9.5). |
| Group signup | Learners register for a workshop together with people they trust. |
| Code of Conduct | Published rules of behaviour for an event. Its existence and enforcement matter most. |

## Concepts

### §10 Chapter objectives
After the chapter a teacher should be able to:
- explain intrinsic vs. extrinsic motivation;
- name and describe three ways teachers can demotivate learners;
- define impostor syndrome and describe ways to combat it;
- explain stereotype threat and fixed vs. growth mindset, how strong the evidence for each is, and what each implies for teaching;
- describe and enact three things that make classes more accessible;
- describe and enact three things that make classes more inclusive.

Framing: learners need encouragement to step into unfamiliar terrain. The chapter is about motivating them, but Wilson says it is *more importantly* about how teachers accidentally demotivate them.

### §10 (intro) Intrinsic and extrinsic motivation
- **Extrinsic motivation** comes from rewards and punishments. **Intrinsic motivation** comes from finding something personally rewarding. Most situations involve both: people teach because they enjoy it *and* because they get paid. We learn best when intrinsically motivated [Wlod2017].
- **Self-determination theory** names three drivers of intrinsic motivation: **competence**, **autonomy**, and **relatedness**. A well-designed lesson supports all three. Worked example: a programming exercise that (a) gives practice with every tool needed for a larger problem (competence), (b) lets learners tackle the parts in any order (autonomy), and (c) lets them talk to peers (relatedness).
- **The problem of grades** (box). Epigraph: "My audience is a rubric" (quoted by Matt Tierney). Grades distort learning and are a stock example of extrinsic motivation. But they "aren't going to go away any time soon" [Mill2016a], so building a system that ignores them is pointless. Instead:
  - [Lang2013]: courses that emphasize grades can incentivize cheating; it gives tips to reduce this.
  - [Covi2017]: balancing intrinsic and extrinsic motivation in institutional education.
  - [Bigg2011] constructive alignment: bring learning activities and learning outcomes into line with each other.
- **Evidence-based motivators.** [Ambr2010] lists evidence-based ways to motivate learners. None is surprising (e.g. "identify and reward what we value"), but checking a lesson against the list ensures it does at least a few of them. Wilson's favourite strategy: have **students who struggled but succeeded come and tell their stories**. Learners believe stories from people like themselves [Mill2016a], and past students have advice the teacher would never think of.
- **Motivating the teacher** (box "Not Just for Students"). Learners respond to a teacher's enthusiasm, and teachers, especially volunteers, must care about a topic to keep teaching it. This is another reason to **co-teach** (§9.3). Like a running partner, a teaching partner gets you going on bad days.
- **Retention drivers** [Bark2014]. Three things drove retention for *all* students:
  1. meaningful assignments;
  2. faculty interaction with students;
  3. student collaboration on assignments.

  Pace and workload relative to expectations also mattered, but mainly for male students. Interactions with teaching assistants, and with peers in extracurricular activities, did *not* drive retention. Wilson's caveat: the results look obvious, but the opposite result would also have looked obvious. Two of the drivers, faculty interaction and student collaboration, take extra effort to replicate online (Ch. 11).

### §10.1 Authentic Tasks
- Dylan Wiliam, in [Hend2017]: motivation doesn't always lead to achievement, but achievement almost always leads to motivation. Helping students succeed motivates them far more than praising them.
- **Figure 10.1 "What to Teach"** is a grid with **mean time to master** on the x-axis and **usefulness once mastered** on the y-axis.
  - Top-left (quick to master, highly useful) is labelled "teach this first".
  - Bottom-right (slow to master, little use) is labelled "don't bother".
  - The diagonal between them is labelled "argue about this".
- **Rules from the grid:**
  - Teach quick, immediately useful things first, *even if practitioners don't consider them fundamental*. Early wins build learners' confidence in their own ability and in the teacher's judgment.
  - Skip things that are hard to learn and have little near-term use.
  - Weigh topics on the diagonal against each other.
- Many foundational CS ideas, such as **recursion and computability**, sit in the "useful but hard to learn" corner. They are worth learning, but if the aim is to convince people they *can* program and that it will help with things they care about, these ideas "can and should be deferred". People often don't want to program for its own sake. They want to make music or explore changes in family incomes, and (rightly) see programming as a tax they pay to do so.
- **Media computation** [Guzd2013] is a well-studied way to put usefulness first without sacrificing fundamentals. Instead of "hello world" or summing integers, a first program might open an image, resize it into a thumbnail, and save it. That is an **authentic task**, and it has a **tangible artifact**: if the image comes out the wrong size, learners have a concrete starting point for debugging.
  - [Lee2013] adapted the approach from Python to MATLAB.
  - Similar courses exist around data science, image processing, and biology [Dahl2018, Meys2018, Ritz2018].
- **Tension.** Authentic problems pull against drills of the individual skills needed to solve them. People don't answer MCQs or do Parsons Problems outside class, just as musicians don't play scales in concerts. Finding the balance is hard. An easy first step is to make sure **exercises contain nothing arbitrary or meaningless**: no variables called `foo` and `bar`, and if learners sort lines of text, use album titles or people's names.

### §10.2 Demotivation
- Epigraph (variously attributed): women aren't leaving computing because they don't know what it's like, but because they do.
- In free-range settings, learners are volunteers who want to be there. The real problem [the EPUB prints "exercise"; see Evidence and caveats] is therefore not how to motivate them but how *not to demotivate* them, which is easy to do by accident.
- **Environmental cues** [Cher2009] (four studies). Replacing stereotypically "CS" objects in a classroom (Star Trek posters, video games) with neutral ones (nature posters, phone books) raised female undergraduates' interest in CS to the level of their male peers.
- **Wording** [Gauc2011] (three studies). Gendered wording in job recruitment materials can maintain gender inequality in male-dominated occupations.
- **The three strongest demotivators for adult learners** (Wilson cites [Wilk2011] for the unfairness point only):
  1. **Unpredictability.** If there's no reliable link between what learners do and the outcome, there's no reason to try.
  2. **Indifference.** Learners who think the teacher or system doesn't care about them or the material won't care either.
  3. **Unfairness, even when it favours the learner.** People worry, consciously or not, that they'll some day be on the losing side.
- In extreme cases learners develop **learned helplessness**.
- **Specific demotivating behaviours** (§10.2 list):
  1. **"A holier-than-thou or contemptuous attitude"** from a teacher or a fellow learner.
  2. **Telling learners their existing skills are rubbish.** For example, Unix users sneering at Windows, jokes about Excel, or calling someone's web framework out of date. Learners invested heavily in those skills, and disparaging them guarantees they won't listen to anything else you say.
  3. **Diving into complex or detailed technical discussion** with the most advanced learners in the class.
  4. **Pretending to know more than you do.** Learners trust teachers who are frank about the limits of their knowledge, and are then more likely to ask questions and seek help.
  5. **Using the J word ("just") or feigning surprise**, e.g. "I can't believe you don't know X" or "you've never heard of Y?" (see Ch. 3). This signals the problem is trivial, so the learner must be stupid.
  6. **Software installation headaches.** First contact with new tools is often demoralizing, and believing something is hard to learn is self-fulfilling. The cost isn't just setup time, or the unfairness of debugging with knowledge you don't have yet. Every such failure reinforces the belief that the old way would get them to next Thursday's deadline faster.
- **Online demotivation** is even easier. [Ford2016] found five barriers to contributing on Stack Overflow that women rated significantly more problematic than men did:
  1. lack of awareness of site features;
  2. feeling unqualified to answer questions;
  3. intimidating community size;
  4. discomfort interacting with or relying on strangers;
  5. feeling they shouldn't be "slacking", i.e. that searching online isn't "real work".

  Fear of negative feedback would have been the sixth if the statistical cutoff had been less strict. Address all of these in person and online with §10.4 methods; doing so "improves outcomes for everyone" [Sved2016]. See Evidence and caveats for the bibliography's nuance on [Sved2016].
- **Productive failure and privilege** (box). In productive failure, learners get problems they can't solve with what they know and must acquire new information to progress [Kapu2016]. Keeping learners **blocked but not frustrated** depends more on classroom culture and expectations than on exercise details. Tech's "fail fast, fail often" mantra looks similar but "is more a sign of privilege than of understanding". Only people sure of a second chance can afford to celebrate failure. Many learners, especially from marginalized or underprivileged groups, can't be sure, and talking as if they could turns them off.

#### §10.2 Impostor Syndrome
- **Definition:** believing you aren't really good enough for a job or position, that your achievements are lucky flukes, and fearing someone will find out. It is common among high achievers doing publicly visible work, and most people feel it sometimes. It **disproportionately affects under-represented groups**. [Wilc2018] (also §7.5): female students with prior computing exposure outperformed male peers in all areas of intro programming, yet were consistently less confident, partly because society keeps signalling that they don't belong.
- **Traditional classrooms fuel it.** Work is done alone or in small groups but results are shared and criticized publicly. We see others' finished work, not their struggles, so it looks as if everyone else finds it easy. Under-represented learners already under pressure to prove themselves may be hit hardest.
- **Ada Initiative guidelines for fighting your own impostor syndrome:**
  1. **Talk about it with people you trust.** Hearing that it's common makes your feelings of fraudulence harder to believe.
  2. **Go to an in-person impostor syndrome session.** You'll discover most of a room of people you respect have it ("90%").
  3. **Watch your words.** "I'm not an expert in this, but…" takes away from the knowledge you have.
  4. **Teach others about your field.** You gain confidence and help others avoid the same shoals.
  5. **Ask questions.** Getting answers ends the agony of uncertainty and fear of failure.
  6. **Build alliances.** Reassure and build up friends, who do the same for you; if they don't, find new friends.
  7. **Own your accomplishments.** Keep recording and reviewing what you've done, built, and achieved.
- **What a teacher can do for learners:**
  - **Share stories of your own mistakes** and of things you struggled to learn. This shows it's OK to find topics hard, builds trust, and makes learners confident enough to ask questions.
  - **Live code.** Your typos show you're human (§8.4).
  - **Say explicitly that you want questions.** You aren't succeeding as a teacher if nobody can follow, so you're asking learners to help you learn and improve.

#### §10.2 Stereotype Threat
- **Definition:** reminding people of negative stereotypes, even subtly, makes them anxious about confirming them, which reduces performance. [Stee2011] summarizes the research and gives classroom mitigation strategies.
- **Hedge:** unwelcoming climates demotivate everyone, especially under-represented groups, but it is "less clear" that stereotype threat is the primary cause. The term has been used in many ways [Shap2007], and key studies have replicability questions.
- **What is clear:** instructors and learners must **avoid language suggesting some people are natural programmers and others aren't**. Guzdial calls this the biggest myth about teaching CS.
- **[Pati2016] on the "geek gene"** (summarized from the abstract Wilson quotes):
  - Of 778 final-grade distributions from a large research university, only **5.8%** passed tests of multimodality.
  - When 53 CS professors were shown ambiguous histograms, those primed with "CS grades are bimodal" labelled more of them bimodal. So did professors who believed some students are innately predisposed to do better.
  - Conclusion: bimodal CS grades are **instructional folklore** produced by confirmation bias and instructors' beliefs.
- **Feedback effect.** Teachers tend to give more attention to learners who seem to be doing well. That attention raises those learners' odds, while neglect leaves others further behind [Alvi1999, Brop1983, Juss2005]. Belief in a "geek gene" therefore becomes self-fulfilling.

#### §10.2 Mindset
- Carol Dweck and others: if people believe competence is intrinsic ("have the gene or don't"), **everyone does worse, including the supposedly advantaged**. If they don't get it at first, they decide they lack aptitude, which biases future performance. If they believe a skill is learned and improvable, they do better on average.
- **Hedge (as with stereotype threat):** growth mindset may be oversold, and harder to put into practice than enthusiasts imply. [Sisk2018] ran two meta-analyses, one on mindset vs. achievement and one on mindset interventions vs. achievement. **Overall effects for both were weak.** Some results support specific tenets: low-SES or academically at-risk students might benefit from mindset interventions.

### §10.3 Accessibility
- Unequal access to lessons and exercises is "about as demotivating as it gets", and is often inadvertent. Wilson's example: his old online programming lessons put the full narration script beside the slides but **none of the Python source code**. A screen-reader user could hear what was said about the program but couldn't know what the program was.
- You can't always accommodate everyone, but you **can put a good working structure in place without knowing anyone's specific disabilities**. Preparing some accommodations in advance also signals that hosts care, and that further concerns will likely be addressed.
- **It helps everyone** (box). Curb cuts were built for physically disabled people but help people with strollers and grocery carts. Likewise, proper image captions give screen readers something to say *and* make images findable by search engines.
- **First and most important step:** involve people with disabilities in decision-making (*nihil de nobis, sine nobis*, "nothing for us without us").
- **Specific recommendations:**
  1. **Find out what you need to do.** The UK government accessibility posters give do's and don'ts for six groups: people on the autistic spectrum, screen-reader users, people with low vision, people with physical or motor disabilities, deaf or hard-of-hearing people, and people with dyslexia. (The EPUB prints "hearing exercises"; see Evidence and caveats.)
  2. **Know how well you're doing.** For example, use WebAIM to check online materials' accessibility for visually impaired users.
  3. **Don't do everything at once.** Just as learners adopt practices gradually, add one new accessibility habit each time you prepare a workshop.
  4. **Do the easy things first.** Many changes are easy and add no cognitive load for anyone: font choice, general text size, checking in advance that the room has elevator or ramp access.
- **Visual design for accessibility** [Coom2012, Burg2015]:
  - Format documents with real headings and other landmarks, not just font size and style changes.
  - Don't use color alone to convey meaning. Add cross-hatching, or use colors that differ noticeably in grayscale.
  - Remove unnecessary elements rather than making them invisible, because screen readers often still read them aloud.
  - Allow self-pacing and repetition for people with reading or hearing issues.
  - Narrate on-screen action in videos.

#### §10.3 Conduct Revisited
- Classes should enforce a Code of Conduct (§1.5; template in the appendix, reproduced below). Wilson frames it **as a form of accessibility**: closed captions make video accessible to people with hearing disabilities, and a Code of Conduct makes lessons accessible to people who would otherwise be marginalized.
- As in §9.1, the details matter, but **the most important things are that it exists and is enforced**. Rules tell people about your values and what learning experience to expect.
- **Group signup** (box). Have people sign up for workshops in groups rather than individually. Everyone then knows in advance they'll be with a few people they trust, which raises the chance they actually come. Afterwards, friends or colleagues can keep working together to use what they learned.

### §10.4 Inclusivity
- **Definition:** a policy of including people who might otherwise be excluded or marginalized. In computing, that means making a positive effort to welcome:
  - women;
  - under-represented racial or ethnic groups;
  - people of various sexual orientations;
  - the elderly;
  - the physically challenged (the EPUB prints "physically exercised");
  - the formerly incarcerated;
  - the economically disadvantaged;
  - "everyone else who doesn't fit Silicon Valley's white/Asian male demographic".
- **[Lee2017] practices.** A brief, practical, research-referenced guide. Its practices help marginalized learners but motivate everyone else too. They are phrased for term-long courses, but many apply to workshops:
  1. **Ask learners to email you before the workshop** explaining how they believe the training could help them reach their goals.
  2. **Review your notes** for gendered pronouns, and include culturally diverse names.
  3. **Emphasize that what matters is the rate at which they are learning**, not the advantages or disadvantages they started with.
  4. **Encourage pair programming.**
  5. **Actively mitigate intimidating behaviour**, e.g. jargon, or "questions" asked to display knowledge.
- **Rethinking content.** Committing to inclusive teaching may mean fundamentally rethinking content. That is a lot of work, but it can pay off. [DiSa2014a]: 65% of male African-American participants in a game-testing program went on to study computing, partly because peers respected the gaming aspect.
- **Do it carefully.** [Lach3018] explored two strategies:
  - **Community representation** highlights learners' social identities, histories, and community networks. Examples: after-school mentors or role models from learners' neighbourhoods, or projects built on community narratives and histories.
    - Main risk: **shallowness**, e.g. using computers to build slideshows instead of doing real computing.
  - **Computational integration** brings ideas from the learner's community into computing, e.g. reverse-engineering indigenous graphic designs in a visual programming environment.
    - Main risk: **cultural appropriation**, e.g. using practices without acknowledging their origins.
  - **When in doubt**, ask learners and members of their community what you ought to do, and give them control over content and direction (more in Ch. 13).

#### §10.4 Spoons
- Christine Miserandino's spoon theory (2003) explains chronic illness. Healthy people start the day with unlimited spoons. People with lupus or other debilitating conditions get only a few, and every activity costs one: getting out of bed, making a meal. Even dressing involves many hidden costs and decisions.
- Spoons are often invisible. Elizabeth Patitsas argues they behave like capital: people with many can accumulate more, while those with few struggle to get ahead.
- **Implication:** when designing classes and exercises, account for learners with **non-obvious physical or mental obstacles**. When in doubt, **ask learners**, who almost certainly know better than anyone what works for them.

#### §10.4 Moving Past the Deficit Model
- **Numbers.** Only 12–18% of CS degree recipients are women, depending on the source. That is less than half the mid-1980s share. Western countries are the odd ones out: elsewhere women are often 30–40% of CS students [Galp2002, Varm2015].
- **Figure 10.2, "Degrees Awarded and Female Enrollment" (from [Robe2017]).** A dual-axis line chart, 1975–2015. Values below are read from the figure by eye.
  - **Solid line, left axis: percentage of CS degrees awarded to women.**
    - About 17% in 1975.
    - Rises steeply to a peak of about 35–36% around 1984.
    - Falls to about 29% by 1989–91, then about 27% through the mid-1990s and about 25–27% from 1997 to 2004.
    - Drops sharply from 2005 to about 16–17% by 2009.
    - Stays flat at about 16–17% through 2015.
  - **Dashed line, right axis: total CS degrees awarded.**
    - About 5,000 in 1975.
    - Rises to a first peak of about 42,000 around 1986.
    - Falls to about 25,000 through the 1990s.
    - Rises to a second peak of about 60,000 around 2004–05.
    - Falls to about 39,000 around 2009–10.
    - Climbs to about 56,000 by 2015.
  - **Visible pattern:** both declines in the female share start at or just after the peaks of an enrollment boom (mid-1980s and mid-2000s). The share doesn't recover when totals fall or rise again. This fits Wilson's point that departments responded to enrollment booms by changing admission requirements [Robe2017].
- **Structural causes, not changes in women.** Women haven't changed drastically in thirty years, so look for structural causes:
  - home computers marketed as "boys' toys" from the 1980s [Marg2003];
  - CS departments responding to enrollment booms in the 1980s and 2000s by changing admission requirements [Robe2017].

  These factors excluded many other people too. Each seems small to the unaffected, but like water dripping on stone they erode motivation and, with it, participation.
- **First and most important fix:** stop thinking in terms of a **"leaky pipeline"** [Mill2015]. More generally, **move past the deficit model**: stop thinking under-represented groups lack something and are responsible for not getting ahead. That belief burdens people who already work harder because of inequities, and gives beneficiaries of the status quo an excuse not to examine themselves.
- **Rewriting history** (box):
  - [Abba2012]: women who shaped early computing were written out of its history.
  - [Ensm2003, Ensm2012]: programming was turned from a female into a male profession in the 1960s.
  - [Hick2018]: Britain lost its early lead in computing by systematically discriminating against its most qualified workers, women.
  - [Milt2018] reviews all three books.

  Discussing this makes some men in computing uncomfortable. Wilson's *opinion* is that this is a good reason to do it more often.
- Some problems "may not be any one person's fault, but they are everyone's responsibility":
  - misogyny in video games;
  - "cultural fit" in hiring used to excuse bias;
  - a culture of silence around harassment;
  - growing inequality that produces preparatory privilege (§9.5).

  Wilson points to an ally-skills workshop for practical advice on being a good ally in tech; see Ch. 13.

## Rules
- **MOT-1** — Design each lesson to support competence, autonomy, and relatedness. *Why:* self-determination theory; intrinsic motivation produces the best learning [Wlod2017]. *Check:* name one concrete feature for each: practice with every needed tool, learner choice of order or approach, and peer interaction. (§10 intro)
- **MOT-2** — Design with grades in mind rather than ignoring them: reduce incentives to cheat and align activities with outcomes. *Why:* grades won't go away [Mill2016a]; grade-heavy courses incentivize cheating [Lang2013]; constructive alignment [Bigg2011]. *Check:* every graded item maps to a stated learning outcome, and high-stakes, grade-only moments are minimized. (§10 intro)
- **MOT-3** — Check the lesson against the evidence-based motivation methods in [Ambr2010], and include at least a few. Where possible, invite former learners who struggled but succeeded to tell their stories. *Why:* learners believe people like themselves [Mill2016a]. *Check:* list which motivators the plan uses, and whether any peer-success story is included. (§10 intro)
- **MOT-4** — Plan for teacher motivation too; co-teach where possible. *Why:* learners respond to teacher enthusiasm, and volunteers burn out (§9.3). *Check:* does the plan name a teaching partner? (§10 intro)
- **MOT-5** — Build in meaningful assignments, direct teacher–learner interaction, and collaboration on assignments. *Why:* these drove retention for all students [Bark2014]. *Check:* each is present; online, each has an explicit mechanism (Ch. 11). (§10 intro)
- **MOT-6** — Order topics by usefulness and time to master: teach quick, immediately useful skills first, defer hard, low-near-term-use topics (even "foundational" ones such as recursion) for novices, and debate the diagonal. *Why:* early wins build confidence in self and teacher; achievement drives motivation [Hend2017]. *Check:* place each topic on the Fig. 10.1 grid; nothing from the "don't bother" corner appears early. (§10.1)
- **MOT-7** — Prefer authentic tasks with a tangible artifact, such as an image, chart, or file the learner cares about, over "hello world" toys. *Why:* learners see the point, and a wrong artifact gives a concrete debugging start [Guzd2013]. *Check:* would a learner believe they'd do this outside class? Does it produce something they can see? (§10.1)
- **MOT-8** — Remove anything arbitrary or meaningless from exercises and examples: no `foo`/`bar`, and use relatable data. *Why:* it eases the tension between drills and authenticity at no cost. *Check:* scan for placeholder names and meaningless data. (§10.1)
- **MOT-9** — Audit the physical and online environment, and all recruitment and lesson wording, for stereotypical cues and gendered language. *Why:* subtle cues measurably change who is interested [Cher2009, Gauc2011]. *Check:* list posters, imagery, and gender-coded words, and replace stereotypical ones. (§10.2)
- **MOT-10** — Make outcomes predictable, show you care, and treat everyone fairly, never unfairly in anyone's favour. *Why:* unpredictability, indifference, and unfairness are the strongest adult demotivators (unfairness: [Wilk2011]) and can produce learned helplessness. *Check:* are grading criteria, schedule, and expectations stated in advance and applied uniformly? (§10.2)
- **MOT-11** — Eliminate the six demotivating behaviours: contempt; disparaging learners' existing tools or skills; deep dives with the most advanced learners; pretending to know more than you do; "just" and feigned surprise; avoidable installation pain. *Why:* each signals the learner is stupid or unwelcome, or reinforces "this is too hard". *Check:* search scripts and slides for "just", "simply", "obviously", "you've never…?", and tool-bashing jokes; time the setup and pre-test installation. (§10.2)
- **MOT-12** — In online spaces, actively counter the [Ford2016] barriers: explain site features, invite people to answer, make the group feel smaller and safer, normalize asking strangers, and say searching *is* real work. *Why:* these barriers disproportionately deter women; fixing them helps everyone [Sved2016]. *Check:* onboarding text addresses each barrier. (§10.2)
- **MOT-13** — If you use productive failure, keep learners blocked but not frustrated through classroom culture and expectations, and never celebrate "fail fast, fail often". *Why:* outcomes depend on culture more than exercise design [Kapu2016]; celebrating failure presumes a privileged second chance. *Check:* does the plan say how struggle will be framed and supported? (§10.2)
- **MOT-14** — Counter impostor syndrome by showing your own struggles: tell stories of your mistakes, live code, and explicitly ask for questions as help for *you*. *Why:* classrooms show only others' finished work; under-represented learners are hit hardest [Wilc2018]. *Check:* the lesson includes at least one teacher-struggle story or live coding, plus an explicit invitation to ask questions. (§10.2)
- **MOT-15** — Never use or tolerate language implying some people are natural programmers, and spread your attention deliberately across all learners. *Why:* the "geek gene" is folklore [Pati2016]; teacher expectations become self-fulfilling [Alvi1999, Brop1983, Juss2005]. *Check:* no "some people just get it" talk; the plan has a mechanism (e.g. circulating, rotating who is called on) to avoid focusing on apparent high performers. (§10.2)
- **MOT-16** — Frame skill as learned and improvable, but don't promise big effects from mindset interventions. *Why:* fixed beliefs hurt everyone, but meta-analytic effects are weak, with possible benefit for low-SES or at-risk learners [Sisk2018]. *Check:* no claims that a mindset talk will transform outcomes. (§10.2)
- **MOT-17** — Involve people with disabilities in accessibility decisions ("nothing for us without us"). *Why:* this is the first and most important step. *Check:* name who with relevant lived experience reviewed the plan or materials. (§10.3)
- **MOT-18** — Put baseline accommodations in place in advance, without waiting to learn specific learners' disabilities. *Why:* this is possible without specific knowledge, and signals care that invites further requests. *Check:* the event checklist includes access (elevator or ramp), readable fonts, and accessible materials before registration closes. (§10.3)
- **MOT-19** — Improve accessibility incrementally: learn the do's and don'ts, measure (e.g. WebAIM), add one new habit per workshop, and do easy, zero-cognitive-load fixes first. *Why:* doing everything at once is unrealistic; easy wins help everyone (curb-cut effect). *Check:* the plan records this workshop's new accessibility habit. (§10.3)
- **MOT-20** — Make materials screen-reader and low-vision friendly:
  - use real headings and landmarks;
  - don't rely on color alone;
  - delete, don't hide, unnecessary elements;
  - allow self-pacing and repetition;
  - narrate on-screen action in video;
  - provide all code as text alongside any narration.

  *Why:* [Coom2012, Burg2015]; in Wilson's lessons, a narration script without the source code locked out screen-reader users. *Check:* run the material through each item. (§10.3)
- **MOT-21** — Adopt a Code of Conduct, publicize it, and enforce it. *Why:* it is a form of accessibility for marginalized people; existence and enforcement matter more than wording (§1.5, §9.1). *Check:* is there a named contact, a reporting channel, and a stated consequence, and has the team agreed who enforces it? (§10.3, appendix)
- **MOT-22** — Offer, and encourage, group signup for workshops. *Why:* knowing trusted people will be there raises attendance by marginalized learners and supports use of the skills afterwards. *Check:* the registration flow allows registering as a group. (§10.3)
- **MOT-23** — Apply the [Lee2017] practices:
  - pre-workshop "how will this help your goals?" email;
  - notes free of gendered pronouns and with culturally diverse names;
  - stress the *rate* of learning over starting point;
  - pair programming;
  - active mitigation of jargon and show-off "questions".

  *Why:* they help marginalized learners and motivate everyone. *Check:* tick each in the plan. (§10.4)
- **MOT-24** — When adapting content to learners' communities, avoid shallowness (no non-computing slideshow projects) and appropriation (acknowledge origins), and give the community control over content and direction. *Why:* these are the major risks of community representation and computational integration [Lach3018]. *Check:* is real computing involved? Are origins credited? Was the community consulted? (§10.4)
- **MOT-25** — Design classes and exercises assuming some learners have invisible, limited energy ("spoons"), and ask learners what works. *Why:* hidden costs accumulate, and people with few spoons fall behind. *Check:* are there breaks, flexibility, and an anonymous channel for needs? (§10.4)
- **MOT-26** — Explain under-representation structurally; never use deficit-model or "leaky pipeline" framing. *Why:* deficit thinking burdens the disadvantaged and excuses the advantaged [Mill2015]; causes are structural [Marg2003, Robe2017]. *Check:* scan materials and talk for "they lack…", "pipeline", or "women just aren't interested". (§10.4)
- **MOT-27** — Avoid phrases that reinforce stereotypes about who computing is for (e.g. "so simple even your grandmother could use it"). *Why:* stereotype cues demotivate and may trigger threat. *Check:* search scripts for age-, gender-, or group-based "even X can do it" phrasing. (§10.2, §10.5 "Common Stereotypes")
- **MOT-28** — Identify topics your audience may be embarrassed not to know, or not want peers to see them learning, and design face-saving ways to learn them. *Why:* shame demotivates; this is the §10.5 "Saving Face" design prompt. *Check:* the plan lists face-saving mechanisms such as anonymous questions or private practice. (§10.5)

## Procedures

### P1. Motivation audit of a lesson (MOT-1, 3, 5, 7, 8, 10)
1. For each exercise, mark which SDT driver it serves. Competence: are all needed tools practised beforehand? Autonomy: can learners choose order or approach? Relatedness: can they talk to peers? Any exercise with none is a candidate for redesign.
2. Ask whether each task is authentic. Would learners believe they'd do it in real life? Does it produce a tangible artifact? If not, look for a media-computation-style substitute in the learners' domain.
3. Remove arbitrary content (`foo`/`bar`, meaningless data).
4. Check for the [Bark2014] retention drivers: a meaningful assignment, teacher–learner interaction, and collaboration.
5. Check predictability, care, and fairness: are expectations, schedule, and assessment stated in advance and applied uniformly?
6. Check the [Ambr2010] motivator list and add at least one more; consider a peer-success story.

### P2. Choosing what to teach first (Figure 10.1) (MOT-6)
1. List candidate topics.
2. For each, estimate mean time to master for *this* audience, and usefulness once mastered for *their* goals, not for practitioners.
3. Plot them on the 2×2 grid:
   - quick and useful: teach first;
   - slow and low-use: drop;
   - on the diagonal: argue it out with co-teachers or stakeholders.
4. If a "foundational" topic lands in slow/useful, defer it until learners have early wins.
5. Re-check: does the first hour give a visible win?

### P3. Demotivation sweep of a script, slides, or live session (MOT-9, 11, 15, 27)
1. Search the text for "just", "simply", "obviously", "of course", "everyone knows", "I can't believe", "you've never…".
2. Search for jokes or asides disparaging tools learners may already use (Windows, Excel, older frameworks).
3. Search for "natural", "gifted", "some people get it", and "even your grandmother".
4. Check the environment and imagery for stereotypical cues, and recruiting text for gendered wording.
5. Plan the installation path: pre-test it, provide a fallback (e.g. a hosted environment), and budget helper time.
6. Plan to handle advanced learners' deep questions off-line rather than in front of the class.
7. Plan to admit the limits of your knowledge openly.

### P4. Accessibility pass (MOT-17 to 21)
1. Recruit or consult people with relevant disabilities.
2. Review materials against the UK government accessibility posters for all six groups.
3. Run online materials through WebAIM-style checks.
4. Apply the visual-design list: real headings, no color-only meaning, delete hidden elements, self-pacing, narrated video, and all code available as text.
5. Physical venue: check elevator or ramp access and route from transit, plus readable fonts and text size.
6. Choose this workshop's one new accessibility habit, and record it for next time.
7. Make sure a Code of Conduct is published, with contacts filled in, and that enforcers are agreed.

### P5. Inclusivity plan (MOT-22 to 26)
1. Enable group signup.
2. Send the pre-workshop "how could this help your goals?" email request.
3. Review notes for pronouns and name diversity.
4. Script a statement that learning rate matters, not starting point.
5. Plan pair programming.
6. Plan how to intervene on jargon and show-off questions.
7. If content is being culturally adapted, consult community members, check for shallowness and appropriation, and hand them control.
8. Build in flexibility for invisible constraints (spoons).
9. Remove deficit framing from any discussion of under-representation; use structural explanations.

### P6. Helping a learner or teacher with impostor syndrome (MOT-14)
1. Normalize it: it is common, especially among high achievers and under-represented groups.
2. Walk through the seven Ada Initiative guidelines (Templates T2) and pick two to act on.
3. As teacher: share a personal struggle story, live code, and invite questions as help for you.

## Diagnostics
| Symptom (in a lesson, class, or community) | Underlying problem | Fix (rule IDs) |
|---|---|---|
| Learners comply but show no interest; "why are we doing this?" | Tasks not authentic; no tangible artifact; extrinsic-only motivation | MOT-1, MOT-7, MOT-8 |
| First session spent on recursion, theory, or "fundamentals" before any win | Topic order ignores the usefulness/time-to-master grid | MOT-6 |
| Learners stop trying after early failures | Unpredictable outcomes or repeated uncontrollable negative feedback (learned helplessness) | MOT-10, MOT-13 |
| Quiet learners stop asking questions | Contempt, "just", feigned surprise, deep dives with advanced learners | MOT-11, MOT-14 |
| Learners revert to old tools after the workshop | Installation pain; existing skills disparaged | MOT-11 |
| Teacher says "some students just don't have it" or sees bimodal grades | Geek-gene belief, confirmation bias, attention skew | MOT-15, MOT-16 |
| High-performing women report low confidence | Impostor syndrome amplified by public critique of finished work | MOT-14 |
| Few women contribute on the course forum | [Ford2016] barriers unaddressed | MOT-12, MOT-21 |
| Screen-reader user can't follow coding lessons | Code not provided as text; color-only meaning; hidden elements | MOT-20 |
| Marginalized registrants don't show up | No trusted peers, no visible conduct policy | MOT-21, MOT-22 |
| Culturally themed lesson feels tokenistic or offends the community | Shallowness or appropriation; community not in control | MOT-24 |
| Discussion of diversity framed as "fixing" under-represented people | Deficit model or leaky-pipeline thinking | MOT-26 |
| Classroom decor or recruiting copy is stereotype-heavy | Ambient-belonging cues | MOT-9 |
| Teacher burns out or dreads sessions | Teacher motivation neglected | MOT-4 |

## Templates and checklists

### T1. Demotivator checklist (from §10.2)
```
[ ] No contemptuous or holier-than-thou tone (teacher or fellow learners)
[ ] No disparaging of learners' existing tools or skills
[ ] Advanced learners' deep dives deferred to breaks or off-line
[ ] Teacher openly admits gaps in knowledge
[ ] No "just" / "simply" / feigned surprise ("you've never heard of...?")
[ ] Installation pre-tested; fallback ready; time budgeted
[ ] Expectations and grading predictable and stated in advance
[ ] Teacher visibly cares about learners and material
[ ] Treatment fair to all (no favouritism, even toward the learner)
[ ] No "fail fast" bravado; struggle framed supportively
[ ] No "natural programmer" or "even your grandmother" language
```

### T2. Impostor-syndrome guide (Ada Initiative list, §10.2)
```
1. Talk about the issue with people you trust.
2. Go to an in-person impostor syndrome session.
3. Watch your words, because they influence how you think.
4. Teach others about your field.
5. Ask questions.
6. Build alliances.
7. Own your accomplishments (keep a record of what you have done).
Teacher moves: share your own mistakes and struggles; live code; ask for questions as help for you.
```

### T3. Accessibility checklist (§10.3)
```
Process
[ ] People with disabilities involved in decisions ("nothing for us without us")
[ ] Reviewed against do's/don'ts for: autistic spectrum, screen readers, low vision,
    physical/motor disabilities, deaf/hard of hearing, dyslexia
[ ] Measured with an accessibility checker (e.g., WebAIM)
[ ] One new accessibility habit added this time: ________
Easy wins
[ ] Readable font; adequate text size
[ ] Venue reachable by elevator/ramp (checked in advance)
Materials
[ ] Real headings/landmarks, not just font changes
[ ] Color never the only signal (hatching / grayscale-distinct colors)
[ ] Unnecessary elements removed, not merely hidden
[ ] Self-pacing and repetition possible
[ ] Video narrates on-screen action
[ ] All code available as text next to any narration or slides
Conduct
[ ] Code of Conduct published, with contacts filled in, and enforced
```

### T4. Inclusivity checklist ([Lee2017] via §10.4, plus §10.3 and §10.4 items)
```
[ ] Group signup available
[ ] Pre-workshop email: "how could this training help you reach your goals?"
[ ] Notes free of gendered pronouns; culturally diverse names in examples
[ ] Teacher states that learning RATE matters, not starting point
[ ] Pair programming used
[ ] Plan to defuse jargon and show-off "questions"
[ ] Community-based content: real computing (not slideshows); origins acknowledged; community consulted and in control
[ ] Flexibility for invisible constraints (spoons); learners asked what works
[ ] No deficit-model or "leaky pipeline" framing
```

### T5. SDT lesson check (§10 intro)
| Driver | Question | Evidence in this lesson |
|---|---|---|
| Competence | Have learners practised every tool the task needs? | |
| Autonomy | Can learners choose order, approach, or topic? | |
| Relatedness | Can learners talk to and work with peers? | |

### T6. What-to-teach grid (Figure 10.1)
```
usefulness once mastered
  ^
  | TEACH THIS FIRST            .
  |                         .
  |                   . (argue about this)
  |              .
  |         .                 DON'T BOTHER
  +------------------------------------------> mean time to master
```

### T7. Code of Conduct template (appendix "Code of Conduct", reproduced verbatim under CC BY 4.0; fill in ADDRESS and PHONE/TEXT)
Context from the appendix: it is based on the Ada Initiative template hosted on the Geek Feminism Wiki. Wilson recommends that **every online or in-person event adopt something like it**, with contact information filled in. (Contributions to the material itself are governed by the covenant in §C.1.)
```
We are dedicated to providing a harassment-free learning experience for everyone,
regardless of gender, sexual orientation, disability, physical appearance, body size,
race, or religion. We do not tolerate harassment in any form, including offensive
communication, sexual images in public spaces, deliberate intimidation, stalking,
following, harassing photography or recording, sustained disruption of talks or other
events, inappropriate physical contact, or unwelcome sexual attention.

Be kind to others. Do not insult or put down other attendees. Behave professionally.
Remember that sexist, racist, or exclusionary jokes are not appropriate.

People asked to stop any harassing behavior are expected to comply immediately. Anyone
violating these rules may be asked to leave the classroom at the sole discretion of the
instructors.

If you believe someone is violating the Code of Conduct we ask that you report it by
emailing ADDRESS, or if the violation occurs during a workshop or other in-person
event, by contacting the host directly at PHONE/TEXT. All reports will be kept
confidential.

Thank you for helping make this a welcoming, friendly event for all.
```
Structure, for adapting it: (1) commitment and protected characteristics; (2) concrete examples of prohibited harassment; (3) positive behaviour norms; (4) consequences (comply immediately; removal at instructors' discretion); (5) reporting channels, online and in person, with a confidentiality promise; (6) thanks.
> **Skill note:** per §10.3 and §9.1, a skill generating a conduct policy should also prompt the user to decide *who enforces it* and to announce it. The book stresses that existence and enforcement matter more than wording.

### T8. Peer-success story slot (§10 intro)
```
Guest: a former learner who struggled but succeeded (ideally similar to current learners)
Prompts: What was hardest? What almost made you quit? What helped? What do you wish you'd known?
```

## Examples
- **SDT exercise design** (§10 intro). Situation: a programming exercise for a larger problem. Design: practise every needed tool first; let learners tackle parts in any order; allow peer talk. Lesson: one task can hit all three drivers.
- **Media computation** (§10.1, [Guzd2013]). Situation: a first program in CS1. Replaced "hello world" with open an image, make a thumbnail, save it. Lesson: authentic tasks with tangible artifacts motivate and make debugging concrete. The approach was adapted to MATLAB [Lee2013] and to data science, image processing, and biology [Dahl2018, Meys2018, Ritz2018].
- **Sorting exercise** (§10.1). Situation: learners sort lines of text. Fix: use album titles or people's names, not meaningless strings. Lesson: remove arbitrariness cheaply.
- **Classroom objects** (§10.2, [Cher2009]). Swapping Star Trek posters and video games for nature posters and phone books raised women's CS interest to men's level. Lesson: ambient cues matter.
- **Wilson's own inaccessible lessons** (§10.3). Narration script shown beside slides, but no Python source. Screen-reader users heard about the program but never got the program. Lesson: give code as text.
- **Curb cuts and image captions** (§10.3). Accommodations help everyone; captions also aid search.
- **Game-testing program** (§10.4, [DiSa2014a]). 65% of male African-American participants went on to study computing, partly because peers respected gaming. Lesson: rethinking content around learners' communities can pay off.
- **Indigenous design reverse-engineering** (§10.4, [Lach3018]). An example of computational integration. Lesson: risk of appropriation, so acknowledge origins.
- **Spoons** (§10.4). Miserandino explains chronic illness with a limited supply of spoons, each activity costing one; even dressing has hidden costs. Lesson: account for invisible constraints and ask learners.
- **Figure 10.2** (§10.4). The women's share of CS degrees fell from about 36% (mid-1980s) to about 17% (2010s), with drops after enrollment booms. Lesson: structural causes, not deficits.

## Evidence and caveats
- **Intrinsic motivation drives learning best:** [Wlod2017], presented as the standard reference on adult motivation.
- **Retention drivers** [Bark2014]: large-scale, multi-institutional study. Wilson cautions that "obvious" results would look obvious either way.
- **Ambient cues** [Cher2009] (four studies) and **gendered wording** [Gauc2011] (three studies) are presented as solid.
- **Strongest adult demotivators:** unpredictability, indifference, and unfairness are stated without a citation, except that the unfairness point (even unfairness in your favour worries you) cites [Wilk2011], *The Spirit Level*, on inequality harming everyone.
- **[Ford2016] Stack Overflow barriers:** five statistically significant; fear of negative feedback just missed the cutoff.
- **[Sved2016]:** the text says addressing barriers "improves outcomes for everyone". The book's own bibliography annotation is more nuanced: a gender-neutral redesign improved completion in general **but decreased it for students with a superficial approach to learning**.
- **Productive failure** [Kapu2016]: presented as "recent work", with success depending on classroom culture.
- **Impostor syndrome and confidence** [Wilc2018]: women with prior exposure outperformed men in all areas but were less confident. The Ada Initiative guidelines are practitioner advice, not research.
- **Stereotype threat:** Wilson explicitly **hedges**. It is unclear that it is the primary cause of unwelcoming climates; the term is used inconsistently [Shap2007]; key studies have replicability questions.
- **Geek gene / bimodal grades:** **debunked** by [Pati2016] (only 5.8% of 778 distributions multimodal; priming experiment with 53 professors). Record it as instructional folklore.
- **Teacher-expectation effects** [Alvi1999, Brop1983, Juss2005]: presented as established.
- **Growth mindset:** Wilson **hedges**. Possibly oversold; [Sisk2018]'s two meta-analyses found weak overall effects, with possible benefit for low-SES or at-risk students.
- **Accessibility guidance** [Coom2012, Burg2015], the UK posters, and WebAIM are presented as practical guides, not experimental findings.
- **Female participation statistics:** 12–18% of CS degrees in the West (sources vary); 30–40% elsewhere [Galp2002, Varm2015]. Figure 10.2 from [Robe2017] (a National Academies-based summary; most likely US data, though the book doesn't say).
- **"Leaky pipeline":** [Mill2015] shows the metaphor stopped being accurate around the 1990s (bibliography annotation).
- **Opinions flagged as Wilson's:** discussing women's erased history is worth doing *because* it makes some men uncomfortable; "fail fast" reflects privilege.
- **Text anomaly:** the EPUB has "exercise" where "challenge" or "problem" is clearly meant, apparently a global substitution. Instances: "the exercise therefore isn't how to motivate them" (problem/challenge), "hearing exercises" (hearing impairments/problems), "the physically exercised" (physically challenged), and "How complete was your list of exercises?" (problems/challenges). This file uses the evident meaning.

## Practice exercises
- **Authentic Tasks** (pairs, 15 min). Take something you did this week using a skill you teach; turn it into a class exercise; place it on the time-to-master × usefulness 2×2 grid; discuss it against "teach most immediately useful first".
- **Core Needs** (whole class, 10 min). Rank Paloma Medina's six core needs at work (belonging, improvement, choice, equality, predictability, significance) from 6 points to 1; compare across the class; consider how learners would rank them.
- **Implement One Strategy for Inclusivity** (individual, 5 min). Pick one [Lee2017] practice; set a calendar reminder three months out to check you acted on it.
- **Brainstorming Motivational Strategies** (think-pair-share, 20 min). Recall a teacher action that demotivated you and how it could have been corrected; discuss in pairs; add to shared notes; the group highlights a few alternatives.
- **Demotivational Experiences** (think-pair-share, 15 min). Recall demotivating, or being demotivated as, a student; discuss what could have been done differently; share in group notes.
- **Walk the Route** (whole class, 15 min). Walk from the nearest transit stop to your office and washroom noting mobility barriers; repeat in a borrowed wheelchair; compare lists. Note that the instructions themselves assumed you could walk.
- **Who Decides?** (whole class, 15 min). Using Wesson's quote in [Litt2004] about standardized tests and a linked article, describe an "objective" assessment from your experience that reinforced the status quo.
- **Common Stereotypes** (pairs, 10 min). List 2–3 phrases like "so simple even your grandmother could use it" that reinforce stereotypes about computing.
- **Not Being a Jerk** (individual, 15 min). Using Gary Bernhardt's rewrite of a hostile message as a model, rewrite an unpleasant Stack Overflow or forum post to be less repellent.
- **Saving Face** (individual, 10 min). Identify topics your audience may be embarrassed not to know, or not want peers to see them learning; design face-saving measures.
- **After the Fact** (whole class, 15 min). [Cutt2017] links adult computing confidence to childhood solo reading and construction toys with no moving parts. Search online for programmers' beliefs about predicting coding ability and see whether these factors appear.
- **How Accessible Are Your Lessons?** (pairs, 30 min). Independently rate an online lesson against the UK accessibility posters; compare agreement and disagreement; score each of the six user categories.
- **Tracing the Cycle** (small groups of 4–6, 15 min). Using [Coco2018]'s pattern of good intentions undermined by leadership unwilling to change, write the emails each party would send at each stage.

## Cross-references
- `01-introduction-and-motivation-to-teach.md`: Code of Conduct introduced (§1.5).
- `03-expertise-and-memory.md`: expert blind spot, why "just" signals triviality, concept maps.
- `05-individual-learning.md`: peer assessment and calibrated peer review (§5.3).
- `06-lesson-design.md`: Bloom's taxonomy, learner personas, lesson maintenance.
- `07-programming-pck.md`: [Wilc2018] prior experience and confidence (§7.5).
- `08-teaching-as-performance.md`: live coding shows the teacher is human (§8.4).
- `09-in-the-classroom.md`: enforcing the Code of Conduct (§9.1), co-teaching (§9.3), preparatory privilege (§9.5), collaborative notes (§9.7).
- `11-teaching-online.md`: online retention drivers, codes of conduct online, video narration.
- `12-exercise-types.md`: MCQs and Parsons Problems as non-authentic but useful drills (the §10.1 tension).
- `13-building-community.md`: allyship, giving communities control.

## Source map
| Book section | Covered under |
|---|---|
| §10 objectives | Concepts §10 Chapter objectives |
| §10 intro (intrinsic/extrinsic, SDT) | Concepts §10 intro; MOT-1; T5 |
| §10 box "The Problem of Grades" | Concepts §10 intro; MOT-2 |
| §10 intro [Ambr2010], peer stories | MOT-3; T8 |
| §10 box "Not Just for Students" | MOT-4 |
| §10 intro [Bark2014] | MOT-5; Evidence |
| §10.1 Authentic Tasks, Fig 10.1 | Concepts §10.1; MOT-6, MOT-7, MOT-8; P2; T6 |
| §10.2 Demotivation (cues, three demotivators, list, [Ford2016]) | Concepts §10.2; MOT-9 to MOT-12; P3; T1 |
| §10.2 box "Productive Failure and Privilege" | MOT-13 |
| §10.2 Impostor Syndrome | Concepts; MOT-14; P6; T2 |
| §10.2 Stereotype Threat | Concepts; MOT-15, MOT-27; Evidence |
| §10.2 Mindset | Concepts; MOT-16; Evidence |
| §10.3 Accessibility, box "It Helps Everyone" | Concepts §10.3; MOT-17 to MOT-20; P4; T3 |
| §10.3 Conduct Revisited, box "Group Signup" | MOT-21, MOT-22; T7 |
| §10.4 Inclusivity ([Lee2017], [DiSa2014a], [Lach3018]) | Concepts §10.4; MOT-23, MOT-24; P5; T4 |
| §10.4 Spoons | MOT-25 |
| §10.4 Moving Past the Deficit Model, Fig 10.2, box "Rewriting History" | Concepts; MOT-26; Evidence |
| §10.5 Exercises | Practice exercises; MOT-27, MOT-28 |
| Appendix "Code of Conduct" | T7; MOT-21 |
