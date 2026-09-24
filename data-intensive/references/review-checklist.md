# Review checklist and incident diagnosis

## Part 1: Design review questions

### Workload and goals
- [ ] Are load parameters stated (RPS, read/write ratio, data size and growth, fan-out, hot keys)?
- [ ] Are latency targets stated as percentiles (p99/p999), measured client-side?
- [ ] Which operations need strong guarantees, and which can be eventually consistent?
- [ ] Is the chosen architecture justified by the numbers, or is it distributed "just in case"?

### Data and models
- [ ] Is there one clear system of record per entity? Is everything else explicitly derived and rebuildable?
- [ ] Does the data model fit the access patterns (relationships, joins, document locality)?
- [ ] Are analytics workloads separated from OLTP?
- [ ] Are indexes matched to queries (and their write cost accepted)?

### Encoding and evolution
- [ ] Explicit schemas for stored data, events, and APIs?
- [ ] Backward and forward compatibility for rolling deploys and old data?
- [ ] Round-trips preserve unknown fields?
- [ ] Schema changes planned as expand–migrate–contract?

### Replication
- [ ] Sync or async? Can an acknowledged write be lost on failover — and is that acceptable?
- [ ] Which read-after-write, monotonic-read, and consistent-prefix guarantees do user flows need, and how are they provided?
- [ ] Failover: how is the leader chosen? What prevents split brain? What happens to writes that didn't replicate?
- [ ] Multi-leader or leaderless: how are conflicts detected and resolved? Is LWW silently dropping data?

### Partitioning
- [ ] Is the partition key aligned with the most important queries and transactions?
- [ ] Hot-key and skew risk assessed? Sequential keys on key-range partitioning?
- [ ] Secondary index strategy (local vs global) and its consequences understood?
- [ ] Rebalancing plan; not `hash mod N`; automatic rebalancing not coupled with aggressive failure detection?

### Transactions and concurrency
- [ ] Actual isolation level known (per product), and matched to each invariant?
- [ ] Every read-modify-write replaced with atomic ops, CAS, or locks?
- [ ] Every check-then-act protected (constraint, lock on checked rows, serializable)?
- [ ] Retries of aborted transactions safe (idempotent, no external side effects inside)?

### Distributed coordination
- [ ] Any timeout treated as certain death? Any wall-clock ordering or LWW across nodes?
- [ ] Locks/leases protected with fencing tokens?
- [ ] Process pauses considered in lease logic?
- [ ] Dual writes to multiple systems? Distributed transactions across heterogeneous systems?
- [ ] Retries idempotent (idempotency keys, dedup at the final store)?
- [ ] Uniqueness and leader election backed by a linearizable mechanism?

### Pipelines and derived data
- [ ] Derived stores fed by CDC or an event log, not dual writes?
- [ ] Batch jobs rerunnable: immutable inputs, deterministic, outputs swapped atomically?
- [ ] Stream processing: event time vs processing time, late data, windowing, state checkpointing, exactly-once effect?
- [ ] Reprocessing path exists for bugs and schema changes?

### Operations and integrity
- [ ] Monitoring of replication lag, compaction backlog, consumer lag, partition skew, clock offset?
- [ ] Backups tested by restoring? Periodic integrity checks between source and derived data?
- [ ] Runbooks for failover, rebalancing, and reprocessing?
- [ ] Privacy: data minimization, retention, deletion possible (including in logs and backups)?

## Part 2: Incident diagnosis

| Symptom | Likely causes | Confirm by | Fix |
|---|---|---|---|
| User's own change disappears after refresh | Read from lagging async replica | Replica lag metrics at the time; which replica served the read | Read-after-write: route own-data reads to leader, or wait for replica to reach the write's position |
| Data appears, then disappears, on refresh | Reads hitting different replicas with different lag | Request logs showing replica per request | Monotonic reads: sticky replica per user |
| Counter/balance off; concurrent edits lost | Read-modify-write race (lost update) | Interleaved request logs; isolation level | Atomic update, CAS, `FOR UPDATE`, or serializable |
| Double booking / duplicate unique values | Write skew or phantom under snapshot/read committed | Two transactions both passing the check | Constraint, lock checked rows, materialized conflict, serializable |
| Duplicate orders/payments/emails | Client or consumer retries without idempotency; at-least-once delivery | Same request/message processed twice in logs | Idempotency key enforced at the final store |
| Two nodes acting as leader; corrupted shared resource | Split brain; lease holder paused (GC/VM) without fencing | GC/pause logs, lease timeline | Fencing tokens; consensus-based election |
| Writes lost after failover | Async replication; new leader lacked recent writes | Compare old leader's log with new leader's | Semi-sync replication; reconcile; avoid reusing IDs |
| Later write overwritten by earlier one | LWW with clock skew; multi-leader conflict | Clock offset metrics; conflicting timestamps | Logical versions/version vectors; CRDTs; avoid LWW for mutable data |
| One shard slow/hot | Hot key, sequential key range, skewed tenant | Per-partition and per-key metrics | Better key, salting hot keys, caching, splitting partition |
| Cascading timeouts and overload | Short timeouts + retries without backoff; failover under load | Retry rates; timeline of failovers | Backoff with jitter, retry budgets, circuit breakers, adaptive timeouts |
| Search index / cache disagrees with DB | Dual writes with partial failure or reordering | Compare records; check write paths | CDC from the DB; rebuild derived store |
| Stream results wrong after restart or delay | Processing-time windows; non-idempotent sink; unhandled late events | Compare event time vs processing time | Event-time windows with watermarks; idempotent/transactional sinks |
| Consumer lag growing | Consumer too slow; partition count too low; one hot partition | Per-partition lag | Scale consumers up to partition count; more partitions; fix skew |
| Tail latency spikes on LSM store | Compaction interfering, or compaction falling behind | Compaction metrics vs latency | Tune compaction, throttle, add capacity |
| In-doubt transactions holding locks | 2PC coordinator failure | Prepared-transaction list | Recover coordinator; heuristic resolution with care; move away from XA |
