# main.py
from UI.cli_handler import MainMenu
from models.project import Project
from models.worksession import Worksession
from db.database import Database
import UI.cli_handler as cli
import os

def main():
    db = Database()
    #active_projects = db.load_active_projects()

    cli.launch()


if __name__ == "__main__":
    main()
