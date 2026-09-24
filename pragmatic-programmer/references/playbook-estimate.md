# ESTIMATE mode: time, size, performance, algorithmic order

## Inputs
- **Required:** what is being estimated.
- **Critical:** the required *accuracy* (a rough feasibility check vs. a commitment), and the scope.
- If the user needs a number *now*, give an order-of-magnitude range with the assumptions stated, and label it preliminary. The book's advice is to say "I'll get back to you" rather than commit at the coffee machine.

## A. Quantities and durations (Tips 18, 19, checklist B12)
1. **Clarify** the accuracy needed and the scope. List the scope assumptions explicitly, because they are part of the answer.
2. **Ask whether it's been done before.** Prior actuals beat any model.
3. **Model** the process or system in the simplest form that works. Modeling often uncovers a cheaper alternative, so report it if it does.
4. **Decompose** into parameters and how they combine (additive, multiplicative, queueing).
5. **Value** each parameter. Spend your effort on the **multiplicative and dividing** ones, since they dominate the result. Where you can, measure the current or a similar system.
6. **Calculate scenarios**, varying the critical parameters, and present the result as a function of them ("~X if A, ~Y if B").
7. **Sanity-check.** A surprising result usually means the model is wrong, and that's useful to know.
8. **Units follow precision:**

   | Duration | Quote in |
   |---|---|
   | 1–15 days | days |
   | 3–8 weeks | weeks |
   | 8–30 weeks | months |
   | 30+ weeks | hesitate: phase it or iterate |

   Avoid false precision. "About 6 months" is better than "127 working days".
9. **Track your record.** Log each estimate against the actual. When you're off by more than 50%, find out whether the parameters or the model were at fault.

### Project schedules
- For anything non-trivial, iterate: requirements → risk → design, build, integrate → validate with users.
- After the first increment, re-estimate the number and content of the remaining iterations.
- Commit to a fixed count only for trivial or near-identical projects.
- Adding people doesn't scale linearly (Brooks), because communication overhead grows with team size.
- Tell stakeholders that the team, its productivity, and the environment determine the schedule, and that the schedule will be revised with each increment (Tip 19).

## B. Algorithmic order (Tips 45, 46)
1. For every loop or recursion, ask **how big n can get**. Bounded is fine. If it depends on external data, look closer.
2. Classify by shape:
   - simple loop → O(n)
   - nested loops → O(n·m) or O(n²)
   - halving → O(log n)
   - divide and conquer → O(n log n)
   - permutations or subsets → O(n!) or O(2ⁿ); use heuristics
3. Project the scaling by ratio. For example, going from 100 to 1,000 items multiplies:
   - O(n) by 10×
   - O(n log n) by ~15×
   - O(n²) by 100×
4. Check memory and stack as well as time. For example, recursion depth × frame size.
5. **Test the estimate** (Tip 46):
   - Time 3–4 input sizes and plot them. Is the curve straight, bending up, or flattening?
   - Profile real data in the real environment.
   - Watch for cliffs: the data outgrows RAM or cache, or pathological input (e.g. presorted data hitting a naive quicksort).
6. **Best isn't always best.** A simple O(n²) can beat a complex O(n log n) for small n or when setup cost is high. Don't hand-roll library algorithms, and don't optimize before measuring.

## Output
```
**Mode:** ESTIMATE · **Accuracy needed:** … · **Scope assumptions:** …
**Answer:** <range in precision-matched units, as a function of critical params>
### Model          (components + how they combine)
### Parameters     | Parameter | Value | Source (measured / assumed) | Sensitivity (×/+) |
### Scenarios      | Scenario | Result |
### Risks & how to refine   (what to measure next; when to re-estimate)
```
