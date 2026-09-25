Your human partner agreed this design in principle and asked you to write it up on the architectural path:

"Build gift card redemption for our existing app (Python 3.12, Postgres 16 at READ COMMITTED, psycopg 3, Alembic, pytest). Each code must be redeemed exactly once, even under concurrent requests. Mobile clients retry the redeem call when it times out. After redemption the user gets a confirmation email. Record who redeemed each code in the existing `gift_cards` table (12M rows). Partial balances are charged through Stripe, and the admin dashboard also issues refunds through Stripe."

Answer with exactly two labelled sections:
SPEC: the spec's key decisions (at most 350 words).
PLAN: the plan's Global Constraints, Review Focus, and task list, one line per task (at most 350 words).
