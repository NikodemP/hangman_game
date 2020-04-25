# Function that select word for game

import random


def choose_word(min_length=6, filename="cleaned_wordlist.txt"):
    # Minimal length variable must be one number bigger because of "/n" in every line.
    min_line_length = min_length + 1

    with open(filename) as f:
        words = [line for line in f if len(line) >= min_line_length]
    return random.choice(words).rstrip('\n')
