# -*- coding: utf-8 -*-

class Project:
    def __init__(self, name, description=None, is_active=True, project_id=None):
        self.id = project_id
        self.name = name
        self.description = description
        self.is_active = is_active
        
    