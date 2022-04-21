import sys
from collections import Counter
import load_dictionary

global ini_name                                             # only input once. declare global just for clarity

dict_file = load_dictionary.load('dictionary.txt')          # load dictionary in to list and lowercase the words inside
dict_file.append('a')
dict_file.append('i')
dict_file = sorted(dict_file)

ini_name = input("Enter a phrase: ")


def find_anagram(name, word_list):
    """
    read a phrase and word list from a dictionary file
    display all anagrams contained in the phrase
    """
    name_letter_map = Counter(name)
    anagrams = []
    for word in word_list:
        test_string = ''
        word_letter_map = Counter(word.lower())
        for letter in word:
            if word_letter_map[letter] <= name_letter_map[letter]:
                test_string += letter
            if Counter(test_string) == word_letter_map:
                anagrams.append(word)
    print(*anagrams, sep=', ')
    print('\n')
    print(f'remaining letter: ', name)
    print(f'number of remaining letters: ', len(name))
    print(f'number of remaining (read word) anagrams: ', len(anagrams))


def process_choice(name):
    """
    check user choice for validity,
    remove letters from the name after user pick from anagram list
    return choice and leftover letters
    :param name: string
    :return: choice,name

    """
    repick = True
    while repick:
        choice = input('\nmake a choice, else Enter to start over, or # to end: ')
        # checkpoint: user is expected to input any word displayed from func:find_anagrams
        if choice == '':
            main()
        elif choice == '#':
            sys.exit()
        else:
            candidate = ''.join(choice.lower().split())
        left_over_list = list(name)
        # import word match from find_anagram
        for letter in candidate:
            if letter in left_over_list:
                left_over_list.remove(letter)
                # if user input match anagram, all letters shld be removed
        if len(name) - len(left_over_list) == len(candidate):
            repick = False
            # input valid: user input exact word from anagrams
        else:
            # user input a string that doesnt match the anagram list,
            print('wont work. please pick a word from the provided anagram list', file=sys.stderr)
        name = ''.join(left_over_list)
        # convert back to string datatype for readability
        # name is not changed throughout this function. but return name to keep
        # readability
        return choice, name


def main():
    """
    helps user to build anagram phrase from their names
    calls func: find_anagram
    calls func: process_choice
    """
    # use new variable to store the username to keep global ini_name unchanged
    # strip all whitespace, hyphens and lowercase for comparison
    name = ''.join(ini_name.lower().split())
    name = name.replace('-', '')

    limit = len(name)                            # store the length of username. when the anagram phra
    phrase = ''                                  # store constructing anagram phrase
    running = True
    # the main while loop control

    while running:
        temp_phrase = phrase.replace(' ', '')      # hold constructing anagram phrase
        if len(temp_phrase) < limit:
            print('number of characters in this anagram phase = ', len(temp_phrase))
            find_anagram(name, dict_file)
            # display anagrams possible
            print('Current anagram phrase = ', end=' ')
            print(phrase, file=sys.stderr)
            choice, name = process_choice(name)
            phrase += choice + ' '
        elif len(temp_phrase) == limit:
            print('\n\n*************************\nFINISHED\n*************************\n')
            print('anagram phrase of your name is ', end=' ')
            print(phrase, file=sys.stderr)
            print()
            try_again = input('\n\nTry again? (Enter to continue, # to quit')
            if try_again == "#":
                running = False
                sys.exit()
            else:
                main()


if __name__ == '__main__':
    main()
