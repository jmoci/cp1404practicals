"""This module contains the definition for the band class"""

class Band:
    def __init__(self,name):
        self.name = name
        self.musicians = []

    def __str__(self):
        return str([musician for musician in self.musicians])

    def add(self,musician):
        self.musicians.append(musician)

    def play(self):
        messages = []
        for musician in self.musicians:
            messages.append(musician.play())
        return "\n".join(messages)
