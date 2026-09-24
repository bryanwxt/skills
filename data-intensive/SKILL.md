---
name: data-intensive
description: Data-systems lens for superpowers workflows, based on Martin Kleppmann's "Designing Data-Intensive Applications" — data models and stores, storage engines, encoding and schema evolution, replication, partitioning, transactions and isolation, distributed failures, clocks, consensus, batch/stream pipelines, CDC, and end-to-end correctness. Use when work involves data guarantees, scale, or concurrency. That covers: designing a data architecture from scratch (through superpowers:brainstorming), choosing a database, queue, or data format, reviewing a data architecture or incident, and supplying data concerns inside superpowers' planning, TDD, debugging, and code-review steps. Don't use for ordinary CRUD with no scale, concurrency, or consistency concern.
---

# Data-Intensive (superpowers lens)

This skill adds a data-systems lens to superpowers: what guarantees each component gives, what they cost, and what happens when things fail. Superpowers owns the process for building software. This skill owns the judgment about data, and runs two flows of its own, choosing technology and reviewing data architecture, using the same discipline as brainstorming.

## What it handles

| Flow | How it runs | Details |
|---|---|---|
| **1. Design a data architecture from scratch** | Through `superpowers:brainstorming`'s architectural path, with this skill's **data track** layered in: extra questions, approach comparison, spec sections, failure analysis, self-review | §1, hooks §1 |
| **2. Choose a technology** (database, queue, format, engine) | This skill runs it, **brainstorming-style**: classify, discover intent, write back, compare options, present, decision record, self-review, user review gate, hand-off | §2 |
| **3. Review a data architecture or an incident** | This skill runs it, **brainstorming-style**, ending with fixes handed to brainstorming | §3 |
| **4. Data concerns inside other superpowers steps** | Hooks into bounded brainstorming, writing-plans, TDD, execution, verification, code review, systematic-debugging | `references/superpowers-hooks.md` |

**Lanes with other skills:**
- **`data-intensive`** decides which store owns each piece of data, which guarantee each operation needs, how data flows between stores, how it's replicated, partitioned, and evolved, and what happens on failure.
- **`software-design`** decides how code is split into modules and what each one hides. For example, the repository module hides which store and isolation level are used.
- **`clean-python`** decides how it's written in Python, for example the transaction retry loop, session handling, or an idempotency-key check.
- For a data-heavy Python feature, use all three. Each adds its own sections to one brainstorming spec, never separate documents.

## Quick rule for small and trivial changes

For a bounded or trivial change, don't open the reference files. Add the `data …` part of the one-line lens check only when the change touches data:
- an unprotected read-modify-write or check-then-act;
- a dual write, or side-effect semantics not stated;
- an incompatible schema or message change;
- a retry without idempotency.

Otherwise stay silent. List pre-existing problems as follow-ups.

## Ground rules (every flow)

1. **Start from the workload.** Get or estimate the load parameters that matter:
   - reads and writes per second, and the read/write ratio;
   - data size and growth;
   - fan-out and hot keys;
   - latency targets at p50, p99, and p999;
   - how bad each kind of failure would be.

   No numbers, no scaling advice. If the user can't give numbers, state assumptions.
2. **Name the guarantee.** Never say "consistent" or "safe" loosely. Say which: linearizable, serializable, snapshot isolation, read committed, read-your-writes, monotonic reads, consistent prefix, causal, or eventual.
3. **Walk the failure.** Take each component through a crash, slowness, a network partition, a restart with stale state, a clock jump, and a retry. Write out the event sequence.
4. **Prefer simple.** One well-run relational database with replicas covers a lot. Recommend distribution only when a named load parameter demands it.
5. **Be concrete.** Give schemas, keys, SQL, partition keys, message formats, and failure sequences.
6. **Name the trade-off.** Say what each choice gives up, and when the user would regret it.
7. **Check product facts.** The book dates from 2017. When a recommendation depends on what a specific product does today, check its current documentation, cite it, and date the check. This is `superpowers:verification-before-completion` applied to claims about products.

## Brainstorming's discipline, reused here

