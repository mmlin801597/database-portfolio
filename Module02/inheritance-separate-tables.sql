
-- Alternative 2: Separate tables for each machine subtype
CREATE TABLE machine (
    machine_id INTEGER PRIMARY KEY,
    machine_name TEXT NOT NULL UNIQUE,
    serial_no TEXT NOT NULL UNIQUE,
    site TEXT NOT NULL,
    installed DATE NOT NULL
);

CREATE TABLE cnc_mill (
    machine_id INTEGER PRIMARY KEY,
    spindle_speed INTEGER NOT NULL,
    tool_capacity INTEGER NOT NULL,
    FOREIGN KEY (machine_id) REFERENCES machine(machine_id)
);

CREATE TABLE injection_molder (
    machine_id INTEGER PRIMARY KEY,
    clamping_force INTEGER NOT NULL,
    injection_volume INTEGER NOT NULL,
    FOREIGN KEY (machine_id) REFERENCES machine(machine_id)
);
