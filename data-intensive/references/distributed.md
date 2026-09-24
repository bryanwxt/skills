# Distributed systems: faults, time, consistency, consensus

## Contents
1. Partial failure
2. Unreliable networks and timeouts
3. Unreliable clocks
4. Process pauses
5. Truth, majorities, and fencing
6. Byzantine faults and system models
7. Linearizability
8. Ordering, causality, and total order broadcast
9. Atomic commit and 2PC
10. Consensus and coordination services
11. Practical patterns

---

## 1. Partial failure
On one machine, things usually either work or crash. In a distributed system, some parts can be broken in unpredictable ways while others work fine — **partial failure** — and it's **nondeterministic**: you may not even know whether something succeeded. Build fault tolerance into the software; assume anything that can go wrong will.

## 2. Unreliable networks
Datacenter networks are **asynchronous packet networks**: a request can be lost, queued, delayed arbitrarily, or the remote node can crash, pause, or be slow; the response can be lost or delayed. **The sender can't tell which.** A timeout tells you only that you didn't get a reply.
- Network faults (partitions, dropped packets, misconfigured switches) happen regularly even in well-run datacenters. Test how the software reacts to them.
- **Detecting faults:** some signals are definitive (connection refused, process crash notified by the OS), but generally you rely on timeouts.
- **Choosing timeouts:** no correct value exists because delays are unbounded (queueing in switches, OS, VMs, TCP retransmission). Too short: false positives, premature failover, duplicated work, cascading overload. Too long: slow detection. Measure the response-time distribution and adapt timeouts to observed jitter (e.g. phi accrual detection).
- Variable delay comes from sharing resources (bursty, statistically multiplexed networks) — a trade-off for cost and utilization, unlike fixed-bandwidth circuits.

