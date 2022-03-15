"""
find inclusive anagrams from single word input by user
i.e. allow leftover letters

methodology:
filter word list from dictionary with exact word length
apply cv map
apply trigram filter
apply diagram filter
allow user to pick from available anagrams
"""


import sys
from itertools import permutations
from collections import Counter
import load_dictionary


def prep_words(name, word_list_ini):
    """
    prepare word list for finding anagrams
    name: string; user name in main()
    word_list_ini: list of strings; imported from dictionary. lowercased and stripped.
    """
    print('length of initial word list = ', len(word_list_ini))
    len_name = len(name)
    word_list = [word.lower() for word in word_list_ini if len(word) == len_name]
    # filter dictionary word list with string length
    print('length of new word list = ', len(word_list))
    return word_list


def cv_map_words(word_list):
    """
    map letters in words to consonants & vowels
    """
    vowels = 'aeiouy'
    cv_mapped_words = []
    for word in word_list:
        temp = ''
        for letter in word:
            if letter in vowels:
                temp += 'v'
            else:
                temp += 'c'
        cv_mapped_words.append(temp)
    # determine number of unique c-v patterns
    total = len(set(cv_mapped_words))
    # threshold  to eliminate
    threshold = 0.05
    # get the number of items in target fraction
    n = int(total*threshold)
    count_pruned = Counter(cv_mapped_words).most_common(total-n)
    filtered_cv_map = set()
    for pattern, count in count_pruned:
        filtered_cv_map.add(pattern)
    print(f'number of filtered c-v maps :  {len(filtered_cv_map)}')
    return filtered_cv_map


def cv_map_filter(name, filtered_cv_map):
    """
    remove permutations of words based on unlikely cons-vowels combos
    accepts filtered cv map and the name of user
    map the name of user and compare this map with filtered cv map
    only permuts of user name which have cv map in filtered cv map are kept
    """
    perms = {''.join(i) for i in permutations(name)}
    print('number of initial permutations is ', len(perms))
    vowels = 'aeiouy'
    filter_1 = set()
    for candidate in perms:
        temp = ''
        for letter in candidate:
            if letter in vowels:
                temp += 'v'
            else:
                temp += 'c'
        if temp in filtered_cv_map:
            filter_1.add(candidate)
    print('letter combinations after filter 1 (c-v map): ', len(filter_1))
    return filter_1


def trigram_filter(filter_1, trigrams_filtered):
    """
    remove unlikely trigrams from permutations
    accepts filter_1
    uses a text file derived from various crytography websites imported in main()
    will return only permuts that include one of these trigrams
    main() will pass this result to filter_3
    """
    dump = set()
    for candidate in filter_1:
        for triplet in trigrams_filtered:
            # triplet = triplet.lower()
            if triplet in candidate:
                dump.add(candidate)
    filter_2 = filter_1 - dump
    print('letter combinations after filter 2 (trigram filter: ', len(filter_2))
    return filter_2


def letter_pair_filter(filter_2):
    """
    defines and apply diagram filter
    """
    dump = set()
    rejects = ['dt', 'lr', 'md', 'mr', 'mt', 'mv',
               'td', 'tv', 'vd', 'vl', 'vm', 'vr', 'vt']
    first_pair_rejects = ['ld', 'lm', 'lt', 'lv', 'rd'
                          'rl', 'rm', 'rt', 'rv', 'tl', 'tm']
    for candidate in filter_2:
        for r in rejects:
            if r in candidate:
                dump.add(candidate)
        for fp in first_pair_rejects:
            if candidate.startswith(fp):
                dump.add(candidate)
    filter_3 = filter_2 - dump
    print('number of letter combinations after filter 3: ', len(filter_3))
    if 'voldemort' in filter_3:
        print('voldemort found!', file=sys.stderr)
    return filter_3


def view_by_letter(name, filter_3):
    print('remaining letters :', name)
    first = input('select a beginning letter or press enter to see all: ')
    subset = []
    for candidate in filter_3:
        if candidate.startwith(first):
            subset.append(candidate)
    print(*sorted(subset), sep='\n')
    try_again = input('press ENTER to try again, or any other key to exit')
    if try_again.lower() == '':
        view_by_letter(name, filter_3)
    else:
        sys.exit()
    return


def main():
    """
    load files, run filters, allow user to view anagrams by 1st letter
    """
    name = 'tmvoordle'
    name = name.lower()

    word_list_ini = load_dictionary.load('dictionary.txt')
    trigrams_filtered = load_dictionary.load('least-likely_trigrams.txt')

    # encapsulate. think about the main skeleton before writing the functions
    word_list = prep_words(name, word_list_ini)
    filtered_cv_map = cv_map_words(word_list)
    filter_1 = cv_map_filter(name, filtered_cv_map)
    filter_2 = trigram_filter(filter_1, trigrams_filtered)
    filter_3 = letter_pair_filter(filter_2)
    view_by_letter(name, filter_3)


if __name__ == "__main__":
    main()