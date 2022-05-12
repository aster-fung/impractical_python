import sys 
import random 
import matplotlib.pyplot as plt

def read_to_list(file_name):
    """
    open a text file containing percentage data of inflations, stock price and bond price over the years and return the data as a list

    param: file_name: str containing relative file path 
    return: decimal: list of formated floats
    """

    with open(file_name) as in_file:
        lines = [float(line.strip()) for line in in_file]
        decimal = [round(line/100,5) for line in lines]
        return decimal
    

def default_input(prompt, default=None):
    """
    enables default input if user inputs none
    """
    prompt = '{} [{}]: '.format(prompt, default)
    response = input(prompt)
    if not response and default:
        return default
    else:
        return response



# load data files 
print('\nNote: input data should be in percent\n')
try:
    bonds = read_to_list('D:\\python_learning\\impractical_python\\impractical_12_morte_carlo_simulation_retirement_nest_egg\\10-yr_TBond_returns_1926-2013_pct.txt')
    stocks = read_to_list('D:\\python_learning\\impractical_python\\impractical_12_morte_carlo_simulation_retirement_nest_egg\\SP500_returns_1926-2013_pct.txt')
    blend_40_50_10 = read_to_list('D:\\python_learning\\impractical_python\\impractical_12_morte_carlo_simulation_retirement_nest_egg\\S-B-C_blend_1926-2013_pct.txt')
    blend_50_50 = read_to_list('D:\\python_learning\\impractical_python\\impractical_12_morte_carlo_simulation_retirement_nest_egg\\S-B_blend_1926-2013_pct.txt')
    infl_rate = read_to_list('D:\\python_learning\\impractical_python\\impractical_12_morte_carlo_simulation_retirement_nest_egg\\annual_infl_rate_1926-2013_pct.txt')
except IOError as e:
    print('{}. \nterminating program',format(e), file = sys.stderr)
    sys.exit(1)

# initialise options for users
investment_type_args = {'bonds' : bonds, 'stocks' : stocks, 'sbc_blend':blend_40_50_10, 'sb_blend':blend_50_50}

# print legend for user
print('     stocks           =      SPF500')
print('     bonds            =      10-yr Treaury Bond')
print('     sb blend         =      50% SP500/50% TBond')
print('     sbc_blend        =      40% SP500/50% TBond/10% Cash\n')
print('Please enter the options as shown above. \nOr press Enter to use the default vales\n')

# get user input
invest_type = default_input('Enter investment type:(stocks, bonds, sb_blend, sbc_blend: \n', 'bonds').lower()
while invest_type not in investment_type_args:
    invest_type = input('invalid investment. please enter the investment type provided, or press enter to use default value').lower()

start_value = default_input('Enter the starting value of investment:\n', '2000000')
while not start_value.isdigit:
    start_value = input('please enter integer only. or press enter to use default value')

withdrawal = default_input('Enter the annual pretax withdrawn:\n', '80000')
while not withdrawal.isdigit:
    withdrawal = input('please enter integer only. or press enter to use default value')

min_years = default_input('Input minimum years of retirement:\n', '18')
while not min_years.isdigit:
    min_years = input('please enter integer only. or press enter to use default value')

most_likely_years = default_input('Input minimum years of retirement:\n', '25')
while not most_likely_years.isdigit:
    most_likely_years = input('please enter integer only.')

max_years = default_input('Input minimum years of retirement:\n', '40')
while not max_years.isdigit:
    max_years = input('please enter integer only.')

num_cases = default_input('Input number of lifetimes to run:\n', '50000')
while not num_cases.isdigit:
    num_cases = input('Please input integers only, or press enter to use the default value')

# check for other invalid input
if not int(min_years) < int(most_likely_years) < int(max_years) or int(max_years) > 99:
    print('some of your numbers doesnt not make sense')
    print('please make sure min_years < most_likely_years < max_years')
    print('please make sure the max_years is less than 99')
    print('exiting the program...', file = sys.stderr)
    sys.exit(1)

def montecarlo(returns):
    """Run MCS and return investment value at end-of-plan and bankrupt count."""
    case_count = 0
    bankrupt_count = 0
    outcome = []
    
    while case_count < int(num_cases):
        investments = int(start_value)
        start_year = random.randrange(0, len(returns))        
        duration = int(random.triangular(int(min_years), int(max_years),
                                         int(most_likely_years)))       
        end_year = start_year + duration 
        lifespan = [i for i in range(start_year, end_year)]
        bankrupt = False

        # build temporary lists for each case
        lifespan_returns = []
        lifespan_infl = []
        for i in lifespan:
            lifespan_returns.append(returns[i % len(returns)])
            lifespan_infl.append(infl_rate[i % len(infl_rate)])
            
        # loop through each year of retirement for each case run
      
        for index, i in enumerate(lifespan_returns):
            infl = lifespan_infl[index]

            # don't adjust for inflation the first year
            if index == 0:
                withdraw_infl_adj = int(withdrawal)
            else:
                withdraw_infl_adj = int(withdraw_infl_adj * (1+infl))

            investments -= withdraw_infl_adj
            investments = int(investments * (1 + i))


            if investments <= 0:
                bankrupt = True
                break

        if bankrupt:
            outcome.append(0)
            bankrupt_count += 1
        else:
            outcome.append(investments)
            
        case_count += 1

    return outcome, bankrupt_count

def bankrupt_prob(outcome, bankrupt_count):
    """return probabilty of ruin"""
    total = len(outcome)
    odds = round(100*bankrupt_count/total, 1)

    print("\nInvestment type: {}".format(invest_type))
    print("Starting value: ${:,}".format(int(start_value)))
    print("Annual withdrawal: ${:,}".format(int(withdrawal)))
    print("Years in retirement (min-ml-max): {}-{}-{}"
          .format(min_years, most_likely_years, max_years))
    print("Number of runs: {:,}\n".format(len(outcome)))
    print("Odds of running out of money: {}%\n".format(odds))
    print("Average outcome: ${:,}".format(int(sum(outcome) / total)))
    print("Minimum outcome: ${:,}".format(min(i for i in outcome)))
    print("Maximum outcome: ${:,}".format(max(i for i in outcome)))
    return odds



def main():
    """
    call mcs simulation
    plot bar charts 
    """
    # user input is at above
    outcome, bankrupt_count = montecarlo(investment_type_args[invest_type])
    odds = bankrupt_prob(outcome, bankrupt_count)

    plot_data = outcome[:3000]
    # only plot the first 3000 lifetimes 
    # stochastic plot can look very messy and confusing in large sample size

    plt.figure('Outcome by Case (showing first {} runs'. format (len(plot_data)), figsize = (16,5))
    # width, height (inch)
    index = [i+1 for i in range(len(plot_data))]        # adjust the indexing to starting from 1
    plt.bar(index, plot_data, color = 'black')          # x, y, color
    plt.xlabel ('Simulated lifetimes', fontsize = 18)
    plt.ylabel('Fund remaining', fontsize = 18)
    ax = plt.gca()                                      # get current axis
    ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    #https://www.w3schools.com/python/ref_string_format.asp
    plt.title('Probability of ruin = {}%'.format(odds))
    plt.show()

if __name__ == '__main__':
    main()






            





        







