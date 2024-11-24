"""This module contains tests for the taxi class"""

from taxi import Taxi

def main():
    my_taxi:Taxi = Taxi("Prius 1",100,1.23)
    my_taxi.drive(40)
    print(my_taxi)
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)

if __name__ == "__main__":
    main()