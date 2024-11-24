"""This module contains the definition for the band class"""
from musician import Musician


class Band:
    def __init__(self,name):
        self.name = name
        self.musicians = []

    def add(self,musician:Musician):
        self.musicians.append(musician)