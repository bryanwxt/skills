# Decision guides

Compare categories before products. Check current product documentation before finalizing — capabilities change.

## Contents
1. Data model
2. OLTP storage engine
3. Analytics store
4. Encoding format
5. Replication topology
6. Partitioning scheme
7. Isolation / concurrency control
8. Messaging system
9. Keeping stores in sync
10. Batch vs stream
11. Coordination
12. When to not distribute at all

---

## 1. Data model
| Choose | When | Watch out for |
|---|---|---|
| Relational | Many-to-one / many-to-many relationships, ad-hoc queries, strong constraints, transactions across rows. The safe default. | Object–relational impedance; schema migrations on huge tables |
| Document | Self-contained trees loaded and saved as a unit, heterogeneous or fast-changing structure, few cross-document references | Emulating joins in the app; denormalized copies drifting; large documents rewritten on each update |
| Graph | Highly connected data, variable-length traversals, many relationship types | Operational maturity; analytics at scale |
| Key-value | Access only by primary key, very high throughput, caching, sessions | No secondary queries without extra machinery |
| Wide-column (Cassandra-style) | Massive write volume, known query patterns, multi-datacenter availability | Must model tables per query; eventual consistency; no joins |
| Search engine | Full-text, fuzzy, faceted queries | Not a system of record; derived from the source |
| Time series | Append-mostly metrics/events by time | Cardinality limits; retention/downsampling |

## 2. OLTP storage engine
| | LSM-tree | B-tree |
|---|---|---|
| Writes | Higher throughput (sequential) | Slower (page updates + WAL) |
| Reads | May check several files | Predictable, one location per key |
| Tail latency | Compaction can cause spikes | More stable |
| Space | Better compression, less fragmentation | Fragmentation |
| Good for | Write-heavy, large datasets | Read-heavy, transactional locking |

## 3. Analytics store
- Separate the analytics workload from OLTP once scans start to hurt user-facing latency.
- Column-oriented warehouse (or columnar files like Parquet in a data lake) for large scans and aggregates.
- Star schema for BI; wide denormalized tables are also common.
- Feed it by CDC or batch ELT from the system of record.

## 4. Encoding format
| Use | When |
|---|---|
| JSON (+ JSON Schema/OpenAPI) | Public APIs, browser clients, cross-org interchange, human debugging |
| Protobuf / Thrift (gRPC) | Internal service RPC, strongly typed languages, compact and fast |
| Avro (+ schema registry) | Kafka/event streams, data lakes, dynamically generated schemas, long-term data |
| Parquet/ORC | Analytics files |
| Language-native serialization | Never for storage or cross-service data |

## 5. Replication topology
| | Single-leader | Multi-leader | Leaderless |
|---|---|---|---|
| Writes | One node | Several nodes / datacenters / devices | Any replicas (quorum) |
| Conflicts | None (serial at leader) | Yes — must resolve | Yes — must resolve |
| Consistency | Can be linearizable (reads from leader) | Eventual | Eventual (tunable staleness) |
| Failover | Needed; risky (lost writes, split brain) | Per-leader | Not needed |
| Use | Default for most systems | Multi-datacenter writes, offline-first, collaboration | High write availability, tolerate slow/failed nodes |

Sync vs async: synchronous (or semi-sync) where losing an acknowledged write is unacceptable; async where latency and availability matter more — and then design for read-after-write and monotonic reads.

## 6. Partitioning scheme
| | Key range | Hash | Compound (hash + sorted) |
|---|---|---|---|
| Range queries | Yes | No | Yes, within the hashed prefix |
| Even load | Risk of sequential hot spots | Even (except single hot keys) | Even across prefixes |
| Example key | `(tenant, date)` | `user_id` | `(user_id) + timestamp` |

Secondary indexes: local (cheap writes, scatter/gather reads) vs global (targeted reads, async/multi-partition writes).

## 7. Isolation / concurrency control
| Situation | Recommended |
|---|---|
| Simple counters / balances | Atomic `UPDATE … SET x = x + n` with guard `WHERE` |
| Read-modify-write of a record | Atomic op, CAS with version column, or `SELECT … FOR UPDATE` |
| Check-then-insert (uniqueness) | Unique constraint |
| No overlapping ranges (bookings) | Exclusion constraint, or lock on materialized slot rows, or serializable |
| Invariants across several rows | Serializable (SSI) with retries, or lock the rows read |
| Long read-only reports/backups | Snapshot isolation |
| Very high contention on hot rows | Serial execution per partition, or queue/log per key |
| Across services | Idempotency keys + outbox/CDC + compensation (sagas) — not XA |

## 8. Messaging system
| | Traditional broker (RabbitMQ, SQS) | Log-based (Kafka, Kinesis) |
|---|---|---|
| Delivery | Message deleted after ack | Retained; consumers track offsets |
| Ordering | Not guaranteed with redelivery/competing consumers | Total order per partition |
| Replay | No | Yes |
| Parallelism | Per message | Per partition |
| Best for | Task queues, expensive per-message work, order irrelevant | Event streams, CDC, many consumers deriving views, reprocessing |

## 9. Keeping stores in sync
| Approach | Verdict |
|---|---|
| Dual writes from application | Avoid — races and partial failure cause permanent divergence |
| Distributed transaction (XA/2PC) across stores | Avoid — fragile, blocks, poor availability |
| CDC from the system of record | Recommended |
| Transactional outbox + CDC/poller | Recommended when you need domain events |
| Event sourcing (log is the source of truth) | Good when history, audit, and multiple views matter; more complexity |
| Periodic batch rebuild | Good when freshness requirements are loose; simplest to reason about |

## 10. Batch vs stream
- **Batch:** bounded input, freshness in hours is fine, reprocessing simple, heavy joins over full datasets.
- **Stream:** freshness in seconds, unbounded input, incremental views, alerts.
- Use a log (Kafka-style) as the backbone so the same data can be processed both ways and reprocessed.

## 11. Coordination
| Need | Use |
|---|---|
| Leader election, locks, membership, partition assignment | Coordination service (etcd, ZooKeeper, Consul) or the database's own mechanism, with fencing tokens |
| Uniqueness | Unique constraint in one database; or single-partition log; or linearizable CAS |
| Global ordering | Single leader or single log partition (limits throughput); otherwise per-key/partition ordering |
| Cross-service atomicity | Outbox + idempotent consumers; sagas with compensation |

## 12. When to not distribute at all
One node with replicas for failover handles far more than people expect (tens of thousands of transactions per second on modern hardware, terabytes of data). Distribute when a specific load parameter demands it, and name which. Distributed systems buy scale and fault tolerance at the price of complexity and weaker guarantees.
