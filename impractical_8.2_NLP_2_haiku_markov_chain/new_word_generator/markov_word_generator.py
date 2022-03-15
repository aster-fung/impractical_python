from collections import defaultdict
import logging
import random
from string import ascii_lowercase
import sys

# comment out of enable logging
logging.disable(logging.CRITICAL)  # comment out to enable debug logs
logging.basicConfig(level=logging.DEBUG, format='%(message)s')


def load_dictionary(file):
    """
    read dictionary txt as strings. remove whitespaces
    arg: file name
    return: a list of words
    """
    with open(file) as f:
        word_list = f.read()
    word_list = word_list.replace('\n', '').split()
    return word_list


def filter_dictionary_by_2_letters (word_list):
    """
    arg: list of words import from the dictionary file
    return: a list of words >= 2 len
    """
    word_list_f = [word.lower() for word in word_list if len(word) > 2]
    return word_list_f


def order_2_map(word_list):
    """
    arg: a list of words >= 2 characters
    return: a default dict object of letter mapping at Markov chain order 2
    """
    letter_map = defaultdict(list)
    for word in word_list:
        limit = len(word) - 2
        for index, letter in enumerate(word):
            key = letter + word[index+1]
            next_letter = word[index+2]
            letter_map[key].append(next_letter)
    return letter_map


def order_3_map(word_list):
    """
    arg: a list of words >= 2 characters
    return: a default dict object of letter mapping at Markov chain order 3
    """
    letter_map = defaultdict(list)
    for word in word_list:
        limit = len(word) - 3
        for index, letter in enumerate(word):
            key = letter + word[index+1] + word[index+2]
            next_letter = word[index+3]
            letter_map[key].append(next_letter)
    return letter_map


def order_4_map(word_list):
    """
    arg: a list of words >= 2 characters
    return: a default dict object of letter mapping at Markov chain order 3
    """
    letter_map = defaultdict(list)
    for word in word_list:
        limit = len(word) - 4
        for index, letter in enumerate(word):
            key = letter + word[index+1] + word[index+2] + word[index+3]
            next_letter = word[index+4]
            letter_map[key].append(next_letter)
    return letter_map


def get_next_letter(seed):

    def random_single_tail():
        return random.choice(ascii_lowercase)

    if len(seed) == 2:
        try:
            candidates = order_2_map(seed)
        except KeyError:
            candidates.append(random_single_tail())
    elif len(seed) == 3:
        try:
            candidates = order_3_map(seed)
        except KeyError:
            candidates.append(random_single_tail())
    else:               # len(seed) > 4
        try:
            candidates = order_4_map(seed)
        except KeyError:
            candidates.append(random_single_tail())
    next_letter = random.choice(candidates)
    return next_letter


def word_build(seed, target_length):

    return final


def main():

    print(
        """
        Welcome to English Word Generator
        Words will be made with Markov chain model
        """)

    print('loading the dictionary...')
    word_list = load_dictionary('dictionary.txt')
    word_list = filter_dictionary_by_2_letters(word_list)

    print('mapping letters...')
    two_map_one = order_2_map(word_list)
    three_map_one = order_2_map(word_list)
    four_map_one = order_3_map(word_list)

    valid = False
    while not valid:
        print('please provide leading letters (must be >= 2)')
        user_seed = input('Seed: ')
        print('please enter your target word size (must be longer than leading letters')
        target = input("Target size: ")
        if len(user_seed) < 2 or len(user_seed) > len(target_size) :
            print('please read again the instructions and input again')
            continue
        else:
            valid = True

    again = True
    while again:

if __name__ == '__main__':
    main()