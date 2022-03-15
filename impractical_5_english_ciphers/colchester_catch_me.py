
import string
import re


def load(file):
    """open a text file and return a list of  lowercase strings"""
    try:
        with open(file) as in_file:
            loaded_text = in_file.read().strip()
            loaded_text = [x.lower() for x in loaded_text]
            loaded_text = ''.join(loaded_text)
            return loaded_text
    except IOError as e:
        print('{}\n error opening {}, terminating program'. format(e, file))


def process(message):
    message_new = re.sub(r'[^\w\s]', '', message)
    # regex start with lower and uppercase
    message_list = message_new.split()
    return message_list


def skip_words(skip, word_list):
    """
    skip : int
    word_list = list of words from the message
    """
    temp = []
    count = 0
    for word in word_list:
        if count % skip == 0:
            temp.append(word)
            count += 1
            continue
        elif count % skip != 0:
            count += 1
            continue
    return temp


def skip_letters(skip, word_list_skipped):
    """
    skip: int
    word_list_skipped = list of words skipped nth
    """
    temp = []
    for word in word_list_skipped:
        if len(word) >= skip:
            temp.append(word[skip-1])
        else:
            temp.append('*')
    output = ''.join(temp)
    return output


message = load('colchester_message.txt')
print('original message: ')
print(message)
word_list = process(message)

while True:
    skip = input('input skip number')
    try:
        skip = int(skip)
        break
    except TypeError:
        print('please input an integer')
        continue

word_list_skipped = skip_words(skip, word_list)
letter_string = skip_letters(skip, word_list_skipped)
print(letter_string)