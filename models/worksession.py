# models/worksession.py

from dataclasses import dataclass
from datetime import datetime

@dataclass
class Worksession:
    start_time: datetime
    description: str = ""
    id: int | None = None
    end_time: datetime = None

    def is_running(self) -> bool:
        """
        Returns True if work session is still running (no end_time set).
        """
        return self.end_time is None

    def end_session(self):
        """
        Ends the work session by setting the end_time to current time.
        """
        if self.is_running():
            self.end_time = datetime.now()
        else:
            print("Deze sessie is al beëindigd.")
