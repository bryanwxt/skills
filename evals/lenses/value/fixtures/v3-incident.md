# Bug report: duplicate orders

**Symptom:** about 0.3% of checkouts create two orders with the same `checkout_id`, so the customer is charged once but gets two shipments. It's worse at peak (up to 1%). It started two weeks ago, when payment webhook handling moved from the web app into a queue worker.

**What we know:**
- Stripe sends `payment_intent.succeeded` to `/webhooks/stripe`, which now just enqueues the event on an SQS **standard** queue and returns 200.
- Three worker processes consume the queue. Visibility timeout: 30 s.
- The handler calls the fulfillment API before acknowledging. At peak, p99 fulfillment latency is 28–40 s.
- Grafana shows read-replica lag alerts at peak (up to 4 s). Order reads in the admin UI go to the replica.
- Carts are cached in Redis (TTL 15 min).
- There's no unique constraint on `orders.checkout_id` (it has a plain index).

**Worker code:**

```python
def handle_payment_succeeded(message):
    event = json.loads(message.body)
    with db.session() as session:
        order = session.query(Order).filter_by(checkout_id=event["checkout_id"]).first()
        if order is None:
            order = Order(checkout_id=event["checkout_id"], amount=event["amount"])
            session.add(order)
            session.commit()
    fulfillment.create_shipment(order.id)   # p99 28–40 s at peak
    message.delete()                        # ack
```
