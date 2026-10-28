# Task 10: Datasette Features

## 1. Table View
- URL: http://127.0.0.1:8001/telemetry/readings
- The table contains 172,800 telemetry readings from three machines: cnc-01, cnc-02, and cnc-03.

## 2. Filter and Facets
- Filter URL: http://127.0.0.1:8001/telemetry/readings?machine=cnc-02
- Facet URL: http://127.0.0.1:8001/telemetry/readings?_facet=machine
- Each machine has 57,600 readings.

## 3. JSON API
- URL: http://127.0.0.1:8001/telemetry/readings.json?_size=5
- This API returns the first five readings in JSON format.

## 4. Custom SQL Query
The following query calculates the average spindle load for each machine.

```sql
SELECT
    machine,
    ROUND(AVG(spindle_load), 2) AS average_spindle_load
FROM readings
GROUP BY machine
ORDER BY average_spindle_load DESC;
```

### Results

| Machine | Average spindle load |
|---|---:|
| cnc-03 | 60.15 |
| cnc-02 | 60.15 |
| cnc-01 | 60.14 |

The query results can be viewed and exported as CSV or JSON through Datasette.

## 5. Screenshot Evidence
- Screenshot: `datasette-filtered-view.png`
- The screenshot shows the filtered Datasette table from the previous task.