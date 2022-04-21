"""
find all word pair palingrams in a dictionary file
"""

import load_dictionary
word_list = load_dictionary.load('dictionary.txt')

def find_palingrams():
    pali_list = []
    words = set(word_list)
    for word in words:
        end = len(word)
        reverse_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == reverse_word[:end-i] and reverse_word[end-i:] in words:
                    pali_list.append((word, reverse_word[end-i:]))
                if word[:i] == reverse_word[end-i:] and reverse_word[:end-i] in words:
                    pali_list.append((reverse_word[:end-i], word))
    return pali_list


palingrams = find_palingrams()
palingrams_sorted = sorted(palingrams)

print('\nNumber of palingrams = ')
print(len(palingrams_sorted))
for first, second in palingrams_sorted:
    print(first, second)
