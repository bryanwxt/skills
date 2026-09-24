# DESIGN mode: requirements, specs, architecture, hard problems

Sub-flows: **Requirements dig** · **Approach choice** (tracer vs. prototype vs. spec) · **Architecture sanity** · **Gordian knot** (stuck) · **Readiness** (nagging doubt). Pick the ones the request needs.

## Inputs
- **Required:** the problem or goal statement, or the draft requirements or design.
- **Helpful:** the users and stakeholders, constraints (hard vs. assumed), deadlines, the existing system, and risk areas.

## Requirements dig (Tips 51–54, checklist B11)
1. For each stated requirement, ask:
   - Is it a **need**, a **policy** (move it to metadata, linked from the requirement), a **UI detail**, or **architecture**?
   - Rewrite it as the simplest accurate statement of need.
2. Capture the **why** behind each one. Ask what the user is ultimately trying to achieve.
3. Recommend **working with a user** (Tip 52): shadow them, do their job for a day, watch real workflows. Look for the hidden requirement of using the skills users already have (the interface *is* the system).
4. Write **use cases** where they help: goal, scope, preconditions, success and failure end conditions, primary actor, trigger, main success scenario, extensions, variations, priority, frequency, performance target, and open issues. They're a meeting agenda as much as a document.
5. Build a **glossary** (Tip 54). Flag synonyms and, worse, homonyms.
6. Identify **semantic invariants** (the inviolable laws) as distinct from changeable policies.
7. Wrap **volatile details** (dates, currency, IDs, time zones) in abstractions (Tip 53).
8. Set up **scope tracking**: record who requested each item, who approved it, and its schedule impact. Assign someone to watch for boiled-frog drift (Tip 6).

## Approach choice (Tips 15, 16, 57)
| Situation | Choose |
|---|---|
| Vague requirements, new tech, the whole-system shape is uncertain, and the code should be kept | **Tracer bullet:** thinnest end-to-end path through all layers, production quality, grown incrementally |
| One specific risk (algorithm, performance, UI feel, third-party fit, external data shape) | **Prototype:** throwaway, dummy data, happy path only. Label it disposable *before* building. Paper or whiteboard is fine for UI and workflow. |
| Public API or library, contractual obligation, life- or safety-critical | **Detailed spec** is warranted |
| Specs piling onto specs, and nobody has written code | Stop the **spec spiral** and switch to a tracer or prototype |
| The organization will ship any convincing demo | Use a tracer, not a prototype |

## Architecture sanity
- Run Architectural Questions (A5). Pay particular attention to whether each module can get the data it needs when it needs it.
- Run the reversibility probes (B3):
  - Is each vendor behind an interface?
  - Is deployment decided by configuration?
- Check orthogonality: map each likely requirement change to the modules it would touch. Aim for one.
- **Concurrency and workflow** (Tips 39–41):
  - Draw the real dependencies (an activity diagram with synchronization points).
  - Find work that is needlessly serialized.
  - Consider services behind queues (the hungry-consumer model).
  - Make objects valid at every call time.
- **Decoupling ladder**, least to most decoupled:
  1. direct calls
  2. events or pub-sub
  3. MVC or model-viewer networks
  4. blackboard (anonymous, async facts plus a rules engine)

  Use a blackboard when data arrives in any order from many sources and the rules change often (Tip 43). Otherwise prefer the simpler options.
- **Domain languages** (Tip 17): if users express rules in a recurring structured form, consider a small DSL or data language. Prefer readability over parser simplicity, because systems outlive expectations.
- **Methods and tools** (Tips 58, 59): adopt notations and tools only where they communicate. Diagrams are not the application.

## Gordian knot: stuck on an "impossible" problem (Tip 55, checklist A10)
1. List **every** avenue, including silly ones. Dismiss none yet.
2. For each, explain *why* it can't work, then challenge that explanation: can you prove it?
3. Separate **real constraints** from **preconceived notions**. Rank the constraints, most restrictive first, and fit the others inside.
4. Run the six questions in A10. Re-check constraints that were set at project start.

## Readiness: a nagging doubt (Tip 56)
Recommend a time-boxed **spike on the hardest part**:
- **Boredom** means it was procrastination. Discard the spike and start the real work.
- **A revelation** means a premise was wrong. Discard the spike and restart on the corrected premise.

Either way, the spike is throwaway.

## Output
Use the default template. Replace the Findings table with **Issues (ranked)** for requirements or design critiques, and add as needed:

```
### Rewritten requirements   (need · why · policy→metadata · glossary terms)
### Recommended approach     (tracer / prototype / spec — with the first thin slice defined)
### Open questions           (for users/stakeholders, max 5)
```
