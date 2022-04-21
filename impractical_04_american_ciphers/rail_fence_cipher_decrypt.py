"""
Decrypt an amercian civil war 2-rail fence type cipher
"""

import math
import itertools

#========================================================================================

############
# USER INPUT
############

ciphertext = "LTSRS OETEI EADET NETEH DOTER EEUCO SVRHR VRNRS UDRHS AEFHT ES"

#========================================================================================


def prep_ciphertext(ciphertext):
    message = ''.join(ciphertext.split())
    print('\nciphertext = {}'.format(ciphertext))
    return message


def split_rails(message):
    row1_len = math.ceil(len(message)/2)
    row1 = message[:row1_len]
    row2 = message[row1_len:]
    return row1, row2


def decrypt(row1, row2):
    plaintext = []
    for r1, r2 in itertools.zip_longest(row1, row2):
        plaintext.append(r1)
        plaintext.append(r2)
    if None in plaintext:
        plaintext.pop()
    print('\nrail 1 = {}'.format(row1))
    print('\nrail2 = {}'.format(row2))
    print('\nplaintext = {}'.format(''.join(plaintext)))


def main():
    """
    Run program to decrypt 2-rail rail fence cipher
    """
    message = prep_ciphertext(ciphertext)       # remove white space
    row1, row2 = split_rails(message)
    # split message into two, always rounding up for the first row
    decrypt(row1, row2)
    # build a list with every other letter in 2 strings then print

if __name__ == '__main__':
    main()
