# insert docstring here

import random

class Hangman:
    """
    This class defines the game Hangman.
    The class is structured following the instructions of the AI Core Hangman project (milestone #4)
    Attributes:
        word_list is a list of words that the use has to guess
        num_lives is the number of wrong tentative before losing the game (5 by default)
    """

    def __init__(self, word_list, num_lives = 5) -> None: # need to remember how's this thing! called
        """
        self.word: randomly picks a word to be guessed from word_list
        word_guessed: initialises a list of underscores, in string format, of the same length of the word to be guessed
        num_letters: the number of unique letters in the string to be guessed
        num_lives: initialises the number of lives, i.e. the wrong tentatives allowed before losing the game (default = 5)
        word_list: is a list of words that the user has to guess
        list_of_guesses: a list of the guesses that have already been tried. Set this to an empty list initially. 
        """
        self.word = random.choice(word_list)
        self.word_guessed =  ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        """
        """
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess: {guess} is in the word")
            # lambda x: x**2 if (x%2) == 0 else x**3

        #else:
        #   print(f"Sorry, {guess} is not in the word")

    def ask_for_input(self):
        while True:
            guess = input("User, please input a letter: ")
            if guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            elif guess.isalpha() == True and guess not in self.list_of_guesses:
                check_guess(guess)
                self.list_of_guesses.append(guess)
