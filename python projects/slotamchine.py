import random
def spinning(symbols, slot):
    print("Spinning...")
    print()
    
    for _ in range(3):
        slot.append(random.choice(symbols))
    return " | ".join(slot)

def bet(bet_amount, balance):
    if bet_amount > balance:
        print("You do not have enough money to place this bet")
        return 0
    elif bet_amount < 0:
        print("You cannot place a negative bet")
        return 0
    else:
         new_balance = balance - bet_amount
         return new_balance
        
def get_payout(slot, bet_amount):
    payout = 0
    if slot[0] == slot[1] == slot[2]:
        if slot[0] == "🍒":
            payout = bet_amount * 2
        elif slot[0] == "🍋":
            payout = bet_amount * 3
        elif slot[0] == "🍊":
            payout = bet_amount * 4
        elif slot[0] == "⭐️":
            payout = bet_amount * 5
        elif slot[0] == "💀":
            payout = bet_amount * 6
        elif slot[0] == "🛎":
            payout = bet_amount * 7
    return payout
    
def main():
    balance = 100
    is_playing = True
    slot = []
    while is_playing:
        print("Welcome to Ayuen's Slot Machine Game!")
        print(f"You have ${balance} in your account")
        symbols = ["🍒", "🍋", "🍊", "⭐️", "💀", "🛎"]

        print("***************************")
        print(spinning(symbols, slot))
        print()
        print("***************************")

        
        bet_amount = input("Enter your bet amount: ")
        if not bet_amount.isdigit():
            print("Please enter a valid number")
            continue
        balance = bet(bet_amount, balance)
        balance += get_payout(slot, bet_amount)
        slot.clear()
        if balance < 0:
            print("You are out of money")
            break
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            is_playing = False
    print("Thank you for playing")
    print(f"Your final balance is ${balance}")


if __name__ == "__main__":
    main()