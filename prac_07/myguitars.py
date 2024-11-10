"""Reads guitars csv file and generates guitar data objects"""

from guitar import Guitar

FILEPATH = 'guitars.csv'

def main():
    guitars = read_guitars_data(FILEPATH)
    guitars.sort()
    for guitar in guitars:
        print(guitar)

def read_guitars_data(filepath:str):
    """Parse file and return it as a list of guitars"""
    guitars = []
    with open(FILEPATH,'r') as file:
        for line in file:
            parts = line.split(',')
            guitar = Guitar(parts[0],int(parts[1]),float(parts[2]))
            guitars.append(guitar)
    return guitars

if __name__ == "__main__":
    main()