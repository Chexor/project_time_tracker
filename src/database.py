# -*- coding: utf-8 -*-

import sqlite3
import json
from pathlib import Path


# ---------------------------------------
# Haal pad naar database uit config file
# ---------------------------------------
ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config" / "config.json"

def get_db_path():
    default = ROOT / "db" / "project_time_tracker.db"
    try:
        data = json.loads(CONFIG.read_text(encoding="utf-8"))
        rel = data.get("database", {}).get("path")
        return (ROOT / rel) if rel else default
    except FileNotFoundError:
        return default

DB_PATH = get_db_path()

# -------------------------
# Maak nieuwe database aan met tabellen
# -------------------------
def create_database():
    """Maakt nieuwe database aan als die nog niet bestaat"""
    if not DB_PATH.exists():
        DB_PATH.parent.mkdir(parents=True, exist_ok=True)
        conn = get_connection()
        conn.close()
        print(f"Nieuwe database aangemaakt op : {DB_PATH}")
    else:
        print(f"Database bestaat al op : {DB_PATH}")

def create_tables():
    """Maakt de noodzakelijke tabellen aan indien die nog niet bestaan"""
    with get_connection() as conn:
        cursor = conn.cursor()
        
        # Tabel: projects
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS projects (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       description TEXT,
                       is_active INTEGER DEFAULT 1
                       )
                """)
                
        # Tabel: sessions
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS sessions (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       project_id INTEGER NOT NULL,
                       start_time TEXT NOT NULL,
                       end_time TEXT,
                       duration REAL,
                       is_active INTEGER DEFAULT 1,
                       FOREIGN KEY (project_id) REFERENCES projects (id)
                       )
                """)

    print("Tabellen gecontroleerd of aangemaakt.")
    
# -------------------------
# Maak connectie met de database
# -------------------------
def get_connection():
    """Geeft een connectie met de database terug"""
    conn = sqlite3.connect(DB_PATH)
    # conn.execute("PRAGMA foreign_keys = ON") # <- afdwingen foreign keys
    return conn

# -------------------------
# Data wijzigen (INSERT, UPDATE, DELETE)
# -------------------------

def execute_query(query, params=None):
    """Voert een query uit die wijzigingen maakt in de database."""
    try:
        with get_connection() as conn:
            cursor = conn.execute(query, params or ())
            return cursor.lastrowid
    except sqlite3.Error as e:
        raise RuntimeError(f"DB write failed: {e}") from e

    
# -------------------------
# Data ophalen uit database (SELECT)
# -------------------------

def fetch_query(query, params=None):
    """Voert een SELECT query uit en geeft de resultaten terug"""
    try:
        with get_connection() as conn:
            cursor = conn.execute(query, params or ())
            return cursor.fetchall()
    except sqlite3.Error as e:
        raise RuntimeError(f"DB read failed: {e}") from e