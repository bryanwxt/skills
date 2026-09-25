Your human partner agreed this design in principle and asked you to write it up on the architectural path:

"Build online appointment booking for our clinic app (Python 3.12, Postgres 16 at READ COMMITTED, psycopg 3, Alembic, pytest). A time slot with a clinician can be booked by only one patient, even when two patients try at the same moment. The mobile app retries the booking call when it times out. After booking, the patient gets an SMS confirmation. Record which booking channel was used in the existing `appointments` table (8M rows). Bookings are mirrored to the clinician's Google Calendar, and front-desk staff also cancel appointments from the admin app, which must remove the calendar event."

Answer with exactly two labelled sections:
SPEC: the spec's key decisions (at most 350 words).
PLAN: the plan's Global Constraints, Review Focus, and task list, one line per task (at most 350 words).
