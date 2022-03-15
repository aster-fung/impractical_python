import sys
import logging
import random
from collections import defaultdict
from count_syllables import count_syllables
from string import punctuation

logging.disable(logging.CRITICAL)  # comment out to enable debug logs
logging.basicConfig(level=logging.DEBUG, format='%(message)s')


def load_training_file(file):
    """return text file as a string"""
    with open(file) as f:
        raw_haiku = f.read()
        return raw_haiku


def prep_training(raw_haiku):
    """load string, remove newline, split words on spaces, and return list"""
    corpus = raw_haiku.replace('\n', ' ').split()
    for word in corpus:
        word = word.replace(punctuation, '')
    return corpus


def map_word_to_word(corpus):
    """load list & use dictionary to map word to word that follows"""
    limit = len(corpus) - 1
    dict_to_1 = defaultdict(list)
    for index, word in enumerate(corpus):
        if index < limit:
            suffix = corpus[index + 1]
            dict_to_1[word].append(suffix)
    logging.debug('map_word_to_word results for \"sake\" = %s\n', dict_to_1['sake'])
    return dict_to_1  # suffix_map_1


def map_2_words_to_words(corpus):
    """load list and use dictionary tp map word-pair to trailing word"""
    limit = len(corpus) - 2
    dict2_to_1 = defaultdict(list)
    for index, word in enumerate(corpus):
        if index < limit:
            key = word + ' ' + corpus[index + 1]
            suffix = corpus[index + 2]
            dict2_to_1[key].append(suffix)
    logging.debug('map_2_words_to_words results for \"sake\" = %s\n', dict2_to_1[
        'sake jug'])
    return dict2_to_1  # suffix_map_2


def random_word(corpus):
    """return random word and syllable count from training corpus"""
    word = random.choice(corpus)
    num_syls = count_syllables(word)
    if num_syls > 4:
        random_word(corpus)
    else:
        logging.debug("random word and syllabus = %s %s\n", word, num_syls)
    return word, num_syls


def word_after_single(prefix, suffix_map_1, current_syls, target_syls):
    """
    return all acceptable words, in a corpus that follow a single word
    i.e. order 1 Markov chain model
    prefix: word to be followed
    suffix_map_1: corpus map returned from map_word_to_word
    current_syls: number of syl of prefix word
    target_syls: number of syl left in this line of haiku
    """
    accepted_words = []
    suffixes = suffix_map_1.get(prefix)  # dictionary method: get item from key; list
    if suffixes is not None:  # not the first word of the haiku
        for candidate in suffixes:
            num_syls = count_syllables(candidate)
            if current_syls + num_syls <= target_syls:
                accepted_words.append(candidate)
    logging.debug("accepted word after \"%s\" = %s\n", prefix, set(accepted_words))
    return accepted_words


def word_after_double(prefix, suffix_map_2, current_syls, target_syls):
    """
    return all acceptable words, in a corpus that follows 2 words
    i.e. order 2 Markov chain model
    prefix: 2 words to be followed
    suffix_map_1: corpus map returned from map_2_words_to_word
    current_syls: number of syl of prefix word
    target_syls: number of syl left in this line of haiku
    """
    accepted_words = []
    suffixes = suffix_map_2.get(prefix)
    if suffixes is not None:
        for candidate in suffixes:
            num_syls = count_syllables(candidate)
            if current_syls + num_syls <= target_syls:
                accepted_words.append(candidate)
    logging.debug("accepted word after \"%s\" = %s\n", prefix, set(accepted_words))
    return accepted_words


