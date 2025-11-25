# db/database.py

import sqlite3

class Database:
    def __init__(self, db_name="project_time_tracker.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                is_active BOOLEAN NOT NULL CHECK (is_active IN (0, 1))
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS worksessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                project_id INTEGER NOT NULL,
                start_time TEXT NOT NULL,
                end_time TEXT,
                description TEXT,
                FOREIGN KEY (project_id) REFERENCES projects (id)
            )
        ''')
        self.connection.commit()

    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        self.connection.commit()
        return self.cursor

    def close(self):
        self.connection.close()



