"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

from random import randint

def main():
    score = float(input("Enter score: "))
    print(get_score_category(score))

    random_score = randint(0, 100)
    print(f"Random: {get_score_category(random_score)}")

def get_score_category(score):
    if score < 0 or score > 100:
       return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Pass"
    else:
        return "Excellent"

main()