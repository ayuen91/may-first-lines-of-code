balance = 0

def check_balance():
    print('***********************************')
    print(f'your current balance is ${balance:.2f}')
    print('***********************************')

def deposit():
    amount = float(input("Enter amount to deposit: "))
    if amount < 0:
        print("Invalid amount")
        return 0
    else:
        return amount

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print(f'insufficient funds. Your current balance is ${balance:.2f}')
        return 0
    else:
        return amount

def main():
    global balance
    is_running = True
    while is_running:
        print('-----------------------------------')
        print("Welcome to the banking system")
        print("Please choose an option: ")
        print('--------------------------------')
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Quit")
        print('-----------------------------------')
        choice = int(input("Enter your choice: "))
                        
        if choice == 1:
            check_balance()
        elif choice == 2:
            amount = deposit()
            balance += amount
            check_balance()
        elif choice == 3:
            amount = withdraw()
            balance -= amount
            if amount > 0:
                check_balance()
        elif choice == 4:
            is_running = False
            print('--------------------------------------')
            print("Thank you for using the banking system")
            print('--------------------------------------')
        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()