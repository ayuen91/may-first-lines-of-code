menu = {"banana": 4,
        "apple": 2,
        "orange": 1.5, 
        "pear": 3,
        "grapes": 0.5,
        "watermelon": 5,
        "strawberry": 6,
        "blueberry": 4,
        "peach": 3,}

cart = []
total = 0
print('----------menu----------')
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print('------------------------')

while True:
    food = input("select food(q to quit): ").lower()
    if food == 'q':
            break
    elif menu.get(food) is not None:
            cart.append(food)
print('-------YOUR ORDER--------')
for food in cart:
    total += menu.get(food)
    print(food, end=' ')
print()
print(f"Total: ${total:.2f}")
print('------------------------')
