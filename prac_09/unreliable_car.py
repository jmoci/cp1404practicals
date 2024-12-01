"""This module contains the definition for the UnreliableCar class"""

from car import Car
from random import randint

class UnreliableCar(Car):
    """Represents an unreliable car"""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        # Chance based on reliability field to drive the car a given distance
        if randint(0, 100) < self.reliability:
            return super().drive(distance)
        return 0