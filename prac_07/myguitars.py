"""Reads guitars csv file and generates guitar data objects"""

from guitar import Guitar

FILEPATH = 'guitars.csv'

def main():
    parse_file(FILEPATH)

def parse_file(filepath:str):
    with open(FILEPATH,'r') as file:
        for line in file:
            parts = line.split(',')
            guitar = Guitar(parts[0],int(parts[1]),float(parts[2]))
            print(guitar)

if __name__ == "__main__":
    main()