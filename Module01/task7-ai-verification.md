# Task 7: The First LLM-Assisted SQL Profiling Task

## 1. Exact prompt used

Here is my SQLite table: `readings(ts TEXT, machine TEXT, temp_c REAL, vib_rms REAL, spindle_load REAL)`. Write a query that returns, for each machine, the average spindle load for readings taken overnight (after 18:00), ordered by average load descending. Explain the query briefly.

## 2. Generated SQL

```sql
SELECT
    machine,
    AVG(spindle_load) AS avg_spindle_load
FROM readings
WHERE time(ts) > '18:00:00'
GROUP BY machine
ORDER BY avg_spindle_load DESC;
```

## 3. Execution results

The query executed successfully against my local SQLite database.

| Machine | Average spindle load |
|---|---:|
| cnc-03 | 60.4340 |
| cnc-01 | 60.3685 |
| cnc-02 | 60.3572 |

## 4. EXPLAIN QUERY PLAN

```text
(7, 0, 216, 'SCAN readings')
(12, 0, 0, 'USE TEMP B-TREE FOR GROUP BY')
(51, 0, 0, 'USE TEMP B-TREE FOR ORDER BY')
```

SQLite scans the readings table and uses temporary structures for grouping and sorting. A full-table scan is expected because the query has no suitable index.

## 5. Verification reflection

The model correctly used `AVG()` to calculate the average spindle load, `GROUP BY` to calculate a separate average for each machine, and descending order to rank the results. I verified the query by running it against my SQLite database and checking its execution plan. The plan showed a full-table scan and temporary structures for grouping and sorting. I also tested the incorrect condition `ts LIKE '%18%'`, which searches for the characters `18` anywhere in the timestamp rather than checking the time of day. This demonstrated why generated SQL must be tested rather than trusted automatically.