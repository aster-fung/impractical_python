"""Check syllable-counting program against training corpus for haiku."""
import sys
import count_syllables
import load_dictionary
import random


def random_word_list_generation(num_words):
    word_list = []
    for i in range(num_words):
        random_word = random.choice(dictionary)
        word_list.append(random_word)
    return word_list


dictionary = load_dictionary.load('dictionary.txt')
dictionary_range = len(dictionary)

num_words = input('please input number of words to be extracted from the dictionary: ')
valid = False
while not valid:
    try:
        num_words = int(num_words)
        valid = True
    except TypeError:
        print('please input any integer between larger than 0 and {}'.format(
            dictionary_range))


random_word_list = random_word_list_generation(num_words)
random_word_syll_count = []
for word in random_word_list:
    try:
        num_syll = count_syllables.count_syllables(word)
        random_word_syll_count.append(num_syll)
    except KeyError:
        print('word not found', file = sys.stderr)
for i,j in zip(random_word_list, random_word_syll_count):
    print(i,j)






