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
