import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    max_wrong_guesses = 6
    wrong_guesses = 0

    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    # mask for the hidden word
    displayed_word = ["_" for _ in secret_word]

    while wrong_guesses < max_wrong_guesses and "_" in displayed_word:
        print("\nCurrent word: ", " ".join(displayed_word)))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        






if __name__ == "__main__":
    play_game()
