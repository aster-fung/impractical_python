import random
import string
import load_dictionary



# remove whitespaces, punctuations and convert to lowercase
message = 'Give your word and we rise'
for char in message:
    if char in string.ascii_letters:
        message += char
message = ''.join(message.split())

# load supporter names
word_list = load_dictionary.load('dictionary.txt')
name_list = load_dictionary.load('supporters.txt')


# build vocabulary word list with hidden message

# switch = True or False
# turn = 2 or 3
first = random.choice(word_list)
switch = True
turn = 2
supporter_name_length = 0

vocab_list = []
for letter in message:
    size = random.randint(6, 10)
    for word in word_list:
        if switch == False:
            turn = 3
        else:
            turn = 2
        if len(word) == size and word[turn].lower() == letter.lower() and word not in \
                vocab_list and word is not first:
            vocab_list.append(word)
            switch = not switch
            add_name = random.choice([True, False])
            if add_name:
                supporter_name = random.choice(name_list)
                vocab_list.append(supporter_name)
                supporter_name_length += len(supporter_name)
            break

if len(vocab_list) < len(message) - supporter_name_length:
    print('cannot find enough matching words to construct the cipher word. please use a '
          'larger dictionary or provide a shorter message.')
else:
    print('Vocabularies for message: ')
    # add a random word at the front
    print(first, end = '')
    print(*vocab_list, sep=' ')