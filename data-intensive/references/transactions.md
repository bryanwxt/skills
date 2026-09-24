# Transactions and isolation

## Contents
1. What transactions give you
2. ACID, precisely
3. Single-object vs multi-object
4. The anomaly catalogue
5. Isolation levels and what they prevent
6. Preventing lost updates
7. Preventing write skew and phantoms
8. Serializability implementations
9. Practical guidance and code patterns

---

## 1. What transactions give you
A transaction groups reads and writes into one logical unit: it either commits entirely or aborts entirely, and it's isolated from concurrent transactions to some degree. It lets the application ignore many failure and concurrency cases. Not every system needs them, but removing them pushes the problems into application code, where they're usually handled worse.

## 2. ACID, precisely
- **Atomicity:** abortability. On error, all of the transaction's writes are discarded, so it's safe to retry. (Nothing to do with concurrency.)
- **Consistency:** the application's invariants hold. This is really a property of the application — the database only enforces the constraints you declare.
- **Isolation:** concurrent transactions don't interfere. The ideal is serializability (as if they ran one at a time); most databases default to something weaker.
- **Durability:** committed data isn't lost — written to disk/WAL and/or replicated. No guarantee is absolute (correlated failures, disks lying about fsync, bugs); backups still matter.
"ACID-compliant" is marketing unless you know which isolation level is used.

## 3. Single-object vs multi-object
- Storage engines almost always make single-object writes atomic and isolated (WAL, per-object locks), and many offer atomic increments and compare-and-set. These are useful but not "transactions" in the full sense.
- Multi-object transactions are needed for foreign keys, denormalized data kept in sync, and secondary indexes.
- **Retrying aborted transactions** is the point of aborts, but beware: the transaction may have committed and only the acknowledgement was lost (retry = duplicate, unless idempotent); retrying on overload makes it worse (use backoff and limits); retry only transient errors; side effects outside the database (e.g. sending email) may repeat.

## 4. The anomaly catalogue
| Anomaly | What happens | Example |
|---|---|---|
| **Dirty read** | T reads another transaction's uncommitted write | Sees a half-done transfer; sees data that's later rolled back |
| **Dirty write** | T overwrites another's uncommitted write | Car sale: buyer from one txn, invoice from another |
| **Read skew (non-repeatable read)** | T's reads come from inconsistent moments — some before another txn committed, some after | Two account balances read before and after a transfer — money appears to vanish. Breaks backups and analytic queries. |
| **Lost update** | Two read-modify-write cycles; one overwrites the other | Two increments of a counter yield +1; two users edit the same doc |
| **Write skew** | Two txns read the same data, each writes a *different* object based on it; together they break an invariant | Two doctors both go off call because each saw the other on call; double booking of a room; two users claim the same username |
| **Phantom** | A write in one txn changes the result of a search query in another | The "is anyone booked in this slot?" check — the row that would conflict doesn't exist yet, so there's nothing to lock |

## 5. Isolation levels
| Level | Prevents | Still allows | Typical implementation |
|---|---|---|---|
| Read uncommitted | dirty writes | dirty reads and everything else | row write locks |
| **Read committed** | dirty reads, dirty writes | read skew, lost updates, write skew, phantoms | row write locks; readers see last committed value |
| **Snapshot isolation** (often called "repeatable read") | + read skew | lost updates (in some products), write skew, phantoms affecting writes | MVCC: each txn reads a consistent snapshot; "readers never block writers" |
| **Serializable** | all of the above | — | serial execution, 2PL, or SSI |

Caveats:
- Level names are inconsistent between products. "Repeatable read" in one product may be snapshot isolation; in another it's something else. "Serializable" in some older products was actually snapshot isolation. **Check the specific product's documentation** for what anomalies its levels prevent.
- Defaults are often read committed. Snapshot isolation is great for long read-only queries (backups, analytics).

