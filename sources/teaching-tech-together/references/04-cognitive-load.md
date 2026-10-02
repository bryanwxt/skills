# Cognitive Load

> Source: Greg Wilson, *Teaching Tech Together* (2018), Ch. 4 "Cognitive Load" (§4.1–§4.3). Licensed CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/); condensed and restructured for skill use, with quotations marked. Rule IDs use prefix `COG`.

## When a skill needs this
- An exercise generator builds **faded-example** series, **Parsons Problems**, or **subgoal-labelled** worked examples for a programming (or any procedural) skill.
- A teaching-feedback reviewer classifies the content of a lesson as intrinsic, germane or extraneous load and recommends cuts.
- A slide or video reviewer checks for **split attention** (narration plus identical captions, text far from graphics, decorative or "seductive" images) using Mayer's six principles.
- A documentation or tutorial writer produces **minimal-manual** pages: one self-contained task per page, with symptom → cause → fix notes.
- A lesson planner decides how much guidance novices need versus open-ended inquiry.

## Key terms
| Term | Meaning (one line) |
|---|---|
| Cognitive load theory | Learning effort splits into intrinsic, germane and extraneous load, which compete for fixed working memory (glossary, Ch 4). |
| Intrinsic load | What learners must keep in mind to absorb the new material itself. Reducible only by teaching less content. |
| Germane load | The desirable effort of linking new information to old; it separates learning from memorization. |
| Extraneous load | Anything in the instruction that distracts from learning. |
| Inquiry-based learning | Learners ask their own questions, set their own goals and find their own path through a subject. |
| Worked example | A solution broken into steps that can each be mastered, then combined. |
| Faded example | A series of examples with progressively more key steps blanked out. |
| Scaffolding | The non-blank, supporting material in early examples, removed over time. |
| Accumulator pattern | Processing items from a collection and repeatedly adding each result to a single variable. |
| Cognitive apprenticeship | A master models, coaches and explains why; the apprentice reflects and eventually explores alone. |
| Parsons Problem | Learners reorder given, jumbled pieces (e.g., lines of code) into a correct answer [Pars2006]. |
| Subgoal labelling | Naming the steps of a step-by-step problem-solving procedure. |
| Split-attention effect | Learning drops when learners must reconcile concurrent, *redundant* streams (e.g., captions plus identical narration). |
| Seductive / decorative / instructive graphics | Interesting but irrelevant / neutral and irrelevant / directly relevant to the goal [Sung2012]. |
| Minimal manual | Training made of single-page, self-contained tasks with error-recognition notes [Carr1987]. |

## Concepts

### Chapter 4 opening (unnumbered): cognitive load theory
- **The provocation, [Kirs2006]** (Kirschner, Sweller & Clark): unguided or minimally guided instruction is "very popular and intuitively appealing", but ignores human cognitive architecture and half a century of evidence that it "is less effective and less efficient than instructional approaches that place a strong emphasis on guidance." "The advantage of guidance begins to recede only when learners have sufficiently high prior knowledge to provide 'internal' guidance."
- **Why it was controversial:** it claimed that **inquiry-based learning**, where learners ask their own questions, set goals and find their own path as in real life, isn't effective. The argument is that it overloads learners by making them master a domain's facts and its problem-solving strategies at the same time.
- **The three loads (cognitive load theory):**
  - **Intrinsic load:** what must be held in mind to absorb the new material, e.g., what a variable is, or how assignment differs from a spreadsheet cell reference. It "can't be reduced except by reducing the amount of content being taught."
  - **Germane load:** the *desirable* effort of linking new information to old, which distinguishes learning from memorization. E.g., remembering that a loop variable gets a new value on each pass.
  - **Extraneous load:** everything else that distracts from learning. E.g., mapping the colours in the teacher's syntax highlighting to the different scheme in the learner's own editor.
