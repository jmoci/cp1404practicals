from datetime import datetime
class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        return f"{self.name}, start: {self.start_date.strftime("%d/%m/%Y")}, priority {self.priority}, estimate: ${self.cost_estimate}, completion: {self.completion_percentage}%"
    def __lt__(self, other):
        return self.priority < other.priority