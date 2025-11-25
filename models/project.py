# models/project.py

from dataclasses import dataclass
from models.worksession import Worksession as ws
from datetime import datetime

@dataclass
class Project:
    name: str
    worksessions: list[ws] = None
    id: int | None = None
    is_active: bool = True
    
    def get_active_session(self) -> ws | None:
        """
        Returns active worksession of project.
        If no running session is found, returns None.
        """
        for session in self.worksessions:
            return any((ws for ws in self.worksessions if ws.is_running()), None)
    
    def show_all_sessions(self) -> list[ws]:
        """
        Returns list of all worksessions in project.
        """
        return self.worksessions.copy() # Returns copy for safety reasons (encapsulation)
        
    def start_new_session(self, description):
        """
        Starts new worksession in project.
        """
        if not self.get_active_session(): # Checks for active session
            self.worksessions.append(ws(datetime.now(), description))
        else:
            print("Er is al een lopende sessie op dit project.")
        
    def __str__(self):
        return f"({self.id}) {self.name} - Active:{self.is_active}"
            