def haiku_line(suffix_map_1, suffix_map_2, corpus, end_prev_line, target_syls):
    """
    build a haiku line from a training corpus and return it
    """

    # base case
    line = '2/3'  # either 2 or 3. for differentiation from '1'
    line_syls = 0
    current_line = []

    if len(end_prev_line) == 0:  # indicates this is the first word of a line
        line = '1'
        word, numsyls = random_word(corpus)
        current_line.append(word)
        line_syls += numsyls
        word_choices = word_after_single(word, suffix_map_1, line_syls, target_syls)

        # if no suffix could be mapped, assign ghost suffix
        while len(word_choices) == 0:
            prefix = random.choice(corpus)
            logging.debug('new random prefix = %s', prefix)
            word_choices = word_after_single(prefix, suffix_map_1, line_syls, target_syls)

        word = random.choice(word_choices)
        num_syls = count_syllables(word)
        logging.debug('word and syllables = %s, %s', word, num_syls)
        line_syls += num_syls
        current_line.append(word)

        if line_syls == target_syls:  # number of syllables == 5/7
            end_prev_line.extend(current_line[-2:0])
            return current_line, end_prev_line  # return when the lined is filled
    else:
        current_line.extend(end_prev_line)
        # start mapping at 2nd order on the same line

    while True:
        logging.debug('line = %s\n', line)
        prefix = current_line[-2] + ' ' + current_line[-1]
        # construct 2 word prefix
        word_choices = word_after_double(prefix, suffix_map_2, line_syls, target_syls)

        while len(word_choices) == 0:
            index = random.randint(0, len(corpus) - 2)
            prefix = corpus[index] + ' ' + corpus[index + 1]
            logging.debug('new random prefix = %s', prefix)
            word_choices = word_after_double(prefix, suffix_map_2, line_syls, target_syls)
            try:
                word = random.choice(word_choices)
            except:
                continue
            #  random.choice sometimes returns None. i = self._randbelow(len(seq))will
            #  return error but I find this doesnt always happen. so I catch this with
            #  continue and it worked hahaha will figure this out later
            num_syls = count_syllables(word)
            logging.debug('word & syllables = %s %s', word, num_syls)

        if line_syls + num_syls > target_syls:
            # send back to the while loop to repick the words
            continue
        elif line_syls + num_syls < target_syls:
            current_line.append(word)
            line_syls += num_syls
            # loop back to add more words
        elif line_syls + num_syls == target_syls:
            current_line.append(word)
            break

    end_prev_line = []  # line finished
    end_prev_line.extend(current_line[-2:])

    if line == '1':
        final_line = current_line[:]
        # there is no prefix to build up from non existent previous
    else:
        final_line = current_line[2:]

    return final_line, end_prev_line


def main():
    """
    give user choice of building a haiku or modifying an existing haiku
    """

    print('skipping any cringy introduction given by the book...')

    raw_haiku = load_training_file('train.txt')
    corpus = prep_training(raw_haiku)
    suffix_map_1 = map_word_to_word(corpus)
    suffix_map_2 = map_2_words_to_words(corpus)

    # initialize
    final = []  # final haiku
    choice = None

    while choice != '0':
        print(
            """
            ***Haiku Generator***
            
            0 - Quit
            1 - Generate a Haiku
            2 - Rewrite Line 2
            3 - Rewrite Line 3
            """
        )

        choice = input('Choice: ')

        # user choose exit
        if choice == '0':
            print('bye')
            sys.exit()
        # user choose to generate a haiku
        elif choice == '1':
            final = []  # reinitialize the entire haiku
            end_prev_line = []
            # placeholder can be reused between lines in the same haiku

            first_line, end_prev_line1 = haiku_line(suffix_map_1, suffix_map_2, corpus,
                                                    end_prev_line, 5)
            final.append(first_line)

            # notice that the end_prev_line was mutated from previous haiku_line call
            second_line, end_prev_line2 = haiku_line(suffix_map_1, suffix_map_2, corpus,
                                                     end_prev_line1, 7)
            final.append(second_line)

            third_line, end_prev_line3 = haiku_line(suffix_map_1, suffix_map_2, corpus,
                                                    end_prev_line2, 5)
            final.append(third_line)


        # user choose to regenerate line 2
        elif choice == '2':
            if not final:  # final is empty
                print('please generate a full haiku first(option 1')
                continue
            else:
                second_line, end_prev_line = haiku_line(suffix_map_1, suffix_map_2,
                                                        corpus, end_prev_line1, 7)
                final[1] = second_line

        # user choose to regenerate line 3
        elif choice == '3':
            if not final:  # final is empty
                print('please generate a full haiku first(option 1')
                continue
            else:
                third_line, end_prev_line = haiku_line(suffix_map_1, suffix_map_2,
                                                       corpus, end_prev_line2, 5)
                final[1] = third_line

        else:
            print('please only input 1/2/3/4')
            continue

        # cleanup punctuation and print
        for sentence in final:
            sentence = ' '.join(sentence)
            print(sentence, file=sys.stderr)

    input('\n\nPress Enter to exit')


if __name__ == '__main__':
    main()
