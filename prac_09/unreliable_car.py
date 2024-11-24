"""This module contains the definition for the UnreliableCar class"""

from car import Car
from random import randint

class UnreliableCar(Car):
    """Represents an unreliable car"""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability