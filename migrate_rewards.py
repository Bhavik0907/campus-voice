"""
migrate_rewards.py
──────────────────
Run this ONCE on an existing Campus Voice database to add
the Student Reward & Points System columns.

Usage:
    python migrate_rewards.py

Safe to run multiple times — skips columns that already exist.
"""

import sqlite3, os

DB = os.path.join(os.path.dirname(__file__), 'database.db')

if not os.path.exists(DB):
    print("❌ database.db not found. Run init_db.py first.")
    exit(1)

conn = sqlite3.connect(DB)

migrations = [
    ("users",      "points",       "INTEGER NOT NULL DEFAULT 0"),
    ("complaints", "reward_given", "INTEGER NOT NULL DEFAULT 0"),
]

for table, column, definition in migrations:
    try:
        conn.execute(f"ALTER TABLE {table} ADD COLUMN {column} {definition}")
        print(f"✅  Added {table}.{column}")
    except Exception as e:
        if "duplicate column" in str(e).lower():
            print(f"ℹ️   {table}.{column} already exists — skipped")
        else:
            print(f"⚠️   {table}.{column}: {e}")

conn.commit()

# Verify
print("\n── Schema verification ──────────────────────────")
for table in ("users", "complaints"):
    cols = [r[1] for r in conn.execute(f"PRAGMA table_info({table})").fetchall()]
    print(f"  {table}: {', '.join(cols)}")

conn.close()
print("\n✅ Migration complete.")
