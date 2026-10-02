# Diagnostics: symptom → problem → fix

> Cross-cutting file for Greg Wilson, *Teaching Tech Together* (2018), CC BY 4.0. Every Diagnostics row from the chapter files, grouped by area, with the source file noted. Rule IDs resolve in `rules-and-checks.md` Part 3. Use it to go from an observed problem in a lesson, class, or community to the rule that fixes it.

## Learning design: models, memory, load, study skills

### From `02-mental-models.md`

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

### From `03-expertise-and-memory.md`

| Symptom (in a lesson, class, or community) | Underlying problem | Fix (rule IDs) |
|---|---|---|
| The teacher says "you just…" repeatedly | Expert blind spot; implies the learner is stupid | MEM-1, P4 |
| The explanation starts from the subject's elegant core principle and loses beginners | Blind spot: organized by deep principles | MEM-2 |
| The expert teacher "can't explain how they knew"; demos skip steps | Intuition (direct-link recall) | MEM-3 |
| Learners can recite facts but can't apply or recall them in context | Facts taught without connections | MEM-5, MEM-6 |
| Learners lose track mid-lesson and earlier material "falls out" | Working-memory overload; too much too fast | MEM-8, P1 step 6 |
| A slide reveals a whole complex diagram at once and learners stare at it | Diagram not built in sync with explanation | MEM-9 |
| Co-teachers contradict each other about what the lesson covers | Divergent mental models of the content | MEM-10, P3 |
| Learners stare at a blank page when asked to map | Unpractised technique | MEM-12 ("Start Anywhere") |
| Polished diagrams draw only polite, superficial feedback | Apparent effort suppresses honest critique | MEM-13 |
| Novices are given a full design-pattern catalogue | Too dry and abstract for novices | MEM-15 |
| Lots of drill, little improvement, bad habits entrenched | Repetition without goal or feedback | MEM-16 |
| Peer review produces vague or incorrect comments | No feedback on the feedback | MEM-17 |
| A department assigns teaching by research prominence | Assumes expertise equals teaching skill | MEM-18 |
| Learners cram the night before and forget quickly | No spacing; recall cues missing | MEM-19; `05-individual-learning.md` |

### From `04-cognitive-load.md`

| Symptom (in a lesson, class, or community) | Underlying problem | Fix (rule IDs) |
|---|---|---|
| Novices given an open-ended project flounder and give up | Unguided inquiry overloads them (facts plus strategy at once) | COG-1, COG-5, COG-6 |
| Learners freeze at a blank editor | No scaffolding; too big a jump | COG-6, P1 |
| Learners copy the teacher's variable names as if they were required (e.g., `result`) | Too few or too uniform examples | COG-8 |
| Learners can follow the demo but can't reproduce the reasoning | The demo shows "what", not "why" | COG-9, COG-12 |
| Syntax errors swamp a lesson about control flow | Syntax load competing with the target concept | COG-11 (Parsons) |
| The video has narration plus verbatim captions, and learners report it is tiring | Split attention (redundancy) | COG-13 |
| A slide reveals a complex diagram in full and learners don't follow | No temporal contiguity | COG-14, COG-18 |
| Learners must read docs, a slide and terminal output at once while learning a basic skill | Premature multi-source integration | COG-15 |
| A lesson full of attractive stock images is rated highly but performance doesn't improve | Seductive or decorative graphics | COG-16 |
| More representations were added "to help" and performance dropped | Excess information for the task | COG-17 |
| A long manual organized by feature; users can't do a real task | Hierarchical sub-skill drilling, context lost | COG-19, COG-20 |
| The teacher's colour scheme or tool layout differs from learners' | Extraneous load | COG-3 |
| A colleague dismisses cognitive load theory as unfalsifiable | Known criticism | Cite [Maso2016] (34% fewer exam failures); COG-21 |

### From `05-individual-learning.md`

