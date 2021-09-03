"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730418254"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")

randint_number: int = randint(1, 4)
if randint_number == 1:
    print("You will meet the love of your life!")
else:
    if randint_number == 2:
        print("Smell the flowers and take in the world!")
    else:
        if randint_number == 3:
            print("Spend time with the people who value you!")
        else: 
            print("Go take on the world, you can do it!")


print("Now, go spread positive vibes!")