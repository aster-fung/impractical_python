"""
this script is a standalone program that solves the Monty Hall problem with Monte Carlo Stimulation approach: it automates the process of choosing doors and recording results in a Monty Hall Program. The program returns probabilty of winning with decision switch or no-switch.

The Monty Hall Problem:
There are 3 doors. Only 1 of the 3 doors has the prize behind. Users are asked to choose 1 of the doors to open. Of one of the remaining 2 doors, one of them will reveal a stinky goat for sure. The player is asked if they decided to stay with the previous pick, or reselect the door(the remaining door that did not reveal the stinky goat.
"""
import random


def user_prompt(prompt, default='20000'):
    """
    user either input the number of games to run or else accept a default value of 20000
    """
    prompt = '{} {}'.format(prompt, default)
    response = input(prompt)
    if not response and default:                # user press enter
        return default
    else:
        return response


num_runs = int(user_prompt('Number of games to simulate (default = '))
# initialize counters to count win
stay_to_win = 0
change_to_win = 0
doors = ['a', 'b', 'c']

# run Monte Carlo simulation
for i in range(num_runs):
    result = random.choice(doors)
    choice = random.choice(doors)
    if choice == result:
        stay_to_win += 1
    else:
        change_to_win += 1

prob_stay_win = "{:2f}".format(stay_to_win/num_runs)
prob_change_win = "{:2f}".format(change_to_win/num_runs)

print(f'Wins with original pick =                    {stay_to_win}')
print(f'Wins with changed pick =                     {change_to_win}')
print(f'probability of winning with initial =        {prob_stay_win}')
print(f'probability of winning by changing choice =  {prob_change_win}')

input('\nPress ENTER to exit')