- **Goal:** people split a fixed amount of working memory among the three, so teachers should **maximize the memory available for germane load**. Do that by reducing intrinsic load at each step and eliminating as much extraneous load as possible.
- **Worked examples.** Searching for a solution strategy is an extra burden on top of applying it. Worked examples that break a procedure into steps, each mastered alone before being combined (combining is "a step in its own right"), speed up learning.
- **Faded examples.** First, a nearly complete use of the strategy just demonstrated, with a few blanks. The next problem is of the same type with more blanks, and so on until the learner solves the whole problem. The non-blank part is **scaffolding**. Faded examples apply in "almost every kind of teaching, from sport and music to contract law."
- **The book's faded-example sequence** (pseudo-Python, all accumulator-pattern problems):
  1. *Demonstrated in full:* `total_length(["red","green","blue"]) => 12`. Set `total = 0`; for each word in the list, `total = total + word.length()`; return total.
  2. *A few blanks* (focuses on **control structures**): `word_lengths(...) => [3, 5, 4]`. `list_of_lengths = []` is given; the learner fills `for each ____ in ____:` and `list_of_lengths.append(____)`.
  3. *More blanks* (focuses on **updating the final result**): `join_all(...) => "redgreenblue"`. The learner fills the initial value `joined_words = ____`, the loop header, and the update line.
  4. *All blank:* `make_acronym(["red","green","blue"]) => "RGB"`. The learner writes the whole body.
- **Why faded examples work:** at each step learners have **one new problem**, which is less intimidating than a blank screen or page (§9.11). Comparing the approaches also encourages learners to notice similarities and differences, which builds the linkages that help retrieval.
- **Designing them:** "The key to constructing a good faded example is to think about the problem-solving strategy it is meant to teach." In the book's series, the strategy is the **accumulator pattern**.
- **"Efficiency vs. Extent" box.** Seeing worked examples speeds learning more than writing lots of code [Skud2014]. Deconstructing code by tracing or debugging also makes learning more efficient [Grif2016] (more in Ch 7). The box then adds: "However, this isn't the same as saying that people learn more unless they see additional problems." The sentence is garbled. Read in context, it seems to mean that worked examples make learning *faster*, which isn't the same as making learners learn *more* (extent).
- **Criticism and response.** Critics say cognitive load theory can justify anything after the fact by labelling whatever hurt performance "extraneous" and whatever didn't "intrinsic" or "germane." Wilson's answer: instruction based on it "is undeniably effective". [Maso2016] redesigned a database course to remove split-attention and redundancy effects and to add worked examples and subgoals. It cut the exam failure rate by **34%** on an identical final exam and raised student satisfaction.
- **Reconciliation.** A decade after [Kirs2006], a growing number of people think cognitive load theory and inquiry-based approaches are compatible "if viewed in the right way." [Kaly2015] calls cognitive load theory micro-management of learning inside a broader context that includes motivation. [Kirs2018] extends it to collaborative learning. As with [Mark2018] (§5.1), researchers' perspectives differ but practical implementations "often wind up being the same."
- **"Cognitive Apprenticeship" box** [Coll1991, Casp2007]. It also uses scaffolding and fading. The master models performance and outcomes, then coaches novices through their first steps, explaining what they're doing and why. The apprentice reflects (thinking aloud, self-critique) and eventually explores problems of their own choosing. **Implications:**
  - Present **several examples** of a new idea so learners can see what to generalize.
  - **Vary the form** of problems so it is clear what is and isn't superficial. Wilson long believed a function's return variable *had* to be called `result` because his instructor always named it that.
  - Present problems in **real-world contexts**.
  - Encourage **self-explanation**, which helps learners organize what they've just been taught (§5.1).
- **Parsons Problems** [Pars2006]. Language-teaching analogy: ask a question and supply the words of the answer in jumbled order. The learner orders them grammatically, freed from deciding *what* to say and *how* to say it at once. Programming version: give the needed lines of code and ask for the right order. Learners concentrate on **control flow and data dependencies** (what has to happen before what) without being distracted by naming variables or remembering function names. "Multiple studies" show Parsons Problems take less time and produce equivalent outcomes [Eric2017].
- **Labelled subgoals.** Subgoal labelling gives names to the steps of a step-by-step procedure. Students with labelled subgoals solved Parsons Problems better [Marg2016, Morr2016], and the benefit appears in other domains too [Marg2012]. The subgoals for the total-length and acronym problems are:
  1. "Create an empty value of the type to be returned."
  2. "Get the value to be added to the result from the loop variable."
  3. "Update the result with that value."
  - *Why it works:* grouping related steps into a chunk (§3.3) and naming each chunk helps learners separate generic information from problem-specific information, which reduces load. It also builds a mental model of that *kind* of problem, so learners can solve others of the kind. And it gives a natural opportunity for self-explanation (§5.1).

