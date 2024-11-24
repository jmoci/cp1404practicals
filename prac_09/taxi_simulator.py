"""This module contains a taxi simulator program"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MAIN_MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    print("Let's drive!")
    display_main_menu()

def display_main_menu():
    # Present the user with a list of menu options
    #chosen_taxi = None
    bill = 0
    chosen_taxi = Taxi("Toyota 1",100)
    print(MAIN_MENU)
    choice = input(">>>").upper()
    while choice != 'Q':
        if choice == 'C':
            pass
        if choice == 'D':
            bill += handle_drive_taxi(chosen_taxi)
            print(f"Bill to date: ${bill:.2f}")
        print(MAIN_MENU)
        choice = input(">>>").upper()

def handle_drive_taxi(taxi):
    if taxi is None:
        print("You need to choose a taxi before you can drive")
        return 0
    input_valid = False
    while not input_valid:
        try:
            distance = float(input("Drive how far?"))
            if distance < 0:
                print("Distance must be a positive number")
            else:
                input_valid = True
                taxi.start_fare()
                taxi.drive(distance)
                print(f"Your {taxi.name} trip cost you {taxi.get_fare()}")
                return taxi.get_fare()
        except ValueError:
            print("Distance must be a valid number")
if __name__ == '__main__':
    main()