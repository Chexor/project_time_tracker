# main.py

from models.project import Project
from models.worksession import Worksession
from db.database import Database
import UI.cli_menu as cli_menu
import os

def main():
    db = Database()

    while True:
        cli_menu.show_main_menu()
        choice = cli_menu.get_user_choice()
        cli_menu.handle_user_input_main(choice)

if __name__ == "__main__":
    main()
