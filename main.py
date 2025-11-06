# -*- coding: utf-8 -*-

import sys

from src.database import create_database, create_tables

create_database()
create_tables()



# def show_menu():
#     print("""
#           \n=== Project Time Tracker ==="
#           1. Add project
#           2. Start session
#           3. End session
#           """)
          
# def selection_handler(selection):
#     if selection == 1:
        
#     if selection == 2:
        
#     if selection == 3: 
        
# def main():
#     while True:
#         show_menu()
#         selection = int(input("Kies een optie: ").strip())
#         selection_handler(selection)