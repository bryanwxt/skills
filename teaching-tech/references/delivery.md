# Delivery: performance, live coding, and the classroom

## Contents
1. Teaching is a learnable performance
2. Feedback on teaching
3. Practising: the video exercise
4. Live coding
5. Peer instruction
6. Co-teaching and helpers
7. Classroom practices
8. Setup and environments
9. Code of conduct enforcement

---

## 1. Teaching is a learnable performance
Knowing a subject and knowing how to teach aren't enough; you need **pedagogical content knowledge** — how to teach *this* topic to *these* learners. It improves through practice and observation, as in other performing arts.
- **Lesson study** (Japanese jugyokenkyu): teachers observe each other, discuss lessons afterward, and plan curriculum together. Most English-speaking teachers work alone and reinvent everything.
- New practices spread socially, rarely from papers; positive learner feedback is what keeps teachers using them.
- **Lateral knowledge transfer:** learners pick up extras (editor shortcuts, habits) while watching you work. Co-teaching and observation spread these between teachers too.
- Tools: mentor observation, recorded practice, co-teaching.

## 2. Feedback on teaching
**Getting useful feedback:**
- Ask for it yourself, with specific questions ("What's one thing I could do to make this more effective?" "What would you want to go over again?"), rather than "any thoughts?".
- Change one thing at a time.
- Use a **feedback translator** — someone who reads all the comments and summarizes them.
- Write your own assessment first to calibrate; most people are harder on themselves than others are.

**Giving feedback:**
- Balance positive and negative.
- Use a rubric so everyone knows the rules. Simplest: a **2×2 grid** — went well / could improve × content / presentation. Observers write sticky notes into quadrants.
- Longer rubric: `assets/presentation-rubric.md`, ordered as the talk unfolds. Keep a **question budget**: add an item only by removing one.
- Critique both the work and other people's critiques (studio/master-class style).
- Feedback from learners should be continuous and include questions and reflections, not just ratings.

## 3. Practising: the video exercise
- Groups of three rotate: teacher, audience, videographer (phone).
- Each teaches for **2 minutes** on one idea as if to high-school students.
- **Record all three before reviewing any.** Watch together; everyone gives feedback on everyone, including themselves. Delete the videos.
- Pool points into a shared 2×2 grid.
- Tips: announce at the start of the session, not days ahead (less fretting); separate groups physically to avoid audio bleed; self-feedback is required.
- **Nervous tells** (speeding up, fidgeting, pacing) are less noticeable than you think. Don't try to eliminate them — **displace** them into something less visible.

## 4. Live coding
"Teaching is theatre, not cinema." Writing code in front of learners beats slides because:
- watching a program being built is more engaging than reading fragments;
- you can follow "what if?" questions;
- it enables lateral knowledge transfer;
- it slows you to roughly twice learners' speed instead of ten times;
- you notice how much you're asking learners to hold in memory;
- learners **see mistakes diagnosed and fixed** — where they'll spend much of their own time — and get permission to make mistakes.

**Practices:**
- **Embrace mistakes** ("the typos are the pedagogy"). Talk through diagnosing them. Faked mistakes feel forced; instead try **twitch coding** (learners tell you what to type next).
- **Ask for predictions** before running; optionally take a vote.
- **Go slowly:** say every command and click aloud, then point to the command and its output again. **Never copy-paste code.** Mention tab completion the first few times. If output scrolls the command off screen, scroll back or re-run.
- **Be seen and heard:** stand if possible, move around, use a microphone if available.
- **Mirror the learners' environment:** default prompt, colours, and shortcuts; a clean teaching account.
- **Use the screen well:** large font (roughly 60–70 columns × 20–30 rows), maximized window, check readability with a thumbs up; dark text on a lightly tinted background; don't fully darken the room; raise the window if the screen bottom is below head height; announce when you enter or leave an in-terminal editor.
- **Accessibility aids help everyone:** cursor highlighters and keystroke displays.
- **Two devices:** projector laptop plus a tablet or printout for notes and shared notes.
- **Diagrams:** prepared ones plus step-by-step whiteboard sketches.
- **No distractions:** notifications off; a separate account without email.
- **Stick to the plan the first time** you teach something; improvise later. Rehearse on the machine you'll teach with.
- **Face the audience;** look at the screen only briefly.
- **Downsides and fixes:** slow typing → practise; constant note-checking → smaller steps; boilerplate typing → provide skeleton code.
- Fully scripted **Direct Instruction** works well but costs a lot to prepare; most volunteer teachers do better with a plan plus improvisation.

