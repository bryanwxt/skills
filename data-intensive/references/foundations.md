# Foundations: goals, data models, storage engines

## Contents
1. Reliability
2. Scalability: describing load and performance
3. Maintainability
4. Data models: relational, document, graph
5. Query languages
6. Storage engines: log-structured vs B-trees
7. Other indexes
8. OLTP vs analytics; data warehouses
9. Column-oriented storage

---

## 1. Reliability
A **fault** is one component deviating from spec; a **failure** is the whole system stopping serving users. Design so faults don't become failures. Deliberately inducing faults (chaos testing) exercises the fault-tolerance machinery.

- **Hardware faults:** disks, RAM, power, network. Traditionally handled with redundancy per machine; at scale, design software to tolerate the loss of whole machines (which also enables rolling upgrades).
- **Software errors:** systematic bugs that hit many nodes at once (a bad input, a runaway process, a slow dependency, cascading failures). Mitigate with careful assumptions, testing, process isolation, crash-and-restart, measurement, and alerts on invariants.
- **Human errors:** the leading cause of outages. Mitigate with well-designed APIs and admin tools, sandboxes, thorough testing, fast rollback and gradual rollout, tools to recompute data, and good monitoring (telemetry).

## 2. Scalability
Scalability isn't a label; it's the question "if load grows in a particular way, how do we cope?"

**Describe load with load parameters** specific to the system: requests per second, read/write ratio, active users, cache hit rate, fan-out. Example: a social feed can either be computed on read (query all followees' posts) or precomputed on write (fan-out each post to followers' timelines). Fan-out-on-write makes reads cheap but writes expensive for users with millions of followers — a hybrid handles celebrities on read.

**Describe performance with distributions, not averages.**
- Response time varies; report percentiles: p50 (median), p95, p99, p999. High percentiles (tail latency) matter because the slowest requests often belong to the most valuable users (those with the most data).
- **Tail latency amplification:** when one user request fans out to many backend calls, the chance of hitting at least one slow call grows quickly.
- Measure response time on the client side; queueing delay (head-of-line blocking) is often most of it. Load tests must keep sending requests independently of response times.
- Aggregate percentiles correctly — don't average percentiles; merge histograms.
- SLOs/SLAs are usually stated as percentiles.

**Coping with load:** scale up (bigger machine) vs scale out (more machines, shared-nothing). Stateless services are easy to scale out; stateful data systems are much harder, so stay on one node until scale or availability forces otherwise. There's no generic scalable architecture — it's built around assumptions about which operations are common and which are rare. Get those wrong and the scaling effort is wasted.

## 3. Maintainability
- **Operability:** visibility into runtime behaviour, good monitoring, automation support, no dependence on individual machines, documentation, sensible defaults with overrides, predictable behaviour.
- **Simplicity:** remove accidental complexity (complexity arising from the implementation, not the problem) through good abstractions.
- **Evolvability:** make change easy. It's closely tied to simplicity and good abstractions.

## 4. Data models
The data model shapes how you think about the problem. Each layer hides the one below with a clean model.

**Relational:** data as relations (tables) of tuples. Excellent for joins, many-to-one and many-to-many relationships, and ad-hoc queries; the query optimizer chooses access paths.

**Document (JSON-like):**
- Good fit when data is a self-contained tree (a one-to-many structure loaded as a whole, e.g. a résumé) — better locality and less object-relational mismatch.
- Weak for many-to-one and many-to-many relationships: joins are weak or absent, so the application emulates them or data gets denormalized (and then must be kept consistent).
- **Schema-on-read** (structure interpreted at read time; like dynamic typing) vs **schema-on-write** (enforced by the database; like static typing). Schema-on-read helps with heterogeneous data or structure controlled by external systems; either way the application depends on some implicit schema.
- Locality helps only if you usually need most of the document; updates often rewrite the whole document, so keep documents small.
- Relational and document databases have converged (JSON columns in relational DBs, joins in some document DBs).

**Normalization:** store human-meaningful information once and refer to it by ID. Duplication (denormalization) speeds reads but needs keeping copies in sync — it's a form of derived data.

