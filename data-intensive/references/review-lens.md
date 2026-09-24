# Data review lens (append to `PLAN_OR_REQUIREMENTS` for the final whole-branch review or a standalone requesting-code-review, only when the diff touches data; never to per-task reviews)

Also review the change for data correctness, based on *Designing Data-Intensive Applications*. For each finding give file:line, the concrete event sequence that goes wrong (two requests, a crash, a retry, a failover), how likely it is, and the fix.

**Critical: data loss, corruption, broken invariants**
- Read-modify-write of shared data without an atomic update, compare-and-set, `SELECT … FOR UPDATE`, or serializable isolation (lost updates).
- Check-then-act (availability, uniqueness, balance) without a constraint, lock on the checked rows, or serializable isolation (write skew or phantoms).
- Writes to two systems from application code (database plus cache, search, or queue) without an outbox or CDC (divergence on partial failure). This includes external side effects tied to a commit (notification, email, webhook) whose delivery semantics aren't stated.
- Retried writes or at-least-once consumers without an idempotency key enforced at the final store (duplicates).
- Schema or message changes that old readers or writers can't handle; round-trips that drop unknown fields; destructive migrations without expand → migrate → contract.

**Important: breaks under load or failure**
- Assumed isolation level not stated, or wrong for this database.
- Ordering or last-write-wins by wall-clock timestamps across nodes.
- Locks or leases without fencing tokens; lease checks that a GC pause can invalidate.
- Timeouts treated as certain failure; retries without backoff or limits.
- Reads after writes going to replicas without a read-your-writes strategy.
- Hot keys or unbounded partitions; queries that scan all partitions on a hot path.
- Transactions held open across network calls or user interaction.

**Minor**
- Missing indexes for new query patterns; secondary-index write cost ignored.
- Missing metrics for replication lag, consumer lag, or retry rates.
