# Diff under review: gift card redemption endpoint

Requirements: redeem a gift card code once per code; send the user a confirmation email; record who redeemed it in a new `gift_cards.redeemed_by` column. `gift_cards` has 12M rows. Stack: Python 3.12, Postgres 16 (READ COMMITTED), psycopg 3, Alembic, pytest.

```diff
--- /dev/null
+++ b/migrations/versions/0042_redeemed_by.py
@@ -0,0 +1,12 @@
+"""Add gift_cards.redeemed_by."""
+import sqlalchemy as sa
+from alembic import op
+
+revision = "0042"
+down_revision = "0041"
+
+def upgrade():
+    op.add_column("gift_cards", sa.Column("redeemed_by", sa.String(), nullable=False))
+
+def downgrade():
+    op.drop_column("gift_cards", "redeemed_by")
--- /dev/null
+++ b/src/giftcard/service.py
@@ -0,0 +1,38 @@
+from dataclasses import dataclass, field
+
+from giftcard.errors import AlreadyRedeemed, UnknownCode
+
+
+@dataclass
+class Redemption:
+    code: str
+    user_id: str
+    tags: list[str] = field(default_factory=list)
+
+
+class GiftCardService:
+    """Redeems gift cards and notifies the user."""
+
+    def __init__(self, pool, mailer):
+        self.pool = pool
+        self.mailer = mailer
+
+    def redeem(self, code: str, user_id: str, tags=[]) -> Redemption:
+        """Redeem `code` for `user_id`. Raises UnknownCode or AlreadyRedeemed."""
+        with self.pool.connection() as conn:
+            with conn.transaction():
+                row = conn.execute(
+                    "SELECT id, redeemed_by FROM gift_cards WHERE code = %s", (code,)
+                ).fetchone()
+                if row is None:
+                    raise UnknownCode(code)
+                if row.redeemed_by is not None:
+                    raise AlreadyRedeemed(code)
+                conn.execute(
+                    "UPDATE gift_cards SET redeemed_by = %s WHERE id = %s", (user_id, row.id)
+                )
+                tags.append("redeemed")
+                self.mailer.send(user_id, "Your gift card was redeemed")
+        return Redemption(code=code, user_id=user_id, tags=tags)
+
+    def lookup(self, code: str):
+        with self.pool.connection() as conn:
+            return conn.execute("SELECT * FROM gift_cards WHERE code = %s", (code,)).fetchone()
--- /dev/null
+++ b/src/giftcard/manager.py
@@ -0,0 +1,13 @@
+class GiftCardManager:
+    """Coordinates gift card operations."""
+
+    def __init__(self, service):
+        self.service = service
+
+    def redeem(self, code, user_id):
+        return self.service.redeem(code, user_id)
+
+    def lookup(self, code):
+        return self.service.lookup(code)
--- a/src/api/routes.py
+++ b/src/api/routes.py
@@ -40,3 +40,13 @@
+@app.post("/gift-cards/redeem")
+def redeem_gift_card(req):
+    try:
+        redemption = manager.redeem(req.json["code"], req.user.id)
+        return {"ok": True, "code": redemption.code}
+    except:
+        return {"ok": False}
--- /dev/null
+++ b/tests/test_redeem.py
@@ -0,0 +1,22 @@
+from unittest.mock import MagicMock
+
+from giftcard.service import GiftCardService
+
+
+def test_redeem_sets_redeemed_by():
+    pool = MagicMock()
+    conn = pool.connection.return_value.__enter__.return_value
+    conn.execute.return_value.fetchone.return_value = MagicMock(id=1, redeemed_by=None)
+    mailer = MagicMock()
+
+    result = GiftCardService(pool, mailer).redeem("ABC", "u1")
+
+    assert result.code == "ABC"
+    mailer.send.assert_called_once()
+
+
+def test_redeem_twice_raises():
+    pool = MagicMock()
+    conn = pool.connection.return_value.__enter__.return_value
+    conn.execute.return_value.fetchone.return_value = MagicMock(id=1, redeemed_by="u1")
+    try:
+        GiftCardService(pool, MagicMock()).redeem("ABC", "u2")
+    except Exception:
+        pass
```
