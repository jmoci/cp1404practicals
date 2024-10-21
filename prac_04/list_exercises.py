def main():
    analyse_numbers() #part 1
    authenticate() #part 2

def authenticate():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    if input("Enter username: ") in usernames:
        print("Access Granted")
    else:
        print("Access Denied")

def analyse_numbers():
    numbers = []
    for i in range(5):
        numbers.append(int(input("Number: ")))
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers {get_average(numbers)}")


def get_average(numbers):
    return sum(numbers) / len(numbers)

main()