| Symptom (in a lesson, class, or community) | Underlying problem | Fix (rule IDs) |
|---|---|---|
| Learners cram the night before and forget within days | No spacing | IND-4, IND-5, P1 |
| Learners re-read notes repeatedly and feel ready, then fail | Recognition mistaken for recall; no retrieval practice | IND-6, IND-7 |
| Practice is essays, the exam is MCQ (or vice versa) | Transfer-inappropriate practice | IND-7 |
| Learners can define terms but can't connect ideas | Fact-only retrieval | IND-8, IND-15 |
| Learners complain mixed practice "feels harder" and want blocked practice | A desirable difficulty of interleaving | IND-10 (explain it's working) |
| Learners stall at a step they don't understand in a worked example | No self-explanation habit | IND-12, IND-11 |
| The course claims "learning to code makes you better at maths / logic in general" | A far-transfer myth | IND-3 |
| A teacher tailors lessons to "learning styles" | A debunked myth [Guzd2015b, Kirs2013] | See Evidence; use IND-18 instead |
| Learners hunt endlessly for a simplification that doesn't exist | No non-examples taught | IND-17 |
| Slides read aloud verbatim | Redundant dual channels | IND-18 |
| Learners brag about all-nighters; quality drops near deadlines | Overwork and sleep deprivation; decline unnoticed | IND-20, P6 |
| Learners study with phones and chat open | Multi-tasking myth; flow lost | IND-22 |
| "I just need more willpower" | Ego depletion | IND-23 |
| The instructor is the only source of feedback, which is slow and sparse | No peer assessment | IND-24, IND-26 |
| Peer reviews are vague or wildly off | Reviewers uncalibrated | IND-26, P4 |
| Team ratings say "bad attitude" or "not a team player" | Trait-based rather than observable criteria | IND-25, IND-28 |
| Fear that peers will collude or be biased | Concern not borne out in class [Kauf2000] | IND-24 |
| Telling learners to "make a study plan" changes nothing | Metacognition taught in the abstract | IND-2 |

## Lesson design and programming content

### From `06-lesson-design.md`

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

### From `07-programming-pck.md`

| Symptom | Underlying problem | Fix (rule IDs) |
|---|---|---|
| Lesson shows only finished, polished code | No "how" taught; novices lack plans | PCK-1, PCK-3, PCK-4 |
| Learners make random edits hoping something works | No plan; merged or fragmented goals | PCK-2, PCK-5 |
| Learners write code top to bottom and get stuck on details first | Never shown outside-in authoring | PCK-3 |
| Learners can't say what a short snippet outputs | Weak tracing skill | PCK-8, PCK-9 |
| Learner puts the same print in both if/else branches, or comments out correct lines | Ineffective debugging habits | PCK-5 |
| Some learners take 3× longer on debugging exercises | Strategy gap, not just speed | PCK-6 |
| Learners' tests all pass but bugs remain | Confirmation-style happy-path tests | PCK-10 |
| Learner names a variable `average` and expects the computer to compute an average | Superbug | PCK-11 |
| Learner expects `total` to update when `grade` changes | Spreadsheet-variable misconception | PCK-12 |
| Learner thinks the while loop exits mid-body the moment its condition becomes false | Constantly-evaluated-condition misconception | PCK-12 |
| Teacher spends class time on `=` vs `==` while learners struggle with brackets and quotes | Priorities set by intuition, not data | PCK-13, PCK-14 |
| Instructor says "the rules are simple" about HTML nesting | Expert blind spot | PCK-14 |
| Operator precedence taught with `5<3` before variables exist | Dependency order violated | PCK-15 |
| Course "works" because evaluations are high | Evaluations don't measure learning | PCK-16 |
| Teens stall on syntax errors in a text language | Text-first for young novices | PCK-17 |
| Python learners omit `self` or misuse attributes | Objects introduced too early | PCK-18 |
| Lesson examples use mixed naming and formatting | No enforced style | PCK-20 |
| Learners ignore or misread compiler errors | No practice reading error messages | PCK-21 |
| Learners watch animations but can't trace themselves | Passive viewing of visualizations | PCK-9 |
| Course redesign relies only on a game theme | Weakest intervention in [Viha2014] | PCK-23 |
| Lesson tailored to "visual learners" or cites the learning pyramid | Debunked myths | PCK-26 |
| Explanations of execution contradict each other across lessons | No consistent notional machine | PCK-25 |

## Delivery: performance and classroom

### From `08-teaching-as-performance.md`

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

### From `09-in-the-classroom.md`

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

## Motivation, accessibility, and inclusion

### From `01-introduction-and-motivation-to-teach.md`

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

### From `10-motivation-and-inclusion.md`

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

## Online teaching and exercises

### From `11-teaching-online.md`

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

### From `12-exercise-types.md`

| Symptom (in a lesson, class, or community) | Underlying problem | Fix (rule IDs) |
|---|---|---|
| MCQ results don't tell you *what* learners misunderstand | Distractors not tied to misconceptions | EXR-2 |
| Correct but unusual solutions rejected; learners demoralized | Grader matches the instructor's code | EXR-4 |
| Novices freeze at an empty editor | Blank-page task too early | EXR-7 |
| Parsons Problems take forever, learning no better | Distractor lines added | EXR-8 |
| Learners hunt through options on tracing questions | Tracing posed as an MCQ | EXR-9 |
| Every learner's trace is in a different format | No table structure | EXR-10 |
| Refactoring submissions impossible to grade at scale | Unconstrained target form | EXR-13 |
| Diagram assignments swamp TAs | Free-form diagrams at scale | EXR-14 |
| Learners mis-enter matching answers | Typed pair lists or pair-set MCQ | EXR-15 |
| Learners complain about the auto-grader, but outcomes improved | Satisfaction ≠ learning; maybe poor messages | EXR-19, EXR-25 |
| Hand-written tests miss many bugs | No fuzz testing | EXR-20 |
| Many "what is this assignment asking?" questions | Spec not understood before coding | EXR-21, EXR-23 |
| Learners hard-code expected outputs | Expected outputs revealed | EXR-24 |
| Style grades don't match human judgment | Raw violation counts; starter code rewarded | EXR-22 |
| Learners test thoroughly but still fail | Requirements misunderstanding, not under-testing | EXR-23 |
| Peer code reviews are shallow | No rubric or calibration | EXR-26 |
| Exercise overruns badly | "Simple" failures unbudgeted (expert blind spot) | EXR-28 |
| Learners misread the exercise prompt | Not piloted | EXR-29 |

## Community, marketing, and partnerships

### From `13-building-community.md`

| Symptom (in a lesson, class, or community) | Underlying problem | Fix (rule IDs) |
|---|---|---|
| Founder wants to start a new coding non-profit in a city that already has several | Founding for status instead of joining and learning first | COM-6, COM-7 |
| Graduates get jobs, but nothing changes for their communities, and organizers are surprised | Aim never decided (succeed in the world vs. change it) | COM-1 |
| Class works on paper but learners keep missing sessions (childcare, hunger, transport) | Ignoring learners' lives outside class | COM-2 |
| Newcomers face expert-level tasks straight away and leave | Cliff instead of ramp; no legitimate peripheral participation | COM-4, COM-11 |
| Group activities drift between advocacy, support group, hobby club | Community type never chosen | COM-5 |
| Volunteers show up once or twice, then vanish | No follow-through: no group onboarding, no mentor | COM-11, COM-12 |
| Mentors exist but newcomers still don't know anyone or "how things work here" | Mentors not told their real duties; no reporting | COM-12 |
| Organizers can't see what's confusing about their offering | Collective expert blind spot; not recruiting from learners | COM-9 |
| Six months after someone left, nobody can book the venue or log into the account | No retirement handover | COM-13 |
| Volunteers assigned tasks they dislike (e.g. finances) and quietly drop out | Guessing preferences instead of asking | COM-14 |
| Founder does everything; few others involved | Too few contribution routes; hoarding tasks | COM-15 |
| Every thread is answered by the leader within minutes; members never talk to each other | Not making space; leader-centered network | COM-17 |
| Long debates over mission statements before anything is delivered | Hymns before soup | COM-20 |
| Small stipends cause resentment or loss of volunteer spirit | Token pay | COM-21 |
| Members afraid to contribute; harsh public criticism; process undocumented | Conditions that breed impostor syndrome | COM-22 |
| Disputes over who may use the logo or charge for workshops; decisions by "whoever's in the room" | Informal, unaccountable power structure | COM-23 |
| Appointed board agrees with itself and ignores the community | Mutual-agreement board; no democracy | COM-25, COM-26 |
| Founding team bogged down drafting bylaws for a group that barely exists | Premature constitution | COM-26 |
| Leader exhausted; organization depends on them | Burnout; no succession | COM-27, COM-28 |
| Meetings are status read-outs | Meeting not needed | COM-29 |
| Meetings run over; later items never reached; follow-up meetings pile up | No timed agenda; overrun causes not diagnosed | COM-30, COM-31 |
| Chair talks most of the time | Chair dominating instead of facilitating | COM-32 |
| Side conversations, laptops open, people checking email | No device or politeness norms enforced | COM-33, COM-34 |
| Same two people talk or interrupt constantly; quiet members give up | Unequal floor; unmanaged interruptions | COM-35, COM-39 |
| "I never agreed to that deadline"; absentees ask "what did I miss?" | No minutes or late minutes; no tickets | COM-36 |
| Online meeting: people talk over each other, speak without listening | First-to-speak-in-a-pause dynamic | COM-40 |
| Post mortem turns into blaming individuals, or goes in circles | No outside moderator; comments on people not actions | COM-41, COM-42 |
| The people who caused the problems skip the retrospective | Optional attendance | COM-41 |
| Multi-week online instructor training loses half its cohort | Format raises drop-out | COM-44 |
| Online-individual trainees can't do concept maps or teaching feedback | Exercises unsuited to the format | COM-45 |
| Outsiders want to fix lesson errors but don't know Git | Only one, technical, contribution channel | COM-46 |
| Contributor submits a huge restructuring without discussion | No "Proposal"/discuss-then-edit norm | COM-46 |

### From `14-marketing.md`

| Symptom (in a lesson, class, or community) | Underlying problem | Fix (rule IDs) |
|---|---|---|
| Free workshops thrive but the organization runs out of money | Mistaking the workshop for the product; neglecting what funders buy | MKT-2 |
| One generic pitch is used for learners, sponsors, and councillors | No per-stakeholder personas or pitches | MKT-3, MKT-4 |
| Website reads "For X who Y, our Z provides…" word for word | Template copied verbatim | MKT-6 |
| Pitch to a sponsor is all ROI; the sponsor's real motive was civic | Ignoring non-economic motives | MKT-5, MKT-7 |
| People in the field ignore announcements | No positioning; attention exhausted | MKT-8 |
| Reports full of statistics fail to move funders | Data without stories | MKT-9 |
| Showcase relies on learners building costly projects in a low-income program | Ignoring "free works for those that can afford free" | MKT-10 |
| Parents can't find the class via search | Site not found by audience search terms | MKT-11 |
| Landing page leads with mission, team, and org chart; no address or schedule | Not answering visitors' first questions | MKT-12 |
| Target community largely offline; only online ads used | No offline findability | MKT-13 |
| Inquiries the group can't serve are turned away cold | Missed referral and alliance opportunity | MKT-14 |
| Cold emails start "I recently came across your website" and get no reply | No specific point of connection | MKT-15 |
| "LIMITED SEATS!!! FREE WORKSHOP" emails land in spam | Bad subject line; hustle tone | MKT-16, MKT-18 |
| Recipients reply "what exactly is this and what does it cost?" | Missing specifics, credibility, or terms | MKT-17 |
| Long cold emails | Not respecting the recipient's time | MKT-19 |
| Team gives up after a dozen emails with no bookings | Unrealistic conversion expectations | MKT-20 |
| New group duplicates a better-established one locally | Not first in category; should reposition or join | MKT-21 |

### From `15-partnerships.md`

| Symptom (in a lesson, class, or community) | Underlying problem | Fix (rule IDs) |
|---|---|---|
| Faculty nod at the proposal but never try it | Unaddressed fear of looking stupid or of bad evaluations | PTN-1 |
| A pitch full of citations persuades no one in a CS department | Researchers distrust education research as a reason to change | PTN-2 |
| Teachers abandon the practice after the first term | Glass's Law slowdown not planned for; room layout fights the practice | PTN-3 |
| Practice disappears once the dean stops checking | Adoption sustained only by mandate | PTN-4 |
| Group expects a school district to adopt its curriculum within a year | Unrealistic timeline; no systematic implementation plan | PTN-5 |
| Proposal written before talking to any teachers | Not listening first | PTN-6 |
| Plan requires a brand-new degree or a long retraining program | Not working within existing frameworks; not incremental | PTN-7 |
| Outsider tries to mandate changes to a whole department | Mismatched change category (acting system/prescribed from an individual/emergent position) | PTN-8 |
| Pitch to a bootcamp is about a new language or framework | Leading with tech rather than teaching expertise | PTN-9 |
| Partnering with a bootcamp that leaves low-income learners in debt without jobs | Partner not vetted; learner barriers ignored | PTN-10 |
| Lone champion burns out; skeptics block the initiative | No allies or tactics; skeptics not engaged | PTN-11 |
| New practice is "optional", training is skimped, used only in toy settings | Farmer's anti-adoption rules in effect | PTN-12 |
| Group keeps pushing JavaScript when partners need spreadsheets | Confusing your passion with partners' needs | PTN-13 |
