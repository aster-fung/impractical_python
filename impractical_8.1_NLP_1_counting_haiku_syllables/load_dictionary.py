"""
load a text file as a list

note: in general practice try-except and sys.exit shld be in main() for clarity and control
"""
import sys


def load(file):
    """open a text file and return a list of  lowercase strings"""
    try:
        with open(file) as in_file:
            loaded_text = in_file.read().strip().split('\n')
            loaded_text = [x.lower() for x in loaded_text]
            return loaded_text
    except IOError as e: 
        print('{}\n error opening {}, terminating program'. format(e,file), file=sys.stderr)
        sys.exit(1)
