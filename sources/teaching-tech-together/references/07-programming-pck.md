# Pedagogical Content Knowledge for Programming

> Source: Greg Wilson, *Teaching Tech Together* (2018), Ch. 7 "Actionable Approximations of the Truth" (§7 intro, §7.1–§7.9), appendix "A Little Bit of Theory" (including "Notional Machines"). Licensed CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/); condensed and restructured for skill use, with quotations marked. Rule IDs use prefix `PCK`.

## When a skill needs this
- Designing or reviewing a programming lesson: what to demonstrate (process, plans, debugging), what misconceptions to target, and in what order to introduce topics.
- Generating diagnostic exercises for programming misconceptions and common errors (tracing, prediction, mangled code, Parsons, Rainfall, roles of variables).
- Advising on tool and language choice for novices: blocks vs. text, objects-first vs. procedural, typed vs. untyped, naming style, error messages, visualization.
- Choosing course-level interventions (collaboration, contextualization, media computation, CS0, peer support) and judging how strong the evidence is.
- Explaining or teaching a notional machine (e.g. for Python), or checking a lesson against debunked learning myths.

## Key terms
| Term | Meaning (one line) |
|---|---|
| Content knowledge | A person's understanding of a subject, e.g. how to program. |
| General pedagogical knowledge | Understanding of the general principles of teaching, e.g. the psychology of learning. |
| Pedagogical content knowledge (PCK) | "The domain-specific knowledge of how to teach a particular concept to a particular audience" (§7 intro): which examples to use, which misconceptions are common. |
| Actionable approximations of the truth | Wilson's framing: research results stated as decisions teachers can act on now, not "nuanced perhapses". |
| CS0 / CS1 / CS2 | CS0: intro for people with no experience who aren't (yet) continuing in computing. CS1: first semester course (variables, loops, functions). CS2: second course (stacks, queues, basic data structures). |
| Programming plan | A pattern experts use to guide how they construct code (the "how", as opposed to the "what") [Solo1984, Solo1986]. |
| Roles of variables | Eleven single-variable design patterns (fixed value, stepper, walker, …) that give novices a vocabulary and set of plans [Kuit2004, Byck2005, Saja2006]. |
| Superbug | The belief that the computer understands intention the way a human would [Pea1986]. |
| Parsons Problem | Glossary: learners rearrange given material to construct a correct answer. |
| Rainfall Problem | Read positive integers until 99999, then print the average of the numbers seen [Solo1986]. |
| Learning trajectory | A literature-derived sequence of ideas from beginner to advanced for a topic; "essentially collective concept maps" [Rich3017]. |
| Blocks-based programming | Tools like Scratch in which programs are assembled from blocks, making syntax errors impossible. |
| Objects first | Teaching objects and classes from the start; educators disagree on what it means [Benn2007b]. |
| Media computation | Courses or activities built around manipulating media (Ch 10); the most effective intervention in [Viha2014]. |
| Unplugged | Teaching computing ideas without computers, e.g. computational creativity exercises [Shel2017]. |
| Notional machine | Glossary: "A general, simplified model of how a particular family of programs executes" [DuBo1986, Sorv2013]. |
| Computational thinking | Glossary: problem-solving inspired by programming, "though the term is used in many other ways"; Wilson prefers the notional machine idea. |
| Cognitivism / behaviorism / constructivism / connectivism / situated learning | Learning theories summarized in the "A Little Bit of Theory" appendix (see Concepts). |
| Instructional design | Glossary: the craft of creating and evaluating specific lessons for specific audiences ("the engineering" to educational psychology's "science"). |

## Concepts

### §7 (introduction) — Three kinds of knowledge; how far to trust the research
- Every instructor needs **content knowledge**, **general pedagogical knowledge**, and **PCK**. In computing, PCK includes which examples to use for parameter passing, or which misconceptions about nesting HTML tags are most common. This chapter adds to the reader's store of PCK.
- **Computing education research is young.** The American Society for Engineering Education was founded in 1893 and the National Council of Teachers of Mathematics in 1920, but the Computer Science Teachers Association only in 2005. "We don't know as much about how people learn to program as we do about how they learn to read, play a sport, or do basic arithmetic." Conferences such as SIGCSE, ITiCSE, and ICER produce a growing stream of rigorous, practical studies. [Ihan2016] surveys the methods they use most.
- **Population caveat:** most studies look at school children and undergraduates, because researchers can reach them most easily [Henr2010] (bib: subjects are mostly Western, educated, industrialized, rich, democratic) and because those are the ages when most people learn to program. Less is known about adults learning in free-range settings.
- **Stance:** an academic treatise would hedge most claims ("Research may seem to indicate that…"). But teachers must decide now, so the chapter gives "actionable approximations of the truth rather than nuanced perhapses." Theories may change as better data arrives.
- **Box "Jargon":** CS1, CS2, CS0 as in Key terms. A CS1 course is often useful to undergraduates in other disciplines. A CS2 course designed for CS students is usually less relevant to artists, ecologists, and other end-user programmers, but is sometimes their only next step. Full definitions are in the ACM Curriculum Guidelines.
- **Wilson's numbered recommendations in this chapter:** (1) show learners *how* to program (§7.1); (2) teach novices how to debug (§7.2); (3) teach that computers don't understand programs (§7.3); (4) measure and track results comparably over time (§7.5); (5) start children and teens with blocks before text (§7.6). Further unnumbered recommendations: start with procedural languages; use consistent style enforced by tools (§7.6); practise reading error messages (§7.7); teach students to trace variables' values (§7.7).

### §7.1 How Do Novices Program?
- [Solo1984, Solo1986] pioneered the study of novice and expert programming strategies. **Key finding:** experts know both "what" (what goes into programs) and "how" (patterns or *plans* to guide construction). Novices lack both, but most teachers teach only the "what", even though bugs often come from having no strategy for the problem rather than from not knowing the language.
- **"The most important recommendation in this chapter is therefore to show learners how to program."** This is consistent with cognitive load theory (Ch 4). [Mull2007b] (bib: explicitly teaching solution patterns improves outcomes) is "just one of many studies proving its benefits". Live coding (§8.4) works partly because it puts "how" front and centre.
- When demonstrating:
  - emphasize **small steps with frequent feedback** [Blik2014];
  - emphasize **picking a plan and sticking to it**, rather than making more-or-less random changes and hoping they work. [Spoh2985] found that merging plans or goals can cause bugs when goals get dropped or fragmented.
- **Order of writing code.** [Ihan2011] (a 2D Parsons Problem tool) found experienced programmers often drag the method signature in first, then most of the control flow (loops and conditionals), and only then details such as variable initialization and corner cases (bib: experts solve "outside-in" rather than line by line). Novices read and write code in page order, so this out-of-order authoring is foreign to them. Live coding lets them see the sequence experts actually use.
- **Roles of variables** [Kuit2004, Byck2005, Saja2006] are single-variable design patterns that Wilson finds very useful. Labelling the parts of novices' programs gives them "a vocabulary to think with" and a set of plans for writing their own code. The patterns are on the Roles of Variables website, with examples:

  | Role | Definition (§7.1) |
  |---|---|
  | Fixed value | A data item that does not get a new proper value after its initialization. |
  | Stepper | A data item stepping through a systematic, predictable succession of values. |
  | Walker | A data item traversing in a data structure. |
  | Most-recent holder | A data item holding the latest value encountered in going through a succession of unpredictable values, or simply the latest value obtained as input. |
  | Most-wanted holder | A data item holding the best or otherwise most appropriate value encountered so far. |
  | Gatherer | A data item accumulating the effect of individual values. |
  | Follower | A data item that gets its new value always from the old value of some other data item. |
  | One-way flag | A two-valued data item that cannot get its initial value once the value has been changed. |
  | Temporary | A data item holding some value for a very short time only. |
  | Organizer | A data structure storing elements that can be rearranged. |
  | Container | A data structure storing elements that can be added and removed. |

### §7.2 How Do Novices Debug and Test?
- [McCa2008]: "It is surprising how little page space is devoted to bugs and debugging in most introductory programming textbooks." Little has changed. There are hundreds of books on compilers and operating systems but only a handful on debugging, and Wilson has never seen an undergraduate course on it. One reason: debugging is a "how", not a "what". Live coding lets teachers demonstrate the process in a way textbooks can't (§8.4).
- **Tracing and writing.** [List2004, List2009] found many novices struggle to predict the output of short code and to pick the correct completion of code when told what it should do. (Bib on List2009: students who can't trace usually can't explain, and good code writers can usually both trace and explain.) [Harr2018] found the gap between tracing and writing has largely closed by CS2, but novices who still have a gap, in either direction, are likely to do poorly.
- **"Our second recommendation is therefore to teach novices how to debug."** [Fitz2008, Murp2008] found good debuggers were good programmers, but not all good programmers were good debuggers. The good debuggers stepped through programs with a symbolic debugger, traced execution by hand, wrote tests, and re-read the spec often. These are all teachable habits. (Bib: Fitz2008, novices use tracing and testing rather than causal reasoning. Murp2008, many students don't recognize when they're stuck.)
- **Ineffective tracing and isolation habits:** putting the same print statement in both branches of an if-else, and commenting out lines that were actually correct while isolating a problem. Teachers can make these mistakes deliberately, point them out, and correct them.
- **Managing pace.** [Alqa2017]: more experienced learners solved debugging problems significantly faster, but times varied widely, typically 4–10 minutes per exercise. So some learners need 2–3 times longer than others. Teaching slower learners what the faster ones do makes the group's progress more uniform.
- **Reading code** is the single most effective way to find bugs, per multiple studies [Basi1987, Keme2009, Bacc2013]. The code quality rubric of [Steg2014, Steg2016a], online at [Steg2016b], is a good checklist of what to look for, but "is best presented in chunks rather than all at once."
- Having learners read code and summarize its behaviour is a good exercise (§5.1) but often too slow for class. **Having them predict a program's output just before running it** reinforces learning (§9.11) and gives a natural moment for "what if" questions. Instructors or learners can also **trace changes to variables** as they go (Figure 7.1), which [Cunn2017] found effective.
- **Figure 7.1, "Tracing the Values of Variables" (description).** Left: a short Python program:
  ```python
  numbers = [1, 3, -2, 5]
  total = 0
  positive = True
  for current in numbers:
      if current < 0:
          positive = False
      if positive:
          total = total + current
  ```
  Right, past a vertical line: a hand trace with one row per variable (`total`, `positive`, `current`). Each new value is written to the right of the previous one as it changes. `total`: 0, 1, 4. `positive`: True, then False. `current`: 1, 3, -2, 5. Once `positive` becomes False at −2, `total` stops changing.
- **Testing.** Novices seem as reluctant to test as professionals. Its value isn't in doubt: [Cart2017] found high-performing novices spent a lot of time testing, while low performers spent much more time working on code with errors. Many instructors require tests for assignments, but how good are those tests?
  - [Bria2015] scored learners' programs by how many teacher-provided tests they passed, and learners' tests by how many deliberately seeded bugs they caught. Novices' tests often had **low coverage** and often **tested many things at once**, making errors hard to pinpoint.
  - [Edwa2014b] pooled all bugs in all novices' submissions and checked which the novices' test suites detected: on average only **13.6%** of the faults in the program population. **90%** of novices' tests were very similar, which suggests novices write tests to confirm code works (the happy path), not to find where it fails.
- **Teaching better testing:** define a programming problem by a set of tests to pass rather than a written description (§12.1). But first, look at how many tests you have written for your own code recently, and decide whether you're teaching what you believe people should do, or what they (and you) actually do.

### §7.3 What Misconceptions Do Novices Have?
- Ch 2 explained why clearing up misconceptions matters as much as teaching problem-solving strategies.
- **The superbug** [Pea1986]: the belief that you can communicate with a computer as with a person, i.e. that it understands intention. **"Our third recommendation is therefore to teach novices that computers don't understand programs."** Calling a variable "cost" doesn't guarantee its value is a cost.
- [Sorv2018] presents more than 40 other misconceptions, many also in [Qian2017]'s survey. Examples:
  - **Spreadsheet-style variables** [Kohn2017]: after `grade = 65; total = grade + 10; grade = 80; print(total)`, novices expect 90 rather than 75. This is a plausible-but-wrong mental model built by analogy. (Bib: students often believe in delayed evaluation, or that whole equations are stored in variables.)
  - A variable holds the history of its values, i.e. remembers what it used to be.
  - Two objects with the same value for a name or id attribute must be the same object.
  - Functions are executed as they are defined, or in the order they are defined.
  - A while loop's condition is evaluated constantly, so the loop stops the moment it becomes false. Likewise, if-conditions are evaluated constantly and their bodies run as soon as the condition becomes true, wherever control happens to be.
  - Assignment moves values: after `a = b`, `b` is empty.
- **Concept-map evidence** [Muhl2016]: 350 concept maps compared people who had done a CS course with people who hadn't. Unsurprisingly, the experienced group's maps looked more like experts'. The details showed what learners take away: "program" was central in both, but next most central for those with prior exposure were "class" (object-oriented sense) and "data structure", and for those without, "processor" and "data".

### §7.4 What Mistakes Do Novices Make?
- Mistakes can tell us what to prioritize, but **most teachers don't know how common different mistakes actually are.**
- [Brow2017], the largest study (novice Java):
  - **Mismatched quotes and parentheses** are the most common error, and the easiest to fix.
  - Some mistakes are usually made only once, e.g. putting an if-condition in `{}` instead of `()`.
  - Mistakes that produce compiler errors are fixed much faster than those that don't.
  - Some mistakes recur many times, e.g. **calling methods with the wrong arguments** (a string instead of an integer).
  - **Caution:** distinguish mistakes from work in progress. An empty if or an unused method may just be unfinished code.
  - **Teachers' beliefs vs. data:** "educators formed only a weak consensus about which mistakes are most frequent, … their rankings bore only a moderate correspondence to the students in the…data, and … educators' experience had no effect on this level of agreement." Example: confusing `=` with `==` in loop conditions was far less common than most teachers believed.
- **Box "Not Just for Code"** [Park2015]: data from an online HTML editor in an intro web development course. Nearly all learners made syntax errors still unresolved weeks in. 20% concerned the relatively complex rules on which HTML elements may nest in which, but 35% concerned the *simpler* tag syntax for how elements nest. Instructors saying "But the rules are simple" is an example of expert blind spot (Ch 3).

### §7.5 What Are We Teaching Them Now?
- Little is known about what bootcamps and other free-range initiatives teach, partly because many won't share their curricula. More is known about schools.
- **[Luxt2017] topics in introductory programming courses, by frequency:**

  | Topic | Number of courses | % |
  |---|---|---|
  | Programming Process | 90 | 87% |
  | Abstract Programming Thinking | 65 | 63% |
  | Data Structures | 41 | 40% |
  | Object-Oriented Concepts | 37 | 36% |
  | Control Structures | 34 | 33% |
  | Operations & Functions | 27 | 26% |
  | Data Types | 24 | 23% |
  | Input/Output | 18 | 17% |
  | Libraries | 15 | 15% |
  | Variables & Assignment | 14 | 14% |
  | Recursion | 10 | 10% |
  | Pointers & Memory Management | 5 | 5% |

- [Luxt2017] also showed how concepts depend on each other. You can't explain operator precedence without first explaining a few operators, and those are hard to explain meaningfully without variables (otherwise you're comparing constants like `5<3`, which confuses learners).
- **Learning trajectories** [Rich3017]: a review of about a hundred articles to find trajectories for elementary and middle school (K-8) computing, covering sequencing, repetition, and conditionals. They are "essentially collective concept maps", combining and rationalizing many educators' implicit and explicit thinking.
- **Figure 7.2, "Learning Trajectory for Conditions" (from [Rich3017]), description.** A directed graph of 12 statements. A legend marks level by border: dashed = beginner, thin solid = intermediate, thick = advanced. Arrows point from prerequisite to dependent idea.
  - Beginner: (A) "Actions often results from specific causes"; (B) "A condition is something that can be true or false"; (C) "A conditional connects a condition to an outcome"; (F) "Each of the two states of a condition may have its own action"; (H) "Conditional statements evaluate conditions and complete connected actions".
  - Intermediate: (E) "Sometimes multiple conditions must be considered"; (G) "Conditions can overlap and more than one can apply"; (I) "Computers require all actions to be specified"; (K) "Conditional statements can create branches in the flow of execution".
  - Advanced: (D) "A Boolean is a variable that can be true or false"; (J) "Logical operators can be used to combine conditions"; (L) "Conditional statements can be combined in several ways".
  - Edges: A→C; B→C; B→D; B→E; C→F; C→H; D→J; E→G; E→I; F→I; G→I; G→J; H→I; H→K; I→L; J→L; K→L. (Reconstructed from the SVG source; edge directions inferred from arrowheads.)
