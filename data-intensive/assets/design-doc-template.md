# Design: <system name>

## Context and goals
<What the system does, for whom, and why now.>

## Load parameters and targets
| Parameter | Value (now) | Value (in 2 years) | Source / assumption |
|---|---|---|---|
| Reads/sec (peak) | | | |
| Writes/sec (peak) | | | |
| Data size / growth | | | |
| Fan-out / hot keys | | | |
| Latency target (p50 / p99) | | | |
| Availability target | | | |

## Guarantees required
| Operation / data | Guarantee | Why |
|---|---|---|
| e.g. payments | serializable + exactly-once effect | money |
| e.g. feed | eventual; read-your-writes for own posts | UX |

## Architecture
<Diagram (Mermaid is fine). Components, stores, and dataflows.>

### Systems of record and derived data
| Data | System of record | Derived copies | How derived (CDC / batch / stream) | Freshness |
|---|---|---|---|---|

### Data model
<Schemas / documents / key design for the main entities.>

### Replication and partitioning
<Topology, sync/async, partition key, secondary indexes, rebalancing.>

### Correctness mechanisms
<How each invariant is enforced: constraints, isolation level, idempotency keys, fencing, consensus.>

### Encoding and evolution
<Formats, schema registry, compatibility rules, migration approach.>

## Failure analysis
| Failure | Effect | Detection | Mitigation |
|---|---|---|---|
| Leader crash | | | |
| Network partition between X and Y | | | |
| Consumer/pipeline bug writes bad data | | | |
| Clock skew / process pause | | | |

## Alternatives considered
<Each option, its trade-offs, and why it lost.>

## Operations
<Monitoring (lag, skew, compaction, consumer lag), backups and restore tests, runbooks, reprocessing.>

## Privacy and retention
<What's collected, retention, deletion path.>

## Open questions
