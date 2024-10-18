from random import randint
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6
def main():
    number_of_picks = int(input("How many quick picks? "))
    while number_of_picks < 0:
        number_of_picks = int(input("That is not a valid number, try again: "))
    for i in range(number_of_picks):
        quick_pick = []
        for j in range(NUMBERS_PER_PICK):
            number = randint(MIN_NUMBER, MAX_NUMBER)
            while number in quick_pick:
                number = randint(MIN_NUMBER, MAX_NUMBER)
            quick_pick.append(number)
            quick_pick.sort()
        print(" ".join([str(num) for num in quick_pick]))
main()