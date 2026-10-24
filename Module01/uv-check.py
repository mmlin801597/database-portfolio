
import sys
import platform
import sqlite3
from importlib.metadata import version, PackageNotFoundError

print("uv-managed Python:", sys.executable)
print("Python version:   ", platform.python_version())
print("SQLite version:   ", sqlite3.sqlite_version)

for pkg in ("duckdb", "datasette", "sqlite-utils", "pydantic", "sqlalchemy"):
    try:
        print(f"{pkg:18s}", version(pkg))
    except PackageNotFoundError:
        print(f"{pkg:18s}", "NOT INSTALLED")
