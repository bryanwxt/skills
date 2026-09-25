# Gift Card Redemption Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Redeem gift card codes exactly once and send a confirmation email.
**Architecture:** `GiftCardService` owns the ledger in Postgres; an outbox table carries redemption events to an email consumer.
**Tech Stack:** Python 3.12, psycopg 3, Postgres 16, pytest, ruff, mypy.
**Spec:** docs/superpowers/specs/2026-09-20-giftcard-design.md

## Global Constraints
- Redemption is exactly-once: unique constraint `redemptions(code)`; Postgres at READ COMMITTED.
- Confirmation email is at-least-once via the `outbox` table and an idempotent consumer; never sent inside the redemption transaction.
- Only `giftcard/service.py` reads or writes ledger tables.
- Checks: `ruff check .`, `ruff format --check .`, `mypy --strict src`, `pytest -q`.

## Review Focus
1. Two concurrent redeems of one code → exactly one succeeds, the other gets AlreadyRedeemed.
2. Client retry with the same request after a timeout → same result, one redemption.
3. Crash after commit, before the email → email still sent once via the outbox.
4. The same outbox event delivered twice → one email.
5. Expired code → ExpiredCode error, no writes.

---

### Task 4: GiftCardService.redeem()
**Files:** Modify `src/giftcard/service.py`; Test `tests/test_redeem.py`
**Interfaces:** Consumes: `redemptions` and `outbox` tables (Task 1). Produces: `GiftCardService.redeem(code: str, request_id: UUID) -> Redemption  # redeems once; raises AlreadyRedeemed, ExpiredCode`
Module card: GiftCardService — abstraction: a gift card ledger; hides: tables, locking, outbox writes.
Python rules: types + docstrings on public functions; `raise … from e`; `with` for connections; inject the connection pool.
Guarantee: exactly-once per code; proven by `test_concurrent_redeem_one_wins` (two connections, explicit interleaving, real Postgres).
- [ ] Steps 1–5 (failing test, run, implement, run, commit) — omitted here.

### Task 5: Confirmation email consumer
**Files:** Create `src/giftcard/email_consumer.py`; Test `tests/test_email_consumer.py`
**Interfaces:** Consumes: `outbox` rows (Task 1). Produces: `EmailConsumer.handle(event: OutboxEvent) -> None  # sends the confirmation email`
Python rules: types + docstrings; inject the mail client; `with` for connections.
- [ ] Steps 1–5 — omitted here.
