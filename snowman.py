"""
snowman.py

The main and logic part of the game.
"""

import random
import ascii_art as ar
# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def display_game_state(wrong_guesses, secret_word, guessed_letters):
    """Draw the snowman and show the 'smelting' state of the game."""

    print(ar.STAGES[wrong_guesses])

    displayed_word = [letter if letter in guessed_letters
                      else "_" for letter in secret_word]
    print("Word: " + " ".join(displayed_word))

    print("Guessed letters: ", " ".join(guessed_letters))
    print(f"Mistakes: {wrong_guesses}/{len(ar.STAGES) - 1}")


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    """The game loop to start, ask for letter,
    check for right or wrong input."""
    secret_word = get_random_word()
    guessed_letters = []
    max_wrong_guesses = 4
    wrong_guesses = 0

    print("Welcome to Snowman Meltdown!")

    # mask for the hidden word
    displayed_word = ["_" for _ in secret_word]

    while (wrong_guesses < max_wrong_guesses
           and "_" in displayed_word):
        print("\n---- Game State ----")
        display_game_state(wrong_guesses, secret_word, guessed_letters)

        guess = input("Guess a letter: ").lower()

        # Check for empty input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # Check for same letter input
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        # Check for wrong or right letter input
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
            for item, letter in enumerate(secret_word):
                if letter == guess:
                    displayed_word[item] = guess
        else:
            wrong_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"Snowman is melting... ")

    # Finish the game
    if "_" not in displayed_word:
        print(f"\nCongrats! You guessed the word: '{secret_word}'")
    else:
        print(f"\nThe snowman is melted! The word was: '{secret_word}'")



if __name__ == "__main__":
    play_game()
