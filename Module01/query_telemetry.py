"""Run the Task 6 telemetry queries and save their results."""

import sqlite3
from pathlib import Path

here = Path(__file__).parent
db_path = here / "telemetry.db"
results_path = here / "telemetry-results.txt"

queries = [
    (
        "1. Number of readings per machine",
        """
        SELECT machine, COUNT(*) AS n
        FROM readings
        GROUP BY machine
        ORDER BY machine;
        """,
    ),
    (
        "2. Peak vibration per machine",
        """
        SELECT machine, MAX(vib_rms) AS peak_vib
        FROM readings
        GROUP BY machine
        ORDER BY machine;
        """,
    ),
    (
        "3. Readings exceeding the 2.0 mm/s alarm",
        """
        SELECT COUNT(*) AS alarm_readings
        FROM readings
        WHERE vib_rms > 2.0;
        """,
    ),
]

with sqlite3.connect(db_path) as conn:
    with results_path.open("w", encoding="utf-8") as output:
        for title, query in queries:
            rows = conn.execute(query).fetchall()
            columns = [
                description[0]
                for description in conn.execute(query).description
            ]

            output.write(title + "\n")
            output.write("-" * len(title) + "\n")
            output.write(" | ".join(columns) + "\n")

            for row in rows:
                output.write(" | ".join(str(value) for value in row) + "\n")

            output.write("\n")

            print(title)
            print(" | ".join(columns))
            for row in rows:
                print(" | ".join(str(value) for value in row))
            print()

print(f"Results saved to {results_path}")