## 3. Unreliable clocks
- **Time-of-day clocks** (wall clock, NTP-synced) can jump backward or forward, drift, and be wrong by far more than you think (misconfigured NTP, leap seconds, VM pauses). **Never use them to measure elapsed time.**
- **Monotonic clocks** always go forward; use them for durations and timeouts. Their absolute value is meaningless and not comparable across machines.
- **Don't order events across nodes by timestamps.** With last-write-wins, a node with a fast clock can silently overwrite a later write from a node with a slow clock; causally later writes can be dropped. Use logical clocks (version numbers, Lamport timestamps, version vectors) for ordering.
- A timestamp has a confidence interval. Some systems expose it (e.g. Spanner's TrueTime waits out the uncertainty for snapshot isolation across datacenters) — most don't.
- Monitor clock offsets; treat a node with a badly drifting clock as dead.

## 4. Process pauses
A thread can be paused for a long time at any point: stop-the-world GC, VM suspension or live migration, OS context switches, swapping, disk I/O, SIGSTOP. Code can't assume elapsed time between two statements is short.
Classic bug: a node checks "my lease is still valid for 10 seconds", pauses for 15 seconds, then acts as leaseholder — while another node has taken over.

## 5. Truth, majorities, and fencing
- A node can't trust its own judgment of the situation; decisions must be made by a **quorum** (majority of nodes). A node declared dead by the majority must step down, even if it feels fine.
- **Fencing tokens:** every time a lock or lease is granted, the lock service issues a monotonically increasing token. The client sends the token with every write to the storage service, which rejects any token lower than the highest it has seen. This protects against paused or partitioned ex-leaseholders. A lock without fencing isn't safe for correctness.
- Consensus-based services (ZooKeeper's zxid or node version, etcd revision) can supply such tokens.

## 6. Byzantine faults and system models
- **Byzantine faults:** nodes lying (sending corrupt or malicious messages). Byzantine fault tolerance matters for aerospace and in peer-to-peer systems like blockchains, but usually not inside one organization's datacenter. Still, add basic protections: checksums, input validation, sanity checks, multiple NTP servers.
- **System models** used to reason about algorithms: timing (synchronous / **partially synchronous** / asynchronous) and failures (crash-stop / **crash-recovery** / Byzantine). Partially synchronous + crash-recovery is the realistic model.
- **Safety** properties (nothing bad happens — e.g. uniqueness) must always hold; **liveness** properties (something good eventually happens — e.g. availability) can have caveats.

## 7. Linearizability
- The strongest single-object consistency guarantee: the system behaves as if there's only one copy of the data and every operation takes effect atomically at some instant between its start and end. Once any read has seen a new value, all later reads must see it too (a **recency guarantee**).
- **Not the same as serializability** (which is about isolation of multi-object transactions). A system can have both ("strict serializability").
- **When you need it:** leader election and locks (all nodes must agree who holds it), uniqueness constraints (usernames, unique filenames, no double-selling of the last item), and cross-channel timing dependencies (e.g. a message queue notifies a worker to fetch a file that a lagging replica doesn't have yet).
- **Which systems give it:** single-leader replication *can* (if reads go to the leader or synchronously updated followers, and there's no split brain); consensus algorithms do; multi-leader doesn't; leaderless with quorums generally doesn't.
- **Cost (CAP):** in a network partition, a system must choose between being linearizable (some replicas become unavailable) and being available (non-linearizable). "CAP" is often misunderstood — it only covers partitions and one consistency model. The deeper reason systems drop linearizability is **performance**: linearizable operations are slow whenever network delay is high, even without partitions.

## 8. Ordering, causality, and total order broadcast
- **Causality** imposes a partial order (question before answer, row created before updated). Causal consistency is the strongest model that doesn't slow down under network delays and stays available during partitions.
- **Sequence numbers / Lamport timestamps** give a total order consistent with causality. But total order alone can't enforce uniqueness in real time: you only know you won once you've heard from every node about lower timestamps.
- **Total order broadcast** (atomic broadcast): all nodes deliver the same messages in the same order, reliably. This is exactly what database replication logs and Kafka-style logs provide per partition, and it's equivalent to consensus. With it you can build linearizable storage (e.g. claim a username by appending to the log and seeing whether your claim is the first one delivered).

## 9. Atomic commit and two-phase commit (2PC)
- Goal: a transaction across multiple nodes either commits everywhere or nowhere.
- **2PC:** a coordinator asks all participants to *prepare* (promise they can commit); if all say yes, it writes its decision to its log and tells everyone to commit. The commit point is the coordinator's decision.
- **Weakness:** if the coordinator crashes after participants prepared, they are **in doubt** and must hold locks until it recovers — blocking other transactions. Orphaned in-doubt transactions may need manual intervention.
- **Database-internal distributed transactions** (within one distributed database) can work well.
- **Heterogeneous transactions (XA)** across different technologies (e.g. a database and a message broker) are operationally painful: the coordinator becomes a single point of failure, it kills availability, and it lowers performance. Generally avoid; prefer log-based approaches (outbox, CDC, idempotent consumers).

## 10. Consensus and coordination services
- **Consensus:** nodes agree on a value, with uniform agreement, integrity, validity, and termination. Problems equivalent to consensus: linearizable compare-and-set, atomic commit, total order broadcast, locks and leases, membership, uniqueness constraints.
- Algorithms: Paxos, Raft, Zab, Viewstamped Replication. They need a **majority** to make progress; they elect leaders within an epoch (term) number and require a quorum vote for each decision.
- **Costs:** synchronous replication to a majority (slower); need a strict majority alive; mostly assume a fixed membership; sensitive to network problems (flapping leader elections).
- **Coordination services** (ZooKeeper, etcd, Consul) provide these primitives as a service: linearizable atomic operations, total ordering (usable as fencing tokens), failure detection via sessions/leases, and change notifications. Use them for leader election, locks, partition assignment, service discovery, and configuration — small, slow-changing data only.
- Most applications should use such a service (or the database's built-in mechanisms) rather than implement consensus.

## 11. Practical patterns
- **Idempotency keys:** clients generate a unique request ID; the server records processed IDs (in the same transaction as the effect) and ignores duplicates. Turns at-least-once delivery into exactly-once effect.
- **Fenced locks:** acquire lock → get token → include token in every write → storage rejects stale tokens.
- **Leader election:** via a coordination service or database with leases; the leader must stop acting when its lease can't be confirmed; protect side effects with fencing.
- **Timeouts and retries:** exponential backoff with jitter, retry budgets, circuit breakers; only retry idempotent operations or ones made idempotent.
- **Timestamps:** use monotonic clocks for durations; logical versions for ordering; wall-clock only for display and rough analytics.
- **Uniqueness across the system:** a unique constraint in a single database, a single-partition log processed sequentially, or a linearizable CAS in a coordination service.
