import random
options = ('rock', 'paper', 'scissors')
answers = random.choice(options)
def game():
    print('Welcome to the rock, paper, scissors game')
    print('-----------------------------------------')
    print('Please choose one of the following options: ')
    print('Rock')
    print('Paper')
    print('Scissors')
    player1 = input("Player 1, enter your choice: ").lower()

    global answers

    if player1 == answers:
        print('It is a tie')
    elif player1 == 'rock' and answers == 'paper':
        print(f'You lose {answers} covers {player1}')
    elif player1 == 'rock' and answers == 'scissors':
        print(f'You win {player1} smashes {answers}')
    elif player1 == 'paper' and answers == 'rock':
        print(f'You win {player1} covers {answers}')
    elif player1 == 'paper' and answers == 'scissors':
        print(f'You lose {answers} cuts {player1}')
    elif player1 == 'scissors' and answers == 'rock':
        print(f'You lose {answers} smashes {player1}')
    elif player1 == 'scissors' and answers == 'paper':
        print(f'You win {player1} cuts {answers}')
    else:
        print('Invalid choice')
        game()
game()
