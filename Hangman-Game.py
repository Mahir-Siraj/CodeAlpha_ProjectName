# Importing the 'random' module to enable selection of a random word from the list.
import random

# Step 1: Define a list of possible words for the game.
# One of these words will be randomly chosen for the player to guess.
words = ["grapes", "house", "horse", "piano", "chair"]

# Randomly select a word from the list for the game.
# random.choice() selects a single element from the list. # .choice() is method of module random 
word_to_guess = random.choice(words)

# List to keep track of letters guessed by the player.
guessed_letters = []

# Counter to track the number of incorrect guesses.
incorrect_guesses = 0

# Maximum number of incorrect guesses allowed before the game ends.
max_guesses = 6

# Now the game loop begins

print("🎯 Welcome to Hangman!")
print("_ " * len(word_to_guess))  # Display underscores to represent the letters of the word.

# Main game loop runs until the player exceeds the maximum number of incorrect guesses
# or successfully guesses the entire word.
while incorrect_guesses < max_guesses:
    # Prompt the player to guess a letter. Convert input to lowercase to ensure consistency.
    guess = input("Guess a letter: ").lower()

    # Check if the letter has already been guessed.
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue  # Skip to the next iteration.

    # Add the current guess to the list of guessed letters.
    guessed_letters.append(guess)

    # Check whether the guessed letter is in the word.
    if guess in word_to_guess:
        print("✅ Correct guess!")
    else:
        # If the guess is incorrect, increment the counter and inform the player.
        incorrect_guesses += 1
        remaining_tries = max_guesses - incorrect_guesses
        print(f"❌ Wrong guess! You have {remaining_tries} tries left.")

    # Display the current state of the word with guessed letters and underscores.
    current_state = ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            current_state += letter + " "
        else:
            current_state += "_ "

    # Remove trailing whitespace and show progress to the player.
    print("Word:", current_state.strip())

    # Check if all letters in the word have been guessed.
    if all(letter in guessed_letters for letter in word_to_guess):
        print("🎉 Congratulations! You guessed the word:", word_to_guess)
        break  # Exit the loop if the player wins.

# If the loop ends without a correct guess, the player loses.
else:
    print("💀 Game Over! The word was:", word_to_guess)