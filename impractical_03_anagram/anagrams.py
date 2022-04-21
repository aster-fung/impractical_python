import load_dictionary

word_list = load_dictionary.load('dictionary.txt')

anagram_list = []

username = input('Hi there. please input your name: ')
username = username.lower()
print('your name in lowercase is ', username)

# sort name in alphabetical order and find its anagram
#single word anagrams only
username_sorted = sorted(username)
for word in word_list:
    word = word.lower()
    if word != username:
        if sorted(word) == username_sorted:
            anagram_list.append(word)
print()
if len(anagram_list) == 0:
    print("anagram no found")
else:
    print('the anagrams are: ', *anagram_list, sep=',  ')
