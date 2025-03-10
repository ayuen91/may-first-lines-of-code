highest_num = 100
lowest_num = 1 

guesses = 0
is_active = True
import random
answer = random.randint(lowest_num, highest_num)

while is_active:
    guess = input('Enter your guess: ')
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess == answer:
            print(f'You got the correct answer, it took you {guesses} guesses')
            is_active = False
        elif guess > answer:
            print('Please guess lower')
        elif guess < answer:
            print('Please guess higher')


    else:
        guess = input('Please !!! Enter your guess: ')