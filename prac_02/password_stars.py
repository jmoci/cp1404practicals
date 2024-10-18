def main():
    min_length = 3
    password_input = get_password(min_length)
    print_hidden_password(password_input)


def print_hidden_password(password_input):
    for i in range(len(password_input)):
        print("*", sep="", end="")
    print()


def get_password(min_length):
    password_input = input("Password: ")
    while len(password_input) < min_length:
        password_input = input(f"Password does not meet minimum length of {min_length}, please try again: ")
    return password_input
main()