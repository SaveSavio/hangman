import random
word_list = ['pera', 'banana']
word = random.choice(word_list)
word_guessed =  ['_'] * len(word)

num_letters = len(set(word))
word_list = word_list
list_of_guesses = []

print(f"word: {word}")
print(f"word_guessed: {word_guessed}")
print(f"num letters: {num_letters}")

def check_guess(word, guess, word_guessed,num_letters ):
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
        if guess in word:
            print(f"Good guess: {guess} is in the word")
            for idx in range(len(word)):
                if guess == word[idx]:
                    word_guessed[idx] = guess
                    print(f"Index: {idx}, self.word_guessed: {word_guessed}")
            num_letters -= 1
        else:
            num_lives -= 1
            print(f"Sorry, {guess} is not in the word")
            print(f"You have {num_lives} left")

check_guess(word=word, guess="a") 

parola = "Ciao"
parola[0].lower()