## 6. Preventing lost updates
In order of preference:
1. **Atomic write operations:** `UPDATE counters SET value = value + 1 WHERE key = ?`. Document databases and Redis offer similar atomic ops. Beware ORMs that generate read-modify-write code instead.
2. **Explicit locking:** `SELECT … FOR UPDATE` on the rows you'll modify, then update. Easy to forget a lock somewhere.
3. **Automatic detection:** some databases detect lost updates under snapshot isolation and abort one transaction (e.g. PostgreSQL's repeatable read); others don't (e.g. MySQL/InnoDB repeatable read). Check your product.
4. **Compare-and-set:** `UPDATE … SET content = 'new' WHERE id = ? AND content = 'old'` (or a version column), then check the affected row count. Be careful if the WHERE reads from an old snapshot.
5. **Replicated/multi-leader data:** locks and CAS don't work across async replicas; use commutative operations, conflict detection with siblings, or CRDTs. LWW loses updates.

## 7. Preventing write skew and phantoms
Write skew needs more than row locks, because the transactions write different rows.
- **Serializable isolation** — the most robust fix.
- **Constraints** where possible: unique constraints, exclusion constraints (e.g. no overlapping time ranges), foreign keys. Multi-object constraints generally need triggers or materialized views.
- **Lock the rows the decision depends on:** `SELECT … FOR UPDATE` on the rows that the check reads (e.g. all doctors on call for this shift).
- **Phantoms** (the check is about rows that don't exist yet): there's nothing to lock. Options: serializable isolation, or **materialize conflicts** — create a table of lockable rows (e.g. one row per room per time slot) and lock those. Materializing conflicts is ugly and a last resort.

Pattern to recognize write skew: (1) a SELECT checks a condition, (2) the application decides based on it, (3) it writes — and the write changes the result of the step-1 check. If another transaction can do the same concurrently, you have write skew.

## 8. Serializability implementations
- **Actual serial execution** (e.g. VoltDB, Redis, Datomic-style): one thread executes transactions one at a time. Works if every transaction is small and fast, the active dataset fits in memory, and transactions are submitted as stored procedures (no interactive round trips). Write throughput is limited to one CPU core per partition; cross-partition transactions are much slower.
- **Two-phase locking (2PL):** readers and writers block each other (shared/exclusive locks held until commit); predicate or index-range locks prevent phantoms. Correct but slower and with unstable latency and deadlocks (the database detects and aborts one).
- **Serializable snapshot isolation (SSI)** (e.g. PostgreSQL serializable, CockroachDB, FoundationDB): optimistic — transactions run on a snapshot and at commit the database checks whether any read premise has been invalidated by a concurrent write; if so, abort. Good performance when contention is low; the application must retry aborted transactions. Keep transactions short.

## 9. Practical guidance and code patterns
- **Know your isolation level.** Many bugs come from assuming serializable while running read committed.
- **Keep transactions short** and avoid user interaction inside them.
- **Every read-modify-write in application code is suspect.** Replace with an atomic update, a CAS, a lock, or serializable isolation.
- **Every check-then-act** (check availability, then book; check username free, then insert) is a write-skew or phantom risk. Use a unique constraint, exclusion constraint, row lock on the checked rows, materialized conflict, or serializable isolation.
- **Retry loop** for serializable/SSI: catch serialization failures (e.g. SQLSTATE 40001) and deadlocks, retry with backoff and a limit, and make the transaction body safe to rerun (no external side effects inside).
- **Operations across services or databases** can't be covered by a single database transaction; use the patterns in distributed.md and derived-data.md (outbox/CDC, idempotency keys, sagas with compensation).
- **Testing:** reproduce races with two connections and explicit interleaving (open txn A, read; open txn B, read; A writes and commits; B writes and commits), and assert the invariant.

Example — prevent double booking with an exclusion constraint (PostgreSQL):
```sql
CREATE EXTENSION IF NOT EXISTS btree_gist;
ALTER TABLE bookings ADD CONSTRAINT no_overlap
  EXCLUDE USING gist (room_id WITH =, tsrange(start_at, end_at) WITH &&);
```

Example — safe counter decrement with a guard:
```sql
UPDATE inventory SET qty = qty - 1 WHERE sku = $1 AND qty > 0;
-- check affected row count: 0 means out of stock
```
