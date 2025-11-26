# models/project.py

from dataclasses import dataclass
from models.worksession import Worksession as ws
from datetime import datetime

@dataclass
class Project:
    name: str
    description: str = ""
    work_sessions: list[ws] = None
    id: int | None = None
    is_active: bool = True
    
    def get_active_session(self) -> ws | None:
        """
        Returns active work session of project.
        If no running session is found, returns None.
        """
        for session in self.work_sessions:
            return next((ws for session in self.work_sessions if ws.is_running()), None)
        return None

    def show_all_sessions(self) -> list[ws]:
        """
        Returns list of all work sessions in project.
        """
        return self.work_sessions.copy() # Returns copy for safety reasons (encapsulation)
        
    def start_new_session(self, description):
        """
        Starts new work session in project.
        """
        if not self.get_active_session(): # Checks for active session
            self.work_sessions.append(ws(datetime.now(), description))
        else:
            print("Er is al een lopende sessie op dit project.")

    def end_active_session(self):
        """
        Ends active work session in project.
        """
        active_session = self.get_active_session()
        if active_session:
            active_session.end_time = datetime.now()
        else:
            print("Er is geen lopende sessie op dit project.")

    def __str__(self):
        return f"({self.id}) {self.name} - Active:{self.is_active}"
            