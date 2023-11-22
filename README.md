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

### `display_welcome_message()`
This function displays a welcome message at the beginning of the game. It explains the rules of Wordle, making sure players understand how to play before they start guessing. The message includes:
- The number of attempts players have (6 attempts).
- The requirement for the guess (a valid 5-letter English word).
- The feedback system for each guess:
  - (✓): Correct letter in the correct position.
  - (?): Correct letter in the wrong position.
  - (✗): Incorrect letter.

### Example Usage
```python
def main():
    valid_words = load_dictionary("valid_words.txt")
    answer_words = load_dictionary("answer_words.txt")
    if valid_words and answer_words:
        display_welcome_message()  # Display the welcome message
        play_wordle(valid_words, answer_words)
    else:
        print("Game cannot start without word lists.")
```

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
# Deployment

## Heroku Deployment
This Python Wordle game is deployed on Heroku, making it accessible to anyone with an internet connection. Deploying on Heroku offers a simple and effective way to host Python applications and make them available to a wide audience.

### Accessing the Game
To play the game, simply click on the following link: [Play Python Wordle on Heroku](https://your-heroku-app-link.com)

This link will take you directly to the game hosted on Heroku. There's no need to install anything; just click the link and start playing!

### How It's Deployed
The game was deployed on Heroku by following these steps:
1. Create a `Procfile` and `requirements.txt` to specify the Python dependencies and entry point for the application.
2. Set up a Heroku app through the Heroku dashboard or Heroku CLI.
3. Link the Heroku app to the GitHub repository containing the project.
4. Deploy the application directly from the repository.

Heroku automatically detects the necessary buildpacks and environment settings to host the Python application. Once deployed, the application is accessible via the provided URL.

### Installation
Clone the repository or download the files and store them in your preferred directory.

### Starting the Game
Run main.py from your Python interpreter to start the game.

# Acknowledgements

I would like to extend my heartfelt gratitude to several individuals and groups who played a pivotal role in the realization of this project.

Firstly, a special thanks to the YouTube channel [Code Entropy](https://www.youtube.com/@Code_Entropy) for being a source of inspiration and providing valuable code snippets that greatly influenced my approach to this project. The insights and ideas presented on this channel were instrumental in shaping the development of this Python Wordle game.

I also want to express my sincere appreciation to everyone at the Code Institute. The unwavering support and guidance from the faculty and staff have been remarkable. Their expertise and encouragement have been crucial in my journey as a Full-Stack Software Development student and have significantly contributed to my growth and learning.

Lastly, but certainly not least, I owe a profound thank you to my family. Your support and belief in my dreams have made all of this possible. Your constant encouragement and faith in my abilities have been a source of strength and motivation. I am grateful for your endless love and support.

This project is not just a reflection of my hard work but also a testament to the support and inspiration provided by each one of you.

Thank you.

Nelson Mehlis
