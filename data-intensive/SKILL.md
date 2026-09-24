---
name: data-intensive
description: Designs, reviews, and debugs data-intensive systems using the principles of Martin Kleppmann's "Designing Data-Intensive Applications" — data models and databases, storage engines, OLTP vs analytics, encoding and schema evolution, replication, partitioning/sharding, transactions and isolation levels, distributed-system faults, clocks, consensus, batch and stream processing, CDC, event sourcing, and end-to-end correctness. Use whenever the user is choosing a database, queue, or data format; designing or reviewing a backend, data platform, or pipeline architecture; scaling a system; hunting race conditions, lost updates, or consistency bugs; diagnosing replication lag, hot shards, or distributed incidents; planning schema migrations; preparing for a system design interview; or asking how some data system works under the hood.
---

# Data-Intensive Systems

A data-intensive application is one where the hard problems are the amount, complexity, and rate of change of data, rather than raw CPU. This skill helps reason about such systems from first principles: what guarantees each component gives, what it costs, and what happens when things fail.

The three goals behind every recommendation:

- **Reliability** — the system keeps working correctly when hardware, software, or people fail.
- **Scalability** — there are reasonable ways to cope as load grows.
- **Maintainability** — people can operate, understand, and evolve it.

Always frame trade-offs in these terms, with concrete load numbers where possible.

## Identify the use case

Pick the use case(s) from the request, then follow that section. Many requests combine several (e.g. a design review usually touches C, E, and F).

| # | Use case | Typical request |
|---|---|---|
| A | Design a new data system | "Design the backend for…", "how should we architect…" |
| B | Review an existing architecture or design doc | "Review this design", "what could go wrong with…" |
| C | Choose a technology | "Postgres or Mongo?", "Kafka or RabbitMQ?", "which storage format?" |
| D | Schema, encoding, and API evolution | "How do we migrate this schema?", "Avro vs Protobuf vs JSON", rolling deploys |
| E | Scale it: replication, partitioning, capacity | "We're outgrowing one DB", "how do we shard?", "read replicas?" |
| F | Concurrency and transaction correctness | "Is this code race-free?", double bookings, lost updates, "which isolation level?" |
| G | Distributed coordination and failure | locks/leases, leader election, timeouts, clocks, idempotency, exactly-once |
| H | Data pipelines and derived data | ETL, batch jobs, stream processing, CDC, event sourcing, caches, search indexes |
| I | Diagnose an incident or weird behaviour | stale reads, lost writes, split brain, hot shard, replication lag |
| J | Learn, explain, or interview prep | "Explain LSM-trees", "quiz me on consistency", system design practice |

Reference files, by topic — read the ones the use case needs:

- `references/foundations.md` — reliability/scalability/maintainability, describing load and latency percentiles, data models, query languages, storage engines, OLTP vs OLAP, column stores.
- `references/encoding-evolution.md` — encoding formats, schema evolution, compatibility, and dataflow through databases, services, and messages.
- `references/replication.md` — single-leader, multi-leader, leaderless; replication lag anomalies; conflict resolution; quorums.
- `references/partitioning.md` — key-range vs hash, hot spots, secondary indexes, rebalancing, routing.
- `references/transactions.md` — ACID, isolation levels, the anomaly catalogue, and how to prevent each one in application code.
- `references/distributed.md` — partial failure, networks, timeouts, clocks, process pauses, fencing, linearizability, ordering, 2PC, consensus, coordination services.
- `references/derived-data.md` — batch processing, stream processing, messaging, CDC, event sourcing, stream joins, fault tolerance, unbundled databases, end-to-end correctness, ethics.
- `references/decision-guides.md` — side-by-side trade-off tables for the common choices.
- `references/review-checklist.md` — the question list for design reviews and incident diagnosis.
- `assets/design-doc-template.md`, `assets/decision-record-template.md` — output formats.

**Currency note:** the book was published in 2017. The principles are durable, but specific product capabilities (which databases support what isolation, which systems offer what guarantees) change. When a recommendation depends on what a specific product does today, check its current documentation (web search if available) and say so, rather than relying on the book's snapshot.

## Ground rules for every use case