- **Teaching ≠ learning.** "Study after study has shown that teaching evaluations don't correlate with actual learning outcomes" [Star2014, Uttl2017]. So use other measures or direct studies.
  - *Pass rates:* roughly two-thirds of post-secondary students pass their first computing course. Rates vary with class size and so on, but show **no significant differences over time or by language** [Benn2007a, Wats2014]. (Bib: Benn2007a, 67% pass, varying from 5% to 100%. Wats2014, on average one-third fail CS1.)
  - *Prior experience* [Wilc2018]: novices with prior experience outscored those without by 10% in CS1, but the gap disappeared by the end of CS2. Women with prior exposure outperformed their male peers in all areas but were consistently less confident (see §10.4).
  - *Direct study* [McCr2001], replicated by [Utti2013]: "…the disappointing results suggest that many students do not know how to program at the conclusion of their introductory courses." For 216 students from four universities, the average score was 22.89 out of 110 on the study's general evaluation criteria. Wilson: this "may say as much about teachers' expectations as it does about student ability".
- **"Our fourth recommendation is to measure and track results in ways that can be compared over time,"** so you can tell whether lessons are getting more or less effective.

### §7.6 Do Languages Matter?
- **Short answer: "yes".** Novices learn to program faster and learn more with blocks-based tools like Scratch, which make syntax errors impossible [Wein2017b]. Block interfaces encourage exploration in a way text doesn't. Like all good tools, Scratch "can be learned accidentally" [Malo2010].
- **"Our fifth recommendation is therefore to start children and teens with blocks-based interfaces before moving to text-based systems."** The age qualification exists because Scratch deliberately looks like it's for younger users. Imitators like Blockly look more grown-up, but adults can still be hard to convince.
- **Figure 7.3, "Scratch" (description; screenshot from opensource.com, not CC BY):** the Scratch editor with a game stage (a map) top left, a sprite list below it, a palette of coloured block categories (Motion, Looks, Sound, Events, Control, Sensing, Operators, Data, …) in the middle, and scripts of interlocking coloured blocks ("when I receive…", "forever", "if … then", "change x by…") on the right.
- Scratch has probably been studied more than any other programming tool. [Aiva2016] analyzed over 250,000 Scratch projects and found about 28% had blocks that are never called or triggered. The authors hypothesize users treat them as a scratchpad for code they don't yet want to discard.
- [Grov2017, Mlad2017] studied novices learning loops in Scratch, Logo, and Python. Misconceptions about loops are minimized with blocks rather than text, and the gap grows as tasks get more complex (e.g. nested loops). (Bib: Grov2017, middle-schoolers using blocks still find loops, variables, and Boolean operators difficult. Mlad2017, fewer nested-loop misconceptions with Logo than Python.)
- [Wein2017a] studied a tool that lets learners switch between blocks and text. Learners tend to migrate from blocks to text over time. When they switched from text to blocks, their next action was to add a new type of command (bib: in two-thirds of such shifts). Possibly because browsing commands is easier with blocks, or because blocks make syntax errors with unfamiliar commands impossible. The authors: "…blocks also offer information about what is possible in the space and provide a low-stakes means of exploring unfamiliar code." Tools like Stride aim to smooth the blocks-to-text transition. Combined with notebooks like Jupyter and Stencila, they "may eventually eliminate the distinction altogether."
- **Box "Harder Than Necessary"** [Stef2013]: language creators make languages harder to learn by skipping basic usability testing. "…the three most common words for looping in computer science, for, while, and foreach, were rated as the three most unintuitive choices by non-programmers." C-style syntax (Java, Perl) is as hard for novices as a randomly designed syntax. Python and Ruby syntax is significantly easier, and Quorum's easier still, because its designers test each feature before adding it. [Stef2017] briefly summarizes what is known about language design and why.
- **Object-oriented and functional programming.**
  - Many educators advocate "objects first", though they disagree on what it means [Benn2007b] (bib: three meanings). [Sorv2014] describes and motivates this approach (bib: three cognitively plausible frameworks for the first weeks of CS1). [Koll2015] describes three generations of tools for novice OO programming.
  - **Challenges of early objects:** [Mill2016b] found most novices using Python struggled with `self`. They omitted it from method definitions, failed to use it for attributes, or both. Object reference errors were more common than other errors; the authors speculate this is partly due to the syntax mismatch between `obj.method(param)` and `def method(self, param)`. [Rago2017] found the same in high school students (with `this`), and that high school teachers often weren't clear on it either.
  - **Functional approach:** the Bootstrap project builds on functional programming, a tradition going back to Scheme and Lisp and to textbooks like [Fell2001, Frie1995, Abel1996]. If functional programming keeps gaining ground among professionals, it may become more popular for teaching.
  - **Recommendation:** "On balance, we recommend that instructors use procedural languages to start with." Don't teach defining classes or higher-order functions until learners understand basic control structures and data types. How fast to introduce them depends on the audience: learners building web apps in JavaScript must master callbacks much sooner than learners generating reports in C#.
