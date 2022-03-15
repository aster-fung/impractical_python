import dictionary_cleanup
import sys


def test(file):
    """
    :argument
    file: dictionary file name
    """
    print('testing dictionary: ', str(file))
    word_list_cleanup = dictionary_cleanup.cleanup(file)
    print("no of words in filtered word list: ", len(word_list_cleanup))
    for word in word_list_cleanup:
        if len(word) < 2:
            print('single letter word is present')
            print('the word is',word)
            sys.exit(1)
    print("filtering successful")


test('dictionary.txt')
test('dictionary_with_single_letter_words.txt')

