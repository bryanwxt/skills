# Replication

## Contents
1. Why replicate
2. Single-leader replication
3. Replication lag anomalies and fixes
4. Multi-leader replication
5. Leaderless replication and quorums
6. Concurrent writes and conflict resolution

---

## 1. Why replicate
Keeping copies of the same data on several machines to: keep data close to users (lower latency), keep working if parts fail (availability), and scale out reads. The hard part is handling **changes** to replicated data.

## 2. Single-leader replication
One replica (leader) accepts writes and sends a replication log to followers; reads can go to any replica. Used by most relational databases and many others (Kafka partitions, for example).

**Synchronous vs asynchronous:**
- Synchronous: the leader waits for the follower before confirming. The follower is guaranteed up to date, but one slow or dead follower blocks writes. In practice, "semi-synchronous": one synchronous follower, the rest async.
- Asynchronous: fast and available, but a write confirmed to the client **can be lost** if the leader fails before replicating it. Durability is weakened; know whether your system does this.

**Adding followers:** take a consistent snapshot, copy it, then catch up from the log position the snapshot corresponds to.

**Follower failure:** catch-up recovery from the log.

**Leader failure (failover)** — detect (usually a timeout), choose a new leader (usually the most up-to-date replica), reconfigure clients and replicas. Things that go wrong:
- With async replication, the new leader may lack writes the old one accepted. They're usually discarded — dangerous if other systems saw them (e.g. reused auto-increment IDs that were already used as keys in a cache or another system).
- **Split brain:** two nodes both believe they're the leader and accept writes. Needs fencing (shutting one down, or fencing tokens).
- Choosing the timeout: too short → unnecessary failovers under load spikes (making things worse); too long → longer outage.

**Replication log implementations:**
- *Statement-based* (replicate SQL statements): breaks with nondeterministic functions (`NOW()`, `RAND()`), autoincrement, and side effects.
- *WAL shipping* (replicate storage-engine bytes): tightly coupled to storage format, so leader and followers usually need the same version — makes zero-downtime upgrades hard.
- *Logical (row-based) log:* describes row-level changes independently of storage format. Allows version differences and is what **change data capture** consumes.
- *Trigger-based:* application-level replication via triggers; flexible but higher overhead and more bug-prone.

## 3. Replication lag anomalies and fixes
With async followers, reads from followers are **eventually consistent**: they lag, sometimes by seconds or minutes under load. Three anomalies and their fixes:

| Anomaly | Symptom | Guarantee needed | How to provide it |
|---|---|---|---|
| Reading your own writes | User submits something, reloads, it's gone | **Read-after-write consistency** | Read things the user may have modified from the leader (e.g. own profile); or for a period after a write, read from the leader; or track the write's log position/timestamp and read only from replicas that have caught up to it. Cross-device needs the metadata stored centrally. |
| Moving backward in time | User sees a comment, refreshes, it's gone (hit a more-lagged replica) | **Monotonic reads** | Route each user's reads to the same replica (e.g. hash of user ID), with rerouting on failure. |
| Causality violation | Observer sees an answer before the question | **Consistent prefix reads** | Write causally related data to the same partition, or track causal dependencies. Mainly a problem with partitioned data. |

Design question to ask always: "What happens if replication lag grows to several minutes?" If the answer is a bad user experience, you need a stronger guarantee — don't pretend replication is synchronous. Transactions exist so applications don't have to solve this piecemeal.

## 4. Multi-leader replication
Several nodes accept writes, replicating to each other.

**Use cases:** multiple datacenters (each has a leader; better latency and tolerance of datacenter outages and network problems); offline clients (each device's local database is a leader — e.g. calendar apps); real-time collaborative editing.

**The big problem is write conflicts.** Two leaders accept conflicting writes concurrently; detection happens later, asynchronously.
- **Avoid conflicts:** route all writes for a given record through the same leader (e.g. user's home datacenter). Breaks down when that routing changes.
- **Converge:** every replica must end in the same state.
  - Last write wins (LWW) by timestamp or ID — simple but **silently loses data**.
  - Replica with higher ID wins — also loses data.
  - Merge values (e.g. concatenate, union).
  - Record the conflict and resolve later (in application code or by the user).
- **Custom resolution** on write (handler runs when conflict is detected) or on read (all versions returned to the application).
- **Automatic resolution:** CRDTs (data types that merge automatically — counters, sets, maps, text), mergeable persistent data structures, operational transformation (collaborative editors).
- Conflicts can be subtle — e.g. two bookings for the same room made on different leaders don't touch the same record, but still violate an invariant.

**Topologies:** circular and star topologies fail if one node fails; all-to-all is more robust but messages can arrive out of order (an update before the insert it depends on), requiring version vectors.

Multi-leader is often retrofitted and full of pitfalls (autoincrement keys, triggers, integrity constraints). Avoid it if you can.

## 5. Leaderless replication (Dynamo-style: Cassandra, Riak, ScyllaDB, DynamoDB internals)
Clients (or a coordinator) send writes to several replicas and read from several in parallel.

- **Catching up stale replicas:** read repair (on read, write back the newer value to stale replicas) and anti-entropy (background process comparing replicas). Without anti-entropy, rarely read values may stay stale.
- **Quorums:** with n replicas, writes confirmed by w, reads from r. If **w + r > n**, a read overlaps at least one up-to-date replica. Typical: n = 3, w = r = 2. Tolerates n − w unavailable nodes for writes, n − r for reads.
- **Limits of quorums** — even with w + r > n, stale reads can happen:
  - sloppy quorums (writes land on nodes outside the usual n),
  - concurrent writes resolved by LWW (clock skew loses writes),
  - a write concurrent with a read,
  - a write that succeeded on fewer than w nodes isn't rolled back where it did succeed,
  - a node carrying a new value fails and is restored from a replica with an old value.
  So quorums are **not linearizable**. Treat them as tuning knobs for probability of staleness, not guarantees. Monitor staleness.
- **Sloppy quorums and hinted handoff:** during a partition, accept writes on reachable nodes not among the key's home n, and forward them later. Increases write availability but a read of w + r nodes may miss the latest value.
- Multi-datacenter: n spans datacenters; confirm writes locally, replicate across asynchronously.

## 6. Concurrent writes and conflict resolution
- Two operations are **concurrent** if neither knows about the other (neither "happened before" the other). Concurrency is about causality, not wall-clock time.
- **Last write wins** resolves conflicts by discarding all but the "latest" — durability is sacrificed; even non-concurrent writes can be lost with clock skew. Safe only if each key is written once and then immutable (e.g. keyed by UUID).
- **Version numbers per key** let the database detect concurrency: the server keeps sibling values for concurrent writes; the client merges them on the next write (unions work for adds; removals need **tombstones**).
- With multiple replicas, use a **version vector** (one counter per replica per key) to tell overwrite from concurrent write.
