# Encoding and evolution

## Contents
1. Compatibility
2. Encoding formats
3. Schema evolution rules per format
4. Dataflow through databases
5. Dataflow through services (REST, RPC)
6. Dataflow through messages
7. Practical rules

---

## 1. Compatibility
Applications change, and during rolling upgrades or with long-lived data, old and new code coexist.
- **Backward compatibility:** new code can read data written by old code. Usually easy — you know the old format.
- **Forward compatibility:** old code can read data written by new code. Harder — old code must ignore additions it doesn't understand.
You need both whenever data outlives the code or deploys aren't instantaneous (which is almost always).

## 2. Encoding formats
- **Language-specific serialization** (Java Serializable, Python pickle): avoid for anything stored or sent between services. Ties you to one language, poor versioning, and deserializing untrusted data can execute arbitrary code.
- **JSON, XML, CSV:** human-readable and ubiquitous, but ambiguous about numbers (large integers lose precision in JavaScript; no int/float distinction), no binary strings (base64 needed), optional and complex schema support, CSV has no schema at all. Fine for public APIs and data interchange between organizations where agreement matters more than efficiency.
- **Binary JSON variants** (MessagePack, BSON): somewhat smaller, but still carry field names.
- **Thrift and Protocol Buffers:** schema-defined, compact binary. Each field has a numeric **tag**; the tag identifies the field, so names can change freely but tags must never change.
- **Avro:** schema-defined, even more compact (no tags). Reader and writer schemas are resolved side by side at read time, so the reader needs to know the writer's schema — carried in the file header, looked up by version number in a schema registry, or negotiated on connection. Friendly to dynamically generated schemas (e.g. dumping database tables).

## 3. Schema evolution rules
**Protobuf / Thrift:**
- Add new fields with new tag numbers. They must be optional or have defaults (old data won't have them).
- Old code ignores unknown tags (forward compatible).
- Remove only optional fields, and never reuse the removed tag number.
- Changing a datatype can truncate values; check the rules for each change.

**Avro:**
- Fields are matched by name. You can add or remove only fields that have a default value.
- Use union types with `null` for nullable fields.
- Renaming uses aliases (backward compatible only).

**All formats:** schemas act as documentation, allow compatibility checks before deploying (e.g. in CI against a schema registry), and enable code generation in statically typed languages.

## 4. Dataflow through databases
- The process that writes to a database encodes; a later process (possibly newer or older code) decodes. "Data outlives code."
- **Preserving unknown fields:** if new code adds a field and old code reads a record, modifies it, and writes it back, the new field can be silently lost. Make sure the decode–modify–encode path keeps unknown fields.
- Migrating (rewriting) a large dataset into a new schema is expensive; most databases allow cheap additions such as a new nullable column, filled in at read time.
- Archives and data dumps can be written in the latest schema (Avro and Parquet suit this).

## 5. Dataflow through services
- REST-style APIs over HTTP (often JSON, with OpenAPI specs) and RPC frameworks (gRPC, Thrift) are both common.
- **A network call is not a local function call.** It can time out with unknown outcome (the request may or may not have been processed), be retried (so it must be idempotent), take wildly variable time, and needs every argument encoded. Frameworks that hide this cause bugs. Design explicitly for timeouts, retries, and idempotency.
- Services are usually upgraded server-first: requests need backward compatibility on the server, responses need forward compatibility on the client.
- Public APIs often must support old versions for a long time. Version via the URL or a header, and document the compatibility policy.

## 6. Dataflow through messages
- A message broker decouples sender and receiver: it buffers when consumers are down, redelivers after crashes, allows one-to-many delivery, and hides consumers' addresses from producers.
- It's usually one-way; responses go on another channel.
- Messages need the same forward and backward compatibility care as databases, and republishing consumers must preserve unknown fields.
- **Actor frameworks** send messages between actors, possibly across nodes. Rolling upgrades need the same compatibility thinking.

## 7. Practical rules
1. Use an explicit schema for anything stored or sent between services (Protobuf, Avro, or JSON Schema).
2. Only add fields; make them optional with defaults.
3. Never reuse field tags or names for different meanings.
4. Keep unknown fields when round-tripping records.
5. Check schema compatibility automatically before deploying.
6. For database schema changes: expand (add new, compatible structure) → migrate (backfill, dual write/read) → contract (remove old) — each step deployable independently.
7. Treat every remote call as possibly failed-with-unknown-outcome; use idempotency keys for retried writes.
