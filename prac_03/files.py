from token import NUMBER

FILENAME = "output.txt"
NUMBERSFILENAME = "numbers.txt"

#Read user input and write it to file
file = open(FILENAME,'w')
name_input = input("Enter your name: ")
print(name_input,file=file)
file.close()

#Load users name from file and print greeting
file = open(FILENAME,'r')
loaded_name = file.read()
print(f"Hello {loaded_name}")
file.close()

#add first 2 numbers in numbers.txt
with open(NUMBERSFILENAME,'r') as file:
    #Assuming the file only contains numeric digits and will not be changed
    number_1 = int(file.readline())
    number_2 = int(file.readline())
    print(number_1+number_2)

#Sum numbers.txt
with open(NUMBERSFILENAME,'r') as file:
    total = 0
    #to make 'read error' messages clearer
    line_number = 0
    for line in file:
        line_number += 1
        try:
            total += int(line)
        except ValueError:
            print(f"Warning value on line {line_number} is invalid")
    print(total)