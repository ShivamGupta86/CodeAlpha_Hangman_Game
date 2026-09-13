import random

# List of 5 predefined words
words = ["python", "java", "computer", "programming", "developer"]

# Randomly select a word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum incorrect guesses
incorrect_guesses = 6

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses.")

# Game loop
while incorrect_guesses > 0:

    # Display the current word
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses left:", incorrect_guesses)

    # Check if player has won
    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You guessed the word:", word)
        break

    # Take input from player
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add guess to guessed letters
    guessed_letters.append(guess)

    # Check whether guess is correct
    if guess in word:
        print("Correct guess!")
    else:
        incorrect_guesses -= 1
        print("Wrong guess!")

# If player loses
if incorrect_guesses == 0:
    print("\nGame Over!")
    print("The word was:", word)