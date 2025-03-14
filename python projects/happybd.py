age = int(input("enter your age: "))
name = input("enter your name: ")
import time
def print_birthday(name, age):
    for x in range(age):
        for i in range(1, age - 1):
            print(f" happy Birthday {name} you are {age} years old")
            time.sleep(1)
    print()  
print_birthday(name, age)      