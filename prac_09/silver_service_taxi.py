"""This module contains the definition for the class SilverServiceTaxi"""

from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Represents a 'sliver service' taxi"""
    flagfall = 4.5

    def __init__(self, name, fuel,fanciness:float):
        super().__init__(name, fuel)
        self.price_per_km *= fanciness