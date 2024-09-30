for i in range(1, 21, 2):
    print(i, end=' ')
print()

#a
for i in range(0,101,10):
    print(i, end=' ')
print()

#b
for i in range(20,0,-1):
    print(i, end=' ')
print()

#c
number_of_stars = int(input("Enter number of stars: "))
for star_index in range(number_of_stars):
    print("*",sep='', end='')
print()

#d
number_of_lines = int(input("Enter number of lines: "))
for line_index in range(number_of_lines):
    for star_index in range(line_index+1):
        print("*",sep='', end='')
    print()