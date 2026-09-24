# Question bank

Ask **one question per message**, multiple choice where possible, with the **recommended option first** and its reason, as brainstorming does. Derive the options and the recommendation from the user's context first, and fall back to the defaults here. Skip anything already answered. Each option must lead to a different design.

## Contents
- §1 Data track for brainstorming (design from scratch)
- §2 Technology choice
- §3 Data architecture or incident review

---

## §1 Data track for brainstorming

Add these to brainstorming's queue, in this order.

**1.1 What's the expected load?**
- a) (Rec. when unclear) Modest: under ~1k requests/s, tens of GB, growing slowly. *Why:* most systems start here, and a single relational database with replicas fits. *If different:* higher numbers bring in partitioning, caching, or specialised stores.
- b) High read volume, moderate writes (feeds, catalogues).
- c) High write volume (events, telemetry, logs).
- d) Unknown. *I'll state assumptions and design for 10× headroom.*

**1.2 Which operations need strong guarantees?** (multi-select)
- a) (Rec. from context) Money or balances (serializable or atomic updates; exactly-once effect).
- b) Inventory, bookings, quotas (no overselling; constraints).
- c) Uniqueness (usernames, IDs, one active X per Y).
- d) None: everything can be eventually consistent.

**1.3 Where should the source of truth for <entity> live?**
- a) (Rec.) One relational database; everything else is derived from it.
- b) An event log (event sourcing); state is derived.
- c) An external system we don't own; we keep a synced copy.

**1.4 How fresh must derived data be (search, caches, analytics)?**
- a) (Rec.) Seconds to minutes: fed by CDC from the source.
- b) Immediately, read-your-writes: read from the source, or wait for the write's log position.
- c) Hours: a batch rebuild is fine.

**1.5 What growth horizon should the design handle without re-architecture?**
- a) (Rec.) 10× current load over 2 years.
- b) 100× (partitioning must be designed in now).
- c) Just current needs; re-architect later if it takes off.

**1.6 What operational constraints apply?**
- a) (Rec. for small teams) Managed services only, one cloud.
- b) Self-hosted is fine; the team has operations experience.
- c) Must run on-premises or on specific infrastructure.

**1.7 What happens if data is lost or wrong?** (sets the synchronous-replication, backup, and audit bar)
- a) Unacceptable: financial or legal records.
- b) Costly but recoverable from other sources.
- c) Tolerable: can be recomputed.

## §2 Technology choice

**2.1 Which path fits?** (announce your classification; the user can override)
- a) (Rec. if hard to reverse) Decision: full comparison plus a decision record.
- b) Quick: an answer in chat.
- c) Spike first: benchmark or experiment, then decide.

**2.2 What will it store or carry, and how is it accessed?** Offer options drafted from context, e.g. key lookups / relational queries with joins / full-text search / append-only events / analytical scans.

**2.3 Which guarantees are non-negotiable?** (multi-select) transactions across rows / ordering per key / durability of acknowledged writes / exactly-once effect / low tail latency (give the target).

**2.4 Operational model?**
- a) (Rec. for small teams) Fully managed.
- b) Self-hosted.
- c) Whatever the platform team already runs.

**2.5 What's already in use that this must fit with?** (options from context: existing database, broker, cloud, language drivers)

**2.6 How long must this choice last, and how costly is it to exit?**
- a) (Rec.) Years; plan an exit path anyway.
- b) Short-lived or experimental.

## §3 Data architecture or incident review

**3.1 What prompted the review?**
- a) (Rec. if unknown) General health check before growth.
- b) A specific incident (give the date and symptoms).
- c) A planned change (migration, new consumer, scale-up).
- d) Performance or cost problems.

**3.2 Targeted or full?**
- a) (Rec. when there's a trigger) Targeted: the component, flow, or incident in question.
- b) Full: the whole data architecture.

**3.3 Which flows matter most?** (multi-select, drafted from context: payments, orders, user data, analytics, search, notifications)

**3.4 Which guarantees does the business assume?** (e.g. no lost orders, no duplicate charges, users see their own changes, reports match the ledger)

**3.5 What can change?**
- a) (Rec.) Targeted fixes within the current stack.
- b) Component replacement is on the table.
- c) Only configuration and operations.
