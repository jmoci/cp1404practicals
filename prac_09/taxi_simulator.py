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
    chosen_taxi = None
    print(MAIN_MENU)
    choice = input(">>>").upper()
    while choice != 'Q':
        if choice == 'C':
            chosen_taxi = handle_choose_taxi()
        if choice == 'D':
            bill += handle_drive_taxi(chosen_taxi)
            print(f"Bill to date: ${bill:.2f}")
        print(MAIN_MENU)
        choice = input(">>>").upper()

def handle_choose_taxi():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Taxis available:")
    for taxi_index in range(len(taxis)):
        print(f"{taxi_index} - {taxis[taxi_index]}")
    input_valid = False
    while not input_valid:
        try:
            choice = int(input("Choose taxi: "))
            if 0 <= choice < len(taxis):
                input_valid = True
                return taxis[choice]
            else:
                print(f"Choice must be between 0 and {len(taxis)-1}")
        except ValueError:
            print("Choice must be a number")


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