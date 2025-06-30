# Importing the 'random' module to enable selection of a random word from the list.
import random

# Step 1: Define a list of possible words for the game.
# One of these words will be randomly chosen for the player to guess.
Words = ["table", "house", "horse", "piano", "chair"]

# Randomly select a word from the list for the game.
# random.choice() selects a single element from the list. # .choice() is method of module random 
Word_To_Guess = random.choice(Words)

# List to keep track of letters guessed by the player.
Guessed_letters = []

# Counter to track the number of incorrect guesses.
Incorrect_Guesses = 0

# Maximum number of incorrect guesses allowed before the game ends.
Max_Guesses = 6

# Now the game loop begins

print(" Welcome to Hangman!")
print("_ " * len(Word_To_Guess))  # Display underscores to represent the letters of the word.

# Main game loop runs until the player exceeds the maximum number of incorrect guesses
# or successfully guesses the entire word.
while Incorrect_Guesses < Max_Guesses:
    # Prompt the player to guess a letter. Convert input to lowercase to ensure consistency.
    guess = input("Guess a letter: ").lower()

    # Check if the letter has already been guessed.
    if guess in Guessed_letters:
        print("You already guessed that letter.")
        continue  # Skip to the next iteration.

    # Add the current guess to the list of guessed letters.
    Guessed_letters.append(guess)

    # Check whether the guessed letter is in the word.
    if guess in Word_To_Guess:
        print("✅ Correct guess!")
    else:
        # If the guess is incorrect, increment the counter and inform the player.
        Incorrect_Guesses += 1
        remaining_tries = Max_Guesses - Incorrect_Guesses
        print(f"❌ Wrong guess! You have {remaining_tries} tries left.")

    # Display the current state of the word with guessed letters and underscores.
    current_state = ""
    for letter in Word_To_Guess:
        if letter in Guessed_letters:
             current_state += letter + " " 
        else:
            current_state += "_ "

    # It shows progres to player 
    print("Word:", current_state)

    # Check if all letters in the word have been guessed.
    if all(letter in Guessed_letters for letter in Word_To_Guess):
        print("🎉 Congratulations! You guessed the word:", Word_To_Guess)
        break  # Exit the loop if the player wins.

# If the loop ends without a correct guess, the player loses.
else:
    print("💀 Game Over! The word was:", Word_To_Guess)