# Learning science for teachers

## Contents
1. Novices, competent practitioners, experts
2. Misconceptions and formative assessment
3. Expertise, concept maps, and blind spots
4. Memory and chunking
5. Cognitive load
6. How learners can learn better
7. Motivation (summary; see inclusion.md for demotivators)
8. Myths to avoid
9. Theories in one line each

---

## 1. Novices, competent practitioners, experts
A simplified three-stage progression:
- **Novices** don't know what they don't know. They have no usable mental model, so they reason by borrowing from other, superficially similar domains. What they say is often "not even wrong". Don't make them feel bad for this — it's the best they can do yet.
- **Competent practitioners** have a mental model good enough for normal tasks under normal conditions.
- **Experts** have richer models covering special cases, so they handle the unusual and diagnose problems.

A **mental model** is a simplified representation of the important parts of a domain — wrong in details but useful. The first job in teaching novices is to help them **build a model to hang facts on**. Piling up facts without a model can even reinforce a wrong model. (Example: a Unix shell lesson that teaches 15 commands in 3 hours is really teaching paths, history, wildcards, pipes, arguments, and redirection — once those make sense, commands are easy.)

**Tutorials vs manuals.** Tutorials help novices build a model; manuals help competent people fill gaps. Each frustrates the other audience (**expertise reversal effect**). Decide early who the material is for.

## 2. Misconceptions and formative assessment
Three kinds of misconception:
- **Factual errors** — easy to correct.
- **Broken models** — fix by reasoning through examples that expose contradictions.
- **Fundamental beliefs** (e.g. "some people are just born programmers") — tied to identity, resistant to evidence.

**Formative assessment** happens during teaching to shape what comes next (a chef tasting while cooking). **Summative assessment** happens at the end to judge the result (guests tasting the dish).

Formative checks must be quick and give a clear answer. Use one every **10–15 minutes** (more often online) so that, if many learners are lost, only a small part needs repeating. The 10–15 minute rhythm isn't because attention collapses after that — it's about limiting the cost of confusion.

