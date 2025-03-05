symbol = "$"
rows = int(input("Enter the number of rows: "))

for row in range(rows):
    for space in range(rows - row - 1):
        print(" ", end="")
    for digit in range(2 * row + 1):
        print(symbol, end="")
    print()