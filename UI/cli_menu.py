# UI/cli_menu.py
import sys
from datetime import datetime
import services.data_handler as data
from models.project import Project
from models.worksession import Worksession

class MainMenu:
    header = "=== Project Time Tracker ==="
    options = {
    1: "Toon alle lopende projecten",
    2: "Voeg nieuw project toe",
    3: "Open project",
    4: "Toon actieve sessie",
    5: "Afsluiten"
    }

    def handle_user_input(self, choice: int) -> None:
        match choice:
            case 1: # Toon alle lopende projecten
                active_project_list = get_all_active_projects()
                while True:
                    print("=== Actieve Projecten ===")
                    for project in active_project_list:
                        print(project)
                    print("=========================")
                    input("Druk op Enter om terug te keren naar het hoofdmenu...")
                    break
            case 2: # Voeg nieuw project toe
                new_project_name = input("Geef de naam van het nieuwe project op: ")
                new_project_description = input("Geef een beschrijving van het nieuwe project op: ")
                data.save_project_to_db()
            case 3: # Open project
                print("Project openen...")
            case 4: # Toon actieve sessie
                print("Toon actieve sessie...")
            case 5: # Afsluiten
                print("Goodbye!")
                exit_program()
            case _:
                print("Ongeldige keuze, probeer het opnieuw.")

class ProjectMenu:
    header = "=== Project Menu ==="
    options = {
    1: "Start nieuwe sessie",
    2: "Stop actieve sessie",
    3: "Bekijk alle sessies",
    4: "Exporteer sessies naar CSV",
    5: "Markeer project als afgewerkt",
    6: "Terug naar hoofdmenu"
    }

    def handle_user_input(self, choice: int) -> None:
        match choice:
            case 1: # Start nieuwe sessie
                print("Nieuwe sessie starten...")
            case 2: # Stop actieve sessie
                print("Actieve sessie stoppen...")
            case 3: # Bekijk alle sessies
                print("Alle sessies bekijken...")
            case 4: # Exporteer sessies naar CSV
                print("Sessies exporteren naar CSV...")
            case 5: # Markeer project als afgewerkt
                print("Project markeren als afgewerkt...")
            case 6: # Terug naar hoofdmenu
                print("Terug naar hoofdmenu...")
            case _:
                print("Ongeldige keuze, probeer het opnieuw.")


def show_menu(menu) -> None:
        print(menu.header)
        for key, value in menu.options.items():
            print(f"{key}. {value}")

def get_all_active_projects() -> list[Project]:
    return data.load_active_projects_from_db()

def get_user_choice(menu) -> int:
    num_of_choices = len(menu.options)
    while True:
        choice = input(f"Maak een keuze (1-{num_of_choices}): ")
        try:
            choice_int = int(choice)
            if 1 <= choice_int <= num_of_choices:
                return choice_int
            else:
                print("Ongeldige keuze, probeer het opnieuw.")
        except ValueError:
            print(f"Voer een geldig nummer in (1-{num_of_choices}).")

def create_new_project() -> Project:
    name = input("Voer de naam van het nieuwe project in: ")
    description = input("Voer een beschrijving voor het nieuwe project in: ")
    new_project = Project(name=name, description=description, work_sessions=[])
    data.save_project_to_db(new_project)
    print("Nieuw project aangemaakt.")
    return new_project

def create_new_worksession() -> Worksession:
    description = input("Voer een beschrijving voor de nieuwe werksessie in: ")
    new_session = Worksession(start_time=datetime.now(), description=description)
    data.save_project_to_db(new_session)
    return new_session

def exit_program() -> None:
    sys.exit(0)

def launch() -> None:
    while True:
        main_menu = MainMenu()
        show_menu(main_menu)
        choice = get_user_choice(main_menu)
        main_menu.handle_user_input(choice)