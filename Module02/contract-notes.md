# Task 3: Data Contract Notes

## Application-level constraints (Pydantic)

- `machine_id` must be at least 1.
- `serial_no` must contain at least three characters and start with `SN-`.
- `installed` and `done_on` must be valid dates.
- `part_nos` is a list, so a maintenance job can use multiple parts.

These rules are checked by the application before it accepts the data.

## Database-level constraints (SQLAlchemy)

- Primary keys identify each record uniquely.
- `serial_no` must be unique and cannot be NULL.
- Foreign keys connect maintenance jobs to machines and parts to jobs.
- Required fields cannot be NULL.
- `unit_price` uses `NUMERIC(9, 2)` instead of text.
- The `job_part` junction table represents the many-to-many relationship between jobs and parts.

These rules protect the database from invalid relationships and duplicate identifiers, even when data comes from different applications.

## Conclusion

Pydantic validates data in the application, while database constraints protect the stored data. Using both provides stronger data integrity.