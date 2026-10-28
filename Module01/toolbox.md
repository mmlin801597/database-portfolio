# Task 11: Datasette Lite and sqlite-utils

## 1. Datasette Lite

Datasette Lite runs Datasette in a web browser without requiring a local installation. It can be used to explore SQLite databases and run SQL queries.

Website: https://lite.datasette.io/

## 2. sqlite-utils

I used `sqlite-utils` version 4.2.1 to inspect and search my SQLite database.

Commands tested:

```bash
uv tool run sqlite-utils tables Module01/tour.db
uv tool run sqlite-utils schema Module01/tour.db reading
uv tool run sqlite-utils rows Module01/tour.db reading --limit 5
uv tool run sqlite-utils enable-fts Module01/tour.db reading machine
uv tool run sqlite-utils search Module01/tour.db reading cnc
```

The `tables` command listed the tables in the database. The `schema` command displayed the table structure, and `rows` displayed example records. I enabled full-text search on the `machine` column and successfully searched for `cnc`.

## 3. Comparing Three Approaches

The `sqlite3` command-line tool is useful for running SQL directly and inspecting databases interactively. The `sqlite-utils` tool requires fewer keystrokes for common tasks such as listing tables, viewing rows, and enabling full-text search. Python's `sqlite3` module is clearer when I need to automate database operations, process CSV files, or combine SQL with Python code. I would choose `sqlite3` for quick SQL experiments, `sqlite-utils` for convenient database inspection, and Python's `sqlite3` module for repeatable data-processing scripts.

## 4. Evidence

The terminal output confirmed that the `reading` table contains machine and vibration data and that full-text search returned matching rows.