### 4.1 Split Attention
- **Mechanism** (Mayer and colleagues, [Maye2003]). Linguistic and visual input are processed, and their memories stored, by different parts of the brain. Correlating the two streams takes effort: reading text while hearing it spoken makes the brain check that both channels carry the same information (see dual coding, §5.1).
- **Principle:** learning improves when information arrives on two channels at once **only if the channels are complementary, not redundant**. People generally learn less from a video with both narration and the same text as captions than from one with either alone, because attention goes to checking that they agree.
- **Exceptions:** people who don't yet speak the language well, and people with hearing impairments or other special needs, may find the extra effort a net benefit. (The book prints "hearing exercises", apparently a typo for "hearing impairments".)
- **Consequence for diagrams:** draw a diagram **piece by piece while teaching** instead of showing it all at once. Parts that appear while things are said become correlated in memory, so pointing at a part later is more likely to trigger recall of what was said as it was drawn.
- **Not a ban on multiple sources.** Reconciling multiple streams is a real-world skill [Atki2000]. Instruction shouldn't *require* it while learners are mastering unit skills; using multiple sources at once should be treated as **a separate learning task**.
- **"Not All Graphics Are Created Equal" box.**
  - [Sung2012] compared **seductive** graphics (interesting but irrelevant), **decorative** graphics (neutral and irrelevant) and **instructive** graphics (directly relevant). Any graphic raised satisfaction ratings significantly, but **only instructive graphics improved performance**.
  - [Stam2013, Stam2014]: more information can *lower* performance. Children got pictures, pictures plus numbers, or numbers only for fraction equivalence and fraction addition. For **equivalence**, pictures and pictures-plus-numbers beat numbers only. For **addition**, pictures beat pictures-plus-numbers, which beat numbers only.

### 4.2 Minimal Manuals
- **Origin:** [Carr1987], "the most extreme use of cognitive load theory." Its starting point is a user's remark: "I want to do something, not learn how to do everything."
- **Format:** every idea is a **single-page, self-contained task**:
  - a title saying what the page is about;
  - step-by-step instructions for something really simple (e.g., deleting a blank line in a text editor);
  - several notes on how to **recognize and debug common problems**.
- **Results:** the rewritten materials were shorter overall, and people learned faster. Later studies such as [Lazo1993] confirmed that it outperformed the traditional approach **regardless of prior computer experience**.
- **Carroll's retrospective [Carr2014]:** minimalist designs "sought to leverage user initiative and prior knowledge, instead of controlling it through warnings and ordered steps." Users bring expertise, e.g., knowledge of the task domain, which designers can use as a resource. Minimalism "leveraged episodes of error recognition, diagnosis, and recovery, instead of attempting to merely forestall error," treating troubleshooting and recovery "as learning opportunities instead of as aberrations."
- **Contrast with the old approach:** instruction used to decompose skills hierarchically into sub-skills and drill them. Context was lost, and the goals weren't apparent until all the pieces had been learned. Because people want to dive in and do real tasks, good instruction should help them do that.

### Learning objective not covered in the text
- The chapter's objectives include "Describe ways instructors differ from students and what effect those differences have on instruction," but the chapter body doesn't address it. (The closest material is the expert blind spot in Ch 3 and the cognitive apprenticeship box.)

