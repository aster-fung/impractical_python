"""
decrypt a path through a Union Cipher

Designed for whole-word transposition cophers with variables rows & columns
Assumes encryption began at either top or bottom of a columns
Key indicates the order to read columns and the directions to transverse
Negative column numbers mean start at the bottom and read upper
Positive column numbers mean start at top

example below is for 4x4 matrix with ket -1 2 -3 4
Note that '0' is not allowed
Arrows shows encryption route; for negative key values read UP.



Required inputs - a text message, # of columns , # of rows, key string

Prints translated plaintext
"""

import sys

#========================================================================================
############
# USER INPUT
############

# the string to be decrypted
ciphertext = 'THIS OFF DETAINED ASCERTAIN WAYLAND CORRESPONDENTS OF AT WHY AND IF FILLS ' \
             'IT YOU GET THEY NEPTUNE THE TRIBUNE PLEASE ARE THEM CAN UP'


# number of columns in the transposition matrix
COLS = 4

# number of rows in the transposition matrix
ROWS = 6

# key with spaces between numbers, use negative numbers for upward columns
key = ' -1 2 -3 4'
#========================================================================================


# users please do not touch this part unless you know what you are doing

def validate_col_row(cipherlist):
    """
    check that input columns and rows are valid versus message length
    """
    factors = []
    len_cipher = len(cipherlist)
    if len_cipher % 2 == 0:
        for i in range(2, len_cipher):
            if len_cipher % i == 0:
                factors.append(i)
    print('\nLength of cipher = {}'.format(len_cipher))
    print('\nAcceptable column/row values in keys are {}'.format(factors))
    print()
    if ROWS*COLS != len_cipher:
        print('\nError: Input keys are not factors of length of the cipher',
              file=sys.stderr)
        sys.exit(1)


def key_to_int(key):
    """
    turn key into list of integers and check validity
    """
    key_int = [int(i) for i in key.split()]
    key_int_low = min(key_int)
    key_int_high = max(key_int)
    if len(key_int) != COLS or key_int_low < -COLS or key_int_high > COLS or 0 in key_int:
        print('\nError: key exceeds column/row values. Terminating', file=sys.stderr)
        sys.exit()
    else:
        return key_int


def build_matrix(key_int, cipherlist):
    """
    turn every n items in a list into a new item in a list of lists
    """
    translation_matrix = [None]*COLS
    start = 0
    stop = ROWS
    for k in key_int:
        if k < 0:
            col_items = cipherlist[start:stop]
        elif k > 0:
            col_items = list((reversed(cipherlist[start:stop])))
        translation_matrix[abs(k)-1] = col_items
        start += ROWS
        stop += ROWS
    return translation_matrix


def decrypt(translation_matrix):
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
    print('\nTrying {} columns'.format(COLS))
    print('\nTrying {} rows'.format(ROWS))
    print('\nTrying key = {}'.format(key))

    cipherlist = list(ciphertext.split())
    validate_col_row(cipherlist)
    key_int = key_to_int(key)
    translation_matrix = build_matrix(key_int, cipherlist)
    plaintext = decrypt(translation_matrix)

    print('plaintext = {}'.format(plaintext))


if __name__ == '__main__':
    main()