Flows 2 and 3 borrow brainstorming's elements so they feel the same as the rest of superpowers:
- **Classify and announce the path** before the first question, so the user can override it. Take the heavier path when in doubt. If hidden complexity appears, step up; never step down mid-task.
- **Discover intent:** ask **one question per message**, multiple choice where possible. Put a recommended option first only for *choices*. For *facts* about the user's world, offer ranges plus "Not sure — assume X" with no recommendation. Use `references/question-bank.md`. Skip anything the request already answers.
- **Write back your understanding:** outcome, constraints, success criteria. Separate what the user said from what you assumed. A default the user accepted counts as assumed. Invite correction.
- **Propose 2–3 options** with trade-offs, leading with your recommendation.
- **Write the document directly** after the write-back. Don't present sections for approval first; the document's review gate is the only content gate. In chat, give a short summary, not the full content.
- **Self-review**: placeholders, contradictions, ambiguity, scope, plus this skill's own checks (named guarantees, failure walk, product facts sourced). Never tick an item you haven't verified; list it under "Not verified" instead.
- **User review gate:** ask the user to review the written document before any hand-off.
- **Hand off**, never implement: adoption or fixes go to `superpowers:brainstorming`, then `writing-plans`.

Documents go under `docs/superpowers/` next to brainstorming's specs (user preferences override):
- decisions: `docs/superpowers/decisions/YYYY-MM-DD-<topic>.md`
- reviews: `docs/superpowers/reviews/YYYY-MM-DD-<topic>-data-review.md`

Commit them, as brainstorming does with specs.

## 1. Design a data architecture from scratch

