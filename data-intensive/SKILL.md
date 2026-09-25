---
name: data-intensive
description: 'Use when work involves data guarantees, scale, or concurrency: choosing a database, queue, or data format; designing or reviewing a data architecture, pipeline, or incident; or superpowers steps touching schemas, migrations, transactions, queues, caches, replication, or races. Not for plain CRUD with no scale, concurrency, or consistency concern. Based on Kleppmann''s "Designing Data-Intensive Applications".'
---

# Data-Intensive (superpowers lens)

This lens judges what guarantees each component gives, what they cost, and what happens when things fail. Superpowers owns the build process. This skill runs two flows of its own: technology choices (Flow A) and data architecture or incident reviews (Flow B).

## Ground rules
1. **Workload first.** Get the load parameters: reads and writes per second, data size and growth, fan-out and hot keys, p99 targets, and the cost of each kind of failure. Without numbers, give no scaling advice; state your assumptions instead.
2. **Name the guarantee:** linearizable, serializable, snapshot, read committed, read-your-writes, monotonic, consistent prefix, causal, or eventual. Never just "consistent".
3. **Walk the failure:** crash, slowness, partition, stale restart, clock jump, retry. Write the event sequence.
4. **Prefer simple.** One relational database with replicas covers a lot. Distribute only when a named load parameter demands it.
5. **Be concrete, and name the trade-off:** schemas, keys, SQL, message formats, and what each choice gives up.
6. **Check product facts.** The book is from 2017. Cite current documentation and date the check.

## Quick rule: bounded and trivial changes

Don't open the reference files. Write the `data …` part of the lens check only when the change touches data. Flag:
- an unprotected read-modify-write or check-then-act;
- a dual write, or a side effect whose delivery semantics aren't stated;
- an incompatible schema or message change (use expand-only);
- a retry without idempotency.

Otherwise stay silent.

After every code change, including debugging fixes, end with the lens-check line. Its segments, in this order: `design` if software-design is installed; `python` if clean-python is installed and a .py file changed; `data` if data-intensive is installed and data changed. Write "ok" only if that lens flags nothing. E.g. only clean-python installed → `Lens check: python ok`; all three installed, a .py change, no data → `Lens check: design ok · python ok`.

Lenses add no questions, and they don't replace brainstorming's. When the request doesn't say what the change is for, brainstorming's first message is its one purpose question and nothing else; lens defaults wait for the design message. In the design, list at most 3 lens defaults the user might not expect under **Defaults chosen**, or leave the list out.

## Inside superpowers steps

When brainstorming classifies the request as bounded or a spike, the quick rule above is all this lens needs: open no reference files for it. Otherwise, at each superpowers step, read two files, one copy each from any lens:
- `references/coordination.md`, the first time only;
- that step's file: `references/steps/brainstorming.md`, `writing-plans.md`, `tdd.md`, `execution.md`, `verification.md`, `review.md`, `debugging.md` or `finishing.md`.

Each step file has the shared rules and a section per lens; skip lenses that aren't installed.

Stay silent at steps with no data-guarantee, scale, concurrency, schema, messaging or multi-store concern. **Designing a data architecture from scratch** is brainstorming's architectural path plus this lens's section of `references/steps/brainstorming.md`; stop after the approved spec if the user wants only the design. For the final whole-branch or a standalone reviewer, use `references/review-lens.md` (per-task reviewers get lens rules only through the plan's Global Constraints).

## Flows A and B (the flows this skill starts)

For a technology choice ("Postgres or DynamoDB?", "Kafka or SQS?", "Avro or Protobuf?"), or a review of a data architecture, pipeline or past incident, follow `references/flows.md`. A live incident goes to `superpowers:systematic-debugging` instead.

**Topic references** (load when needed):
- `foundations.md`
- `encoding-evolution.md`
- `replication.md`
- `partitioning.md`
- `transactions.md`
- `distributed.md`
- `derived-data.md`

*Condensed and paraphrased from Martin Kleppmann, "Designing Data-Intensive Applications" (O'Reilly, 2017). Superpowers © Jesse Vincent (MIT).*
