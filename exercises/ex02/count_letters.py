"""Counting letters in a string."""

__author__ = "730418254"


# Begin your solution here...
letter: str = input("What letter do you want to search? ")
word: str = input("Enter a word: ")
i: int = 0

counted_letters: int = 0
while i < len(word):
    if letter == word[i]:
        counted_letters = counted_letters + 1
        i = i + 1
    else: 
        i = i + 1

print("Count: " + str(counted_letters))