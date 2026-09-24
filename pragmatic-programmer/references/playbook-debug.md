# DEBUG mode

**Goal:** find the root cause (not the symptom), prove it, fix it with a regression test, and harden the system so the bug class is caught earlier next time.

## Inputs
- **Required:** the symptom (what happened vs. what was expected), and the code or the area it's in.
- **Strongly wanted:** the exact error or log, repro steps, the environment, and what changed recently.
- If there's no repro and no logs, ask for them, at most 2 questions. Otherwise go to "Can't reproduce" below.

## Mindset (state briefly if the user is frustrated)
- **Fix the problem, not the blame** (Tip 24).
- **Don't panic** (Tip 25). "That's impossible" is false by definition, since it happened. Some assumption is wrong.
- Beware **myopia**: the visible symptom may sit several steps away from the cause.

## Procedure
1. **Clean baseline.** Turn compiler, linter, and type-checker warnings to maximum, and fix what they report first.
2. **Gather accurate data.**
   - Use exact messages, versions, inputs, and timing.
   - Second-hand reports lose detail. Ask for the reporter's exact actions, or watch them do it.
   - Don't debug coincidences: separate what was observed from what was inferred.
3. **Reproduce with one command.**
   - Shrink the repro to a script, test, or `curl` call.
   - If it can't be reproduced, a fix can't be verified.
   - Isolating the conditions often reveals the cause on its own.
4. **Suspect recent change first.** If "only one thing changed", that thing is responsible, however indirectly. Include dependency, OS, runtime, config, and data changes. ⟳ modern: lockfile diffs, container image digests, feature-flag history.
5. **Suspect your own code before platform code** (Tip 26, "select isn't broken").
   - Assume you're calling the library wrong, and re-read its docs.
   - Only after you have a minimal repro against the bare library should you treat it as upstream's bug.
   - When you see hoof prints, think horses, not zebras.
6. **Choose instruments:**
   - **Visualize data:** print `name=value`, inspect structures, plot series. For garbage values, inspect the neighboring memory or bytes as text.
   - **Trace over time:** use a consistent, parseable log format (e.g. log every open and close, then script the log to find unbalanced pairs). Tracing is essential for concurrency and event-driven bugs, because a debugger shows only *now*.
   - **Rubber duck:** walk through the code line by line out loud, or have the user do it. State every assumption you normally skip.
   - **Binary chop:** halve the search space.
     - Over commits, use `git bisect`.
     - Over inputs, bisect the data.
     - Over code, disable halves of it or add midpoint checks.
   - **Element of surprise:** when behavior surprises you, the code you "know" works is the prime suspect. **Prove it** in this context, with this data, at these boundaries (Tip 27).
7. **Root cause statement:** "X happens because Y, which is true when Z." Check it against the Debugging Checklist (A6). Is this the bug, or a symptom? Do the same conditions exist elsewhere?
8. **Fix:**
   - Write a test that reproduces the bug and **fails first**, then apply the minimal fix and watch the test pass (Tips 63, 66).
   - Reinject the bug briefly, or reason explicitly about it, to show the test would catch it (Tip 64).
9. **Harden** using the post-fix checklist (B8):
   - Add an earlier check or assertion near where the bad data originates (Tips 32, 33).
   - Fix sibling occurrences.
   - Add observability so you'll know if it recurs.
   - If it was a wrong assumption, write it down for the team.

## Can't reproduce / intermittent
- Add targeted tracing around the suspected area, in a consistent format, and capture environment details on failure.
- Consider concurrency (ordering, shared state, temporal coupling), resource exhaustion (handles, memory, disk, pool limits), time (time zones, DST, leap seconds, clocks), and data-dependent paths (boundaries, encodings, empty or huge inputs).
- Propose the *experiment* that would discriminate between hypotheses, not a speculative fix. If you must ship a mitigation, label it a **board-up** and keep the investigation open.

## Output
Override the findings table with this block:

```
**Mode:** DEBUG · **Symptom:** … · **Repro:** <one command or "not yet">
### Hypotheses (ranked)
| # | Hypothesis | Evidence for | Evidence against | Discriminating check |
### Root cause   (once proven; otherwise "Not yet proven — run check #N")
### Fix          (patch + failing-first test)
### Hardening    (post-fix checklist items that apply)
### Next actions
```
Never present a hypothesis as the root cause until it has been proven. Mark it `VERIFY:`.