1. **Start from the workload.** Ask for (or estimate) the load parameters that matter: reads/writes per second, read/write ratio, data size and growth, fan-out, access patterns, latency targets at p50/p99/p999, consistency needs, and how bad each kind of failure would be. No numbers, no scaling advice — state assumptions explicitly if the user can't provide them.
2. **Name the guarantee.** Don't say "consistent" or "safe" loosely. Say which one: linearizable, read-your-writes, monotonic reads, consistent prefix, serializable, snapshot isolation, read committed, causal, eventual. Most bugs live in the gap between the guarantee someone assumed and the one they have.
3. **Walk the failure.** For each component, ask what happens when it crashes, is slow, is partitioned, restarts with old state, or its clock jumps. Walk a concrete failure sequence step by step.
4. **Prefer simple.** Many systems don't need distribution. One well-provisioned relational database with replicas covers a lot. Recommend distributed machinery only when the workload demands it, and name the cost.
5. **Be concrete.** Give schemas, key designs, SQL, partition keys, message formats, and step-by-step failure sequences — not just principles.
6. **Name the trade-off.** Every choice gives something up. Say what, and when the user would regret it.

## A. Design a new data system

1. Gather requirements and load parameters (ground rule 1). Identify the core entities and the main read and write paths, and which operations need strong guarantees (money, inventory, uniqueness) versus which can be eventually consistent (feeds, analytics, recommendations).
2. Pick the **system of record** for each kind of data — the authoritative source. Everything else (caches, search indexes, analytics copies, materialized views) is **derived data**, rebuilt from the source. Read `references/derived-data.md` §Unbundling.
3. Choose data models and stores per access pattern: relational, document, graph, key-value, wide-column, search, column-oriented analytics, object storage. Use `references/decision-guides.md`. Avoid one-store-for-everything if access patterns differ wildly, but avoid needless sprawl too.
4. Design the dataflow between stores: synchronous writes, CDC, event log, batch jobs. Prefer a log-based flow (CDC or an event log) over dual writes from application code, which drift out of sync on partial failure.
5. Plan evolution: encoding formats with explicit schemas, backward and forward compatibility, rolling upgrades (`references/encoding-evolution.md`).
6. Plan for scale only as far as the numbers require: replication for availability and read scaling, partitioning when data or write volume outgrows one node (`references/replication.md`, `references/partitioning.md`).
7. Identify every place correctness needs coordination — uniqueness constraints, balances, inventory, bookings — and decide how each is enforced: DB constraint, serializable transaction, single-partition log processing, or consensus (`references/transactions.md`, `references/distributed.md`).
8. Walk the failure modes (ground rule 3) and the operational story: monitoring, backups, restore testing, reprocessing.
9. Write it up with `assets/design-doc-template.md`, including rejected alternatives.

## B. Review an existing architecture

1. Map the system: components, stores, the system of record for each entity, dataflows, and which guarantees each link provides. Draw it (a Mermaid diagram is fine).
2. Work through `references/review-checklist.md`. Prioritize by blast radius: data loss and silent corruption first, then correctness anomalies, then availability, then performance, then operability.
3. For each finding give: where, what can go wrong (as a concrete event sequence), how likely and how bad, and the fix with its trade-off.
4. Call out dual writes, check-then-act races, reliance on wall-clock ordering, missing idempotency, locks without fencing, and assumptions about isolation levels — these are the most common serious issues.
5. Credit the parts that are sound.

## C. Choose a technology

1. Pin down the workload and the non-negotiables (ground rule 1).
2. Use `references/decision-guides.md` to compare categories first (e.g. document vs relational, log-based vs traditional broker), then specific products.
3. Check current product facts against their docs where the decision hinges on them (currency note).
4. Record the decision with `assets/decision-record-template.md`: context, options, decision, consequences, and the conditions that would make you revisit it.

## D. Schema, encoding, and API evolution

Read `references/encoding-evolution.md`.

1. Identify every place data crosses a process boundary or outlives the code that wrote it: databases, service APIs, message queues, files, caches.
2. For each, determine who writes and who reads, and whether old and new code run at the same time (rolling deploys, mobile clients, long-lived data). You then need backward compatibility (new code reads old data) and forward compatibility (old code reads new data).
3. Recommend formats and rules: explicit schemas (Protobuf, Avro, or JSON Schema), only add optional fields with defaults, never reuse field tags or names, don't remove required fields, and watch for old code dropping unknown fields on read-modify-write.
4. For database schema changes, plan expand–migrate–contract: add new structure, dual-read/backfill, switch, then remove old structure. Note which DDL operations lock or rewrite tables in the specific database.

## E. Scale it

