"""
Randomly returns two numbers between 1 and 6
"""
import random
# Generate two random integer between 1 and 6 (inclusive)
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
# Tell the user what the result was
print(f"You rolled {die1} and {die2}")