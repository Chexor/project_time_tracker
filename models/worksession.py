# models/worksession.py

from dataclasses import dataclass
from datetime import datetime

@dataclass
class Worksession:
    start_time: datetime
    description: str = ""
    id: int | None = None
    end_time: datetime = None