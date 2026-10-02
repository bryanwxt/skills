# Expertise and Memory

> Source: Greg Wilson, *Teaching Tech Together* (2018), Ch. 3 "Expertise and Memory" (§3.1–§3.5). Licensed CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/); condensed and restructured for skill use, with quotations marked. Rule IDs use prefix `MEM`.

## When a skill needs this
- A lesson-design assistant drafts or critiques a **concept map** for a topic and uses it to count how many new items a lesson asks learners to hold, then splits the lesson into chunks.
- A teaching-feedback reviewer flags **expert blind spot**: skipped steps, "just", and explanations ordered by the subject's deep principles instead of by what learners already know.
- An exercise generator designs practice as **deliberate practice** (clear goal plus immediate feedback, progressing from receiving feedback to giving it to self-critique), not as plain repetition.
- A workshop planner runs concept mapping as a group activity (sticky notes, or a simultaneous "reveal" in a team meeting).
- A skill explaining to a user why their dense lesson overwhelms people (working memory 7 ± 2, perhaps 4 ± 1).

## Key terms
| Term | Meaning (one line) |
|---|---|
| Expert | Someone who can diagnose and handle unusual situations, knows when the usual rules don't apply, and tends to recognize solutions rather than reason to them (glossary). |
| Graph metaphor of knowledge | Facts are nodes and relationships are arcs; experts' graphs are more densely connected ("definitely not how our brains work, but… useful"). |
| Intuition | The expert's one-step jump from problem to solution along a direct link; often can't be explained afterwards. |
| Fluid representation | The ability to switch quickly between different models of a problem [Petr2016]. |
| Expert blind spot | Experts' tendency to organize explanation by the subject's deep principles instead of by what learners already know [Nath3003]; inability to empathize with novices. |
| Concept map | A picture of a mental model: concepts as nodes, relationships as *labelled* arcs. |
| Externalized cognition | Using graphical, physical or verbal aids to augment thinking and make mental models visible. |
| Long-term (persistent) memory | Essentially unbounded but slow memory. |
| Short-term (working) memory | Fast but small memory: 7 ± 2 items [Mill1956], perhaps 4 ± 1 [Dida2016]. |
| Chunking | Grouping related items so they are stored and processed as one unit. |
| Design pattern | A named, reusable solution to a common problem. |
| Deliberate practice (reflective practice) | Doing similar but subtly different things, noticing what works, and changing in response to feedback. |

## Concepts

### Chapter 3 opening (unnumbered): what expertise is
- Epigraph: "Memory is the residue of thought." — Dan Willingham.
- **Usual definition:** experts solve problems much faster than the "merely competent," recognize and handle cases where the normal rules don't apply, and make it look effortless. Often they "instantly know what the right answer is" [Parn2017].
- **Expertise isn't more facts.** Competent practitioners can memorize lots of trivia with no gain in performance.
- **Graph metaphor:** knowledge is a network of facts (nodes) and relationships (arcs). Wilson flags that this is "definitely not how our brains work, but it's a useful metaphor." Experts' models are much more **densely connected**: they are much more likely to know a connection between any two randomly chosen pieces of information.
- **What the metaphor explains:**
  - **Intuition.** Experts jump straight from problem to solution because a direct link exists: where a competent practitioner reasons A → B → C → D → E, the expert goes A → E. This isn't always good: experts often **can't explain their reasoning**, because they recognized the answer rather than reasoning to it.
  - **Fluid representations** [Petr2016]. Experts switch between views of a problem, e.g., treating a maths problem geometrically, then as a set of equations.
  - **Diagnosis.** More links make it easier to reason backward from symptoms to causes. (This is why debugging in job interviews gives a more accurate picture of ability than programming does.)
  - **Teaching handicap.** Experts are often so familiar with their subject that they can't imagine not seeing it their way, so they may teach it worse than less expert people who still remember learning it.
