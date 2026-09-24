# Derived data: batch, streams, and end-to-end correctness

## Contents
1. Systems of record vs derived data
2. Batch processing
3. Messaging and event streams
4. Databases and streams: CDC and event sourcing
5. Stream processing
6. Unbundling the database
7. End-to-end correctness
8. Doing the right thing

---

## 1. Systems of record vs derived data
- **System of record (source of truth):** holds the authoritative version; each fact represented once (normalized).
- **Derived data:** the result of transforming data from another system — caches, denormalized copies, search indexes, materialized views, recommendation models, analytics tables. Redundant, but essential for read performance. If lost, it can be rebuilt from the source.
- Being explicit about which is which clarifies the dataflow of the whole system.

## 2. Batch processing
Takes a bounded input, produces output, doesn't modify the input. Measured by throughput.

**Unix philosophy** as a model: small tools that do one thing, a uniform interface (files/streams), composition, immutable inputs, easy experimentation.

**MapReduce and successors:**
- Distributed filesystems (HDFS, object stores like S3) hold input and output; computation moves to the data.
- Map extracts key-value pairs; the framework sorts and groups by key; reduce processes each group.
- **Joins in batch:**
  - *Sort-merge join* (reduce-side): both inputs keyed by the join key, brought together in the reducer. General but costs a full sort/shuffle.
  - *Broadcast hash join* (map-side): one input is small enough to load into memory on every mapper.
  - *Partitioned hash join*: both inputs partitioned the same way, so each mapper joins matching partitions.
  - Handle **skew** (hot keys) by spreading hot keys across reducers and replicating the other side.
- **Outputs:** build search indexes or key-value stores as immutable files and swap them in atomically. Don't write to a production database record-by-record from a batch job (overloads it, and a failed partial job leaves partial output).
- **Why batch is robust:** inputs are immutable and outputs replace old outputs, so any bug can be fixed by rerunning — "human fault tolerance". Failed tasks are retried; this is safe because they're deterministic and side-effect free.
- **Beyond MapReduce:** dataflow engines (Spark, Flink, Tez) treat the whole workflow as one job, avoid writing every intermediate result to disk, and recompute lost partitions from lineage. Graph processing uses the Pregel (bulk synchronous parallel) model. High-level declarative APIs (SQL, DataFrames) let optimizers choose join strategies.
- Hadoop-style systems vs MPP databases: data lakes store raw data in any format ("sushi principle: raw data is better") and allow diverse processing; MPP databases are faster for SQL analytics on structured data. The two have converged.

## 3. Messaging and event streams
An **event** is a small, immutable record of something that happened, with a timestamp. Producers write, consumers read; related events are grouped into a topic/stream.

Key questions for any messaging system: What happens if producers outpace consumers (drop, buffer, apply backpressure)? What happens when nodes crash — are messages lost?

**Traditional brokers** (AMQP/JMS style — RabbitMQ, ActiveMQ, SQS):
- Delete messages once acknowledged; assign each message to one consumer (load balancing) or all (fan-out).
- With load balancing and redelivery, **message order is not preserved**.
- Good when messages are expensive to process, order doesn't matter, and there's no need to reread history.

**Log-based brokers** (Kafka, Kinesis, Pulsar-style):
- Append-only log, partitioned; within a partition, total order. Consumers track offsets; the broker keeps messages for a retention period.
- Parallelism = number of partitions (one consumer per partition in a group). A slow message blocks its partition (head-of-line).
- Consumers can **replay** from an old offset — great for reprocessing, adding new consumers, and recovery.
- Good for high throughput, ordered processing, and deriving multiple views from one stream.

## 4. Databases and streams
**Dual writes** (application writes to database and also to cache/search index/queue) are a trap: race conditions can apply writes in different orders to different systems, and partial failure leaves them permanently inconsistent.

**Change data capture (CDC):** capture the database's replication log (row-level changes) as a stream and apply it in the same order to derived systems (search index, cache, warehouse). The database is the leader; derived stores are followers.
- Initial load: snapshot plus log position, or log compaction (keep the latest value per key, so the log itself contains the full state).
- **Outbox pattern:** in the same transaction as the business change, write an event row to an outbox table; CDC publishes it. Gives atomicity between state change and message without 2PC.

**Event sourcing:** store all changes to application state as an immutable log of domain events (e.g. "seat reserved") rather than mutable state; derive current state by replaying.
- Separate **commands** (requests, which are validated and may be rejected) from **events** (facts, which are immutable once written).
- Benefits: full history and audit, easy to derive new views, easier debugging, can reprocess with new logic.
- Needs snapshotting of derived state for performance, careful event schema evolution, and a plan for deleting data (legal/privacy requirements conflict with immutability — use crypto-shredding, log compaction, or rewriting history deliberately).

