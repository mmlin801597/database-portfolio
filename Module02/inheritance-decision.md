
# Task 4: Machine Inheritance

## Alternative 1: Single Table

All machines are stored in one table. The `machine_type` column identifies whether a machine is a CNC mill or an injection molder. Type-specific columns are nullable, and CHECK constraints restrict which attributes can be used for each type.

## Alternative 2: Separate Tables

Common machine attributes are stored in the `machine` table. CNC mill attributes are stored in `cnc_mill`, while injection molder attributes are stored in `injection_molder`. Foreign keys connect each subtype to its parent machine.

## Decision

I would choose separate tables because they avoid many NULL values and keep subtype-specific attributes clearly separated, although the disjointness rule requires additional enforcement.
