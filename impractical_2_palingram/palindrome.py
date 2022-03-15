"""
load the dictionary
loop through the dictionary word list to find palindromes
saves the palindromes and print them out
"""

import load_dictionary
# the load_dictionary module has the sys module imported


word_list = load_dictionary.load('dictionary.txt')
palindrome_list = []

for word in word_list:
    if len(word)>1 and word == word [::-1]:
        palindrome_list.append(word)

print('\n\nnumber of palindromes found: ', len(palindrome_list))
print(*palindrome_list, sep='\n')


