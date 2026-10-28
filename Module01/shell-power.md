# Task 9: SQLite Shell Power Moves

## Commands I Ran

- Used `.mode json` to display query results as JSON.
- Used `.mode markdown` to display query results as a Markdown table.
- Saved query output to `Module01/result.json`.
- Created a database backup using `.backup Module01/backup.db`.
- Compared the sizes of `telemetry.db` and `backup.db`.
- Stored SQL queries in `Module01/queries.sql` and executed them using PowerShell.

## Findings

The telemetry database and its backup were both 10,526,720 bytes. This is expected because the backup contains the same database data.

JSON output uses structured key-value pairs, while Markdown output presents the results in a readable table. These formats are useful for different purposes.