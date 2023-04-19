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
```

## Milestone 4
- The code has been developed so to become so that the key functions now live under the Hangman class
- The class methods have been extended in functionality

1. The init method defines the attributes of the class. Details provided in the code below
```python
        """
        self.word: the word to be guess. Initialized as a randomly picked word from word_list
        word_guessed: initialised a list of underscores, in string format, of the same length of the word to be guessed
            for each guessed letter, it will show the guessed letter in the correct place
        num_letters: the number of unique letters in self.word
        num_lives: initialises the number of lives, i.e. the wrong tentatives allowed before losing the game. Default = 5)
        word_list: is a list of words that the user has to guess
        list_of_guesses: a list of the guess letters that have already been tried. Initialized to an empty list. 
        """
        self.word = random.choice(word_list)
        self.word_guessed =  ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
```
2. The check_guess method whether the guess appears in the word to be guessed.
If the answer is "yes", it puts the guessed letter(s) in the position in  which they appear in the word.
If not, it prints a message and diminishes the number of lives. Then is prints the number of lives left.
```python
   def check_guess(self, guess):
        """
        Checks if guess (alphabetical single letter) is in word (word to be guessed)
        If guess is in word
            updates word_guessed accordingly
            diminishes num_letters by 1
        If guess is NOT in word
            reduces the number of lives
        """
        # convert to a lower case before comparison
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess: {guess} is in the word")
            for idx in range(len(self.word)):
                if guess == self.word[idx]:
                    self.word_guessed[idx] = guess
                    print(f"Index: {idx}, self.word_guessed: {self.word_guessed}")
            self.num_letters -= 1
            print(f"self.num_letters: {self.num_letters}")
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word")
            print(f"You have {self.num_lives} left")
```
3. The ask_for_input method asks for an input and checks if the input is a single alphabetic value.
It also check if the letter has been already guessed. If the checks are passed, it calls check_guess.
Otheriwise it plots messages asking the user to enter the guess correctly.

```python
           def ask_for_input(self):
        while True:
            guess = input("User, please input a letter: ")
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                # CONFIRM: please note that I am calling check_guess() as a method
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                return
            return
```