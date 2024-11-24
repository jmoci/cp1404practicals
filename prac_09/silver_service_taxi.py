"""This module contains the definition for the class SilverServiceTaxi"""

from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Represents a 'sliver service' taxi"""
    flagfall = 4.5

    def __init__(self, name, fuel,fanciness:float):
        super().__init__(name, fuel)
        self.price_per_km *= fanciness

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        # Get the cost of the current fare
        return self.flagfall + self.price_per_km * self.current_fare_distance