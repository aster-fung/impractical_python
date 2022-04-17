# Python program to solve JSONDecodeError: Expecting value: line 1 column 1 (char 0)
import json

file_path = "C:\\Users\\User\\Documents\\impractical_python" \
            "\\impractical_9_NLP_2_haiku_markov_chain\\missing_words.json"

with open(file_path, 'r') as j:
     contents = json.loads(j.read())
     print(contents)