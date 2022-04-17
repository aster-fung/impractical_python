import sys
from string import punctuation
import json
from nltk.corpus import cmudict

# load the phenome dictionary of words that are missing from nltk cmudict
# is made using missing_words.py
with open('missing_words.json') as f:
    missing_words = json.load(f)

cmudict = cmudict.dict()


def count_syllables(words):
    """
    argument: words(string)
    return: total_syl (int): total number of syllabus in words
    remove punctuations and non-sylllable characters
    if the word is not in cmudict,
    call missing_word dictionary for syllable counts
    else call cmudict to count syllables
    """
    words = words.replace('-', ' ')
    words = words.lower().split()
    total_syl = 0
    for word in words():
        word = word.strip(punctuation)
        if word.endswith("'s") or word.endswith("`s"):
            word = word[:-2]
        if word in missing_words:
            total_syl += missing_words[word]
        else:
            for phoneme in cmudict[word][0]:
                for unit in phoneme:
                    if unit[-1].isdigit():
                        # assume that vowel at last position means a syllable
                        total_syl += 1
    return total_syl


def main():
    while True:
        print('**syllable counter**')
        input_word = input('enter word or phrase to start \n press Enter to exit')
        if input_word == '':
            sys.exit()
        try:
            num_syl = count_syllables(input_word)
            print('number of syllabus: {}'.format(num_syl))
            print('\n')
        except KeyError:
            print('word not found. Please update dictionary or missing word list '
                  'manually', file= sys.stderr)


if __name__ == '__main__':
    main()






