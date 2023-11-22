import random


def load_dictionary(file_path):
    """
    Safely loads a list of words from a text file.
    Handles file not found errors and empty file cases.
    """
    try:
        with open(file_path, 'r') as file:
            words = [line.strip().lower() for line in file if line.strip()]
        return words
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []


def display_welcome_message():
    """
    Displays a welcome message and explains the rules of the game.
    """
    print("Welcome to Python Wordle!")
    print("Rules of the Game:")
    print("1. You have 6 attempts to guess a 5-letter word.")
    print("2. Each guess must be a valid 5-letter English word.")
    print("3. After each guess, you will receive feedback:")
    print("   - (✓): Correct letter in the correct position.")
    print("   - (?): Correct letter in the wrong position.")
    print("   - (✗): Incorrect letter.")
    print("Try to guess the word in as few attempts as possible. Good luck!\n")


def is_valid_guess(guess, valid_words):
    """
    Checks if the guess is valid.
    """
    return guess.isalpha() and len(guess) == 5 and guess in valid_words


def evaluate_guess(guess, secret_word):
    """
    Evaluates the guess against the secret word, providing feedback.
    """
    feedback = []
    for i in range(5):
        if guess[i] == secret_word[i]:
            feedback.append(f"(✓){guess[i]}")
        elif guess[i] in secret_word:
            feedback.append(f"(?) {guess[i]}")
        else:
            feedback.append(f"(✗) {guess[i]}")
    return ' '.join(feedback)


def play_wordle(valid_words, answer_words):
    """
    Main game loop for Wordle.
    """
    secret_word = random.choice(answer_words)
    attempts = 0

    while attempts < 6:
        guess = input(f"Enter guess #{attempts+1}: ").lower()

        if not is_valid_guess(guess, valid_words):
            print("Invalid guess. Try a different 5-letter word.")
            continue

        print(evaluate_guess(guess, secret_word))
        if guess == secret_word:
            print("Congratulations! You've guessed the word correctly!")
            break
        attempts += 1

    if attempts == 6:
        print(f"Game Over. The secret word was: {secret_word}")

    if input("Play again? (y/n): ").lower() == 'y':
        play_wordle(valid_words, answer_words)


def main():
    valid_words = load_dictionary("valid_words.txt")
    answer_words = load_dictionary("answer_words.txt")
    if valid_words and answer_words:
        display_welcome_message()  # Display the welcome message
        play_wordle(valid_words, answer_words)
    else:
        print("Game cannot start without word lists.")


if __name__ == "__main__":
    main()
