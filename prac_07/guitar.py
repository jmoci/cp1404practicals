class Guitar:
    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self,other):
        return self.get_age() <= other.get_age()

    def get_age(self):
        #Change this to use the current year if functionality is required beyond 2024
        return 2024 - self.year

    def is_vintage(self):
        return self.get_age() >= 50