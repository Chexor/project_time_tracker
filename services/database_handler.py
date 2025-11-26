# services/database_handler.py
import sqlite3

from models.project import Project
from db.database import Database
from models.worksession import Worksession
import config.config as config
from datetime import datetime

db = config.DATABASE_PATH

def load_active_projects_from_db() -> list[Project]:
    """
    Loads active projects from the database.
    Returns list of projects.
    """
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute('SELECT id, name, description FROM projects WHERE is_active = 1')
    rows = cursor.fetchall()
    projects = []
    for row in rows:
        project = Project(id=row[0], name=row[1], description=row[2])
        projects.append(project)
    connection.close()
    return projects

def load_all_projects_from_db() -> list[Project]:
    """
    Loads all projects (active and inactive) from the database.
    Returns list of projects.
    """
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute('SELECT id, name, description, is_active FROM projects')
    rows = cursor.fetchall()
    projects = []
    for row in rows:
        project = Project(id=row[0], name=row[1], description=row[2], is_active=bool(row[3]))
        projects.append(project)
    connection.close()
    return projects

def save_project_to_db(db: Database, project: Project) -> None:
    """
    Saves a project and its work sessions to the database.
    """
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    if project.id is None:
        cursor.execute(
            'INSERT INTO projects (name, description, is_active) VALUES (?, ?, ?)',
            (project.name, project.description, int(project.is_active))
        )
        project.id = cursor.lastrowid
    else:
        cursor.execute(
            'UPDATE projects SET name = ?, description = ?, is_active = ? WHERE id = ?',
            (project.name, project.description, int(project.is_active), project.id)
        )
    connection.commit()
    connection.close()

def load_sessions_for_project_from_db(project_id: int) -> list[Worksession]:
    """
    Loads all work sessions for a given project from the database.
    Returns list of work sessions.
    """
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute(
        'SELECT id, start_time, end_time, description FROM worksessions WHERE project_id = ?',
        (project_id,)
    )
    rows = cursor.fetchall()
    sessions = []
    for row in rows:
        start_time = datetime.fromisoformat(row[1])
        end_time = datetime.fromisoformat(row[2]) if row[2] else None
        session = Worksession(id=row[0], start_time=start_time, end_time=end_time, description=row[3])
        sessions.append(session)
    connection.close()
    return sessions

def save_session_to_db(db: Database, project_id: int, session: Worksession) -> None:
    """
    Saves a single work session to the database.
    """
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    if session.id is None:
        cursor.execute(
            'INSERT INTO worksessions (project_id, start_time, end_time, description) VALUES (?, ?, ?, ?)',
            (project_id, session.start_time.isoformat(),
             session.end_time.isoformat() if session.end_time else None,
             session.description)
        )
        session.id = cursor.lastrowid
    else:
        cursor.execute(
            'UPDATE worksessions SET start_time = ?, end_time = ?, description = ? WHERE id = ?',
            (session.start_time.isoformat(),
             session.end_time.isoformat() if session.end_time else None,
             session.description, session.id)
        )
    connection.commit()
    connection.close()