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



