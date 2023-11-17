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
        