- **Expert blind spot.** As originally defined in [Nath3003] (the book's key for Nathan & Petrosino 2003), it is "the tendency of experts to organize explanation according to the subject's deep principles, rather than being guided by what their learners already know." It "can be overcome with training." It is part of why there is **no correlation between research skill in an area and skill at teaching it** [Mars2002].
- **"The J Word" box.** Experts betray the blind spot by saying "just" ("you just fire up a new virtual machine and then you just install these four patches…"). It signals that the speaker thinks the problem is trivial, so the person struggling must be stupid (Ch 10). "Don't do this."

### 3.1 Concept Maps
- **Why connections matter:** "helping learners make connections is as important as introducing them to facts." Without connections it is hard to recall what you know. Analogy: the more people you know at a party, the less likely you are to leave early.
- **A concept map** shows a mental model as a graph: facts are bubbles and connections are **labelled** arcs. The labels are essential, because "X and Y are related" helps only if you say *how*. Different people can draw different maps for the same topic, and making those differences explicit is one of the benefits.
- **Figure 3.1, Concept Map for Seasons (from the IHMC CMap site).** *Described, not copied:*
  - "seasons" *are determined by* "amount of sunlight", which *results in* "seasonal temperature variations".
  - "amount of sunlight" *is determined by* "length of day" and "height of sun above horizon". Length of day *is longer in* summer and *is shorter in* winter. Height of sun *is higher in* summer and *is lower in* winter.
  - Both of those *are determined by* "tilt of axis" (which *in summer points toward* the sun) and "position in orbit" (where the *axis points toward or away from* the sun).
  - "position in orbit" comes *with* "slight variation in distance", which *has* "negligible effect".
  - It shows how labelled arcs carry the explanation, including the explicit dismissal of a common misconception (that distance from the sun causes seasons).
  - Figure 11.1 elsewhere in the book uses a concept map to explain making a good screencast.
- **Figure 3.2, Concept Map for a For Loop.** The code is `for letter in "abc": print(letter)`, which outputs a, b, c on separate lines.
  - *Top half:* three unconnected nodes, "loop variable", "collection" and "loop body". These are the key "things", but "only half the story."
  - *Bottom half:* the same nodes with labelled arcs. Loop variable → *takes each value in order from* → collection. Loop variable → *changes each time through* → loop body. Loop body → *runs once for each value of* → collection.
  - Point: the relationships are as important to understanding as the concepts themselves.
- **Four uses of concept maps:**
  1. **Helping teachers figure out what they are trying to teach.** A map separates content from order. People rarely end up teaching things in the order they first drew them. Maps reduce the *teacher's* cognitive load (Ch 4).
  2. **Aiding communication between lesson designers.** Teachers with different ideas of the goal pull learners in different directions. Sharing maps doesn't guarantee alignment, but it helps.
  3. **Aiding communication with learners.** You *can* hand out a pre-drawn map to annotate, but it is better to **draw it piece by piece while teaching**, to tie the map to what was said (§4.1, split attention).
  4. **For assessment.** Having learners draw what they think they just heard shows what was missed or miscommunicated. *But* reviewing learners' maps is too slow for in-class formative assessment. It is very useful in weekly lectures **once learners know the technique**, because any new method slows people down at first, and asking a programming novice to learn to draw their thoughts at the same time "is an unfair load."
- **[Kepp2008]** studied concept mapping in computing education: "…concept mapping is troublesome for many students because it tests personal understanding rather than knowledge that was merely learned by rote." Wilson counts this as a benefit.
- **Skepticism:** some teachers doubt that novices can map their own understanding, because introspection and explaining understanding are more advanced skills than understanding itself. Wilson's answer: like any tool, concept mapping must be taught and practised to be effective.
- **"Start Anywhere" box (procedure for blank-page paralysis):** write down two words associated with the topic, draw a line between them, and label how they are related. Then ask what else is related in the same way, what parts those things have, and what happens before or after the existing concepts, to find more nodes and arcs. "After that, the hard part is often stopping." (The book prints "right down", a typo for "write down".)
- **Alternatives** [Eppl2006]:
  - mind maps (usually radial and hierarchical);
  - conceptual diagrams (predefined categories and relationships);
  - visual metaphors (striking images overlaid with text);
  - maps, flowcharts and blueprints;
  - decision trees such as [Abel2009], a chart-chooser decision tree.
- **Externalized cognition.** Each of these representations makes thought processes and mental models visible so they can be compared, contrasted and combined. [Cher2007] suggests this may be the main reason developers draw diagrams in discussions. Most developers couldn't identify the parts of their own diagrams shortly after drawing them. The diagrams aren't archives but "a cache for short-term memory": a participant can point at a "wiggly bubble" and say "that" to recall minutes of debate.
- **"Rough Work and Honesty" box.** Many UI designers show rough sketches rather than polished mock-ups because people give more honest feedback on something that looks quick to make. If it looks like hours of work, "most will pull their punches." So when drawing concept maps to start discussion, use pencils and scrap paper, or pens and a whiteboard, not fancy drawing tools.

### 3.2 Seven Plus or Minus Two
- **Two-layer memory model,** which Wilson says has a "sounder physiological basis" than the graph metaphor:
  - **Long-term (persistent) memory** holds friends' names, your address, the scary clown at your eighth birthday. It is essentially unbounded ("we will die before it fills up"), but too slow to help with "hungry lions and disgruntled family members."
  - **Short-term (working) memory** is much faster and much smaller. [Mill1956] estimated **7 ± 2 items** for the average adult. That is why phone numbers are 7–8 digits: on dial phones it was the longest string most adults could hold while the dial turned. Working memory may really be as small as **4 ± 1** (§3.3); our tendency to group things makes it seem larger.
- **"Participation" box (hedged).** Working-memory size is sometimes used to explain why sports teams have about half a dozen members or split into sub-groups (forwards and backs in rugby), and why meetings stop being productive beyond a certain size: with twenty people, "either three meetings are going on at once or half a dozen people are talking while everyone else listens." The argument is that keeping track of peers is limited by working memory, "but so far as I know, the link has never been proven."
- **"7 ± 2 is probably the most important number in programming."** To write or understand the next line of code, you must hold a set of arbitrary facts (what each variable represents, its current value…). If there are too many, your mental model of the program "comes crashing down."
- **It is "also the most important number in teaching."** A teacher can't push information straight into long-term memory. What they present goes first into short-term memory and transfers to long-term memory only after being held there and rehearsed (§5.1). If the teacher presents too much too fast, the new displaces the old before it can consolidate.
- **Using concept maps to manage the load.** One reason to draw a concept map when designing a lesson is that it shows how many separate pieces of information learners must hold as the lesson unfolds. Wilson's own practice: he often draws a map, realizes it is far too much for one pass, and **carves out tightly connected subsections**, each a digestible piece that **leads to a formative assessment**.
- **"Building Concept Maps Together" box:**
  - *Classroom version:* small groups of 2–4 get sticky notes with a few key concepts written on them. They place the notes on a whiteboard, connect them with labelled arcs, and add any other concepts they think they need.
  - *Team-meeting version:* everyone draws a concept map of the shared project **separately** on paper for a few minutes, and all reveal on the count of three. The differences between their mental models start "a lot of interesting discussion."
- **The model is itself superseded.** The simple two-store model has largely been replaced by one in which short-term memory consists of several modal stores (e.g., visual vs linguistic), each doing some involuntary preprocessing [Mill2016a]. Wilson presents the simple model on purpose, as an example of a mental model that aids learning and work and is later replaced by something more complicated.
- **Recall, not retention, is the bottleneck.** Research now indicates the limit on long-term memory is the ability to recall what is stored, not storage. Studying in short, spaced periods in varied contexts improves recall, perhaps because it creates more cues than cramming (§5.1).

### 3.3 Pattern Recognition
- Short-term memory may be only **4 ± 1** items [Dida2016]. To handle more, minds create **chunks**: we remember words as single items, not letter sequences, and the five-spot pattern on dice or cards as one whole.
- **Key research finding:** experts have **more and larger chunks** than non-experts. They "see" larger patterns and have more patterns to match against, which lets them reason at a higher level and search for information faster and more accurately.
- **Chunking can mislead:** misidentifying a pattern leads you astray, so "newcomers really can sometimes see things that experts have looked at and missed."
- **Teaching patterns directly.** **Design patterns** (reusable solutions to common problems) help competent practitioners think and talk in many domains, including teaching [Berg2012]. But pattern catalogues are "too dry and too abstract for novices to make sense of on their own." Naming **a small number** of patterns does seem to help, mainly by giving learners a richer vocabulary to think and communicate with [Kuit2004, Byck2005, Saja2006] (roles of variables; more in §7.1).

### 3.4 Becoming an Expert
- **The 10,000 hours claim** is "widely quoted but probably not true." Doing the same thing over and over is more likely to solidify bad habits than to improve performance.
- **What works is deliberate practice** (also called reflective practice): "doing similar but subtly different things, paying attention to what works and what doesn't, and then changing behavior in response to that feedback to get cumulatively better."
- **Common three-stage progression:**
  1. **Act on feedback from others.** E.g., a student writes an essay about their summer holiday and the teacher tells them how to improve it.
  2. **Give feedback to others.** E.g., critiquing character development in *The Catcher in the Rye*. For this to be effective, learners **must get feedback on their feedback**: the teacher critiques their analysis.
  3. **Give feedback to themselves.** They critique their own work in (near) real time with the skills they have built. This is so much faster than waiting for others that "proficiency suddenly starts to take off."
- **"What Counts as Deliberate Practice?" box.**
  - [Macn2014] (meta-analysis): deliberate practice explained "26% of the variance in performance for games, 21% for music, 18% for sports, 4% for education, and less than 1% for professions."
  - [Eric2016] critiqued it: "Summing up every hour of any type of practice during an individual's career implies that the impact of all types of practice activity on performance is equal—an assumption that…is inconsistent with the evidence."
  - Conclusion as Wilson states it: effective deliberate practice requires **both a clear performance goal and immediate informative feedback**.

## Rules
- **MEM-1** — Remove "just" from explanations. *Why:* "just" signals the task is trivial and implies that anyone struggling is stupid; it betrays the expert blind spot (Ch 3 box, Ch 10). *Check:* search the lesson text or transcript for "just" used as a minimizer; it should find zero hits. (Ch 3 intro)
- **MEM-2** — Order explanations by what learners already know, not by the subject's deep principles. *Why:* organizing by deep principles is the definition of expert blind spot [Nath3003]. *Check:* each new idea in the sequence connects to something learners have already met, and nothing depends on concepts introduced later. (Ch 3 intro)
- **MEM-3** — Expect experts to be unable to explain their own intuitive leaps, and make them spell out intermediate steps. *Why:* experts recognize solutions instead of reasoning to them (A→E instead of A→B→C→D→E). *Check:* worked solutions show each intermediate step a competent practitioner would need. (Ch 3 intro)
- **MEM-4** — Before teaching even a short snippet, break it down to the level of every detail a novice must understand (e.g., the brackets, commas, quotes and spaces in one Python list literal). *Why:* experts overlook such details (the "Noticing Your Blind Spot" exercise). *Check:* the lesson notes list the micro-details a single example relies on, and each is either taught or deliberately deferred. (§3.5)
- **MEM-5** — Teach connections, not only facts: make relationships explicit and named. *Why:* without connections people struggle to recall what they know. Expertise is dense connection, not more facts. *Check:* every new concept is linked in the lesson to at least one earlier concept by a stated relationship. (Ch 3 intro, §3.1)
- **MEM-6** — Label every arc in a concept map with the relationship. *Why:* "X and Y are related" is useless unless the relationship is stated. *Check:* no unlabelled edges. (§3.1)
- **MEM-7** — Draw a concept map when designing a lesson, to decide what to teach separately from the order you teach it in. *Why:* it separates content from order and reduces the designer's cognitive load. *Check:* the design includes a map, and the teaching order is decided afterwards. (§3.1)
- **MEM-8** — Use the concept map to count the new items a lesson asks learners to hold. If there are too many, carve the map into tightly connected sub-maps, each ending in a formative assessment. *Why:* working memory holds 7 ± 2 (perhaps 4 ± 1) items. New information displaces old before it consolidates. *Check:* each lesson chunk introduces only a handful of new items and ends with a check. (§3.2, §3.3)
- **MEM-9** — When showing a diagram or concept map in class, build it piece by piece while talking instead of revealing it all at once. *Why:* drawing in sync with speech ties each part to what was said, so pointing at it later triggers recall (§3.1 → §4.1). *Check:* the slides or board plan build the diagram incrementally. (§3.1)
- **MEM-10** — Have designers and co-teachers share concept maps to surface disagreements about what is being taught. *Why:* teachers with different ideas pull learners in different directions. Sharing maps helps, though it doesn't guarantee alignment. *Check:* co-taught lessons have a shared map. (§3.1)
- **MEM-11** — Use learner-drawn concept maps for assessment only after learners have practised the technique, and not as quick in-class formative checks. *Why:* reviewing them is too slow for in-class use, and a new technique adds unfair load for novices. *Check:* a map-based assessment is preceded by map-drawing practice and is scheduled for weekly or reflective use. (§3.1)
- **MEM-12** — Teach concept mapping explicitly before relying on it, and use "start anywhere" prompts for blank-page paralysis. *Why:* introspection is harder than understanding, so the tool must be taught and practised. *Check:* the first mapping activity includes the two-words-and-a-labelled-line starter. (§3.1)
- **MEM-13** — Use rough media (pencil, scrap paper, whiteboard) for maps and sketches meant to start discussion. *Why:* people give more honest feedback on work that looks quick. *Check:* discussion-starting diagrams aren't polished renderings. (§3.1)
- **MEM-14** — Use diagrams to externalize cognition during group discussions, and expect them to work as short-term memory caches, not archives. *Why:* [Cher2007]: developers couldn't identify parts of their own diagrams shortly afterwards. *Check:* don't treat discussion sketches as documentation without annotation. (§3.1)
- **MEM-15** — Introduce a small number of named patterns to learners, not a pattern catalogue. *Why:* names give learners vocabulary [Kuit2004, Byck2005, Saja2006]; catalogues are too dry and abstract for novices. *Check:* novice material names only a few patterns, each with examples. (§3.3)
- **MEM-16** — Design practice as deliberate practice: similar but subtly varied tasks, a clear performance goal, and immediate informative feedback. Never use repetition alone. *Why:* repetition solidifies bad habits [Eric2016]; deliberate practice needs a goal and feedback. *Check:* every practice set states its goal, varies its items, and gives immediate feedback. (§3.4)
- **MEM-17** — Sequence feedback skills: first learners act on others' feedback, then they give feedback (and receive feedback on their feedback), then they self-critique. *Why:* self-feedback is so much faster that proficiency takes off. Peer feedback works only if it is itself critiqued. *Check:* the course includes peer review with teacher review of the reviews before expecting self-assessment. (§3.4)
- **MEM-18** — Don't assume subject expertise (or research excellence) implies teaching ability. Value teachers who still remember learning the material. *Why:* there is no correlation between research skill and teaching skill [Mars2002]; the blind spot can be overcome with training. *Check:* teacher recruitment and training don't use subject expertise as a proxy for teaching skill. (Ch 3 intro)
- **MEM-19** — Spread learning over short, spaced sessions in varied contexts. *Why:* recall, not storage, is the limit, and spacing and variety create more retrieval cues (§3.2 → §5.1). *Check:* the course schedule revisits topics across sessions. (§3.2)

> **Skill note:** Wilson names only "just" (MEM-1). A reviewer skill might reasonably also flag "simply" and "obviously", but that extension is ours, not the book's.

> **Skill note:** Wilson gives memory limits (7 ± 2, perhaps 4 ± 1), not a quota of new items per lesson chunk (MEM-8). Using "at most about 7, ideally about 4 new items per chunk" as a heuristic is our operationalization.

## Procedures

### P1: Draw a concept map for a topic (lesson design)
1. Pick one small topic, something you would teach in about five minutes.
2. If stuck, use "Start Anywhere": write two words associated with the topic, connect them, and label the relationship.
3. Grow the map with these prompts: What else is related in the same way? What parts do these things have? What happens before or after these concepts?
4. Make sure every arc carries a relationship label (MEM-6). Prefer concepts over surface detail.
5. Stop. "The hard part is often stopping."
6. Count the distinct items a learner must hold (MEM-8). If there are too many for one pass, carve out tightly connected sub-maps.
7. Turn each sub-map into a lesson episode that ends with a formative assessment (see `02-mental-models.md`).
8. Decide the teaching order only now, separately from how you drew the map (MEM-7).
9. Optionally have a partner critique it: does it present concepts or surface detail? Which of their relationships would you treat as concepts, and vice versa? (the §3.5 exercise)

### P2: Use a concept map live in class
1. Plan the full map in advance.
2. Draw it piece by piece as you explain each part, so speech and drawing coincide (MEM-9).
3. Later, point back to parts of the map to trigger recall of the related explanation.
4. Optionally (for learners familiar with mapping) ask learners to draw their own map of what they just heard, to reveal gaps (MEM-11).

### P3: Group concept-mapping activities
- **Sticky-note mapping (class):** groups of 2–4, sticky notes pre-written with key concepts, whiteboard. Groups place the notes, connect them with labelled arcs, and add missing concepts. Debrief by comparing groups.
- **Simultaneous reveal (team or co-teachers):** each person spends a few minutes mapping the project or lesson alone on paper. Everyone reveals at once on "three." Discuss the differences. Use rough materials (MEM-13).

### P4: Find your own expert blind spot
1. Take a very short artifact from your lesson (one line of code, one command, one formula).
2. List everything a novice must know to read it, down to punctuation and conventions. Model: Elizabeth Wickes's breakdown of `answers = ['tuatara', 'tuataras', 'bus', "lick"]`:
   - square brackets around content mean a list (unlike brackets to the right of something, which extract data);
   - commas separate elements and sit outside the quotes;
   - quotes mark each element as a string; other data types would need no quotes;
   - single and double quotes are mixed and Python doesn't care as long as each string balances;
   - the space after each comma isn't required but aids readability.
3. Mark which details your lesson teaches, which it assumes, and which it should defer.
4. Scan your script for "just" and similar minimizers (MEM-1).

### P5: Design deliberate practice
1. State a clear performance goal for the skill.
2. Create a series of similar but subtly different tasks, not the same task repeated.
3. Arrange immediate, informative feedback for each attempt.
4. Progress learners from receiving feedback, to giving it (with teacher feedback on their feedback), to self-critique (MEM-17).

## Diagnostics
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

## Templates and checklists

**Concept map quality checklist:**
- [ ] Every arc is labelled with a relationship.
- [ ] Nodes are concepts, not surface details.
- [ ] Covers about 5 minutes of teaching per map (for practice), or is carved into sub-maps.
- [ ] Item count per chunk is within working-memory limits (7 ± 2, perhaps 4 ± 1).
- [ ] Each sub-map leads to a formative assessment.
- [ ] Teaching order decided separately from drawing order.
- [ ] Drawn roughly if the purpose is discussion.

**"Start Anywhere" prompts:**
```
1. Write two words connected to the topic. Draw a line. Label how they relate.
2. What other things are related in the same way?
3. What parts do these things have?
4. What happens before / after the concepts already on the page?
5. Stop when the map serves its purpose.
```

**Blind-spot breakdown frame:**
```
Artifact (one line / one command):
Every symbol, convention, and implicit rule a novice must know:
  - <detail> | taught? assumed? deferred?
Minimizers found in script ("just", ...): <list>  -> remove
```

**Deliberate-practice design check:**
- [ ] Clear performance goal.
- [ ] Tasks varied subtly, not identical repeats.
- [ ] Immediate, informative feedback.
- [ ] Learners progress from receiving feedback to giving it (with feedback on their feedback) to self-feedback.

## Examples
- **For loop map (Figure 3.2).** Three nodes alone are "half the story". Adding the labelled relationships (takes each value in order from; changes each time through; runs once for each value of) carries the understanding (§3.1).
- **Seasons map (Figure 3.1).** Labelled arcs build a full causal explanation and explicitly record that distance from the sun has a "negligible effect" (§3.1).
- **Debugging interviews.** Asking candidates to debug reveals expertise better than asking them to program, because diagnosis relies on dense connections (Ch 3 intro).
- **Dial phones and 7-digit numbers:** a real-world artifact of the 7 ± 2 limit (§3.2).
- **Wilson's own lesson design.** He draws a map, finds it too big, and carves it into tightly connected pieces, each ending in a formative assessment (§3.2).
- **Team meeting reveal.** Separately drawn project maps revealed at once show how differently team members model the same project (§3.2 box).
- **Developers' whiteboard diagrams** [Cher2007]. Within a short time, creators couldn't identify the parts of their own diagrams. Diagrams act as shared short-term memory ("that"), not archives (§3.1).
- **Essay → Catcher in the Rye critique → self-critique:** the three-stage route to expertise (§3.4).
- **Python list literal** (Wickes): five non-obvious details in one line (§3.5).

## Evidence and caveats
- **Graph metaphor:** explicitly "not how our brains work", but useful (Ch 3 intro).
- **[Parn2017]:** experts often instantly know the answer.
- **[Petr2016]:** experts' fluid representations.
- **[Nath3003]:** the original definition of expert blind spot. It can be overcome with training.
- **[Mars2002]:** no correlation between research productivity and teaching effectiveness.
- **[Kepp2008]:** concept mapping is troublesome because it tests personal understanding rather than rote knowledge (Wilson: a benefit).
- **[Eppl2006]:** comparison of concept maps, mind maps, conceptual diagrams and visual metaphors.
- **[Cher2007]:** developers' diagrams as short-term memory caches.
- **[Mill1956]:** working memory holds 7 ± 2 items. **[Dida2016]:** perhaps 4 ± 1, with chunking creating the illusion of more. The two-store model has largely been superseded by modal stores [Mill2016a]; Wilson keeps it as a "useful but eventually superseded" model.
- **The working-memory explanation of team and meeting sizes is unproven** ("the link has never been proven"). Don't present it as fact.
- **Recall, not retention, limits long-term memory;** spaced, varied study helps, possibly via more cues (the mechanism is hedged with "may").
- **Experts have more and larger chunks** ("one key finding in cognition research"; no specific key given).
- **[Kuit2004, Byck2005, Saja2006]:** naming a few patterns (roles of variables) "does seem to help" (hedged).
- **The 10,000-hours rule:** "widely quoted but probably not true". **Record it as debunked or doubtful.**
- **[Macn2014]:** deliberate practice explains 26% (games), 21% (music), 18% (sports), 4% (education) and under 1% (professions) of the variance in performance. **[Eric2016]** disputes the method (it counts all practice hours as equal). The evidence on how much deliberate practice explains is therefore **contested**. What survives is that a clear goal and immediate feedback are required.
- Typos in the book: "right down" (for "write down") in the "Start Anywhere" box; the key [Nath3003] (actually 2003).

## Practice exercises
- **Concept Mapping** — draw a concept map for something you would teach in five minutes, swap with a partner, and critique each other's (concepts or surface detail? which of their relationships would you call concepts, and vice versa?). Pairs / 30 min.
- **Concept Mapping (Again)** — in groups of 3–4, each person independently maps their mental model of what goes on in a classroom, then the group compares common and differing concepts and relationships. Small groups / 20 min.
- **A Concept Map for This Material** — after finishing the book, map one small topic from it and send it to the authors (Appendix C) for possible inclusion, with credit. Individual / 30 min.
- **Noticing Your Blind Spot** — study Wickes's five-point breakdown of one Python list literal, then break down an equally short item from a lesson you recently taught or took to the same level of detail. Small groups (3–4) / 10 min.

## Cross-references
- `02-mental-models.md` — novice/competent/expert; formative assessment that each map chunk should lead to.
- `04-cognitive-load.md` — concept maps reduce the designer's load; split attention explains drawing maps piece by piece (§4.1); subgoal labels build on chunking.
- `05-individual-learning.md` — rehearsal, spacing and retrieval practice (§5.1); concept maps as retrieval checks; peer assessment and calibrated peer review (§5.3).
- `06-lesson-design.md` — using concept maps in a lesson design process.
- `07-programming-pck.md` — patterns and roles of variables (§7.1).
- `08-teaching-as-performance.md` — reflective practice for teachers.
- `10-motivation-and-inclusion.md` — why "just" demotivates (Ch 10).
- `11-teaching-online.md` — Figure 11.1, a concept map for making a good screencast.

## Source map
| Book section | Covered under |
|---|---|
| Ch 3 intro (expertise, graph metaphor, intuition, fluid representations, diagnosis, expert blind spot, "The J Word") | Concepts › Ch 3 opening; MEM-1, MEM-2, MEM-3, MEM-18 |
| §3.1 Concept Maps (Figs 3.1, 3.2; four uses; Kepp2008; "Start Anywhere"; alternatives; externalized cognition; "Rough Work and Honesty") | Concepts › 3.1; MEM-5–MEM-14; P1, P2 |
| §3.2 Seven Plus or Minus Two ("Participation"; "Building Concept Maps Together"; modal stores; recall) | Concepts › 3.2; MEM-8, MEM-19; P3 |
| §3.3 Pattern Recognition | Concepts › 3.3; MEM-15 |
| §3.4 Becoming an Expert ("What Counts as Deliberate Practice?") | Concepts › 3.4; MEM-16, MEM-17; P5 |
| §3.5 Exercises | Practice exercises; MEM-4; P4 |
