# main.py

from models.project import Project
from models.worksession import Worksession
from db.database import Database
import UI.cli_menu as cli_menu

def main():
    db = Database()

    while True:
        cli_menu.show_main_menu()
        choice = cli_menu.get_user_choice()

        match choice:
            case 1:
                print("Lijst alle projecten geselecteerd.")
            case 2:
                name = cli_menu.get_project_name()
                print(f"Nieuw project toegevoegd: {name}")
            case 3:
                description = cli_menu.get_session_description()
                print(f"Nieuwe werktijdsessie gestart met beschrijving: {description}")
            case 4:
                print("Beëindig een werktijdsessie geselecteerd.")
            case 5:
                print("Bekijk alle werktijdsessies voor een project geselecteerd.")
            case 6:
                cli_menu.exit_program()
            case _:
                print("Ongeldige keuze, probeer het opnieuw.")

if __name__ == "__main__":
    main()
