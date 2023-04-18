# Create a function that will run all the code to run the game as expected. You should begin by creating a new script called milestone_5.py. Copy all the codes in milestone_4.py file into the newly created milestone_5.py file.

# Step 1. Create a function called play_game that takes word_list as a parameter. Inside the function, write the code for the following steps

# Step 1. Create a variable called num_lives and assign it to 5.

# Step 2. Create an instance of the Hangman class. Do this by calling the Hangman class and assign it to a variable called game.

# Step 3. Pass word_list and num_lives as arguments to the game object.

# Step 4. Create a while loop and set the condition to True. In the body of the loop, do the following:
# 1. Check if the <code>num_lives</code> is 0. If it is, that means the game has ended and the user lost. Print a message saying 'You lost!'.
# 2. Next, check if the <code>num_letters</code> is greater than 0. In this case, you would want to continue the game, so you need to call the <code>ask_for_input</code> method. 
# 3. If the <code>num_lives</code> is not 0 and the <code>num_letters</code> is not greater than 0, that means the user has won the game. Print a message saying 'Congratulations. You won the game!'.

# Step 2. Outside the function, call your play_game function to play your game. Don't forget to pass in your list of words as argument to the function.


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
        [Redundant] Defines the attributes of the class
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
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word")
            print(f"You have {self.num_lives} left")
        

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