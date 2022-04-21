from random import randint
import string
import load_dictionary



# remove whitespaces, punctuations and convert to lowercase
message = input('please input message: ')
for char in message:
    if char in string.ascii_letters:
        message += char
message = ''.join(message.split())

# load dictionary to retrieve vocabulary
word_list = load_dictionary.load('dictionary.txt')

# build vocabulary word list with hidden message
# in this exercise the hidden position is fixed at position 2 of each word
vocab_list = []
for letter in message:
    size = randint(6, 10)
    for word in word_list:
        if len(word) == size and word[2].lower() == letter.lower() and word not in \
                vocab_list:
            vocab_list.append(word)
            break

if len(vocab_list) < len(message):
    print('cannot find enough matching words to construct the cipher word. please use a '
          'larger dictionary or provide a shorter message.')
else:
    print('Vocabularies for message: ')
    print(*vocab_list, sep='\n')
