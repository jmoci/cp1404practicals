"""This module contains a taxi simulator program"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MAIN_MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    print("Let's drive!")
    display_main_menu()

def display_main_menu():
    # Present the user with a list of menu options
    print(MAIN_MENU)
    choice = input(">>>").upper()
    while choice != 'Q':
        if choice == 'C':
            pass
        if choice == 'D':
            pass
        choice = input(">>>").upper()

if __name__ == '__main__':
    main()