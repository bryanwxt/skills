# Partitioning (sharding)

## Contents
1. Goals
2. Partitioning key-value data
3. Skew and hot spots
4. Secondary indexes
5. Rebalancing
6. Request routing
7. What gets harder

---

## 1. Goals
Split data so each piece lives on one node (and is usually replicated), spreading data and query load evenly for scalability. Needed when data volume or write throughput exceeds a single node. Replication and partitioning are orthogonal: each partition is replicated; each node holds several partitions.

The enemy is **skew**: uneven partitions, and **hot spots** (one partition receiving disproportionate load).

## 2. Partitioning key-value data
**By key range** (continuous ranges of sorted keys; e.g. HBase, Bigtable, many NewSQL systems):
- Efficient range scans.
- Boundaries can adapt to the data distribution (split ranges as they grow).
- Risk: sequential keys like timestamps send all current writes to one partition. Fix by prefixing the key with something else (e.g. sensor ID, then time), at the cost of multi-query range scans.

**By hash of key** (e.g. Cassandra, DynamoDB, MongoDB hashed shard keys, Redis Cluster):
- Distributes keys evenly; kills sequential hot spots.
- Loses efficient range queries across keys.
- Use a stable hash (not a language's built-in hash, which may differ per process).
- **Compound keys** (Cassandra-style): hash the first part to choose the partition, keep the rest sorted within it. E.g. key `(user_id, timestamp)` → all of a user's items on one partition, range-scannable by time.

## 3. Skew and hot spots
Hashing doesn't help when one key is extremely hot (a celebrity's ID, a viral item). Mitigations:
- Add a random suffix (e.g. 2 digits → 100 sub-keys) to spread writes; reads must then query all sub-keys and combine. Only do this for known hot keys, and track which keys are split.
- Cache hot reads; batch or aggregate hot writes.
- Detect hot keys with per-key metrics.

## 4. Secondary indexes
Secondary indexes don't map neatly to partitions.

**Document-partitioned (local) indexes:** each partition indexes only its own data.
- Writes touch one partition.
- Reads by secondary attribute must query **all** partitions (scatter/gather) — tail latency amplification.
- Used by MongoDB, Cassandra, Elasticsearch, and others.

**Term-partitioned (global) indexes:** the index itself is partitioned by the indexed term (by range or hash).
- Reads hit only the relevant index partition.
- Writes may touch several partitions; global index updates are usually **asynchronous**, so the index may lag the data.
- Used by DynamoDB global secondary indexes and others.

Choose by the read/write mix and whether index lag is acceptable.

## 5. Rebalancing
Moving load when nodes are added or removed. Requirements: fair load afterwards, keep serving during the move, move no more data than necessary.

- **Don't use hash mod N**: changing N moves almost every key.
- **Fixed number of partitions:** create many more partitions than nodes (e.g. 1,000 on 10 nodes); new nodes steal whole partitions. Simple; but the partition count must be chosen up front — too few limits growth, too many adds overhead.
- **Dynamic partitioning:** split partitions that grow past a size threshold, merge small ones (natural for key ranges; can pre-split an empty database).
- **Partitioning proportional to nodes:** fixed number of partitions per node (e.g. Cassandra vnodes).
- **Automatic vs manual:** fully automatic rebalancing is convenient but dangerous combined with automatic failure detection — an overloaded node can be declared dead, triggering a rebalance that adds more load, cascading. Keeping a human in the loop for rebalancing is often wiser.

## 6. Request routing
How does a client find the right node? Options: any node forwards; a routing tier; or partition-aware clients. All need an authoritative, up-to-date mapping of partitions to nodes — typically in a coordination service (ZooKeeper, etcd) or via gossip, which is weaker. Stale routing sends requests to the wrong node; the system must detect and redirect.

## 7. What gets harder
- Queries across partitions (scatter/gather, parallel execution in analytic engines).
- Transactions across partitions (need distributed commit — see distributed.md).
- Uniqueness and other constraints across partitions.
- Ordering across partitions (only per-partition order is cheap).
- Choose the partition key so the most important queries and transactions stay within one partition.
