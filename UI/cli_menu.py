# UI/cli_menu.py
import sys
from models.project import Project

def display_main_menu():
    print("=== Project Time Tracker ===")
    print("1. Lijst alle projecten")
    print("2. Voeg nieuw project toe")
    print("3. Start een nieuwe werksessie")
    print("4. Beëindig een werksessie")
    print("5. Bekijk alle werksessies voor een project")
    print("6. Sluit af")

def get_user_choice() -> int:
        while True:
            choice = input("Maak een keuze (1-6): ")
            try:
                choice_int = int(choice)
                if 1 <= choice_int <= 6:
                    return choice_int
                else:
                    print("Ongeldige keuze, probeer het opnieuw.")
            except ValueError:
                print("Voer een geldig nummer in (1-6).")

def get_project_name() -> str:
    name = input("Voer de naam van het project in: ")
    return name

def get_session_description() -> str:
    description = input("Voer een beschrijving voor de werktijdsessie in: ")
    return description

def exit_program() -> None:
    sys.exit(0)

def main():
    display_main_menu()
    choice = get_user_choice()

    match choice:
        case 1:
            print("Lijst alle projecten geselecteerd.")
        case 2:
            name = get_project_name()
            print(f"Nieuw project toegevoegd: {name}")
        case 3:
            description = get_session_description()
            print(f"Nieuwe werktijdsessie gestart met beschrijving: {description}")
        case 4:
            print("Beëindig een werktijdsessie geselecteerd.")
        case 5:
            print("Bekijk alle werktijdsessies voor een project geselecteerd.")
        case 6:
            exit_program()
        case _:
            print("Ongeldige keuze, probeer het opnieuw.")