## Rules
- **COG-1** — Give novices strong guidance (worked examples, scaffolding) rather than unguided inquiry. Reduce guidance only as their prior knowledge grows. *Why:* minimal guidance is less effective and efficient for novices; its disadvantage recedes only with high prior knowledge [Kirs2006]. *Check:* novice-level activities include a demonstrated solution or scaffold before open-ended tasks. (Ch 4 intro)
- **COG-2** — Reduce intrinsic load per step by limiting the amount of new content in each step. *Why:* intrinsic load can only be reduced by teaching less at once. *Check:* each step introduces a small, bounded amount of new material. (Ch 4 intro)
- **COG-3** — Remove extraneous load: anything that distracts from the learning goal, such as mismatched tool setups, colour schemes, irrelevant detail or redundant channels. *Why:* extraneous load takes working memory from germane load. *Check:* list every element of the lesson and justify each as intrinsic or germane; cut or fix the rest. (Ch 4 intro, §4.3 exercise)
- **COG-4** — Protect germane load: build in moments that link new ideas to old ones. *Why:* that linking is what distinguishes learning from memorization. *Check:* each new concept is explicitly related to a previous one. (Ch 4 intro)
- **COG-5** — Teach procedures with worked examples that break the solution into steps, before asking learners to solve problems themselves. *Why:* searching for a strategy is extra load on top of applying it; worked examples speed learning [Skud2014]. *Check:* a full worked example precedes the first independent exercise of each kind. (Ch 4 intro)
- **COG-6** — Follow a worked example with a faded series: same strategy, progressively more blanks, ending with a blank solution. Fade one new aspect at a time. *Why:* learners face one new problem per step, and comparing variants builds retrieval links. *Check:* the series has at least three steps, each blanking more than the previous, all using the same strategy. (Ch 4 intro)
- **COG-7** — Choose what to fade by the problem-solving strategy being taught (e.g., the accumulator pattern), not by surface features. *Why:* "the key to constructing a good faded example is to think about the problem-solving strategy it is meant to teach." *Check:* the series names its target strategy, and each blank exercises a part of it. (Ch 4 intro)
- **COG-8** — Show several examples of each new idea and vary their surface form (names, contexts) so learners can tell what is essential. *Why:* cognitive apprenticeship; otherwise learners generalize from incidental features (the `result` anecdote). *Check:* at least two examples per idea, differing in incidental details. (Ch 4 box)
- **COG-9** — Model expert thinking aloud: explain what you do, why, how you know it's right, and which alternatives you rejected. Then have learners reflect and self-explain. *Why:* cognitive apprenticeship [Coll1991, Casp2007]. *Check:* demos include "why" and rejected alternatives, not just "what". (Ch 4 box, §4.3 exercise)
- **COG-10** — Present problems in real-world contexts. *Why:* this is a cognitive-apprenticeship implication. *Check:* exercises use authentic scenarios, not abstract placeholders. (Ch 4 box)
- **COG-11** — Use Parsons Problems to practise control flow and data dependencies separately from syntax and naming. *Why:* they take less time with equivalent outcomes [Eric2017]. *Check:* lines are complete and correct but shuffled; in Python, indentation is removed; in curly-brace languages, braces are removed. (Ch 4 intro, §4.3)
- **COG-12** — Label the subgoals of each taught procedure, and reuse the same labels across problems of the same kind. *Why:* labelled subgoals improve Parsons-problem performance [Marg2016, Morr2016] and transfer in other domains [Marg2012]. Naming chunks reduces load and supports self-explanation. *Check:* worked examples carry named step labels, e.g., "create empty result / get value from loop variable / update result". (Ch 4 intro)
- **COG-13** — Don't present the same words simultaneously as narration and on-screen text. Use complementary channels (e.g., a picture plus narration). *Why:* redundant channels force cross-checking (split attention [Maye2003]). *Check:* the video or slides don't duplicate the spoken script as text, except where the audience needs captions (non-native speakers, hearing impairments, special needs). (§4.1)
- **COG-14** — Build diagrams incrementally in step with the explanation. *Why:* synchronous drawing and speech correlate in memory, and pointing later triggers recall. *Check:* the diagram reveal is progressive and tied to narration. (§4.1)
- **COG-15** — Don't make novices integrate multiple information sources while they are learning unit skills. Teach integration as its own later task. *Why:* it is a real-world skill [Atki2000], but it adds load during skill acquisition. *Check:* early exercises use a single source; multi-source exercises come later and are explicitly framed as such. (§4.1)
- **COG-16** — Use only instructive graphics. Remove decorative and seductive images. *Why:* all graphics raise satisfaction, but only instructive ones improve performance [Sung2012]. *Check:* every image directly supports the learning goal. (§4.1)
- **COG-17** — Don't assume more representations help. Choose the representation that fits the task. *Why:* for fraction addition, pictures alone beat pictures plus numbers [Stam2013, Stam2014]. *Check:* each added representation is justified for the specific task. (§4.1)
- **COG-18** — Apply Mayer's six diagram principles: signalling, spatial contiguity, temporal contiguity, segmenting (with learner-controlled pace), pretraining, and modality. *Why:* [Maye2009], summarized in [Mill2016a]. *Check:* rate each graphic poor, average or good on each principle (§4.3 exercise). (§4.3)
- **COG-19** — For how-to material, write minimal-manual pages: one self-contained task per page with a descriptive title, simple steps, and notes on recognizing and recovering from common errors. *Why:* shorter materials and faster learning regardless of prior experience [Carr1987, Lazo1993]. *Check:* each page stands alone, covers one real task, and includes at least three or four symptom → cause → fix notes (§4.3 exercise). (§4.2)
- **COG-20** — Let learners start on real tasks early and use their prior knowledge. Treat errors as learning opportunities, not things to prevent at all costs. *Why:* drilling decomposed sub-skills loses context and hides goals [Carr2014]. *Check:* the first activity produces something meaningful, and error recovery is explicitly taught. (§4.2)
- **COG-21** — Treat cognitive load theory and inquiry as compatible at different grain sizes: manage load in the moment within a broader design that attends to motivation and collaboration. *Why:* [Kaly2015, Kirs2018]; perspectives differ, but practice often converges. *Check:* the lesson pairs guided skill-building with motivating, learner-directed goals. (Ch 4 intro)

