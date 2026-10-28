import sqlite3
from pathlib import Path

db_path = Path(__file__).with_name("telemetry.db")

query = """
SELECT
    machine,
    AVG(spindle_load) AS avg_spindle_load
FROM readings
WHERE time(ts) > '18:00:00'
GROUP BY machine
ORDER BY avg_spindle_load DESC;
"""

with sqlite3.connect(db_path) as conn:
    print("Generated SQL results:")
    for row in conn.execute(query):
        print(row)

    print("\nEXPLAIN QUERY PLAN:")
    for row in conn.execute("EXPLAIN QUERY PLAN " + query):
        print(row)