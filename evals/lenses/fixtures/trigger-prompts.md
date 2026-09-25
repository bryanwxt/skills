For each request, you are at the very START of handling it (nothing loaded yet). No CLAUDE.md lists any lenses. List every skill from the list you would load now or at any later step while handling it.

P1. "Add a --verbose flag to the export command in our Python CLI."
P2. "Review the architecture of this TypeScript monorepo and tell me what to fix."
P3. "Postgres or DynamoDB for our user-session store?"
P4. "Is src/billing/invoice.py Pythonic? Review it."
P5. "Fix the failing test in tests/test_orders.py — orders are occasionally duplicated under load." (Python service)
P6. "Fix the typo in README.md."
P7. "Add an endpoint to our Go service that lists users. Single Postgres, low traffic, read-only."
P8. "Write the implementation plan for the approved spec: a new ledger service in Python with Postgres migrations and an outbox."
P9. "Our Go Kafka consumer keeps replaying events after restarts and double-applying them."
P10. "Make this React component re-render less."
