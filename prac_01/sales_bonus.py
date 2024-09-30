"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

total_sales = float(input("Enter sales($): \n"))
while total_sales >= 0:
    bonus = 0
    if total_sales < 1000:
        bonus = 0.1
    else:
        bonus = 0.15
    print(f"Your bonus is: {bonus*total_sales:.2f}")
    total_sales = float(input("Enter sales($): \n"))
print("Quit Successfully")