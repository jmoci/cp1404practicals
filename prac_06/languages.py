"""estimated time 5 min
started at 7:23pm
finished at 7:30pm
total time 7min"""

from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
languages = [python, ruby, visual_basic]

print("The dynamically typed languages are:")
print("\n".join((language.name for language in languages if language.is_dynamic())))