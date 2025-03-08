number = int(input("Enter the number you want to use: "))
rows = int(input("Enter the number of rows: "))

def diamond_maker(number, rows):
    

    for row in range (rows):
        for i in range(rows - row -1):
            print(" ", end="")
        for j in range(2 * row + 1):
            if number % 2 == 1:
                print(number, end="")
            
        print()
    for row in range (rows - 1, 0, -1):
        for i in range(rows - row):
            print(" ", end="")
        for j in range(2 * row - 1):
            if number % 2 == 1:
                print(number, end="")
            
                                      
        print()

diamond_maker(number, rows)