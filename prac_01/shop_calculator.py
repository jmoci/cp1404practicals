number_of_items = int(input("Number of items: "))
while number_of_items <= 0:
    number_of_items = int(input("Number of items must be greater than 0. Please try again: "))

price_total = 0
for i in range(number_of_items):
    item_price = float(input("Price of item: "))
    price_total += item_price
if price_total > 100:
    discounted_price = price_total * 0.9
else:
    discounted_price = price_total
print(f"Total price for {number_of_items} item(s) is ${discounted_price:.2f}")
