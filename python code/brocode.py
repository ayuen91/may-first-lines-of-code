symbol = input("Enter the symbol you want to use: ")
rows = int(input("Enter the number of rows: "))

def diamond_maker(symbol, rows):
    

    for row in range (rows):
        for i in range(rows - row -1):
            print(" ", end="")
        for j in range(2 * row + 1):
            print(symbol, end="")
        print()

diamond_maker(symbol, rows)