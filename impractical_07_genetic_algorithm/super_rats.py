import time
import random
import statistics
import pandas as pd
import matplotlib.pyplot as plt

# global constants ( weight in grams)
GOAL = 50000
NUM_RATS = 20
INITIAL_MIN_WT = 200
INITIAL_MAX_WT = 600
INITIAL_MODE_WT = 300
MUTATE_ODDS = 0.01
MUTATE_MIN = 0.5
MUTATE_MAX = 1.2
LITTER_SIZE = 8
LITTERS_PER_YEAR = 10
GENERATION_LIMIT = 500

if NUM_RATS % 2 != 0:
    NUM_RATS += 1


def populate(num_rats, min_wt, max_wt, mode_wt):
    """
    initialize a population with given arguments
    although this function is only called once with global constants, it is better to
    isolate the variables to keep global constants global
    """
    return [int(random.triangular(min_wt, max_wt, mode_wt)) for i in range(num_rats)]


def fitness(population, goal):
    """
    purpose: rate the fitness of each generation

    arguments:
    population: list of current generation weights
    goal: global weight goal of selection
    """
    average = statistics.mean(population)
    return average/goal


def select(population, retain):
    """
    purpose: cut off population lower than threshold

    arguments:
    population: list of current generation weights
    retain: total no of individuals to keep for the next generation
    selected_females, selected males: selected body weights after cut off
    """
    sorted_population = sorted(population)
    to_retain_per_sex = retain//2
    members_per_sex = len(sorted_population)//2
    # assume the heaviest female is lighter than the lightest male
    # nested splicing in 2 steps
    females = sorted_population[:members_per_sex]       # first half
    males = sorted_population[members_per_sex:]         # second half
    selected_females = females[-to_retain_per_sex:]
    # remove the lighter ones with negative slicing i.e. later part of each sorted sex
    selected_males = males[-to_retain_per_sex:]
    return selected_males, selected_females


def breed(males, females, litter_size):
    """
    crossover weights phenotypes from the current generation male and females

    arguments:
    male: filtered male body weights from the function select
    female: filtered female body weights from the function select
    litter_size: global constant LITTER_SIZE
    """
    random.shuffle(males)
    random.shuffle(females)
    children = []
    for male, female in zip(males, females):
        for child in range(litter_size):
            child = random.randint(female, male)
            children.append(child)
    return children


def mutate(children, mutate_odds, mutate_min, mutate_max):
    """
    randomly mutate children weight when probability is greater than the mutate_odds
    the mutation  degree is between mutate_min and mutate_max

    argument:
    children: the list of offspring return from function breed(males, female, litter_size)
    mutate_odds, mutate_min, mutate_max = global constants
    """

    for (index, weight) in enumerate(children):
        if mutate_odds >= random.random():
            children[index] = round(weight*random.uniform(mutate_min, mutate_max))
    return children


def main():
    generation = 0
    population = populate(NUM_RATS, INITIAL_MIN_WT, INITIAL_MAX_WT, INITIAL_MODE_WT)
    fit = fitness(population, GOAL)

    average_per_generation = []

    while fit<1 and generation< GENERATION_LIMIT:
        selected_males, selected_females = select(population, NUM_RATS)
        children = breed(selected_males, selected_females, LITTER_SIZE)
        children = mutate(children, MUTATE_ODDS, MUTATE_MIN, MUTATE_MAX)
        average = statistics.mean(children)
        average_per_generation.append(average)
        population = selected_males+selected_females+children
        fit = fitness(population, GOAL)
        generation += 1

    accumulated_generation_count = [i+1 for i in range(generation)]
    years = generation//LITTERS_PER_YEAR
    accumulated_year_count = [i+1 for i in range(years)]
    datatable1 = zip (accumulated_generation_count, average_per_generation)
    datatable2 = zip(accumulated_year_count, average_per_generation)
    df1 = pd.DataFrame(datatable1, columns=['generation','average_weight'])
    df2 = pd.DataFrame(datatable2, columns=['year', 'average_weight'])
    df1.plot(x='generation', y='average_weight', title='Rat breeding project')
    df2.plot(x='year', y='average_weight', title='Rat breeding project')
    print('number of generations it takes = {}'.format(generation))
    print('number of years it takes = {}'.format(years))
    plt.show()
    exit()

if __name__ == '__main__':
    main()






