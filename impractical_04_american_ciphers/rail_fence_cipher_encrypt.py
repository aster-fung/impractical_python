"""
Encrypt a civil war rail fence type cipher

example text to decrypt: 'Buy more Maine potatoes'

Rail fence style:
B Y O E A N P T T E
 U M R M I E O A O S

encrypted text:
BYOEA NPTTE UMRMI EOAOS

"""

#========================================================================================

############
# USER INPUT
############

plaintext = 'Let us cross over the river and rest under the shade of the trees'

#========================================================================================


def prep_plaintext(plaintext):
    """
    strip spaces and capitalize
    """
    message = "".join(plaintext.split())
    message = message.upper()
    print('\nplaintext : '.format(plaintext))
    return message


def build_rails(message):
    """
    Build a pair of string with every other letter in a message
    """
    evens = message[::2]
    odds = message[1::2]
    rails = evens + odds
    return rails


def encrypt(rails):
    """
    Split letters in ciphertext into chucks of 5 letters
    and join them to make a new string
    """
    ciphertext = " ".join(rails[i:i+5] for i in range(0, len(rails),5))
    print('ciphertext = {}'.format(ciphertext))


def main():
    """
    run program to encrypt message using 2-rail rail fence cipher
    """
    message = prep_plaintext(plaintext)     # remove space and capitalize
    rails = build_rails(message)            # stack and stagger letters into two levels
                                            # and merge the two levels
    encrypt(rails)                          # split the letters into a group of 5


if __name__ == '__main__':
    main()
