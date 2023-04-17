# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Milestone 1

- In this project, we'll use GitHub to track changes to our code and save them online in a GitHub repo.
An automated bot provided by AI Core automatically creates a new GitHub repo called "Hangman".

## Milestone 2

- This part of the project consists in instantiating the basic code for the hangman software. It is called milestone_2.py.
Milestone 2 is divided into steps:

1. Create a list containing the names of your 5 favorite fruits.

1. Assign a randomly chose word from the fruitlist to a variable. The random.choice method from the random module has been used for this task.

1. Ask the user to input a letter and check that is a single, alphabetic entry.

```python
import random
# create a list with your 5 top favourite fruits and print it to the screen
word_list = ["prickly pear", "lemon", "orange", "cherry", "mulberry"]
print(word_list)

# choose a random element from word_list
word = random.choice(word_list) 
print(word)

guess = input("User, please input a letter")
if len(guess) == 1 and guess.isalpha == True:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
```

## Milestone 3

- The code is now organized into two main functions.

1. ask_for_input iteratively asks the user to input a letter and checks if the input is compatible with the game requirements, i.e. whether the input is a single alphabetic character. If the check is passed, the second function *check_guess* is called.

```python
def ask_for_input():
    while True:
        guess = input("User, please input a letter: ")
        if len(guess) == 1  or guess.isalpha() == True:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess()
```
2. check_guess checks if the alphabetic variable requested by *ask_for_input* belongs to the word that has to be guessed.

```python
def check_guess(guess, word):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess: {guess} is in the word")
    else:
        print(f"Sorry, {guess} is not in the word")
'''