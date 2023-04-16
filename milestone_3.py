
# The check_guess function will take the guessed letter as an argument and check if the letter is in the word.
# Step 1: Define a function called check_guess. pass in the guess as a parameter for the function. Write the code for the following steps in the body of this function.
# Step 2: Convert the guess into lower case.
# Step 3. Move the code that you wrote to check if the guess is in the word into this function block.

# import necessary packages
import random
# create a list with your 5 top favourite fruits and print it to the screen
word_list = ["prickly pear", "lemon", "orange", "cherry", "mulberry"]

# choose a random element from word_list
word = random.choice(word_list) 
print(word)

def check_guess(guess, word):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess: {guess} is in the word")
    else:
        print(f"Sorry, {guess} is not in the word")

# The ask_for_input function.
# Step 1. Define a function called ask_for_input.
# Step 2. Move the code that you wrote in the Iteratively check if the input is a valid guess task into this function block.
# Step 3. Outside the while loop, but within this function, call the check_guess function to check if the guess is in the word. Don't forget to pass in the guess as an argument to the method.
# Step 4. Outside the function, call the ask_for_input function to test your code.

def ask_for_input():
    while True:
        guess = input("User, please input a letter: ")
        if len(guess) == 1  or guess.isalpha() == True:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess()

ask_for_input()
