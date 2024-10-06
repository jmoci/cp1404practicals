
"""Answers to questions:
1. Any integer between 5 and 20 inclusive on both ends
2. 3,5,7 or 9 is the set of possible return values. Function returns random number between 3 and 10 inclusive with a step of 2. Could not have produced a 4.
3. returns a random floating point number between 2.5 and 5.5. Function documents the smallest possible number as a (2.5) and the largest b (5.5).
"""
import random
#Random float
print(f"Random float: {random.uniform(1,100)}")
#Random int
print(f"Random int: {random.randint(1,100)}")