**Graph:** vertices and edges, best when anything can relate to anything (social graphs, road networks, fraud rings, knowledge graphs).
- **Property graphs** (vertices and edges with labels and properties; Cypher, Gremlin).
- **Triple stores** (subject–predicate–object; SPARQL, RDF).
- Graph queries with variable-length paths are awkward in SQL (recursive CTEs) but natural in graph languages. Datalog underlies many of these ideas.
- Good for evolvability: new kinds of relationships don't need schema changes.

## 5. Query languages
- **Declarative** (SQL, Cypher, CSS) says *what* you want; the system decides *how*. This allows optimizers and parallel execution and hides implementation changes. Prefer declarative over imperative querying where available.
- MapReduce-style querying is somewhere between; higher-level declarative layers usually replace it.

## 6. Storage engines
Two families of OLTP storage engines:

**Log-structured (LSM-trees; e.g. RocksDB, LevelDB, Cassandra, HBase):**
- Writes go to an in-memory sorted structure (memtable), flushed to immutable sorted files (SSTables); background compaction merges files and discards overwritten or deleted (tombstoned) values. A write-ahead log protects the memtable.
- Reads check the memtable, then SSTables newest to oldest; Bloom filters skip files that don't contain a key.
- Strengths: high write throughput (sequential writes), lower write amplification in many cases, better compression, smaller files.
- Weaknesses: compaction can interfere with foreground reads and writes, causing unpredictable tail latency; compaction can fall behind under heavy write load (monitor it); a key may exist in several places.
- Simpler relative: **hash indexes** over an append-only log (Bitcask) — fast but keys must fit in memory and range queries don't work.

**B-trees (most relational databases):**
- Fixed-size pages in a balanced tree, updated in place, with a write-ahead log (WAL/redo log) for crash recovery and latches for concurrency.
- Strengths: predictable reads, each key in exactly one place (nice for transactional locking), mature.
- Weaknesses: every write goes to the WAL and a page (write amplification), page splits, fragmentation.

Rule of thumb: LSM tends to be faster for writes, B-trees for reads — but benchmark your workload.

## 7. Other indexes
- **Secondary indexes** can be non-unique; they store either the row (clustered/covering) or a reference (heap file). Covering indexes answer queries from the index alone at the cost of extra writes and storage.
- **Multi-column indexes:** concatenated indexes (column order matters) or spatial/multidimensional indexes (R-trees) for ranges on multiple dimensions.
- **Full-text and fuzzy indexes** (e.g. Lucene) for search, synonyms, and typos.
- **In-memory databases** are fast mainly because they avoid encoding data for disk, not just because they avoid disk reads. Durability comes from logs, snapshots, or replication.
- Every index speeds reads and slows writes. Choose indexes from the query patterns.

## 8. OLTP vs analytics
| | OLTP | OLAP / analytics |
|---|---|---|
| Reads | Few records by key | Aggregates over huge numbers of records |
| Writes | Random, low-latency, from user input | Bulk import (ETL) or event streams |
| Users | End users via the application | Analysts, BI, data science |
| Data | Latest state | History of events |
| Size | GB–TB | TB–PB |

- Run analytics on a **data warehouse** (a separate, read-optimized copy loaded via ETL/ELT or CDC), not on the OLTP database, so heavy scans don't hurt user-facing latency.
- **Star schema:** a large fact table of events, with foreign keys to dimension tables (who, what, where, when). Snowflake schemas normalize dimensions further.

## 9. Column-oriented storage
- Store each column separately, so queries read only the columns they need. Ideal for fact tables with hundreds of columns where queries touch a few.
- Columns compress extremely well (bitmap encoding, run-length encoding), and processing can be vectorized to fit CPU caches.
- **Sort order:** choose a sort key from common filters (e.g. date first); the first sort column compresses best. Replicas can use different sort orders.
- Writes are harder: buffer in a row-oriented, in-memory store and merge into column files in bulk (LSM-style).
- **Materialized aggregates / data cubes** precompute common aggregates; faster queries, less flexibility.
- Columnar file formats (Parquet, ORC) apply the same ideas to data lakes.
