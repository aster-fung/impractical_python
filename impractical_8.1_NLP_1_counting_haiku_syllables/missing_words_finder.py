import sys
from string import punctuation
import pprint
import json
from nltk.corpus import cmudict


def load_haiku(filename):
    """
    opens and return training corpus of haiku as a set
    """
    with open(filename) as in_file:
        haiku = set(in_file.read().replace('-', ' ').split())
    return haiku


def cmudict_missing(word_set):
    """find and return words in word set missing from cmudict"""
    exceptions = set()
    for word in word_set:
        word = word.lower().strip(punctuation)
        if word.endswith("'s") or word.endswith("`s"):
            word = word[:-2]
        if word not in cmudict:
            exceptions.add(word)
    print('\nexceptions: ')
    print(*exceptions, sep='; ')
    print('\nNumber of unique words in haiku corpus = {}'.format(len(word_set)))
    print('\nNumber of words not in CMUdict = {}'.format(len(exceptions)))
    membership = (1-(len(exceptions)/len(word_set)))*100
    # to evaluate the percentage of words in haiku vs cmudict
    print('CMUmembership = {:1f}{}'.format(membership, '%'))
    return exceptions


def make_exceptions_dict(exceptions_set):
    """return dictionary of words and syllable counts (phenomes) from a set of words"""
    missing_words = {}
    print('input syllables in word. mistakes can be corrected later \n')
    for word in exceptions_set:
        valid_input = False
        while not valid_input:
            num_sylls = input('Enter number syllabus in {}: '.format(word))
            if num_sylls.isdigit():
                valid_input = True
            else:
                print('please input an integer to count syllables of the word')
        missing_words[word] = int(num_sylls)
    print()
    pprint.pprint(missing_words, width=1)

    print('\nmake changes to the dictionary before saving? y/n')
    print("""
    0 - exit and save
    1 - add a word or change a syllable count
    2 - remove a word
    """)

    valid = False
    while not valid:
        choice = input('\nEnter choice: ')
        if choice == '0':
            break
        elif choice == '1':
            word = input('\nEnter word to add or change: ')
            syl = input('Enter number of syllabus in {}'.format(word))
            missing_words[word] = int(syl)
            # may needa catch error if input is not an integer
        elif choice == '2':
            word = input('\nEnter word to remove: ')
            missing_words.pop(word, None)
            # adding Nome argument to pop() meaning the program wont rise KeyError if
            # the user enters a word that is not in the dictionary

    print('\nNew words or syllable changes:')
    pprint.pprint(missing_words, width=1)

    return missing_words


def save_exceptions(missing_words):
    """
    save exceptions dictionary as json file
    """
    json_string = json.dumps(missing_words)
    f = open('missing_words.json', 'w')
    f.write(json_string)
    f.close()
    print('\nFile saved as missing words.json')

cmudict = cmudict.dict()


def main():
    haiku = load_haiku('train.txt')
    exceptions = cmudict_missing(haiku)
    build_dict = ''
    while build_dict != 'y' or 'n':
        build_dict = input('\nMannually build an exceptions dictionary? y/n')
        if build_dict.lower() == 'n':
            sys.exit()
        else:
            missing_word_dict = make_exceptions_dict(exceptions)
            save_exceptions(missing_word_dict)


if __name__ == '__main__':
    main()
