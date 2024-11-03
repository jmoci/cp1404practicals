class ProgrammingLanguage:
    def __init__(self, name, typing, has_reflection, year):
        self.name = name
        self._typing = typing
        self._has_reflection = has_reflection
        self._year = year
    def __str__(self):
        return f"{self.name}, {self._typing} Typing, Reflection={self._has_reflection}, First appeared in {self._year}"

    def is_dynamic(self) -> bool:
        return self._typing.lower() == 'dynamic'