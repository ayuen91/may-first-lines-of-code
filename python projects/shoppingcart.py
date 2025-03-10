food = []
price = []
total = 0

while True:
    item = input('Enter food item: ')
    if item.upper() == 'Q':  # Check for 'Q' or 'q' to quit
        break  # This breaks the while loop when 'Q' or 'q' is entered
    food.append(item)
    price_input = float(input('Enter price: '))
    price.append(price_input)
    
    print(f"Food: {item} Price: {price_input:.2f}")
    total += price_input
    print(f"Total: {total:.2f}")