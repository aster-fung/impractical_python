

import time
from random import randint, randrange


def fitness (combo, attempt):
    """compare items in two lists and count number of matches"""
    grade = 0
    for i,j in zip(combo, attempt):
        if i == j:
            grade += 1
    return grade


def main():
    combination = '6822858902'
    print('combination: {}'.format(combination))
    combo = [int(i) for i in combination]

    # initialize
    best_attempt = [0] * len(combo)
    best_attempt_grade = fitness (combo, best_attempt)

    count = 0

    while best_attempt != combo:
        next_try = best_attempt[:]
        # removing the [:] will cause infinite failed attempts in creating a matching
        # combination and I have no idea why
        lock_wheel = int(randrange(0, len(combo)))
        next_try[lock_wheel] = randint(0, len(combo))

        next_try_grade = fitness(combo, next_try)
        if next_try_grade > best_attempt_grade:
            print('\nprevious best try: {}'.format(best_attempt))
            print('current try:       {}'.format(next_try))
            best_attempt = next_try
            best_attempt_grade = next_try_grade

        else:
            print('.', end = '')
        count += 1

    print()
    print('combination cracked')
    print('the combination is {}'.format(best_attempt))
    print ('times attempted : {}'.format(count))


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print('total runtime : {}'. format(end_time-start_time))