- **Type declarations.** [Gao2017] found about 15% of bugs in JavaScript programs could be caught by requiring type declarations, "which is either high or low depending on what answer you wanted in the first place." But programming and learning to program differ. [Endr2014] found requiring novices to declare types adds some complexity, but pays off fairly quickly by documenting a method's use, forestalling questions about what is available and how to use it. **"We don't know enough yet to recommend typed or untyped languages for novices."** Python's optional typing may let researchers explore introducing types gradually.
- **Variable naming style.**
  - [Kern1999]: "Programmers are often encouraged to use long variable names regardless of context. This is a mistake: clarity is often achieved through brevity." Many programmers believe this, but [Hofm2017] found full-word names gave on average **19% faster comprehension** than letters and abbreviations.
  - [Beni2017]: single-letter names didn't affect novices' ability to *modify* code. Possibly because novice programs are shorter, or because some single letters carry implicit types and meanings: `i`, `j`, `n` are assumed to be integers, `s` a string, and `x`, `y`, `z` floats or integers about equally.
  - [Bink2012]: reading code differs fundamentally from reading prose. "…the more formal structure and syntax of source code allows programmers to assimilate and comprehend parts of the code quite rapidly independent of style. In particular…beacons and program plans play a large role in comprehension." Experienced developers are relatively unaffected by identifier style. (Bib adds: beginners benefit from camel case over "pothole" (underscore) case.)
  - **Recommendation:** use a consistent style in all examples. Since most languages have style guides (e.g. PEP 8) and checkers, the full recommendation is "to use tools to ensure that all code examples adhere to a consistent style."