## 5. Peer instruction
Scales some of the benefit of one-to-one tutoring (which can improve outcomes by about two standard deviations):
1. Brief introduction to the topic.
2. An MCQ probing a **misconception**, not a fact.
3. Everyone votes (publicly).
4. All right → move on. All the same wrong answer → address it. Split → learners discuss in groups of 2–4 for a few minutes, then vote again.
5. Reveal the answer and discuss.
Gains are real, not follow-the-leader: learners do better on follow-up questions answered alone, even where no one in the group initially knew.

## 6. Co-teaching and helpers
**Models:** team teaching (alternating leads); teach and assist (one teaches, one circulates); alternative teaching (one takes a small group aside); teach and observe (one collects data); parallel teaching (class split, same material); station teaching (groups rotate).

**Rules:**
- Spend 2–3 minutes before class agreeing who teaches what; ideally sketch a concept map together.
- Agree **hand signals**: slow down, speak up, someone needs help, break time.
- Switch no more than every **10–15 minutes**.
- The non-teaching partner **doesn't interrupt** — no corrections or anecdotes; at most, an occasional leading question.
- Check what your partner will cover next so you don't pre-empt it.
- The non-teaching partner stays engaged: monitor notes, watch for strugglers, jot feedback. No email.
- Debrief afterwards.

**Helpers** (trainee teachers, alumni, advanced learners, IT staff) handle setup problems, answer questions during exercises, watch for stuck learners, and monitor the shared notes. Using advanced learners as helpers also keeps them engaged.

## 7. Classroom practices
- **Assess prior knowledge** with a short questionnaire about concrete tasks, not self-ratings (Dunning–Kruger makes those unreliable). Be gentle — assessment can scare off exactly the novices you want. Follow up with non-responders. See `assets/pre-assessment-questionnaire.md`.
- **Mixed abilities:** advertise the level and sample exercises in advance; extra self-paced exercises; ask advanced learners to help neighbours; watch for learners falling behind and intervene early; accept you can't serve everyone every minute. **False beginners** (studied before) look like beginners on pre-tests but move much faster — a form of preparatory privilege.
- **Pair programming:** driver types, navigator reviews; **switch 3–4 times an hour**; pair everyone (not just strugglers); demonstrate good pairing; flat, dinner-style seating. Benefits are largest for under-represented groups. Rotating partners has pros and cons (new ideas vs disruption and strain on introverts).
- **Collaborative notes** (shared doc): learners fill gaps together, advanced learners stay busy, you see what was missed; also a place for code snippets and data. Paste a list of names for turn-based contributions to avoid collisions.
- **Sticky notes:**
  - *Status flags:* two colours — "done / check my work" and "I need help". Discreet, readable at a glance, usable for votes.
  - *Attention tracking:* names on notes; remove when you've called on or helped someone; reset when all are down. Spreads attention fairly.
  - *Minute cards:* before each break, one positive and one "too fast/too slow/confusing/still unanswered". Cluster them during the break.
- **Never a blank page:** have learners extend the live-coded example or start from starter code in the notes.
- **Start with introductions** (teacher shows competence, approachability, enthusiasm; learners introduce themselves or add names to the notes).
- **Have water or tea** — useful as a pause when asked a hard question. **Cough drops** for long days.
- **Don't touch the learner's keyboard** — talk them through it.
- **Repeat questions** before answering (checks understanding, lets everyone hear, gets it on any recording).
- **One up, one down** at day's end: alternate a positive and a negative, no repeats.
- **Predictions** before demos improve learning.
- **Think-pair-share:** think alone, discuss in pairs, a few pairs share with the room.
- **No homework** during all-day workshops.
- **Seating:** flat, dinner-style tables, good power access, clear sightlines.
- **Humour:** sparingly; never at anyone's expense but your own.
- **Chronotypes:** schedules that suit learners' body clocks (and childcare) help.
- **Credibility** comes from competence, trustworthiness (fair and consistent treatment), and enthusiasm.
- **Limit innovation:** one new technique at a time.

## 8. Setup and environments
- Adults want to leave with their own machine set up for real work — support Windows, macOS, and Linux.
- Send per-OS setup instructions and a reminder email a couple of days before.
- At the start, everyone runs a simple check command and shows the result; helpers fix failures.
- Avoid OS-specific features, or point them out.
- Virtual machines and containers are slow on old laptops and confuse learners about what's running where.
- Browser-based tools avoid installs but depend on the venue's WiFi and leave nothing working locally.
- Try "may I drive?": swap computers with someone on a different OS to feel what novices go through.

## 9. Code of conduct enforcement
- Depending on severity and intent: warn, require an apology, or expel.
- Act in front of witnesses.
- If you expel someone, tell the class why (prevents rumours, shows you're serious).
- Contact the host promptly.
- A code without reporting and enforcement procedures is meaningless. See `assets/code-of-conduct.md`.
