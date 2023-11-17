# Python Wordle Project

## Project Overview
The Python Wordle Project is an implementation of the popular word-guessing game Wordle in Python. It aims to provide users with a fun and interactive gameplay experience where they guess a randomly selected 5-letter word within six attempts.

## Game Rules
- Players have 6 attempts to guess the word.
- Each guess must be a valid English word with 5 letters.
- Feedback for each guess:
  - ✓: Correct letter in the correct position
  - ?: Correct letter in the wrong position
  - ✗: Incorrect letter
- The game ends if the word is not guessed within 6 attempts.

## Setup
Ensure the `valid_words.txt` and `answer_words.txt` files are in the same directory as `main.py`.

## Dependencies
- Python 3.x

## Key Code Functions

### `load_dictionary(file_path)`
This function loads a list of words from a specified text file. It handles file-not-found errors and cases where the file is empty, returning an empty list in such cases. This function is crucial for reading both `valid_words.txt` and `answer_words.txt`.

