# software-design: hooks per superpowers step

Rules shared with the other lenses (questions, spec outline, plan order, tests, bounded changes, reviews) live in `coordination.md`. This file adds only the design lens.

## brainstorming (architectural)
- **Context:** list the modules the work touches and what each hides. Note leaked knowledge. Unrelated refactoring goes under design debt.
- **Questions** (within the shared budget):
  - Where is this likely to change? Module boundaries go around those decisions.
  - What's the common case? Make it trivial.
  - What should callers never need to know?
- **Approaches = design it twice:**
  - Decompose around knowledge, not around the order things happen (that's temporal decomposition).
  - Approaches must differ in their boundaries and in what each module hides.
  - Compare them on: how simple the interface is for the common case, how much each hides, generality at no extra cost to callers, performance, and weaknesses.
  - If no approach is attractive, generate another from their weaknesses.
- **Module card** in Components (`assets/spec-sections.md`):
  - abstraction in one sentence;
  - what it hides;
  - interface: signatures, each with a one-line comment;
  - errors: defined away / masked / exposed;
  - defaults.

  If a module is hard to name or describe, fix the decomposition.
- **Self-review red flags:**
  - shallow module;
  - information leakage;
  - temporal decomposition;
  - overexposure;
  - pass-through method or variable;
  - special-general mixture;
  - conjoined modules;
  - too many exceptions;
  - configuration sprawl;
  - a name or description that is hard to write.

## brainstorming (bounded / spike)
- **Bounded:** use the SKILL.md quick rule. If the clean fix would restructure components, say so, so brainstorming can step up.
- **Spike:** don't apply the lens to throwaway code. Mention any design implication in the recommendation.

## writing-plans
- Build in increments of abstractions, not features.
- A new module's first task defines its interface and interface comments.
- Refactors go in their own green tasks.
- Name what each task's module hides.
- A task that edits many modules for one change points to leakage; send it back to the spec.

## test-driven-development
- Test through the public interface and its documented behaviour, not helpers.
- Heavy setup or many mocks is a design signal: note it for review.

## execution (subagent-driven / executing-plans)
- Put the relevant module card in the task brief.
- An implementer who finds an interface problem raises it, never silently redesigns. Local fixes inside the module are fine.

## requesting- / receiving-code-review
- **Requesting:** only when module boundaries or interfaces change, append `review-lens.md` and the touched module cards to `PLAN_OR_REQUIREMENTS`.
  - Important: red flags that spread change amplification in shared modules.
  - Minor: local issues.
- **Receiving:**
  - Push back on "split it smaller" when that makes pieces shallow, pass-through, or conjoined.
  - Push back on "add an option" when the module could decide itself.
  - Accept feedback that reveals leakage or special cases.

## systematic-debugging
- Don't redesign mid-fix.
- After the fix, record any design root cause (duplicated knowledge, a special case in a general mechanism, an error that should have been defined away) as a follow-up.

## finishing-a-development-branch
- Optionally list the design debt the branch revealed: location, red flag, fix.
