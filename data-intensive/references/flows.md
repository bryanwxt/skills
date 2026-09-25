# Flows A and B (data-intensive)

## Flow A: technology choice
Use this for "Postgres or DynamoDB?", "Kafka or SQS?", "Avro or Protobuf?", and similar. Announce the path first:
- **Quick:** reversible and low-stakes. Answer in chat: recommendation, trade-off, when to revisit.
- **Decision:** hard to reverse.
- **Spike:** a measurement decides it. Propose a throwaway benchmark in 2–3 sentences, get a nod, run it cheaply, then continue on the decision path.

The decision path follows the standalone flow in `references/standalone.md` (shared by all lenses; if you've already read any lens's copy this session, use that one):
1. **Questions** from `references/question-bank.md` §2: access patterns, non-negotiable guarantees, operational model, existing stack, horizon.
2. **Compare categories before products** (`references/decision-guides.md`). Keep 2–3 options, recommendation first.
3. **Check product facts** in current docs, and cite them with dates.
4. **Write the record** with `assets/decision-record-template.md` to `docs/superpowers/decisions/`. It covers:
   - fit to the workload;
   - failure behaviour of each option;
   - operational cost;
   - exit cost;
   - "revisit when".

   Adoption is handed to brainstorming.

## Flow B: data architecture or incident review
Use this for "review our data flow", "what could go wrong with this pipeline", and post-incident analysis. A live incident goes to `superpowers:systematic-debugging` instead. Choose a path: **targeted** (one flow or incident) or **full**. Then follow the standalone flow in `references/standalone.md`:
1. **Questions** from `references/question-bank.md` §3.
2. **Map** components, the system of record for each entity, dataflows with the guarantee each link actually provides, the isolation level (read from config), replication, and partitioning. Add a timeline for incidents.
3. **Walk it** with `references/review-checklist.md`, by blast radius: loss and corruption → correctness anomalies → availability → performance → operability. Look hardest for:
   - dual writes and side effects in the write path;
   - check-then-act races;
   - ordering by wall clock;
   - missing idempotency;
   - locks without fencing;
   - assumed isolation levels.
4. **Severity:**
   - Critical: loss, silent corruption, broken invariants.
   - Important: problems that show up under load or failure.
   - Minor: everything else.

   Every data finding is written as an event sequence.
5. **Write** with `assets/review-template.md` to `docs/superpowers/reviews/YYYY-MM-DD-<topic>-data-review.md`. Hand each fix off to brainstorming.