## Procedures

### P1: Build a faded-example series
1. Name the problem-solving strategy to teach (e.g., accumulator pattern; counting items by category).
2. Define the audience (absolute beginners vs people who program but are new to this language). This changes what can be left unfaded.
3. Write a complete worked example of at most about 10 lines that uses the strategy. Annotate it with subgoal labels (P3).
4. Write a second problem of the same type on a different surface (different data or output) with **a couple of blanks** targeting one part of the strategy (e.g., the loop header and the append, for control structure).
5. Write a third with more blanks targeting another part (e.g., initializing and updating the result).
6. Write a final problem that is entirely blank apart from its signature and expected output.
7. Test it: give it to someone without saying the intended level, and after they fill it in ask them what level they think it's for. If their answer doesn't match, adjust.
8. For non-programmers, the same approach works in other domains (sport, music, law).

### P2: Build a Parsons Problem
1. Write five or six lines of correct code that do something useful.
2. Strip indentation (Python) or curly braces (Java and similar), so that structure must be inferred.
3. Shuffle the lines.
4. Optionally add subgoal labels to scaffold the ordering (COG-12).
5. For non-programmers, use another procedural domain (e.g., the steps for making guacamole).
6. Use it as a quick formative check: there is a single correct order, so the result is clear (see `02-mental-models.md`).

### P3: Label subgoals
1. Write out the procedure for one solved example step by step.
2. Group consecutive steps that achieve one purpose into a chunk.
3. Give each chunk a short, generic, imperative name, independent of the specific problem (e.g., "Create an empty value of the type to be returned").
4. Apply the same labels to other problems of the same kind so learners see the shared structure.
5. Prompt learners to explain each labelled step (self-explanation).

### P4: Audit a lesson's cognitive load
1. List every idea, instruction and explanation in the lesson in point form, to the level of detail in the "Noticing Your Blind Spot" exercise (`03-expertise-and-memory.md`).
2. Tag each item **intrinsic** (needed for the new content), **germane** (links new to old) or **extraneous** (distracts).
3. Remove or fix the extraneous items (tool and colour mismatches, decorative images, redundant captions, irrelevant tangents).
4. If intrinsic load is still too high, cut content or split the lesson.
5. Check that germane moments exist: comparisons, "how is this like X?", self-explanation prompts.

### P5: Write a minimal-manual page
1. Choose a single small task learners will meet (e.g., centring text horizontally; printing a number with N decimal places).
2. Title it with what the page achieves.
3. Give brief step-by-step instructions for the simple case.
4. List at least three or four incorrect behaviours or outcomes the learner might see. For each, give a one- or two-line explanation of why it happens and how to fix it (symptom → cause → fix).
5. Make sure the page stands alone, with no "see previous page" dependencies.

### P6: Review a graphic, slide or video for load
1. Is each graphic instructive, or decorative or seductive? Remove the latter (COG-16).
2. Is narration duplicated by on-screen text? Remove the duplication unless the audience needs captions (COG-13).
3. Rate it on Mayer's six principles (COG-18): signalling, spatial contiguity, temporal contiguity, segmenting, pretraining, modality.
4. Are diagrams built progressively in step with the talk (COG-14)?

