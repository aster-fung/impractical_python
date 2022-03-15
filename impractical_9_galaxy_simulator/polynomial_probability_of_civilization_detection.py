from random import randint
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt


#global constants
NUM_EQUIV_VOLUMES = 1000
MAX_CIVS = 5000
TRIALS = 1000
CIV_STEP_SIZE = 100

# initializing
x = []
y = []


def polyeq(x,y):
    coeff = np.polyfit(x, y, 4)
    p = np.poly1d(coeff)
    print('\n{}'.format(p))
    xp = np.linspace(0, 5)
    curve = plt.plot(x, y, '.', xp, p(xp), '-')
    plt.ylim(-0.5, 1.5)
    plt.savefig('polynomial.png')
    plt.show()

    # output the equation as in a text file
    # coeff_list = coeff.tolist()
    #eq = str(coeff_list[0])+'x^4'+ str(coeff_list[1])+'x^3'+ str(
    # coeff_list[2])+'x^2'+str(coeff_list[3])+'x'
    p1 = np.array2string(p, formatter={'float_kind': lambda p: "%.2f" % x})
    with open('polynomial_equation.txt', 'w') as f2:
        f2.write(p1)

    return p

# generate civilizations
f = open('civ_coordinates.txt', 'w')
for num_civs in range(2, MAX_CIVS, CIV_STEP_SIZE):
    civs_per_vol = num_civs/NUM_EQUIV_VOLUMES
    num_single_civs = 0
    for trial in range(TRIALS):
        locations = []
        while len(locations) < num_civs:
            location = randint(1, NUM_EQUIV_VOLUMES)
            locations.append(location)
        overlap_count = Counter(locations)
        overlap_rollup = Counter(overlap_count.values())
        num_single_civs += overlap_rollup[1]

    prob = 1 - (num_single_civs/(num_civs*TRIALS))

    #print('{:.4f}, {:.4f}'.format(civs_per_vol, prob))
    x.append(civs_per_vol)
    y.append(prob)
    print('.', end = '')

    temp = str(civs_per_vol) + ',' + str(prob)
    f.write(temp)
    f.write('\n')
f.close()

# generate polynomial equation and and plot
polynomial_equation = polyeq(x, y)







