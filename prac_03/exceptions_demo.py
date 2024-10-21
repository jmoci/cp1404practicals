"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?

Answers:
1.When the input cannot be cast to an integer which happens when the input string contains non-numeric characters
i.e. when the user does not enter a number.
2. If the denominator is 0
3. Yes. We could use input validation to either exit when the input is invalid or ask the user to
input a valid value while the value is invalid.
"""
from charset_normalizer.utils import is_arabic

"""
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
"""

is_valid_input = False
while not is_valid_input:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        if denominator == 0:
            print("Denominator cannot be zero! Try again.")
        else:
            is_valid_input = True
    except ValueError:
        print("Numerator and denominator must be valid numbers! Try again.")
print(numerator/denominator) #No possibility of undefined values