import random
import time

def main():
    balance = 100
    is_playing = True
    slot = []

    while is_playing:
        print("**WELCOME TO AYUEN'S SLOT MACHINE GAME!**")
        print(f"You have ${balance} in your account")
        symbols = ["🍒", "🍋", "🍊", "⭐️", "💀", "🛎"]

        
        
        def spinning(symbols, slot):
            for _ in range(3):
                slot.append(random.choice(symbols))
            return " | ".join(slot)

        bet_amount = input("Enter your bet amount: ")
        time.sleep(.5)
        print("---------------------------")
        print("Spinning...")
        time.sleep(.5)
        print("---------------------------")
        time.sleep(1)
        print("***************************")
        print()
        time.sleep(.1)
        print(spinning(symbols, slot))
        time.sleep(.1)
        print()
        print("***************************")

        try:
            bet_amount = float(bet_amount)
            if bet_amount <= 0:
                print("Bet amount must be positive")
                continue
        except ValueError:
            print("Please enter a valid number")
            continue
            
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
            
        balance = bet(bet_amount, balance)

        def get_payout(slot, bet_amount):
            payout = 0
            if slot[0] == slot[1] == slot[2]:
                print(f"You win! JACKPOT!!!") 
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
            elif slot[0] == slot[1] or slot[1] == slot[2] or slot[0] == slot[2]:
                print("You win small payout!")
                payout = bet_amount * 1.5   
            else:
                print("You lose!")
                payout = 0
            return payout
        
        balance += get_payout(slot, bet_amount)
        print(f"Your balance is now ${balance}")
        slot.clear()

        def game_over(balance):
            if balance < 0:
                print(f"GAME OVER!! You are out of money, your balance is ${balance}")
                return False
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again != "y":
                return False
            return True
        is_playing = game_over(balance)

    print("Thank you for playing")
    print(f"Your final balance is ${balance}")

if __name__ == "__main__":
    main()