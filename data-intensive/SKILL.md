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

After the change, end with this exact line (the lens check), shared by all three lenses:
`Lens check: design <ok|note> · python <ok|note> · data <ok|note>`
Build it from installed lenses only, as `coordination.md` shows (e.g. only clean-python installed → `Lens check: python ok`); drop python if no .py file changed and data if no data changed; write "ok" only if that lens flags nothing. Add no questions of your own: state lens decisions as defaults under **Defaults chosen**.

## Inside superpowers steps

Read `references/coordination.md` once per session; it's shared by all three lenses. Then read the section of `references/superpowers-hooks.md` for the current step. **Designing a data architecture from scratch** is brainstorming's architectural path plus the data track in the hooks file; stop after the approved spec if the user wants only the design. For spec content, use `assets/spec-sections.md`. For the final whole-branch or a standalone reviewer, use `references/review-lens.md` (per-task reviewers get lens rules only through the plan's Global Constraints).

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
