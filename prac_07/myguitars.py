"""Reads guitars csv file and generates guitar data objects"""

from guitar import Guitar

FILEPATH = 'guitars.csv'

def main():
    guitars = read_guitars_data(FILEPATH)
    output_guitars(guitars)
    guitars += get_new_guitars()
    output_guitars(guitars)
    save_guitars(guitars,FILEPATH)

def save_guitars(guitars,filepath):
    """Save guitars data to file"""
    with open(filepath, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")

def output_guitars(guitars):
    """Print guitars to console"""
    print("These are my guitars:")
    guitars.sort()
    max_name_length = max(len(guitar.name) for guitar in guitars)
    max_cost_length = max(len(str(guitar.cost)) for guitar in guitars)
    for i, guitar in enumerate(guitars, 1):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        print(
            f"Guitar {i}: {guitar.name:>{max_name_length}} ({guitar.year:>4}), worth ${guitar.cost:>{max_cost_length}} {vintage_string}")

def read_guitars_data(filepath):
    """Parse file and return it as a list of guitars"""
    guitars = []
    with open(FILEPATH,'r') as file:
        for line in file:
            parts = line.split(',')
            guitar = Guitar(parts[0],int(parts[1]),float(parts[2]))
            guitars.append(guitar)
    return guitars

def get_new_guitars():
    """Prompt user to input new guitars"""
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
    return guitars

if __name__ == "__main__":
    main()