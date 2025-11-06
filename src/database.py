# -*- coding: utf-8 -*-

import sqlite3
from pathlib import Path

# Path naar database
DB_PATH = Path("db/project_time_tracker.db")

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
    conn = get_connection()
    cursor = conn.cursor()
    
    # Tabel: projects
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS projects (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   decription TEXT,
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
    
    conn.commit()
    conn.close()
    print("Tabellen gecontroleerd of aangemaakt.")
    
# -------------------------
# Maak connectie met de database
# -------------------------
def get_connection():
    """Geeft een connectie met de database terug"""
    return sqlite3.connect(DB_PATH)

# -------------------------
# Data wijzigen (INSERT, UPDATE, DELETE)
# -------------------------

def execute_query(query, params=None):
    """Voert een query uit die wijzigingen maakt in de database."""
    conn = get_connection()
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    conn.commit()
    conn.close()
    
# -------------------------
# Data ophalen uit database (SELECT)
# -------------------------

def fetch_query(query, params=None):
    """Voert een SELECT query uit en geeft de resultaten terug"""
    conn = get_connection()
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows