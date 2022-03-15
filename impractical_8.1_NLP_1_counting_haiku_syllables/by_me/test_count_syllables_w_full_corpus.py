import sys
import count_syllables

with open('train.txt') as in_file:
    words1 = set(in_file.read().split())

missing = []

for w1 in words1:
    try:
        num_syllables = count_syllables.count_syllables(w1)
        print(w1, num_syllables, end='\n')
    except KeyError:
        missing.append(w1)

print('Missing words: ', missing, file=sys.stderr)