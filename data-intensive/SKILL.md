---
name: data-intensive
description: Data-systems lens for superpowers workflows, based on Martin Kleppmann's "Designing Data-Intensive Applications": data models and stores, storage engines, encoding and schema evolution, replication, partitioning, transactions and isolation, distributed failures, clocks, consensus, batch and stream pipelines, CDC, and end-to-end correctness. Use it when work involves data guarantees, scale, or concurrency. That covers designing a data architecture from scratch (through superpowers:brainstorming); choosing a database, queue, or data format; reviewing a data architecture or an incident; and supplying data concerns inside superpowers' planning, TDD, debugging, and code-review steps. Don't use it for ordinary CRUD with no scale, concurrency, or consistency concern.
---

# Data-Intensive (superpowers lens)

This lens judges what guarantees each component gives, what they cost, and what happens when things fail. Superpowers owns the build process. This skill runs two flows of its own, technology choices and data reviews, using the shared standalone discipline.

**Lanes**
- **data-intensive:** which store owns each piece of data, which guarantee each operation needs, how data flows, replicates, partitions and evolves, and what happens on failure.
- **software-design:** which module hides those choices.
- **clean-python:** the Python that enforces them.

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

## Inside superpowers steps

Read `references/coordination.md` once per session; it's shared by all three lenses. Then read the section of `references/superpowers-hooks.md` for the current step. **Designing a data architecture from scratch** is brainstorming's architectural path plus the data track in the hooks file; stop after the approved spec if the user wants only the design. For spec content, use `assets/spec-sections.md`. For the reviewer, use `references/review-lens.md`.

## Flow A: technology choice
Use this for "Postgres or DynamoDB?", "Kafka or SQS?", "Avro or Protobuf?", and similar. Announce the path first:
- **Quick:** reversible and low-stakes. Answer in chat: recommendation, trade-off, when to revisit.
- **Decision:** hard to reverse.
- **Spike:** a measurement decides it. Propose a throwaway benchmark in 2–3 sentences, get a nod, run it cheaply, then continue on the decision path.

The decision path follows the coordination file's standalone flow:
1. **Questions** from `references/question-bank.md` §2: access patterns, non-negotiable guarantees, operational model, existing stack, horizon.
2. **Compare categories before products** (`references/decision-guides.md`). Keep 2–3 options, recommendation first.
3. **Check product facts** in current docs, and cite them with dates.
4. **Write the record** with `assets/decision-record-template.md` to `docs/superpowers/decisions/`. It covers:
   - fit to the workload;
   - failure behaviour of each option;
   - operational cost;
   - exit cost;
   - "revisit when".

   Adoption is handed to brainstorming.

## Flow B: data architecture or incident review
Use this for "review our data flow", "what could go wrong with this pipeline", and post-incident analysis. A live incident goes to `superpowers:systematic-debugging` instead. Choose a path: **targeted** (one flow or incident) or **full**. Then follow the coordination file's standalone flow:
1. **Questions** from `references/question-bank.md` §3.
2. **Map** components, the system of record for each entity, dataflows with the guarantee each link actually provides, the isolation level (read from config), replication, and partitioning. Add a timeline for incidents.
3. **Walk it** with `references/review-checklist.md`, by blast radius: loss and corruption → correctness anomalies → availability → performance → operability. Look hardest for:
   - dual writes and side effects in the write path;
   - check-then-act races;
   - ordering by wall clock;
   - missing idempotency;
   - locks without fencing;
   - assumed isolation levels.
4. **Severity:**
   - Critical: loss, silent corruption, broken invariants.
   - Important: problems that show up under load or failure.
   - Minor: everything else.

   Every data finding is written as an event sequence.
5. **Write** with `assets/review-template.md` to `docs/superpowers/reviews/YYYY-MM-DD-<topic>-data-review.md`. Hand each fix off to brainstorming.

**Topic references** (load when needed):
- `foundations.md`
- `encoding-evolution.md`
- `replication.md`
- `partitioning.md`
- `transactions.md`
- `distributed.md`
- `derived-data.md`

*Condensed and paraphrased from Martin Kleppmann, "Designing Data-Intensive Applications" (O'Reilly, 2017). Superpowers © Jesse Vincent (MIT).*
