# Project Time Tracker

Een CLI-applicatie om gewerkte uren te registreren per project.

## Features
- Voeg projecten toe en beheer ze.
- Registreer gewerkte uren per project.
- Bekijk een overzicht van gewerkte uren per project.
- Exporteer rapporten van gewerkte uren naar CSV-bestand.

## Installation
1. Clone de repository:
   ```bash
   git clone https://github.com/Chexor/project_time_tracker
    ```
2. Navigeer naar de projectmap:
    ```bash
   cd project-time-tracker
   ```
3. creer een virtuele omgeving en activeer deze:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Voor Windows gebruik: venv\Scripts\activate
   ```
4. Installeer de vereiste pakketten:
   ```bash
   pip install -r requirements.txt
   ```
## Usage
Start de applicatie met het volgende commando:
```bash
  python project_time_tracker/main.py
```
Volg de instructies in de CLI om projecten toe te voegen, uren te registreren en rapporten te genereren.

## Technical Details
- Bij opstart wordt een SQLite-database (`project_time_tracker.db`) met tabellen (`projects`, `worksessions`) aangemaakt in de projectmap (indien deze nog niet bestaat).
- Alle data wordt lokaal opgeslagen in de SQLite-database.
- Bij opstart worden alle actieve projecten in het geheugen geladen uit de database.
- Na het selecteren van een project wordt de actieve werksessie (als die bestaat) in het geheugen opgeslagen totdat deze wordt gestopt.
- Gegenereerde CSV-rapporten worden opgeslagen in de map `export/` binnen de projectmap.