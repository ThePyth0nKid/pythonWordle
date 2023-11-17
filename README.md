# Python Wordle Project

## Introduction
This project represents my third portfolio project as a Full-Stack Software Development student at the Code Institute. My journey to this particular project began with a phase of research and inspiration-seeking on YouTube. It was there that I stumbled upon the fascinating concept of the Wordle game. Intrigued by its simplicity and challenge, I decided to implement my own version of it.

The specific inspiration for this project came from a YouTube video, which can be found [here](https://www.youtube.com/watch?v=GPekrrKcymA). This video provided a foundation, but I aimed to add my unique touch. Before diving into coding, I spent time on Miro, a collaborative visual platform, to brainstorm and visualize my ideas. This pre-coding phase was crucial as it allowed me to lay out a clear plan and structure for the implementation.

After this careful planning, I transformed these visualized concepts into code, making several modifications to the original idea to better fit my vision. These alterations were not just in terms of functionality but also in making the code more efficient and user-friendly. This project not only served as a significant learning experience but also as a testament to my growth and skills as a budding Full-Stack Developer. Miro board can be found [here](https://miro.com/app/board/uXjVNNiPdoY=/?share_link_id=329398393965)

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

```python
def load_dictionary(file_path):
    try:
        with open(file_path, 'r') as file:
            words = [line.strip().lower() for line in file if line.strip()]
        return words
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
```

### `is_valid_guess(guess, valid_words)`
This function checks if the player's guess is valid. A valid guess is a five-letter alphabetical word that exists in the list of valid words.

```python
def is_valid_guess(guess, valid_words):
    return guess.isalpha() and len(guess) == 5 and guess in valid_words
```
### `evaluate_guess(guess, secret_word)`
This function evaluates the player's guess against the secret word, providing letter-by-letter feedback. It indicates whether each letter in the guess is correct and in the right position, correct but in the wrong position, or not in the word at all.

```python
def evaluate_guess(guess, secret_word):
    feedback = []
    for i in range(5):
        if guess[i] == secret_word[i]:
            feedback.append(f"(✓){guess[i]}")
        elif guess[i] in secret_word:
            feedback.append(f"(?) {guess[i]}")
        else:
            feedback.append(f"(✗) {guess[i]}")
    return ' '.join(feedback)
```
### `play_wordle(valid_words, answer_words)`
The main game loop. It randomly selects a secret word and processes player inputs, providing feedback and checking for the end of the game.

```python
def play_wordle(valid_words, answer_words):
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
```
### `main()`
The main function that loads the word lists and initiates the game if the lists are present. This function serves as the entry point of the game.

```python
def main():
    valid_words = load_dictionary("valid_words.txt")
    answer_words = load_dictionary("answer_words.txt")
    if valid_words and answer_words:
        play_wordle(valid_words, answer_words)
    else:
        print("Game cannot start without word lists.")
```


