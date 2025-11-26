# services/export_csv.py

import csv
from models.project import Project
from models.worksession import Worksession
from datetime import datetime
from typing import List

def export_projects_to_csv(projects: List[Project], filename: str) -> None:
    """
    Exports the given list of projects and their worksessions to a CSV file.

    :param projects: List of Project instances to export.
    :param filename: The name of the CSV file to create.
    """
    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Project ID', 'Project Name', 'Session ID', 'Description', 'Start Time', 'End Time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for project in projects:
            for session in project.worksessions:
                writer.writerow({
                    'Project ID': project.id,
                    'Project Name': project.name,
                    'Session ID': session.id,
                    'Description': session.description,
                    'Start Time': session.start_time.strftime('%Y-%m-%d %H:%M:%S'),
                    'End Time': session.end_time.strftime('%Y-%m-%d %H:%M:%S') if session.end_time else 'Running'
                })
    print(f"Gegevens succesvol geëxporteerd naar {filename}")