**Reading MCQ results:**
- Everyone right → move on (or skip ahead: a pre-question can show a section is unnecessary, which also respects learners' time).
- Most pick the same wrong answer → address that misconception.
- Answers spread evenly → they're guessing; re-explain in a different way.
- Most right, a few wrong → a judgment call between the minority and keeping the majority engaged.

Formative assessments should prepare learners for the summative one: nobody should meet an exam question type they haven't practised.

Designing formative assessments is useful even if unused, because it forces you to see the topic from the learner's point of view.

**Concept inventories** (e.g. the Force Concept Inventory in physics) are validated MCQ sets that pinpoint misconceptions. Expensive to build; few exist for programming.

## 3. Expertise, concept maps, and blind spots
- Model knowledge as a graph: facts are nodes, relationships are edges. Experts' graphs are **far more densely connected**, which explains intuition (direct links from problem to solution), fluid switching between representations, and better diagnosis.
- **Expert blind spot:** experts organize explanations around the subject's deep principles instead of what learners already know, and can't remember not knowing. Research skill doesn't predict teaching skill.
- **The "just" tell:** "you just…" signals the speaker thinks it's trivial — and implies the struggling learner is stupid. Don't say it.
- **Concept maps:** concepts in bubbles, **labelled** arrows for relationships. Uses:
  - figure out what you're really teaching (separates content from order);
  - align co-designers and co-teachers;
  - draw piece by piece while teaching;
  - assess learners (have them draw what they heard) once they know the technique.
- To start a map, write two related terms, connect them, label the link, then ask what else relates in the same way, what parts things have, and what comes before or after.
- Drawing diagrams **externalizes cognition**; rough sketches invite more honest feedback than polished ones.
- Counting the nodes in a lesson's concept map tells you how much learners must hold at once; split big maps into tightly connected chunks, each ending in a formative assessment.

**Deliberate practice** (not repetition) builds expertise: similar-but-different tasks, attention to what works, adjusting from feedback. A typical progression: act on others' feedback → give feedback to others (and get feedback on it) → give feedback to yourself in real time. It needs a clear goal and immediate, informative feedback.

## 4. Memory and chunking
- **Long-term memory** is effectively unlimited but slow; the limit is **recall**, not storage.
- **Working memory** is small: classically 7 ± 2 items, possibly 4 ± 1. New information passes through it and must be rehearsed to be stored. Too much too fast displaces what came before.
- **Chunking** groups items into larger units (a word rather than letters). Experts have more and larger chunks; naming a few patterns gives learners vocabulary.
- Design implication: count the new items in each chunk of a lesson; keep it within working-memory limits.

## 5. Cognitive load
- **Intrinsic load:** what's inherent in the new material. Reduced only by teaching less at a time.
- **Germane load:** effort that links new material to old — desirable.
- **Extraneous load:** everything else that distracts (mismatched colour schemes, irrelevant detail, boilerplate).
- Goal: minimize extraneous, manage intrinsic in steps, leave room for germane.
- Minimally guided "discovery" learning overloads novices; guidance helps until learners have enough prior knowledge. Cognitive load theory and inquiry approaches can be compatible when viewed as micro and macro levels.

**Techniques:**
- **Worked examples**, then **faded examples**: the same strategy with progressively more blanks, until learners write the whole thing. Teach the *strategy* (e.g. the accumulator pattern), not just the answer.
- **Parsons problems:** reorder given lines. Focuses on control flow without vocabulary recall; takes less time with equivalent outcomes.
- **Labelled subgoals:** name the steps of a strategy (e.g. "create empty result / get value from loop variable / update result"). Helps learners separate the general from the specific.
- **Cognitive apprenticeship:** model, then coach, explaining what and why; show several varied examples so learners can tell essential features from incidental ones (e.g. a return variable doesn't have to be called `result`).
- **Split attention:** people process words and images through different channels. Complementary words + images help; the same words shown and spoken at once hurt (captions + narration), except for people who benefit from both (non-native speakers, people with hearing difficulties). Draw diagrams step by step while talking.
- **Graphics:** only *instructive* graphics improve learning; decorative and "seductive" ones raise satisfaction without helping, and extra information can reduce performance.
- **Multimedia design principles:** signalling (highlight what matters), spatial contiguity (captions next to what they describe), temporal contiguity (narration with visuals), segmenting (short learner-paced chunks), pretraining (teach key terms first), modality (pictures + narration beats pictures + text, except with technical symbols or non-native speakers).
- **Minimal manuals:** one self-contained task per page — title, short steps, then common wrong outcomes with cause and fix. Learners want to do something, not learn everything; errors are learning opportunities.

## 6. How learners can learn better
**Metacognition** (thinking about one's thinking) improves learning; it has to be built into lessons and named, not just recommended.

**Transfer:** near transfer (between similar things) is common; far transfer (chess → maths) rarely happens, and mostly only after mastery.

**Six evidence-based study strategies** — teach them by name and use them in class:
1. **Spaced practice** — spread study over days; review after class (not immediately), including some older material.
2. **Retrieval practice** — practise recalling (quizzes, flash cards, solving without notes then with notes, read-cover-retrieve, redrawing concept maps). Practise in a format close to the test.
3. **Interleaving** — mix topics (A-B-C-B-A-C) rather than blocking; feels harder but works.
4. **Elaboration** — explain why an answer is right and others wrong; compare new ideas with known ones; self-explanation.
5. **Concrete examples** — pair every principle with examples and every example with its principles. **ADEPT:** Analogy, Diagram, Example, Plain language, Technical details. Teach by contrast (show what something is *not*).
6. **Dual coding** — words plus complementary images (timelines, call graphs, labelled diagrams).

**Hypercorrection:** confident wrong answers, once corrected, are *more* likely to be fixed for good. Committing to an answer before seeing the solution helps.

**Time and focus:** long hours reduce total output; sleep deprivation severely impairs thinking; multitasking doesn't work (it takes ~10 minutes to regain flow after an interruption); willpower depletes, so build habits. Teach prioritization and interruption-free work blocks.

**Peer assessment** gives more, faster feedback and exercises higher-level thinking; concerns about bias and collusion are mostly unfounded in class settings. **Calibrated peer review:** learners grade examples until their grades match the instructor's, then grade peers. **Contributing student pedagogy:** learners make things (videos, questions, notes) for other learners, which helps the makers learn.

## 7. Motivation (summary)
- Intrinsic motivation (the task is rewarding) beats extrinsic (reward/punishment).
- **Self-determination theory:** competence, autonomy, relatedness. A good exercise lets learners use the tools they've learned, choose their approach, and talk to peers.
- **Achievement creates motivation** more reliably than the reverse. Help people succeed early.
- **Authentic tasks** (things learners believe they'd really do) and **tangible artifacts** (a thumbnail image, a chart) motivate and give concrete debugging starting points. No `foo`/`bar`.
- Prioritize material by **time to master × usefulness once mastered**: teach quick-and-useful things first; defer hard-and-not-yet-useful fundamentals.
- See `inclusion.md` for demotivators, impostor syndrome, and stereotype threat.

## 8. Myths to avoid
- **Learning styles** (visual/auditory/kinesthetic) — not supported by evidence.
- **The learning pyramid** ("we remember 10% of what we read…") — made up.
- **Brain-training games** raise general intelligence — no.
- **"Natural programmers" / the geek gene** — grade distributions are rarely bimodal; believing in innate talent makes teachers neglect everyone else.
- **Attention collapses after 10 minutes** — weak evidence; check in often for other reasons.
- **Course evaluations measure learning** — they don't correlate well.
- **Teaching ability is innate** — it's a practised skill.
- **Deep end is best / use "real" tools from day one** — overloads novices.
- **Growth mindset interventions transform outcomes** — effects are small overall, though possibly helpful for at-risk learners.

## 9. Theories in one line each
- **Cognitivism:** how memory, recall, and pattern recognition work.
- **Behaviourism:** stimulus and response conditioning.
- **Constructivism:** learners actively construct knowledge.
- **Situated learning:** learning is joining a community of practice.
- **Connectivism:** knowledge lives in networks; learning is building and pruning connections.
None prescribes a teaching method on its own; instructional design tests methods with real learners.