### §7.7 Does Better Feedback Help?
- Incomprehensible error messages are a major source of frustration for novices, and sometimes for experts.
- [Beck2016] rewrote some Java compiler messages. Instead of `error: cannot find symbol` pointing at `public static void main(string[ ] args){`, learners saw: "Looks like a problem on line number 2. If "string" refers to a datatype, capitalize the 's'!" Novices given these messages made **fewer repeated errors and fewer errors overall**.
- [Bari2017] used eye tracking to show people really do read error messages, spending **13–25%** of their time on them. But reading error messages is as hard as reading source code, and how hard a message is to read strongly predicts task performance. **So instructors should give learners practice reading and interpreting error messages.** [Marc2011] has a rubric for classifying responses to error messages that is useful for grading such exercises.
- **Does visualization help?**
  - Visualizing programs is perennially popular. Tools like [Guo2013] (web-based Python execution visualizer, Online Python Tutor) and Loupe (JavaScript's event loop) are useful teaching aids.
  - But people learn more from **constructing** visualizations than from viewing others' [Stas1998, Ceti2016].
  - [Cunn2017] replicated a study of the sketches students make when tracing code. **Not sketching at all correlates with lower success.** Tracing changes to variables by writing new values near their names as they change was the most effective strategy (Figure 7.1). Confound checked: sketchers take significantly longer, but time taken didn't correlate with score. **Recommendation: teach students to trace variables' values when debugging.**
  - **Box "Flowcharts"** [Scan1989]: students understand flowcharts better than pseudocode *when both are equally well structured*. Earlier work favouring pseudocode compared structured pseudocode with tangled flowcharts. On a level playing field, novices did better with the graphical representation.

### §7.8 What Else Can We Do to Help?
- [Viha2014] examined the average improvement in pass rates for various interventions in programming classes. **Their own caveats:** pre-change teaching practices are rarely stated clearly; the quality of change isn't judged; only 8.3% of studies reported negative findings, so either there is positive reporting bias "or the way we're teaching right now is almost the worst way possible and anything would be an improvement"; and they looked only at university classes, so findings may not generalize.
- **The ten interventions (definitions, §7.8):**
  - **Collaboration:** activities that encourage student collaboration in classrooms or labs.
  - **Content Change:** parts of the teaching material changed or updated.
  - **Contextualization:** content and activities aligned with a specific context such as games or media.
  - **CS0:** a preliminary course before the intro programming course, possibly only for some (e.g. at-risk) students.
  - **Game Theme:** a game-themed component added to the course.
  - **Grading Scheme:** a change in grading; most commonly more points for programming activities and less weight on the exam.
  - **Group Work:** more group-work commitment, e.g. team-based and cooperative learning.
  - **Media Computation:** activities explicitly using media computation (Ch 10).
  - **Peer Support:** support by peers as pairs, groups, hired peer mentors, or tutors.
  - **Other Support:** umbrella for all other support, e.g. more teacher hours or extra support channels.
- **Figure 7.4, "Effectiveness of Interventions": data.** A horizontal bar chart. The x-axis runs 0–60 with gridlines every 10 and no axis title; per the text, the values are the average improvement in pass rates (presumably percent). Values read from bar lengths (pixel-measured, ±1):

  | Intervention | Approx. improvement |
  |---|---|
  | Media Computation | 48 |
  | Group Work | 45 |
  | CS0 | 43 |
  | Contextualization | 40 |
  | Collaboration | 34 |
  | Content Change | 34 |
  | Peer Support | 34 |
  | Other Support | 33 |
  | Grading Scheme | 29 |
  | Game Theme | 18 |

  (The book lists the bars alphabetically; sorted here.) Every intervention shows a positive average. Media computation is highest and game theme lowest by a wide margin. The bibliography annotation agrees: [Viha2014] "finds media computation the most effective, while introducing a game theme is the least effective."
- **Cooperative learning.** The list highlights its importance. [Beck2013] studied it over three academic years in courses by two instructors and found significant benefits overall and for many subgroups. Students got higher grades and left fewer questions blank on the final exam, which indicates greater self-efficacy and willingness to try to debug.
- **Unplugged / computational creativity.** Writing code isn't the only way to teach programming. [Shel2017]: computational creativity exercises improve grades at several levels (bib: done in small groups). Typical exercise: pick an everyday object (nail clipper, paper clip, Scotch tape) and describe it in terms of inputs, outputs, and functions. This is sometimes called "unplugged"; the CS Unplugged site collects such lessons.

### §7.9 Exercises
Summarized under **Practice exercises**. The [Sirk2012] common-error list is captured in **Templates and checklists** (T2).

### Appendix "A Little Bit of Theory"
- **What "learning" means is complicated**, especially beyond the standardized Western classroom. Two perspectives within educational psychology have mainly shaped Wilson's teaching:
  - **Cognitivism:** pattern recognition, memory formation, and recall. Good at low-level questions, but generally ignores larger ones like "What do we mean by 'learning'?" and "Who gets to decide?"
  - **Situated learning:** bringing people into a community; it recognizes that teaching and learning are always rooted in who we are and who we aspire to be (Ch 13).
- **Other perspectives** (the Learning Theories website and [Wibu2016] summarize them):
  - **behaviorism:** education as stimulus/response conditioning;
  - **constructivism:** learning is an active process in which learners construct knowledge for themselves;
  - **connectivism:** knowledge is distributed, and learning is navigating, growing, and pruning connections, with emphasis on the social learning the Internet makes possible.
  "It would help if their names were less similar." None of them can tell us how to teach on its own, because several methods may fit what we know about learning. We have to try methods in class with real learners to see how well they balance the forces in play.
- **Instructional design** is that trial work: "If educational psychology is the science, instructional design is the engineering."
- **Phonics vs. whole language example.** There are good reasons to think children read best by starting from letter sounds (phonics). There are equally good reasons to think they learn best by recognizing whole simple words like "open" and "stop" so they can use them sooner (whole language). Whole language may seem upside down, but more than a billion people learned Chinese and similar ideogrammatic languages this way. Only careful trials can tell which works best for most children most of the time. Confounds abound: the teacher's enthusiasm for a method may matter more than the method, since children model their teacher's excitement. Accounting for all that, "phonics does seem to be better than other approaches" [Foor1998].
- **Debunked myths.** Painstaking research is "essential to dispel myths that can get in the way of better teaching." Each of the following is recorded **as debunked**:
  - **Learning styles (visual/auditory/kinesthetic, VAK):** that teaching works better when matched to whether a learner likes to see, hear, or do. "Easy to understand, but as [DeBr2015] explains, it is almost certainly false." It is still marketed to parents, school boards, and the public.
  - **The learning pyramid** ("we remember 10% of what we read, 20% of what we hear…"): myth.
  - **"Brain games"** improve intelligence or slow its decline in old age: myth.
  - **The Internet is making us dumber:** myth.
  - **Young people read less than they used to:** myth.
  "Just as we need to clear away our learners' misconceptions in order to help them learn, we need to clear away our own about teaching."
- **Notional machines.** "Computational thinking" is bandied about partly because people agree it matters while meaning very different things by it. Wilson finds it more useful to aim for learners understanding a **notional machine**. The term was introduced in [DuBo1986] and means an abstraction of the structure and behaviour of a computational device. Per [Sorv2013], a notional machine:
  1. "is an idealized abstraction of computer hardware and other aspects of the runtime environment of programs;"
  2. "serves the purpose of understanding what happens during program execution;"
  3. "is associated with one or more programming paradigms or languages, and possibly with a particular programming environment;"
  4. "enables the semantics of program code written in those paradigms or languages (or subsets thereof) to be described;"
  5. "gives a particular perspective to the execution of programs; and"
  6. "correctly reflects what programs do when executed."
  (Bib: [Sorv2013] argues instructors should make the notional machine an explicit learning objective.)
- **Wilson's notional machine for Python** (14 points):
  1. Running programs live in memory, divided between a call stack and a heap.
  2. Memory for data is always allocated from the heap.
  3. Every piece of data is stored in a two-part structure: the first part says what type it is, the second is the actual value.
  4. Atomic data (Booleans, numbers, character strings) is stored directly in the second part, and is never modified after creation.
  5. The scaffolding for collections like lists and sets is also stored in the second part, but holds references to other data, not the values themselves. Scaffolding can be modified after creation (a list extended, key/value pairs added to a dictionary).
  6. When code is loaded, Python parses it into a sequence of instructions stored like any other data. (This is why functions can be aliased and passed as parameters.)
  7. When code is executed, Python steps through the instructions, doing what each says in turn.
  8. Some instructions make Python read data, operate on it, and create new data.
  9. Other instructions make Python jump to another instruction instead of the next one; this is how conditionals and loops work.
  10. Another instruction calls a function: a temporary switch from one blob of instructions to another.
  11. When a function is called, a new stack frame is pushed on the call stack.
  12. Each stack frame stores variable names and references to data. (Parameters are just another kind of variable.)
  13. When a variable is used, Python looks in the top stack frame, and if it isn't there, in the bottom (global) frame.
  14. When the function finishes, Python erases its frame and switches back to the calling blob. If there is no "beforehand", the program has finished.
- **How Wilson uses it:** he doesn't explain it all at once, but draws on it "over and over again" when drawing pictures, tracing execution, and so on. After about **25 hours of class and 100 hours of work on their own time**, he expects adult learners to understand most of it.

## Rules
- **PCK-1** — Show learners *how* to program: demonstrate the process, not just the language features. *Why:* experts have "what" and "how" (plans), and novices lack both, but teaching usually covers only "what". Bugs often come from having no strategy [Solo1984, Solo1986, Mull2007b]. Wilson calls this the chapter's most important recommendation. *Check:* does the lesson include live demonstration of writing, running, and fixing code (§8.4), not just finished code on slides? (§7.1)
- **PCK-2** — When demonstrating, take small steps with frequent feedback, and pick a plan and stick to it. *Why:* [Blik2014]. Merging plans or goals, or making random changes, drops or fragments goals and causes bugs [Spoh2985]. *Check:* does the demo run code often, and narrate the plan before deviating? (§7.1)
- **PCK-3** — Show the expert writing order explicitly: signature first, then control flow, then initialization and corner cases. *Why:* experts work outside-in, novices write in page order [Ihan2011]. *Check:* does a live-coding script build skeleton-first, and say so? (§7.1)
- **PCK-4** — Give novices a vocabulary of programming plans, e.g. label variables with their roles (stepper, gatherer, most-wanted holder…). *Why:* labels are "a vocabulary to think with" and plans for writing code [Kuit2004, Byck2005, Saja2006]. *Check:* are example programs annotated with variable roles or named plans? (§7.1)
- **PCK-5** — Teach debugging explicitly as a skill: stepping with a debugger, hand tracing, writing tests, and re-reading the spec. Deliberately commit and correct typical bad habits (the same print in both branches; commenting out correct lines). *Why:* good programmers aren't necessarily good debuggers, and these habits are teachable [Fitz2008, Murp2008, McCa2008]. Wilson's second recommendation. *Check:* is there at least one debugging demonstration and exercise per major topic? (§7.2)
- **PCK-6** — Teach slower learners the strategies faster learners use. *Why:* debugging times vary 2–3× (4–10 min typical) [Alqa2017]; sharing strategies evens out group progress. *Check:* does the plan include explicit strategy sharing, not just extra time? (§7.2)
- **PCK-7** — Teach code reading as the main bug-finding method, using a code-quality rubric introduced in chunks. *Why:* reading code is the single most effective way to find bugs [Basi1987, Keme2009, Bacc2013]; rubric [Steg2014, Steg2016a, Steg2016b]. *Check:* are there code-reading activities, and is the rubric staged rather than dumped at once? (§7.2)
- **PCK-8** — Before running code in class, have learners predict its output. *Why:* it reinforces learning (§9.11), opens "what if" questions, and practises tracing, which novices are weak at [List2004, List2009, Harr2018]. *Check:* count predict-then-run moments in the lesson. (§7.2)
- **PCK-9** — Teach learners to trace variables' values by writing each new value next to the variable's name as it changes. Have them construct visualizations, not just watch them. *Why:* not sketching correlates with lower success, and this tracing style was most effective regardless of time taken [Cunn2017]. Constructing beats viewing [Stas1998, Ceti2016]. *Check:* does a debugging or tracing exercise ask learners to produce a trace table (Figure 7.1 style)? (§7.2, §7.7)
- **PCK-10** — Teach testing as a way to *find* bugs, not just confirm the happy path. Consider specifying problems as tests to pass (§12.1). Be honest about whether you practise what you preach. *Why:* novice tests have low coverage, test many things at once [Bria2015], catch only 13.6% of faults, and 90% are near-identical [Edwa2014b]. High performers test a lot [Cart2017]. *Check:* do testing exercises reward catching seeded bugs or edge cases? (§7.2)
- **PCK-11** — Explicitly teach that computers don't understand programs or intentions (the "superbug"). *Why:* it is the biggest novice misconception [Pea1986]. Wilson's third recommendation. *Check:* is there an example where a meaningful name (e.g. `cost`) doesn't guarantee meaning, or where code does what was written rather than what was meant? (§7.3)
- **PCK-12** — Target known misconceptions with diagnostic exercises: spreadsheet-style variables, variables remembering history, same-id-means-same-object, functions running when defined, constantly re-evaluated loop or if conditions, assignment moving values, and the [Sirk2012] list. *Why:* misconceptions must be cleared, not just correct models added (Ch 2) [Sorv2018, Qian2017, Kohn2017]. *Check:* for each core concept, does an exercise have a wrong answer that reveals the matching misconception? (§7.3, §7.9)
- **PCK-13** — Prioritize errors by measured frequency, not teacher intuition, and distinguish unfinished code from mistakes. *Why:* educators agree only weakly on which mistakes are most frequent, experience doesn't help, and `=` vs `==` is overrated [Brow2017]. *Check:* is the error-focus list grounded in data (studies or your own logs)? Does feedback avoid flagging work in progress? (§7.4)
- **PCK-14** — Never dismiss syntax as "simple". Expect basic syntax errors (mismatched quotes and brackets, tag syntax) to persist for weeks, and teach them explicitly. *Why:* in HTML, 35% of persistent errors were simple tag syntax, against 20% for complex nesting rules [Park2015]. Mismatched quotes and parentheses are the most common Java error [Brow2017]. Saying "the rules are simple" is expert blind spot. *Check:* search lesson text for "simple", "easy", "just", and check that basic syntax gets practice. (§7.4)
- **PCK-15** — Sequence topics by conceptual dependency, using published trajectories where they exist (e.g. variables → operators → precedence; the conditionals trajectory). *Why:* [Luxt2017] dependencies; [Rich3017] trajectories are collective concept maps. *Check:* does any concept appear before its prerequisites (e.g. comparing constants like `5<3` before variables exist)? (§7.5)
- **PCK-16** — Measure and track learning in ways comparable over time. Don't use teaching evaluations as evidence of learning. *Why:* evaluations don't correlate with learning [Star2014, Uttl2017]; many students can't program after CS1 [McCr2001, Utti2013]. Wilson's fourth recommendation. *Check:* is there a repeatable assessment (same or equivalent tasks) whose results are kept term over term? (§7.5)
- **PCK-17** — Start children and teens with blocks-based tools before moving to text. For adults, expect resistance to childish-looking tools. *Why:* blocks give faster, more learning and fewer loop misconceptions, especially for nested loops; they encourage exploration [Wein2017b, Malo2010, Grov2017, Mlad2017, Wein2017a]. Wilson's fifth recommendation. *Check:* for under-18 novices, is the first environment blocks-based? For adults, is the choice justified? (§7.6)
- **PCK-18** — Start with procedural programming. Delay defining classes and higher-order functions until learners grasp basic control structures and data types, and adjust timing to learners' goals (e.g. JavaScript callbacks early for web apps). *Why:* early objects cause specific trouble (`self`/`this`) for students and even teachers [Mill2016b, Rago2017]. *Check:* does a unit on classes or HOFs come before loops, conditionals, and types are solid? (§7.6)
- **PCK-19** — Don't claim research settles typed vs. untyped languages for novices. *Why:* "We don't know enough yet" (§7.6) [Gao2017, Endr2014]. *Check:* any language-choice advice presents this as open. (§7.6)
- **PCK-20** — Use one consistent naming and code style in all examples, enforced by a style-checking tool (e.g. PEP 8 for Python). Prefer full-word names. *Why:* full words gave 19% faster comprehension [Hofm2017]; single letters with conventional meanings don't hurt novices modifying code [Beni2017]; experienced readers are style-independent but consistency matters [Bink2012]. *Check:* run a linter over all lesson code. (§7.6)
- **PCK-21** — Give learners deliberate practice reading and interpreting error messages, and use enhanced, novice-friendly messages where tools allow. *Why:* people do read errors (13–25% of time), and readability predicts performance [Bari2017]; enhanced messages reduce errors [Beck2016]; grading rubric in [Marc2011]. *Check:* is there an exercise where learners explain what an error message means and what to do? (§7.7)
- **PCK-22** — When comparing graphical and textual representations (e.g. flowcharts vs. pseudocode), make both equally well structured. *Why:* the earlier pro-pseudocode result came from tangled flowcharts [Scan1989]. *Check:* are diagrams as clean as the text they replace? (§7.7)
- **PCK-23** — Favour interventions with the strongest reported effects: media computation, group work, cooperative learning, CS0 bridging, contextualization, peer support. Don't count on a game theme alone. *Why:* [Viha2014] (Figure 7.4); cooperative learning raises grades and self-efficacy [Beck2013]. *Caveat:* positive reporting bias and university-only samples. *Check:* does the course plan include at least one collaborative structure and a meaningful context? (§7.8)
- **PCK-24** — Include non-coding ("unplugged") computational creativity exercises, e.g. describing everyday objects by inputs, outputs, and functions. *Why:* they improve grades at several levels [Shel2017]. *Check:* is there at least one non-programming exercise in a programming course? (§7.8)
- **PCK-25** — Make an explicit notional machine a learning objective, introduce it piece by piece, and reuse it whenever you draw pictures or trace execution. *Why:* Wilson prefers it to vague "computational thinking"; it must correctly reflect execution [DuBo1986, Sorv2013]. Adults reach most of his Python model after about 25 class hours plus 100 hours of their own work. *Check:* can the lesson's diagrams be explained in terms of one consistent model (stack, heap, frames, references)? (Theory appendix)
- **PCK-26** — Don't design lessons around debunked myths: VAK learning styles, the learning pyramid percentages, brain games. *Why:* [DeBr2015] and the Theory appendix. *Check:* reject any plan that matches content to "visual/auditory/kinesthetic learners" or cites "we remember 10% of what we read". (Theory appendix)
- **PCK-27** — Present research as actionable approximations, but carry its scope limits. Most findings come from school children and undergraduates, not adult free-range learners. *Why:* [Henr2010]; [Viha2014]'s own caveats. *Check:* when citing a finding for adult workshops, note the population gap. (§7 intro, §7.8)

## Procedures

### P1. Building a programming lesson with PCK built in
1. **List the concepts** and order them by dependency (PCK-15). Check [Luxt2017]-style prerequisites and any trajectory (e.g. Figure 7.2 for conditionals).
2. **For each concept, list the misconceptions to target** (PCK-11, PCK-12): the superbug, the §7.3 list, and the [Sirk2012] list. Write one diagnostic exercise per misconception (see T2).
3. **Plan the "how":** script a live-coding demo that builds skeleton-first (PCK-3), runs often in small steps, and states its plan (PCK-2). Name variable roles as they appear (PCK-4).
4. **Insert predict-then-run moments** before each run (PCK-8).
5. **Add a debugging episode:** introduce a bug, model debugger or trace-table use and re-reading the spec, and deliberately show and correct a bad habit (PCK-5, PCK-9).
6. **Add an error-message reading exercise** for the errors most likely at this stage. Use frequency data, not intuition (PCK-13, PCK-14, PCK-21).
7. **Add testing practice** aimed at finding bugs (seeded bugs, edge cases), or define a problem by its tests (PCK-10).
8. **Choose the environment:** blocks for children and teens; procedural before OO or HOF; consistent, linted style (PCK-17, PCK-18, PCK-20).
9. **Wrap in a supportive structure:** pairs or groups, a meaningful context (media or domain), perhaps an unplugged opener (PCK-23, PCK-24).
10. **Decide how you'll measure outcomes comparably over time** (PCK-16).

### P2. Teaching a variable trace (Figure 7.1 method)
1. Put the code on the left and a vertical line to its right.
2. List each variable name, one per row, to the right of the line.
3. Step through execution. When a variable changes, write the new value to the right of its previous value in that row; don't erase old values.
4. Ask learners to predict the final values before finishing the trace (PCK-8).
5. Have learners make their own traces for the next example: constructing beats viewing (PCK-9).

### P3. Diagnosing a learner's bug through PCK lenses
1. Is it a syntax slip (quotes, brackets, tags)? Common and quick; point to the error message and have them read it aloud (PCK-21).
2. Is it a plan problem: random edits, merged goals? Get them to state the plan, then pick one and stick to it (PCK-2).
3. Is it a misconception (superbug, spreadsheet variables, constantly evaluated conditions, assignment moves values, function runs at definition, `self` omitted)? Do a trace (P2) against the notional machine (PCK-25).
4. Is it actually unfinished code? Don't treat work in progress as an error (PCK-13).
5. Are they debugging ineffectively (same print in both branches, commenting out correct lines)? Model the better habit (PCK-5).

### P4. Introducing a notional machine (Wilson's practice)
1. Choose or write a model that meets [Sorv2013]'s six properties for the language taught.
2. Don't present it all at once. Introduce each part when a lesson needs it (e.g. stack frames when functions arrive; references when lists arrive).
3. Reuse the same pictures and vocabulary in every trace and diagram.
4. Expect adult learners to grasp most of it after about 25 class hours plus 100 hours of their own work.

## Diagnostics
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

## Templates and checklists

### T1. Novice misconception bank (§7.3)
| Misconception | Probe exercise idea |
|---|---|
| Superbug: the computer understands intent [Pea1986] | Variable named `cost` holds a non-cost; ask what the program "knows". |
| Spreadsheet-style variables [Kohn2017] | `grade = 65; total = grade + 10; grade = 80; print(total)`: answer 75, distractor 90. |
| Variable remembers its history | Ask for "the previous value" of a reassigned variable. |
| Same name or id attribute means same object | Two objects with equal ids: are they identical? |
| Functions run when defined, or in definition order | Define functions in one order, call them in another; predict output. |
| While/if conditions are constantly evaluated | Loop whose condition becomes false mid-body; predict how many statements still run. |
| Assignment moves values (`a = b` empties `b`) | Print `b` after `a = b`. |

### T2. [Sirk2012] common errors (write one exercise per chosen error)
| Error | Definition (§7.9) |
|---|---|
| Inverted assignment | The student assigns the value of the left-hand variable to the right-hand variable, rather than the other way around. |
| Wrong branch | Even though the conditional evaluates to False, the student jumps to the then clause. |
| Wrong False | As soon as the conditional evaluates to False, the student returns False from the function. |
| Executing function instead of defining it | The student believes a function is executed as it is defined. |
| Unevaluated parameters | The student believes the function starts running before the parameters have been evaluated. |
| Parameter evaluated in the wrong frame | The student creates parameter variables in the caller's frame, not the callee's. |
| Failing to store return value | The student does not assign the return value in the caller. |
| Assignment copies object | The student creates a new object rather than copying a reference. |
| Method call without subject | The student tries to call a method from a class without first creating an instance. |

### T3. Roles of variables quick card
See the §7.1 table: fixed value, stepper, walker, most-recent holder, most-wanted holder, gatherer, follower, one-way flag, temporary, organizer, container.

### T4. Good-debugger habits checklist [Fitz2008, Murp2008]
- [ ] Step through with a symbolic debugger.
- [ ] Trace execution by hand (trace table, Figure 7.1 style).
- [ ] Write tests.
- [ ] Re-read the spec frequently.
- [ ] Don't put the same print in both branches.
- [ ] Don't comment out lines that are actually correct.
- [ ] Read the code, the most effective bug-finding method.
- [ ] Read the error message closely.

### T5. Intervention menu with [Viha2014] effect sizes (Figure 7.4, approximate)
Media Computation ~48 · Group Work ~45 · CS0 ~43 · Contextualization ~40 · Collaboration ~34 · Content Change ~34 · Peer Support ~34 · Other Support ~33 · Grading Scheme ~29 · Game Theme ~18. Caveats: positive reporting bias (only 8.3% negative), baselines unclear, change quality not judged, university-only.

### T6. Language and tool choice checklist (§7.6)
- [ ] Audience under 18 → blocks first (Scratch); adults → justify; Blockly looks more grown-up.
- [ ] Prefer languages with learner-tested syntax; C-style syntax is as hard as random syntax for novices [Stef2013].
- [ ] Procedural first; classes and HOFs after control structures and data types (adjust for goals such as JS callbacks).
- [ ] Typed vs. untyped: undecided by research.
- [ ] Full-word names; one consistent style; linter enforced.
- [ ] Novice-friendly error messages if available; practise reading them.
- [ ] Visualizer available (e.g. [Guo2013]), but learners also draw their own traces.

### T7. Notional machine properties check [Sorv2013]
Idealized abstraction of hardware and runtime · explains what happens during execution · tied to paradigm(s), language(s), maybe environment · lets code semantics be described · gives a particular perspective on execution · correctly reflects what programs do.

## Examples
- **Enhanced compiler message** [Beck2016]: the Java error "cannot find symbol" for `string[] args` was replaced by "Looks like a problem on line number 2. If "string" refers to a datatype, capitalize the 's'!" → fewer repeated and overall errors. Lesson: rewrite or annotate errors in novice terms.
- **Spreadsheet variables** [Kohn2017]: `grade=65; total=grade+10; grade=80; print(total)` gives 75, but novices answer 90. Lesson: analogies produce plausible-but-wrong models; probe with exactly this kind of question.
- **Trace table (Figure 7.1):** a running sum skips values once a flag flips; the trace shows `total` stopping at 4. Lesson: writing values beside names makes control flow visible.
- **Concept maps** [Muhl2016]: after a CS course, "class" and "data structure" become central; without one, "processor" and "data". Lesson: concept maps reveal what learners actually took away.
- **Scratch dead code** [Aiva2016]: 28% of 250,000 projects contain uncalled blocks, perhaps used as a scratchpad. Lesson: unused code isn't necessarily an error (compare the work-in-progress caution in §7.4).
- **Blocks↔text switching** [Wein2017a]: switching to blocks precedes adding a new command type. Lesson: blocks double as a browsable menu of what's possible.
- **Objects early** [Mill2016b, Rago2017]: `self`/`this` confusion among students, and among some teachers. Lesson: delay OO, or teach the syntax mismatch explicitly.
- **Self-test honesty (§7.2):** before demanding tests, count your own recent tests. Lesson: teach what you actually believe and practise.
- **Computational creativity** [Shel2017]: describe a nail clipper, paper clip, or Scotch tape by inputs, outputs, and functions. Lesson: unplugged exercises improve programming grades.
- **Phonics vs. whole language** (Theory appendix): both are theoretically reasonable, so only trials decide; teacher enthusiasm is a confound; phonics seems better [Foor1998]. Lesson: theory constrains but doesn't choose methods; instructional design must test.
- **Wilson's Python notional machine** (Theory appendix): 14 statements on stack, heap, typed two-part data, immutable atoms, reference-holding collections, instructions-as-data, jumps, frames, and lookup. Lesson: one consistent model to return to throughout a course.

## Evidence and caveats
- **Field maturity:** computing education research is young (CSTA founded 2005). Most studies are of school children and undergraduates [Henr2010], and less is known about adult free-range learners. Wilson deliberately states findings as "actionable approximations" rather than hedged claims, so the skill should restore the hedges when stakes are high.
- **Expert/novice plans:** [Solo1984, Solo1986]; teaching patterns works [Mull2007b] ("one of many studies"); small steps [Blik2014]; goal/plan bugs [Spoh2985]; outside-in authoring [Ihan2011]; roles of variables [Kuit2004, Byck2005, Saja2006].
- **Debugging and tracing:** [McCa2008] neglect in textbooks; [List2004, List2009] weak prediction and completion; [Harr2018] trace–write gap closes by CS2, and a persistent gap predicts poor results; [Fitz2008, Murp2008] debugger habits; [Alqa2017] 4–10 min spread; code reading is most effective [Basi1987, Keme2009, Bacc2013]; quality rubric [Steg2014, Steg2016a, Steg2016b]; [Cunn2017] tracing values is most effective, and not sketching correlates with lower success, with time not a confound.
- **Testing:** [Cart2017] high performers test more; [Bria2015] low coverage, multi-concern tests; [Edwa2014b] 13.6% fault detection, 90% similar tests.
- **Misconceptions:** [Pea1986] superbug; [Sorv2018] 40+ misconceptions; [Qian2017] survey; [Kohn2017] spreadsheet model; [Muhl2016] 350 concept maps; [Sirk2012] error list.
- **Mistakes:** [Brow2017], the largest study: teachers' rankings only moderately match the data, and experience doesn't help; [Park2015] HTML syntax errors (35% basic tag syntax, 20% nesting rules).
- **Curriculum:** [Luxt2017] topic frequencies and dependencies; [Rich3017] K-8 trajectories.
- **Outcomes:** teaching evaluations don't correlate with learning [Star2014, Uttl2017]; about 2/3 pass CS1, with no significant change over time or by language [Benn2007a, Wats2014]; prior experience gives +10% in CS1, gone by the end of CS2, and women with prior exposure outperform male peers but are less confident [Wilc2018]; 22.89/110 average across 216 students [McCr2001], replicated [Utti2013]. Wilson notes it may reflect teachers' expectations as much as ability.
- **Languages:** blocks are better for novices [Wein2017b, Malo2010, Grov2017, Mlad2017]; blocks as exploration [Wein2017a]; [Aiva2016] 28% dead blocks; syntax usability [Stef2013, Stef2017]; objects-first contested [Benn2007b, Sorv2014, Koll2015]; `self`/`this` trouble [Mill2016b, Rago2017]; functional tradition [Fell2001, Frie1995, Abel1996]. **Types: unresolved** [Gao2017] (15% of JS bugs, interpretation depends on prior beliefs) and [Endr2014] (types pay off as documentation). **Naming:** [Kern1999] brevity claim vs. [Hofm2017] 19% faster with words; [Beni2017] single letters fine for modification; [Bink2012] style matters little to experts.
- **Feedback and visualization:** [Beck2016] enhanced messages help; [Bari2017] 13–25% of time on error messages, and difficulty predicts performance; [Marc2011] response rubric; visualization tools [Guo2013]; constructing beats viewing [Stas1998, Ceti2016]; flowcharts beat pseudocode when equally structured [Scan1989].
- **Interventions:** [Viha2014] (strong caveats: reporting bias with only 8.3% negative, unclear baselines, change quality not judged, university-only); [Beck2013] cooperative learning over three years with two instructors; [Shel2017] computational creativity.
- **Theory appendix:** [Wibu2016] theory summaries; [Foor1998] phonics better; [DeBr2015] VAK learning styles "almost certainly false". **Debunked (myths):** VAK learning styles, the learning pyramid, brain games, "the Internet makes us dumber", "young people read less". Notional machine [DuBo1986, Sorv2013]. The 25 h + 100 h figure is Wilson's personal expectation, not a research finding.
- **Methods survey:** [Ihan2016].

## Practice exercises
- **Checking for Common Errors** — pick three [Sirk2012] errors (T2) and write an exercise for each that checks learners aren't making it. Individual, 20 min.
- **Mangled Code** — take a past exercise solution, mangle it in two ways (remove comments, delete, replace, or move lines, insert unneeded lines), and swap with a partner to reconstruct. [Chen2017]: performance on these correlates strongly with code-writing assessments and needs less in-person marking. Pairs, 15 min.
- **The Rainfall Problem** — solve [Solo1986]'s Rainfall Problem (read positive integers until 99999, then print their average) in any language and compare with a partner. Used in many studies [Fisl2014, Simo2013, Sepp2015]. (Bib: Fisl2014, fewer low-level errors in a functional language; Simo2013, harder now because novices are less used to keyboard input, so comparisons with past results may be unfair; Sepp2015, a meta-study of its difficulty.) Pairs, 10 min.
- **Roles of Variables** — classify each variable in a 5–15 line program by role (§7.1 table), compare with a partner, and discuss disagreements. Pairs, 15 min.
- **Choose Your Own Adventures** — which of [Sorv2014]'s three approaches do you use when teaching, or is yours different? Individual, 10 min. (The exercise points to §7.5, but [Sorv2014] is discussed in §7.6.)
- **What Are You Teaching?** — compare your topics with [Luxt2017]'s list: which do you cover, and what extras? Individual, 10 min.
- **Beneficial Activities** — which [Viha2014] interventions do you already use, which could you easily add, and which are irrelevant? Individual, 10 min.
- **Visualizations** — what visualization do you most like to use (static or animated), and do learners see it, discover it, or something in between? Individual, 10 min.
- **Misconceptions and Challenges** — choose a section (e.g. data structures, functions) of the Professional Development for CS Principles Teaching misconception list, and discuss which you had, still have, or have seen in learners. Small groups, 15 min.

## Cross-references
- `02-mental-models.md`: misconceptions and why clearing them matters (Ch 2); concept maps; diagnostic MCQs.
- `03-expertise-and-memory.md`: expert blind spot ("the rules are simple"); expert vs. novice knowledge.
- `04-cognitive-load.md`: why showing "how" fits cognitive load theory; Parsons Problems; faded examples.
- `05-individual-learning.md`: reading and summarizing code (§5.1); study strategies.
- `06-lesson-design.md`: where PCK feeds the brainstorm (misconceptions, concepts) and exercise design; PRIMM.
- `08-teaching-as-performance.md`: live coding (§8.4), the main vehicle for showing "how" and debugging.
- `09-in-the-classroom.md`: predict-then-run and related in-class practices (§9.11); pair programming.
- `10-motivation-and-inclusion.md`: media computation; confidence gap in women with prior experience (§10.4).
- `12-exercise-types.md`: tests as problem specifications (§12.1); Parsons, tracing, and debugging exercise formats.
- `13-building-community.md`: situated learning and communities of practice.

## Source map
| Book section | Covered under |
|---|---|
| §7 intro (three knowledges, field maturity, population caveat, Jargon box) | Concepts §7 intro; PCK-27 |
| §7.1 How Do Novices Program? (incl. Roles of Variables) | Concepts §7.1; PCK-1 to PCK-4; T3 |
| §7.2 How Do Novices Debug and Test? (Figure 7.1) | Concepts §7.2; PCK-5 to PCK-10; P2; T4 |
| §7.3 What Misconceptions Do Novices Have? | Concepts §7.3; PCK-11, PCK-12; T1 |
| §7.4 What Mistakes Do Novices Make? ("Not Just for Code") | Concepts §7.4; PCK-13, PCK-14 |
| §7.5 What Are We Teaching Them Now? (Luxt2017 table, Figure 7.2) | Concepts §7.5; PCK-15, PCK-16 |
| §7.6 Do Languages Matter? (Figure 7.3, "Harder Than Necessary", OO/FP, types, naming) | Concepts §7.6; PCK-17 to PCK-20; T6 |
| §7.7 Does Better Feedback Help? (visualization, Flowcharts box) | Concepts §7.7; PCK-9, PCK-21, PCK-22 |
| §7.8 What Else Can We Do to Help? (Figure 7.4) | Concepts §7.8; PCK-23, PCK-24; T5 |
| §7.9 Exercises | Practice exercises; T2 |
| Appendix "A Little Bit of Theory" (theories, phonics, myths) | Concepts; PCK-26; Evidence |
| Appendix "A Little Bit of Theory" — Notional Machines | Concepts; PCK-25; P4; T7 |
