# Task 2: Integrity Defects

## Defect 1: Orphan maintenance jobs
**Evidence:** Job 3 references machine `cnc-05`, which does not exist in the machine table.

**Production impact:** The maintenance job cannot be reliably linked to a machine or site.

## Defect 2: Duplicate part numbers
**Evidence:** Part number `P-1003` appears twice.

**Production impact:** Duplicate part records can lead to incorrect inventory counts and purchasing reports.

## Defect 3: Prices stored as text
**Evidence:** The price query returns only `P-1001` with price `12.50`.

**Production impact:** Text-based price comparisons can produce incorrect financial reports.

## Defect 4: Invalid installation date
**Evidence:** Machine `RANDOM-NAME` has the installation date `unknown`.

**Production impact:** Invalid dates can break equipment-age calculations and maintenance schedules.

## Defect 5: Comma-separated part list
**Evidence:** Job 1 uses `P-1001,P-1002`, but the join does not return that job.

**Production impact:** Maintenance reports can omit jobs that use multiple parts.

## Evidence files
- `defect-queries.sql` — the five SQL queries.
- `defect-results.txt` — their saved results.