This is `superpowers:brainstorming`'s architectural path. Brainstorming leads: its questions, approval gates, spec location, and hand-off to `writing-plans`. This skill layers in a **data track** (details in `references/superpowers-hooks.md` §1):
- **Questions** (from `references/question-bank.md` §1, asked in brainstorming's queue, one per message):
  - load parameters;
  - operations needing strong guarantees (money, inventory, uniqueness) vs those that can lag;
  - the source of truth for each entity;
  - freshness needs for derived data;
  - growth horizon;
  - the operational constraints the team has to live with.
- **Approaches:** 2–3 data architectures that differ in substance, not in brand. For example: a single relational store plus replicas; a relational store plus a log feeding derived stores through CDC; a partitioned store sharded by tenant. Compare them on guarantees, scaling headroom, operational cost, and failure behaviour.
- **Spec:** add the sections from `assets/spec-sections.md` to brainstorming's spec:
  - load and targets;
  - guarantees required;
  - systems of record and derived data;
  - data model;
  - replication and partitioning;
  - correctness mechanisms;
  - encoding and evolution;
  - failure analysis;
  - operations.
- **Self-review:** add the data checks from the hooks file to brainstorming's spec self-review.
- **Design only?** If the user wants the architecture but not the implementation yet, stop once the spec is approved, and tell them `writing-plans` is the next step when they're ready. Brainstorming's gates still apply up to that point.

## 2. Choose a technology

For "Postgres or DynamoDB?", "Kafka or SQS?", "Avro or Protobuf?", "do we need a separate search index?", and similar questions.

**Classify and announce** one path:
- **Quick:** a low-stakes, reversible choice where the workload is clear. Answer in chat, recommendation first, with the trade-off and when you'd revisit it. No document.
- **Decision:** a hard-to-reverse or high-stakes choice. Run the full process below and write a decision record.
- **Spike:** the choice hinges on an unknown that only a measurement settles, such as tail latency under your write pattern or behaviour under failover. Present the question and a throwaway benchmark or experiment in 2–3 sentences, get a nod, run it as cheaply as correctness allows, then continue on the decision path with the results. Label anything built as throwaway.

**Decision path:**
1. **Discover intent**, one question per message (`references/question-bank.md` §2). Cover the workload and access patterns, the non-negotiable guarantees, operational constraints (managed vs self-hosted, team skills, cloud, budget), the time horizon, and what's already in use.
2. **Write back your understanding.** Separate what the user said from your assumptions, and invite correction.
3. **Compare categories before products** (`references/decision-guides.md`), for example log-based vs traditional broker before Kafka vs Kinesis. Keep 2–3 real options and lead with your recommendation.
4. **Check product facts** in current docs, with dated citations (ground rule 7).
5. **Write the decision record directly** with `assets/decision-record-template.md` and commit it. Cover:
   - how each option fits the workload;
   - how each behaves under the named failures;
   - operational cost;
   - migration and exit cost.

   No section-by-section approvals. In chat, give the recommendation and a short summary.
6. **Self-review** (never tick an unverified item):
   - brainstorming's placeholder, contradiction, ambiguity, and scope checks;
   - guarantees named precisely;
   - failure behaviour covered for each option;
   - product facts cited and dated;
   - a "revisit when" condition stated.
7. **User review gate.** Ask the user to review the record.
8. **Hand off.** Adopting the choice is a new `superpowers:brainstorming` request, usually architectural when it replaces an existing store.

## 3. Review a data architecture or an incident

For "review our data architecture", "what could go wrong with this pipeline?", "why did we lose writes last week?", and design-doc reviews. For a **live** incident, `superpowers:systematic-debugging` leads (hooks §7). This flow is for reviews and post-incident analysis. If the request also covers module structure or Python code, run one joint review instead (see "Standalone reviews" in the coordination section of `references/superpowers-hooks.md`).

**Classify and announce** one path:
- **Targeted:** one component, flow, or incident. Go deep, with a short report.
- **Full:** the whole data architecture. Map everything, then prioritise.

**Process:**
1. **Discover intent**, one question per message (`references/question-bank.md` §3):
   - what prompted the review;
   - which flows matter most;
   - known incidents;
   - the guarantees the business assumes;
   - what can change.
2. **Write back your understanding**, including which guarantees you'll check against.
3. **Map the system:**
   - components and stores;
   - the system of record for each entity;
   - dataflows, and the guarantee each link provides;
   - replication and partitioning.

   A Mermaid diagram is fine. For an incident, add a timeline.
4. **Walk it** with `references/review-checklist.md`. Prioritise by blast radius: data loss and silent corruption first, then correctness anomalies, availability, performance, and operability. For each finding, write the concrete event sequence that goes wrong, how likely and how bad it is, and the fix with its trade-off.
5. **Look hardest for** dual writes, check-then-act races, ordering by wall clock, missing idempotency, locks without fencing, and assumptions about isolation levels.
6. **Rate each finding** with superpowers' severities:
   - **Critical:** data loss, silent corruption, broken invariants.
   - **Important:** correctness or availability problems that will surface under load or failure.
   - **Minor:** everything else.

   A side effect in the write path (notification, email, webhook) is its own finding, written as an event sequence.
7. **Write the review directly** with `assets/review-template.md`, findings sorted by severity, and commit it. No findings-by-section approvals. In chat, give a short summary: counts per severity and the top 3.
8. **Self-review** (never tick an unverified item):
   - every finding cites evidence you actually read or ran;
   - every failure is written as an event sequence;
   - guarantees are named;
   - product facts are fetched and dated, or listed as not verified;
   - unverified areas are listed.
9. **User review gate.**
10. **Hand off.** Each fix the user wants becomes its own `superpowers:brainstorming` request, which decides bounded vs architectural.

## Reference files

- `references/superpowers-hooks.md`: the data track for brainstorming, and additions to writing-plans, TDD, execution, verification, code review, and debugging. **Read it whenever this skill is active inside a superpowers step.**
- `references/question-bank.md`: questions with recommended defaults for flows 1–3.
- `references/foundations.md`: reliability, scalability, and maintainability; load and percentiles; data models; storage engines; OLTP vs OLAP.
- `references/encoding-evolution.md`: formats, schema evolution, compatibility.
- `references/replication.md`: single-leader, multi-leader, leaderless; replication-lag anomalies; conflicts; quorums.
- `references/partitioning.md`: key-range vs hash partitioning, hot spots, secondary indexes, rebalancing, routing.
- `references/transactions.md`: isolation levels, the anomaly catalogue, and how to prevent each anomaly in code.
- `references/distributed.md`: partial failure, timeouts, clocks, fencing, linearizability, 2PC, consensus, practical patterns.
- `references/derived-data.md`: batch, stream, CDC, event sourcing, exactly-once, unbundled databases, end-to-end correctness.
- `references/decision-guides.md`: trade-off tables for common choices.
- `references/review-checklist.md`: review questions and a symptom → cause → fix table for incidents.
- `references/review-lens.md`: a short checklist for the superpowers code reviewer, used only when a change touches data.
- `assets/spec-sections.md`, `assets/decision-record-template.md`, `assets/review-template.md`: output formats.
- `README.md`: the human-facing guide to this skill with superpowers, `software-design`, and `clean-python`.

## Credit

Condensed and paraphrased from Martin Kleppmann, *Designing Data-Intensive Applications* (O'Reilly, 1st ed., 2017). Superpowers is by Jesse Vincent (MIT), included in this repo as a reference at `vendor/superpowers`.
