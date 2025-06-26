import random

# Words to choose randomly from
word_bank = ["apples", "oranges", "crazy", "pencil", "excel"]

# Word picked for this round
word = random.choice(word_bank)

# Holds currently guessed letters and hidden letters
guessed_word = ['_'] * len(word)

# How many attempts the player gets to guess
attempts = 5

# Loop until player wins or uses all attempts
while attempts > 0:
    print("\nCurrent word: " + " ".join(guessed_word))
    guess = input("Guess a letter: ")
    
    # Checks if letter is in word
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print("Great guess!")
    else:
        attempts -= 1
        print("Wrong guess! Attempts left: " + str(attempts))

    # Checks if all letters have been guessed
    if "_" not in guessed_word:
        print("\nCongratulations!! You guessed the word: " + word)
        break
    elif attempts == 0:
        print("\nYou\'ve run out of attempts! The word was: " + word)
