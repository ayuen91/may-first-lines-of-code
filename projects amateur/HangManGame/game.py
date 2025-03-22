import random
from assets import words
from assets import hangman_art

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        def dispay_hangman(wrong_guesses):
            for line in hangman_art[wrong_guesses]:
                print(line)
            print()
        dispay_hangman(wrong_guesses)

        def display_hint(hint):
            print(" ".join(hint))
            print()
        display_hint(hint)

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.add(guess)
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        def display_answer(answer):
            print(f"The word was: {answer}")
            print()
            
        if "_" not in hint:
            dispay_hangman(wrong_guesses)
            display_answer(answer)
            print("You win!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            dispay_hangman(wrong_guesses)
            display_answer(answer)
            print("You lose!")
            is_running = False
if __name__ == "__main__":
    main()