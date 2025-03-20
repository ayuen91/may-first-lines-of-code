def check_balance(balance):
    print('***********************************')
    print(f'your current balance is ${balance:.2f}')
    print('***********************************')
    return balance
def deposit():
    amount = float(input("Enter amount to deposit: "))
    if amount < 0:
        print("Invalid amount")
        return 0
    else:
        return amount
def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print(f'insufficient funds. Your current balance is ${balance:.2f}')
    else:
        return amount

balance = 0    
def main():
    
    print('-----------------------------------')
    print("Welcome to the banking system")
    print("Please choose an option: ")
    print('--------------------------------')
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Quit")
    print('-----------------------------------')
    choice = float(input("Enter your choice: "))
                    
    if choice == 1:
        check_balance(balance)
    elif choice == 2:
        amount = deposit()
        balance += amount
        print('***********************************')
        print(f'your current balance is ${balance:.2f}')
        print('***********************************')
    elif choice == 3:
        withdraw(amount)
        balance -= amount
        
        
    elif choice == 4:
        print("Thank you for using the banking system")
    else:
        print("Invalid choice")
    
main()
if __name__ == '__main__':
    main()