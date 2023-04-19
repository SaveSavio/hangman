
# Functions that allows to play the game by calling the defining the parameters and calling the class Hangman
def play_game(word_list):
    # Define the numbers of lives for the game, then pass it as a parameter when instantiating Hangman
    num_lives = 5
    # Create an instance of the Hangman class.
    game = Hangman(word_list=word_list, num_lives=num_lives)
    while True:
    # Check if the player has any lives left
        if game.num_lives == 0:
            print("You lost!")
            break
        # Check if num_letters is > 0, i.e. if there are any letters to be guessed
        if game.num_letters > 0:
            # call the function that asks the player to input
            print(f"the number of lives is {game.num_lives}")
            print(f"the number of letters is {game.num_letters}")
            game.ask_for_input()
        # if the user has still lives left and there is no letter to be guessed, then it won
        if game.num_lives != 0 and game.num_letters <= 0:
            print(f"the number of lives is {game.num_lives}")
            print(f"the number of letters is {game.num_letters}")
            print("Congratulations! You have won the game")



import random

class Hangman:
    """
    This class defines the game Hangman.
    The class is structured following the instructions of the AI Core Hangman project (milestone #4)
    Attributes:
        word_list is a list of words that the use has to guess
        num_lives is the number of wrong tentative before losing the game (5 by default)
    """

    def __init__(self, word_list, num_lives = 5): # TO DO: need to remember how's this thing! called
        """
        Arguments:
            num_lives: initialises the number of lives, i.e. the wrong tentatives allowed before losing the game. Default = 5)
            word_list: is a list of words that the user has to guess
        self.word: the word to be guess. Initialized as a randomly picked word from word_list
        word_guessed: initialised a list of underscores, in string format, of the same length of the word to be guessed
            for each guessed letter, it will show the guessed letter in the correct place
        num_letters: the number of unique letters in self.word
        
        list_of_guesses: a list of the guess letters that have already been tried. Initialized to an empty list. 
        """
        self.word = random.choice(word_list)
        print(f"init: self.word: {self.word}")
        self.word_guessed =  ['_'] * len(self.word)
        print(f"init: self.word_guessed: {self.word_guessed}")
        self.num_letters = len(set(self.word))
        print(f"init: num_letters: {self.num_letters}")
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
            self.num_letters += -1
            #return self.num_letters
        else:
            self.num_lives += -1
            print(f"Sorry, {guess} is not in the word")
            print(f"You have {self.num_lives} lives left")
            #return self.num_lives
    
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

word_list = ["abcdef", "abc"]
             #lemon", "orange", "cherry", "mulberry"]
play_game(word_list)