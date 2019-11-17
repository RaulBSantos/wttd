#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys


def mimic_dict(filename: str) -> dict:
    """Returns mimic dict mapping each word to list of words which follow it."""
    with open(filename) as f:
        content = f.read()
    words = content.split()

    dict_res = {'': [words[0]]}
    for w in words:
        dict_res.update({w: get_all_next_words(w, words)})

    dict_res.update({words[-1]: ['']})

    return dict_res


def get_random_word(words_dict: dict, word: str) -> str:
    """If words_dict contains the word as a key, returns a random word.
    Otherwise, returns the first word from words_dict (key= '')."""
    choices = words_dict.get(word)
    if choices:
        word = random.choice(choices)
    else:
        word = words_dict.get('')[0]
    return word


def print_mimic(mimic_dict: dict, word: str) -> str:
    """Given mimic dict and start word, prints 200 random words."""
    words_list = []
    while len(words_list) < 200:
        word = get_random_word(mimic_dict, word)
        if word:
            words_list.append(word)
    res = ' '.join(words_list)
    print(res)
    return res


def get_all_next_words(word: str, words: list) -> list:
    """Returns a list from all words placed at next position to the word
    from parameter"""
    last_index = len(words) - 1
    return [words[i+1] for i, w in enumerate(words)
            if w.lower() == word.lower() and i < last_index]


# Provided main(), calls mimic_dict() and mimic()
def main():
    if len(sys.argv) != 2:
        print('usage: ./mimic.py file-to-read')
        sys.exit(1)

    dict_res = mimic_dict(sys.argv[1])
    print_mimic(dict_res, '')


if __name__ == '__main__':
    main()

    print()
    # Tests `get_all_next_words` function
    words = 'Tudo bem? Tudo ótimo'.split()
    assert get_all_next_words('tudo', words) == ['bem?', 'ótimo']
    assert get_all_next_words('ótimo', words) == []
    assert get_all_next_words('bem?', words) == ['Tudo']

    # Tests `mimic_dict` function - Passing `small.txt` file
    dict_res = mimic_dict(sys.argv[1])
    print_mimic(dict_res, '')
    assert dict_res['we'] == ['are', 'should', 'are', 'need', 'are', 'used']

    print()
    bla_bla_bla = print_mimic(dict_res, 'we')
    words_count = len(bla_bla_bla.split())
    print('\r\n', words_count, 'words written')
    assert words_count == 200
    assert 'we are' in bla_bla_bla
