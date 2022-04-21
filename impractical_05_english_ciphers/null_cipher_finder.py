import sys
import string


def load_text(file):
    """Load a text file as a string"""
    with open(file) as f:
        return f.read().strip()


def solve_null_cipher(message, lookahead):
    """solve a null cipher based on bnumber of letters after punctuation mark"""
    for i in range(1, lookahead+1):
        plaintext = ''      # hold the translated text template
        pointer = 0           #
        found_first = False
    for char in message:
        if char in string.punctuation:
            pointer = 0
            found_first = True
        elif found_first:       # found the punctuation and character is not a punctuation
            pointer += 1
        if pointer == i:
            plaintext += char
        print('Using offset of {} after punctuation = {}'.format(i, plaintext))


def main():
    """load text, solve null cipher"""
    # load and process message
    filename = input("\nEnter full filename for message to translate: ")
    try:
        loaded_message = load_text(filename)
    except IOError as e:
        print("{}.terminating program".format(e), file=sys.stderr)
        sys.exit(1)
    print("\nOriginal Message = {}".format(loaded_message), "\n")
    print("\nList of punctuation mark to check = {}".format(string.punctuation),'\n')

    # remove whitespace
    message = ''.join(loaded_message.split())

    # get range of possible cipher keys from user
    # avoid type error
    while True:
        lookahead = input('\nNumber of letters to check after punctuation mark: ')
        if lookahead.isdigit():
            lookahead = int(lookahead)
            break
        else:
            print('please input a number', file=sys.stderr)
    print()

    # run function to decode cipher
    solve_null_cipher(message, lookahead)


if __name__ == '__main__':
    main()





























