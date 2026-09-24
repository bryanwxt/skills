# Data subsections for a brainstorming spec

These go inside the superpowers spec (`docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md`) as `###` subsections under brainstorming's own headings, the layout set in `references/coordination.md` (Spec). Never add a separate "Data architecture" heading or document. Omit any subsection that doesn't apply.

## Architecture

### Load and targets
| Parameter | Now | Horizon | Source / assumption |
|---|---|---|---|
| Reads/s (peak) | | | |
| Writes/s (peak) | | | |
| Data size / growth | | | |
| Fan-out / hot keys | | | |
| Latency p50 / p99 | | | |
| Loss tolerance | | | |

### Guarantees required
| Operation / data | Guarantee (named precisely) | Enforced by |
|---|---|---|

### Systems of record and derived data
| Data | System of record | Derived copies | Produced by (sync / CDC / batch / stream) | Freshness |
|---|---|---|---|---|

## Data flow

### Dataflow diagram
```mermaid
flowchart LR
  app[Service] -->|tx + outbox| db[(Primary DB)]
  db -->|CDC| log[[Log]]
  log --> search[(Search index)]
  log --> wh[(Warehouse)]
```

### Data model
<Schemas / documents / key design for the main entities; indexes and why.>

### Replication and partitioning
<Topology; sync vs async and what an acknowledged write means; read-your-writes strategy; partition key and why; hot-key plan; secondary-index approach. Or: "single node + replicas is sufficient because …">

### Correctness mechanisms
<For each invariant: constraint / isolation level / atomic update / idempotency key / fencing / single-partition log. Name the database's actual isolation level.>

### Encoding and evolution
<Formats; schema registry or compatibility checks; expand → migrate → contract plan for schema changes.>

## Error handling

Data failures are rows in the spec's ONE error table (columns from `coordination.md`). Cover at least these rows, and write each failure as an event sequence:

| Failure (event sequence) | Handled where and how | Exception type | Caller-visible? | Detection |
|---|---|---|---|---|
| Leader loss / failover: … | | | | |
| Network partition between A and B: … | | | | |
| Consumer bug writes bad data: … | | | | |
| Retry after timeout (unknown outcome): … | | | | |
| Clock skew / process pause: … | | | | |

## Testing

### Data-correctness tests
<Race, idempotency, migration, rerun and failure-injection tests, all run against the real engine; how the test database is provisioned.>

## Implementation notes

### Operations
<Monitoring (replication lag, consumer lag, partition skew, compaction), backups and restore tests, reprocessing path, runbooks.>

### Product facts relied on
| Claim | Source | Checked on |
|---|---|---|
