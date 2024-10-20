def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        parts = email.split("@")
        parts = parts[0].split(".")
        name = " ".join(parts).title()
        name_confirmation = input(f" Is your name {name}? (Y/N)").upper()
        if name_confirmation == "N":
            name = input("Enter your name: ").title()
        email_to_name[email] = name
        email = input("Email: ")
    for email,name in email_to_name.items():
        print(f"{name} ({email})")
main()
