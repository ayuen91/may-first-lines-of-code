food = input("What is your favorite food? ")
while not food in ('q', 'quit', 'Quit', 'Q'):
    print(f'Your favorite food is {food} ')
    food = input("What is your other favorite food (press q to quit)? ")
print('bye')