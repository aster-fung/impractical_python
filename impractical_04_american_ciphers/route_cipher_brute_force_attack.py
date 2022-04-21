"""
decrypt a path through a Union Cipher

Designed for whole-word transposition ciphers with variables rows & columns
Assumes encryption began at either top or bottom of a columns
Key indicates the order to read columns and the directions to transverse
Negative column numbers mean start at the bottom and read upper
Positive column numbers mean start at top

example below is for 4x4 matrix with key -1 2 -3 4
Note that '0' is not allowed
Arrows shows encryption route; for negative key values read UP.



Required inputs - a text message, # of columns , # of rows, key string

Prints translated plaintext
"""

import sys
import itertools

#========================================================================================

# the string to be decrypted
# ciphertext = '16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19'
ciphertext = 'REST TRANSPORT YOU GODWIN VILLAGE ROANOKE WITH ARE YOUR IS JUST SUPPLIES FREE SNOW HEADING TO GONE TO SOUTH FILLER'
# key with spaces between numbers, use negative numbers for upward columns
#key = ' -1 2 -3 4'
#========================================================================================


# users please do not touch this part unless you know what you are doing

global ROWS
global COLS

def get_factors(cipherlist):
    """
    check that input columns and rows are valid versus message length
    """
    factors = []
    len_cipher = len(cipherlist)
    for i in range(2, len_cipher):
        if len_cipher % i == 0:
            factors.append(i)
            factors.append(len_cipher//i)
    mid = len(factors)//2
    non_redundant_factors = factors[:mid]
    print('\nLength of cipher = {}'.format(len_cipher))
    print('\nAcceptable column/row values in keys are {}'.format(non_redundant_factors))
    return non_redundant_factors

def generate_keys(factors):
    keys_half = []
    for factor in factors:
        temp_key = []
        number = 1
        switch = -1
        while number < factor+1:
            temp_key.append(number*switch)
            number += 1
            switch *= -1
        keys_half.append(temp_key)
    # print('half')
    # print(keys_half)
    keys_full = []
    for key in keys_half:
        keys_full.append(key)
        keys_full.append([i*-1 for i in key])
    print('possible keys are:')
    for key in keys_full:
        print(key)
    return keys_full

def build_matrix(key, COLS, ROWS, cipherlist):
    """
    turn every n items in a list into a new item in a list of lists
    """
    translation_matrix = [None]*COLS
    start = 0
    stop = ROWS
    for k in key:
        if k < 0:
            col_items = cipherlist[start:stop]
        elif k > 0:
            col_items = list((reversed(cipherlist[start:stop])))
        translation_matrix[abs(k)-1] = col_items
        start += ROWS
        stop += ROWS
    return translation_matrix


def decrypt(translation_matrix, ROWS):
    """
    loop through nested lists pooping off last item to a string
    """
    plaintext = ''
    for i in range(ROWS):
        for matrix_col in translation_matrix:
            word = str(matrix_col.pop())
            plaintext += word + ' '
    return plaintext


def main():
    print('\nCiphertext = {}'.format(ciphertext))
    cipherlist = list(ciphertext.split())
    factors = get_factors(cipherlist)
    keys_full = generate_keys(factors)
    contin = True
    while contin:
        if len(keys_full) < 1:
            print('all keys have been used. quiting the program')
            contin = False
        for key in keys_full:

            print('\nTrying key = {}'.format(key))
            COLS = abs(key[-1])
            print('column: ', COLS)
            ROWS = abs(len(cipherlist) // COLS)
            print('row: ', ROWS)

            translation_matrix = build_matrix(key, COLS, ROWS, cipherlist)
            keys_full.pop(0)

            output = decrypt(translation_matrix, ROWS)
            print('decrypted message: ', output)
            # display deciphered matrix
            ans = input('try next key? enter to continue or "n" to exit ')
            if ans == 'n':
                contin = False


if __name__ == '__main__':
    main()