## Diagnostics
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

## Templates and checklists

**Faded-example scaffold (structure of the book's example):**
```
Strategy: <name, e.g., accumulator pattern>
Audience: <level>
Subgoals: 1) <...> 2) <...> 3) <...>

Step 1 (worked, complete):   <full solution, ≤10 lines, subgoal-labelled>
Step 2 (few blanks):         <same strategy, new surface; blanks on subgoal X>
Step 3 (more blanks):        <same strategy, new surface; blanks on subgoals X+Y>
Step 4 (blank body):         <signature + example input/output only>
Reality check: partner guesses intended level -> matches?
```

**Book's subgoal labels for accumulator problems (verbatim, Ch 4):**
```
- Create an empty value of the type to be returned.
- Get the value to be added to the result from the loop variable.
- Update the result with that value.
```

**Parsons Problem checklist:**
- [ ] 5–6 lines of correct, useful code.
- [ ] Indentation removed (Python) or braces removed (curly-brace languages).
- [ ] Lines shuffled.
- [ ] One unambiguous correct order (for formative use).
- [ ] A non-programming domain is available for non-programmers.

**Mayer's six principles for teaching graphics ([Maye2009] via [Mill2016a]; rate each poor / average / good):**
| Principle | Meaning |
|---|---|
| Signalling | Visually highlight the most important points so they stand out from less critical material. |
| Spatial contiguity | Put captions and text as close to the graphics as practical; label components in place, not in one big block of text. |
| Temporal contiguity | Present narration and graphics as close in time as practical; together beats one after the other. |
| Segmenting | Break long or unfamiliar material into shorter segments and let learners control how fast they advance. |
| Pretraining | If learners don't know the key concepts and terms, teach them in a module completed beforehand. |
| Modality | Pictures plus audio narration beat pictures plus text, unless there are technical words or symbols or the learners are non-native speakers. |

**Minimal-manual page template:**
```
Title: <what this page lets you do>
Steps:
  1. ...
  2. ...
If you see...                 | Because...                 | Do this...
<symptom 1>                   | <cause>                    | <fix>
<symptom 2>                   | <cause>                    | <fix>
<symptom 3>                   | <cause>                    | <fix>
```

**Cognitive-load audit table:**
```
| Item in lesson | Intrinsic / Germane / Extraneous | Keep / Cut / Fix |
```

## Examples
- **Accumulator faded series:** total_length → word_lengths (blanks on control structure) → join_all (blanks on initializing and updating the result) → make_acronym (blank). It teaches one strategy across varied surfaces (Ch 4 intro).
- **Database course redesign** [Maso2016]. Removing split-attention and redundancy effects and adding worked examples and subgoals cut exam failures by 34% on an identical final and raised satisfaction (Ch 4 intro).
- **"result" variable.** Wilson believed for years that return variables had to be called `result` because his instructor always used that name, which shows why surface form must vary (Ch 4 box).
- **Language-learning Parsons:** supplying jumbled words frees the learner from choosing both content and form (Ch 4 intro).
- **Narration plus captions video:** harder to learn from than either alone, except for non-native speakers or learners with hearing or other special needs (§4.1).
- **Fractions** [Stam2013, Stam2014]: the best representation depends on the task, so more isn't always better (§4.1).
- **Minimal manual page:** e.g., "delete a blank line in a text editor", with simple steps and error-recovery notes (§4.2).

## Evidence and caveats
- **[Kirs2006]:** minimal guidance is less effective and efficient for novices. It is **contested**: it "set off a minor academic storm." Later work [Kaly2015, Kirs2018] sees cognitive load theory and inquiry as compatible, and practice often converges (cf. [Mark2018]).
- **The unfalsifiability critique** of cognitive load theory (post-hoc labelling) is acknowledged. Wilson's counter is practical effectiveness, e.g., [Maso2016]'s 34% reduction in exam failures.
- **[Skud2014]:** worked examples beat writing lots of code for learning speed. **[Grif2016]:** deconstructing code (tracing, debugging) increases efficiency. The box cautions that faster isn't the same as more (extent); the sentence is garbled.
- **[Pars2006]:** origin of Parsons Problems. **[Eric2017]:** less time, equivalent outcomes ("multiple studies").
- **[Marg2016, Morr2016]:** subgoal labels improve Parsons performance. **[Marg2012]:** the benefit extends to other domains.
- **[Maye2003]:** split attention, i.e., the redundancy of identical concurrent channels. The exceptions are language learners and people with hearing or other special needs.
- **[Atki2000]:** integrating multiple streams is a real-world skill; teach it separately.
- **[Sung2012]:** graphics raise liking, but only instructive ones raise learning.
- **[Stam2013, Stam2014]:** more information can lower performance (task-dependent).
- **[Carr1987, Lazo1993, Carr2014]:** minimal manuals are shorter, learners learn faster, and this holds regardless of prior experience.
- **[Maye2009] via [Mill2016a]:** six design principles (given in an exercise, not argued in the body).
- **[Coll1991, Casp2007]:** cognitive apprenticeship (a model, not a single finding).

## Practice exercises
- **Create a Faded Example** — write a ≤10-line example of counting items by category, plus a similar example with a couple of blanks; explain what you faded and what would come next; define the audience; have a partner fill it in and guess the intended level. Non-programmers play learners or use another domain. Pairs / 30 min.
- **Classifying Load** — in groups of 3–4, list in point form the ideas, instructions and explanations of a short lesson one of you taught or took, and classify each as intrinsic, germane or extraneous (detail level as in "Noticing Your Blind Spot"). Small groups / 15 min.
- **Create a Parsons Problem** — write five or six useful lines of code, jumble them (no indentation in Python, no braces in Java), and have a partner order them. Non-programmers use a domain such as making guacamole. Pairs / 20 min.
- **Minimal Manuals** — write a one-page guide to a simple task learners will meet (e.g., centring text, formatting decimals), with at least three or four wrong behaviours, each explained as symptom → cause → fix. Individual / 20 min.
- **Cognitive Apprenticeship** — think aloud while solving a 2–3 minute coding problem, explaining what, why, how you know it's right and which alternatives you rejected, while a partner asks questions; then swap roles. Pairs / 15 min.
- **Critiquing Graphics** — pick an online lesson or talk video with slides and rate its graphics poor, average or good on Mayer's six principles. Individual / 30 min.

## Cross-references
- `02-mental-models.md` — Parsons Problems as quick, unambiguous formative assessment; tutorials vs manuals; expertise reversal (why guidance recedes with expertise).
- `03-expertise-and-memory.md` — working memory 7 ± 2 / 4 ± 1 and chunking, the basis of load and subgoal chunks; concept maps reduce the designer's load; drawing maps piece by piece.
- `05-individual-learning.md` — dual coding (complements split attention), self-explanation and elaboration, [Mark2018].
- `07-programming-pck.md` — tracing and debugging to deconstruct code [Grif2016]; patterns.
- `08-teaching-as-performance.md` — live coding as worked examples and thinking aloud.
- `09-in-the-classroom.md` — the blank-page problem (§9.11).
- `12-exercise-types.md` — fill-in-the-blank, Parsons and other exercise formats.

## Source map
| Book section | Covered under |
|---|---|
| Ch 4 intro: [Kirs2006], inquiry-based learning, three loads | Concepts › Ch 4 opening; COG-1–COG-4 |
| Ch 4 intro: worked and faded examples, accumulator pattern | Concepts; COG-5–COG-7; P1; template |
| "Efficiency vs. Extent" box | Concepts; Evidence |
| Criticism, [Maso2016], [Kaly2015], [Kirs2018] | Concepts; COG-21; Evidence |
| "Cognitive Apprenticeship" box | Concepts; COG-8, COG-9, COG-10 |
| Parsons Problems | Concepts; COG-11; P2 |
| Labelled Subgoals | Concepts; COG-12; P3 |
| §4.1 Split Attention; "Not All Graphics Are Created Equal" | Concepts › 4.1; COG-13–COG-17; P6 |
| §4.2 Minimal Manuals | Concepts › 4.2; COG-19, COG-20; P5 |
| §4.3 Exercises (incl. Mayer's six principles) | Practice exercises; COG-18; P4; Mayer table |
