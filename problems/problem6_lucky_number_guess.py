"""
This code should get the user to guess a random number between 1 and 10.
If the user is right, congratulate them.
If they're wrong, say if the answer is higher or lower.
Then say what the answer was.
"""

import random
answer = random.randint(1, 10)

guess = int(input("I'm thinking of a number between 1 and 10: "))

# If the number is correct, tell the user
if guess == answer:
    print("You guessed correct")
    # Otherwise, tell them if the answer is higher or lower than their guess
elif guess > answer:
    print("You guessed higher")
else:
    print("You guessed lower")


print('The number was {}'.format(answer))