**State, streams, and immutability:** mutable state and an append-only log of changes are two sides of the same coin. The log is the source of truth; the database is a cached view of the latest values. Immutability gives auditability and the ability to derive several read-optimized views (**CQRS**: separate write and read forms of data). Main cost: concurrency control becomes asynchronous (reads may not yet reflect a write).

## 5. Stream processing
Uses: complex event processing (search for patterns), stream analytics (rates, rolling averages, windows), maintaining materialized views, search on streams, and triggering actions.

**Reasoning about time:**
- **Event time** (when it happened) vs **processing time** (when it was processed). Use event time for correctness; processing-time windows go wrong when processing is delayed or restarted.
- **Stragglers / late events:** decide whether to ignore them (and count them as a metric) or publish corrections. Watermarks estimate when a window is complete.
- Device clocks are untrustworthy: record the event time on the device, the send time on the device, and the receive time on the server, and estimate the offset.
- **Window types:** tumbling (fixed, non-overlapping), hopping (fixed, overlapping), sliding (any events within an interval of each other), session (grouped by activity with an inactivity gap).

**Stream joins:**
- *Stream–stream (window) join:* e.g. match search events with clicks within an hour; keep state for the window.
- *Stream–table (enrichment) join:* enrich events with a local copy of a table kept up to date by CDC.
- *Table–table (materialized view) join:* maintain a join result as both inputs change (e.g. a timeline cache).
- **Time-dependence:** if joined state changes over time, which version is used affects results; make joins deterministic (e.g. version the dimension data) if you need reproducibility.

**Fault tolerance and exactly-once:**
- Streams never finish, so "rerun the job" doesn't work directly. Approaches: microbatching (Spark Streaming), checkpointing operator state (Flink), atomic commit of outputs, offsets, and state within the stream framework (Kafka transactions).
- **Idempotent writes** to external systems (e.g. include the offset or event ID and ignore duplicates) give exactly-once *effect* with at-least-once delivery.
- Rebuild operator state from a changelog stream or by replaying input.
- "Exactly-once" really means "effectively once": each event's effect is applied once, even if it was processed more than once.

## 6. Unbundling the database
- No single tool fits every access pattern, so real systems combine OLTP databases, caches, search, analytics, and ML. Treat the whole system as one "database" whose indexes and views are maintained by an ordered log (**unbundled database**): the log is the commit log; derived stores are asynchronously maintained indexes.
- **Prefer asynchronous, log-based integration** over distributed transactions: it's more robust (faults stay local), keeps systems loosely coupled, and allows independent evolution.
- **Lambda architecture** (batch + stream in parallel, merged) has been largely superseded by unifying batch and stream in one engine, and by **reprocessing** from the log for schema changes: run the old and new derived views side by side, shift reads gradually, and drop the old one — schema migrations without downtime.
- **Designing applications around dataflow:** application code becomes a function transforming state changes into derived state. Stream processors consume events, and derived state is pushed to clients (subscriptions, websockets) rather than pulled.
- **Reads as events:** logging read requests too allows tracking causal dependencies and reconstructing what a user saw.

## 7. End-to-end correctness
- **The end-to-end argument:** duplicate suppression and integrity must be implemented end to end — from client to final storage. TCP-level or database-level deduplication doesn't stop a user resubmitting a form. Generate a **unique request ID at the client** and enforce uniqueness at the final store.
- **Enforcing constraints in a log-based system:** route all requests that might conflict (e.g. all claims to one username) to the same log partition, and process them sequentially — the first wins, others are rejected. Multi-partition operations can be split into stages, each processed deterministically, with the request ID linking them.
- **Timeliness vs integrity:**
  - *Timeliness:* users see an up-to-date state (violations are temporary — just wait).
  - *Integrity:* no corruption, no loss, no contradictions (violations are permanent — need explicit repair).
  - Integrity is far more important. Event-based dataflow can ensure integrity without requiring timeliness, avoiding costly coordination.
- **Loosely interpreted constraints:** many business constraints can be violated temporarily and fixed with a compensating action (apology, refund, overbooking handling). Checking them asynchronously is often acceptable and cheaper. Coordination-avoiding systems keep strong integrity with weak timeliness.
- **Trust, but verify:** hardware and software bugs corrupt data. Run periodic integrity checks, compare replicas, test restores from backups, and prefer designs that are auditable (event logs, deterministic derivations, hashes/Merkle trees).

## 8. Doing the right thing
- Data systems affect people. Predictive systems can encode bias, deny opportunities, and create feedback loops; accountability and explanation matter.
- **Privacy:** collect only what's needed, be transparent, respect consent and deletion requests, protect data from breaches, and recognise that tracking-based data collection shifts power away from users. Design deletion and retention into the architecture (especially with immutable logs).
