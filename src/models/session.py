# -*- coding: utf-8 -*-

class Session:
    def __init__(self, project_id, start_time, is_active=True, end_time=None, duration=None, session_id=None):
        self.id = session_id
        self.project_id = project_id
        self.start_time = start_time
        self.is_active = is_active
        self.end_time = end_time
        self.duration = duration
        
    def save(self):
        """Werkt sessie bij in database."""
        