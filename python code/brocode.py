import getpass
name = input("Enter your name: ")
password = getpass.getpass("Enter your password: ")


print(f"Your name has {len(name)} characters {name.upper()} your password is {password}" )