1. Get the numbers. Find the actual bottleneck: reads, writes, storage, a hot key, fan-out, or one expensive query. Latency percentiles, not averages.
2. Cheaper fixes first: indexes, query fixes, caching, bigger machine, read replicas, moving analytics off the OLTP database.
3. Replication (`references/replication.md`): choose the topology, sync vs async, and decide which read-after-write guarantees the application needs, and how to provide them.
4. Partitioning (`references/partitioning.md`): choose the partition key from the access pattern, check for skew and hot spots, decide how secondary indexes work, and plan rebalancing and request routing.
5. Say what gets harder: cross-partition queries and transactions, uniqueness, and ordering.
6. Back-of-envelope the result: nodes needed, data per node, headroom.

## F. Concurrency and transaction correctness

Read `references/transactions.md`.

1. Identify the invariant at stake (no double booking, balance ≥ 0, unique username, at most N seats).
2. Identify the database and the **actual** isolation level in use (check config; defaults differ, and "repeatable read" means different things in different products).
3. Walk the interleaving: write out two concurrent transactions step by step and show whether the invariant can break. Classify it: dirty read/write, read skew, lost update, write skew, phantom.
4. Recommend the lightest fix that actually prevents it: atomic update (`UPDATE … SET x = x + 1`), compare-and-set, `SELECT … FOR UPDATE`, a unique constraint, materializing the conflict, or serializable isolation (with retries on serialization failure).
5. If the operation spans services or databases, go to use case G (no single transaction covers it).
6. Show the corrected code or SQL, and a test that reproduces the race if feasible.

## G. Distributed coordination and failure

Read `references/distributed.md`.

1. Name what the user is actually trying to guarantee: mutual exclusion, a single leader, uniqueness, exactly-once effect, ordering, or an atomic commit across systems.
2. Check for the classic traps: timeouts treated as proof of death, wall-clock timestamps used to order events or for last-write-wins, locks or leases without fencing tokens, process pauses (GC, VM suspension), retries without idempotency, and distributed transactions across heterogeneous systems.
3. Recommend: fencing tokens with a storage check, idempotency keys and deduplication, consensus-backed coordination (etcd, ZooKeeper, or the database's own mechanisms) for leader election and locks, a single-leader log for total ordering, and the outbox pattern or CDC instead of dual writes and 2PC.
4. Say what the system does when the coordination service is unreachable (it must stop, not guess).

## H. Data pipelines and derived data

Read `references/derived-data.md`.

1. Identify the sources of truth, the derived outputs, and freshness needs. Batch (bounded input, rerunnable) versus stream (unbounded, low latency) — or both.
2. Design for rerunnability: immutable inputs, deterministic transforms, outputs replaced wholesale or written idempotently. The ability to reprocess from the source is the biggest reliability lever.
3. For keeping stores in sync, prefer CDC or an event log as the single ordered source, feeding each derived store, over dual writes.
4. For stream processing, decide on event time vs processing time, windowing and late-data handling, join type, state and checkpointing, and how exactly-once *effect* is achieved (idempotent sinks, transactional commits, deduplication).
5. For event sourcing, separate commands (validated) from events (immutable facts), and plan snapshotting, schema evolution of events, and deletion (e.g. for privacy law).

## I. Diagnose an incident

1. Get the symptoms and a timeline. Ask which guarantees the code assumed.
2. Match the symptoms to known failure patterns (the "symptoms" column of `references/review-checklist.md` §Diagnosis): stale reads after writes → replication lag; lost updates → read-modify-write race; two leaders → failed failover / no fencing; inconsistent ordering → clock skew or multi-leader conflicts; one slow shard → hot key or skew; cascading timeouts → retries without backoff or queueing.
3. Propose how to confirm the hypothesis (which metrics, logs, or a reproduction), then the immediate mitigation and the durable fix.

## J. Learn, explain, interview prep

- **Explain** a concept at the level asked, using a concrete example and a step-by-step failure scenario. Connect it to the trade-off it resolves. Offer a diagram when the mechanism is spatial (replication, partitioning, LSM compaction).
- **Quiz**: ask one question at a time, wait for the answer, then correct and explain. Mix recall ("what does write skew mean?") with application ("this booking code runs at snapshot isolation — can it double-book?").
- **System design practice**: play interviewer. Give a prompt, make the user drive requirements and estimates, then probe with follow-ups on data model, scaling, consistency, and failure. Finish with feedback against the ground rules above.

## Credit

Condensed and paraphrased from Martin Kleppmann, *Designing Data-Intensive Applications* (O'Reilly, 1st ed., 2017). The book, with its extensive references, is worth reading in full.
