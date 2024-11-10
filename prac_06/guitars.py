from prac_06.guitar import Guitar

print("My guitars!")
guitars = []
name = input("Name:").title()
while name != "":
    is_valid_year = False
    while not is_valid_year:
        try:
            year = int(input("Year:"))
            is_valid_year = True
        except ValueError:
            print("Year must be an integer")
    is_valid_cost = False
    while not is_valid_cost:
        try:
            cost = float(input("Cost:").replace("$", ""))
            is_valid_cost = True
        except ValueError:
            print("Cost must be a float")
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(f"{guitar} added.")
    name = input("Name:").title()

print("These are my guitars:")
max_name_length = max(len(guitar.name) for guitar in guitars)
max_cost_length = max(len(str(guitar.cost)) for guitar in guitars)
for i, guitar in enumerate(guitars,1):
    vintage_string = ""
    if guitar.is_vintage():
        vintage_string = "(vintage)"
    print(f"Guitar {i}: {guitar.name:>{max_name_length}} ({guitar.year:>4}), worth ${guitar.cost:>{max_cost_length}} {vintage_string}")