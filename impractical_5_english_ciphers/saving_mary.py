"""hide a null cipher within a list of name """
import load_dictionary

# write a short message and use no punctuation or numbers
message = 'Give your word and we rise'
message = ''.join(message.split())

# open name file
names = load_dictionary.load('supporters.txt')

name_list = [names[0]]

# start the list with a name not in the cipher

# add letter of null cipher to 2nd letter of names, then 3rd  then repeat
count = 1                       # count of letters in each name
for letter in message:
    for name in names:
        if len(name) > 2 and name not in name_list:
            if count % 2 == 0 and name[2] == letter.lower():
                name_list.append(name)
                count += 1
                break
            elif count % 2 != 0 and name[1] == letter.lower():
                name_list.append(name)
                count += 1
                break

# display list with null cipher
print(*name_list, sep= '\n')

# add two null words
name_list.insert(3, 'Stuart')
name_list.insert(6, 'Jacob')

