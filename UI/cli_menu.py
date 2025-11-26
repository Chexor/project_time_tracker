# UI/cli_menu.py
import sys
import os
from models.project import Project

main_menu_options = {
    1: "Toon alle lopende projecten",
    2: "Voeg nieuw project toe",
    3: "Open project",
    4: "Toon actieve sessie",
    6: "Afsluiten"
    }

project_menu_options = {
    1: "Start nieuwe sessie",
    2: "Stop actieve sessie",
    3: "Bekijk alle sessies",
    4: "Exporteer sessies naar CSV",
    5: "Markeer project als afgewerkt",
    6: "Terug naar hoofdmenu"
    }

def show_main_menu():
    print("=== Project Time Tracker ===")
    for key, value in main_menu_options.items():
        print(f"{key}. {value}")

def show_project_menu():
    print("=== Project Menu ===")
    for key, value in project_menu_options.items():
        print(f"{key}. {value}")

def display_project_menu():
    projectlist = {}
    print("=== Project Menu ===")
    for project in Project.get_all_projects():
        projectlist[project.id] = project
        print(f"{project.id}. {project.name} - Active: {project.is_active}")
    print("0. Terug naar hoofdmenu")

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

def get_project_name_from_user() -> str:
    name = input("Voer de naam van het project in: ")
    return name

def get_session_description_from_user() -> str:
    description = input("Voer een beschrijving voor de werktijdsessie in: ")
    return description

def exit_program() -> None:
    sys.exit(0)

def handle_user_input_main(choice: int):
    match choice:
        case 1: # Toon alle lopende projecten
            while True:
                print("=== Active Projects ===")
            # Hier zou je de logica toevoegen om actieve projecten weer te geven
        case 2: # Voeg nieuw project toe
            name = get_project_name()
            print(f"Nieuw project toegevoegd: {name}")
        case 3: # Open project
            description = get_session_description()
            print(f"Nieuwe werktijdsessie gestart met beschrijving: {description}")
        case 4: # Toon actieve sessie
            print("Beëindig een werktijdsessie geselecteerd.")
        case 5: # Bekijk alle sessies
            print("Bekijk alle werktijdsessies voor een project geselecteerd.")
        case 6:
            exit_program()
        case _:
            print("Ongeldige keuze, probeer het opnieuw.")