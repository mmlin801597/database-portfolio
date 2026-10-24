
-- Alternative 1: Single table with a type discriminator
CREATE TABLE machine (
    machine_id INTEGER PRIMARY KEY,
    machine_name TEXT NOT NULL UNIQUE,
    machine_type TEXT NOT NULL
        CHECK (machine_type IN ('CNC_MILL', 'INJECTION_MOLDER')),
    serial_no TEXT NOT NULL UNIQUE,
    site TEXT NOT NULL,
    installed DATE NOT NULL,

    -- CNC mill attributes
    spindle_speed INTEGER,
    tool_capacity INTEGER,

    -- Injection molder attributes
    clamping_force INTEGER,
    injection_volume INTEGER,

    -- Only CNC mills may have these attributes
    CHECK (
        machine_type = 'CNC_MILL'
        OR (spindle_speed IS NULL AND tool_capacity IS NULL)
    ),

    -- Only injection molders may have these attributes
    CHECK (
        machine_type = 'INJECTION_MOLDER'
        OR (clamping_force IS NULL AND injection_volume IS NULL)
    )
);
