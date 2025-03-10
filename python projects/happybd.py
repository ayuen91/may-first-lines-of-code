age = int(input("enter your age: "))
name = input("enter your name: ")

def print_birthday(name, age):
    for x in range(age):
        for i in range(age - x - 1):
            print(f" happy Birthday {name} you are {age} years old")
    print()  
print_birthday(name, age)      