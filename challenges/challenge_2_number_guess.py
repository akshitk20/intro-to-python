"""
Number guessing game
The number to guess will be from 1 to 20 (inclusive).
The user will have 4 guesses to guess the number correctly.
After each wrong guess, the user will be told whether to
guess higher or lower next time.
If the user doesn't win, tell them the number.
"""
import random


def run_game():
    answer = random.randint(1, 20)

    print("I'm thinking of a number between 1 and 20")
    x = 3
    while x >= 0:
        guess = int(input("Guess a number: "))
        if answer == guess:
            print("Correct!")
            return
        elif answer > guess:
            print("Higher")
        else:
            print("Lower")
        x = x - 1


run_game()
