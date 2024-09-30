MENU = """G - Enter Score
P - Print Score Result
S - Show Stars
Q - Quit"""

def main():
    print(MENU)
    choice = input(">>> ").upper()
    score = 0
    while choice != "Q":
        if choice == "G":
            score = get_score()
        elif choice == "P":
            print(f"Your result is {get_score_category(score)}!")
        elif choice == "S":
            print(score * "*")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def get_score_category(score):
    if score < 0 or score > 100:
       return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Pass"
    else:
        return "Excellent"

def get_score():
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        score = input("Score must be between 0 and 100. Try again: ")
    return score

main()