number = input("Enter the number you want to use: ")
rows = int(input("Enter the number of rows: "))
import time
is_running = True

def diamond_num(number, rows):
    while is_running:
        for row in range (rows):
            for i in range(rows - row -1):
                print(" ", end="")
            for j in range(2 * row + 1):
                print(number, end="")
            time.sleep(0.05)    
            print()
        for row in range (rows - 1, 0, -1):
            for i in range(rows - row):
                print(" ", end="")
            for j in range(2 * row - 1):
                print(number, end="")
            time.sleep(0.05)  
                                        
            print()

diamond_num(number, rows)