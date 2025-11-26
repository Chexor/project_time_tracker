# db/database.py

import sqlite3
import config.config as config

class Database:
    def __init__(self, db_name=config.DATABASE_PATH):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
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