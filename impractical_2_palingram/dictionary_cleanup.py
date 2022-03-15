'''
removes one letter words from dictionary word list

'''
import load_dictionary

def cleanup(file):
    """
    argument
    file: dictionary file name

    returns
    a list of dictionary without single letter words

    """
    word_list = load_dictionary.load(file)
    word_list = list(set(word_list))
    word_list_new = [word for word in word_list if len(word) > 1]
    word_list_cleanup = sorted(word_list_new)

    return word_list_cleanup

