"""
use monte carlo simulation to determine the minimal number of people to reach the probabilty where half of the people share the same birth month and day in a room

output:
- the miminal number of people needed to be in the room to be 50/50 chance that 2 of them share the same birth month and day
- plot probabilty of meeting a person with same birth month and day against the number of people in the room

"""
import datetime
from random import randrange
import pandas as pd


def generate_bdays(population):
    """
    params:
    population: int object

    return:
    collection_new_bday: list containing tuples (month, day)
    looks like this [(7, 25), (11, 29), (11, 1)]
    """
    # bdays = list[datetime.object]
    start_day = datetime.date(1902,1,1)
    end_day = datetime.date.today()
    delta_range = end_day-start_day         # return milliseconds
    delta_range = delta_range.days          # datatime.day 
    bdays = []

    counter = 0
    while counter < population+1:
        days_add = randrange(delta_range)
        bday = start_day + datetime.timedelta(days = days_add)
        bdays.append(bday)
        counter += 1

    collection_bday = []
    for each_bday in bdays:
        new_bday = (each_bday.month, each_bday.day)
        collection_bday.append(new_bday)
    collection_bday.pop()                   # quick fix to remove one extra bday 
    # print(collection_bday)
    return collection_bday


def count_bday_match(popul, bdays):
    """
    params:
    popul: int object: total no. of people in the room
    bdays: list object: 1d array containg birthdays (tuples: month(int), day(int)

    return:
    popul_bday_matches: int object: no of people in the room that share their bday with at least one person 
    """

    unique_bdays_count = len(set(bdays))
    if unique_bdays_count >= popul//2:
        popul_match = 2*(popul - unique_bdays_count)
    else:
        popul_match = 0
    #s print('number of unique bdays: ', unique_bdays_count)
    #s print('total ppl in the room: ', popul)
    #s print('shared bday ppl no: ',popul_match)
    return popul_match

def zero_cleanup(total, match):
    """
    removes 0s from match to avoid ZeroDivisionError when it comes to probability calculation
    removes value in totalcorresponding to the same of index position of that element removed from the match list 
    (better avoid try/except)


    param:
    total: 1D list of int
    match: 1D list of int. shld be same len as total

    return:
    total, match with 0 removed
    """
    i = 0
    for value in total:
        if value == 0:
            del total[i]
            del match[i]
        i +=1
    check = len(total) == len(match)
    #print("lenisequal", check)
    #print ('0 in total: ', 0 in total)
    #print('0 in match: ', 0 in match)
    return total, match


def generate_probability(total, match):
    """
    param: 
    total: 1D list: no of ppl in the room 
    match: 1D list: no of ppl with matching bdays corresponding to total 
    """
    prob_list = []
    for i in range(0, len(total)):
        # print('total: ', total[i],'match: ', match[i])
        prob = match[i]/total[i]
        prob_list.append(prob)
    return prob_list 


def minimal_total(total, probi,target = 0.5):
    """
    calculates minimal total number of people needed to reach the target probabilty

    param:
    total: 1D list: no of ppl in the room per iter
    probi: 1D list: corresponding probability to get ppl with identical bdays in the room per iter
    target: threshold probability for minimal total ppl cutoff

    returns:
    minimal: int: round up from float; minimal no of ppl need to reach the target prob with matching bdays
    """
    current_probi = 0
    current_total = 0
    for i in range(0, len(total)):
        if probi[i] >= target:
            current_probi = probi[i]
            current_total = total[i]
            break
    return current_total, current_probi


def display_min (simulation_cycles, min_total, min_prob):
    """
    param:
    simulation_cycles: user defined no of runs
    min_total: a list of minimum no of ppl needed for threshold probability
    min_prob: list of probability maching min_total

    return:
    df: Pandas.DataFrame object 
    """
    cycles = [cycle for cycle in range(1, simulation_cycles+1)]
    zipped = list(zip(cycles, min_total, min_prob))
    df = pd.DataFrame(zipped, columns = ['cycle', 'minimal people required', 'probability matching bdays'])
    print(df)
    return df

def main():
    play = True
    while play:
        check_input = False
        while not check_input:
            popul_range_str = input('maximum numbers of peoples in the room to test (2~ ): ')
            simulation_cycles_str = input('no of simulation cycles (10~ ):')
            try:
                popul_range = int(popul_range_str)
                simulation_cycles = int(simulation_cycles_str)      
                # limit total iteration to 10000 times?
                if popul_range>=2 or simulation_cycles>=10:
                    check_input = True
                    print('simulation running')
                else:
                    print('please enter the numbers in the range specified')
            except ValueError:
                print('please input integers only')
                continue
        
        print('.',end = '')
        total_turn = 0                       # total no of iteration for monitoring
        min_total_collection = []
        min_prob_collection = []

        for iter in range(simulation_cycles):
            #probi_per_iter = []                 # for clarity. in fact reinit in function 
            total_popul_per_iter = []            # 
            match_popul_per_iter = []            # 
            
            for popul in range(0,popul_range+2,2):
                total_turn += 1       
                bdays = generate_bdays(popul)                          
                popul_match = count_bday_match(popul, bdays)           
                total_popul_per_iter.append(popul)
                match_popul_per_iter.append(popul_match)

            total_popul_per_iter, match_popul_per_iter = zero_cleanup(total_popul_per_iter,match_popul_per_iter)   
            probi_per_iter = generate_probability(total_popul_per_iter, match_popul_per_iter)
            min_total, min_probi = minimal_total(total_popul_per_iter, probi_per_iter, 0.5)
            if min_probi > 0.5:
                min_total_collection.append(min_total)
                min_prob_collection.append(min_probi)
        
        if len(min_total_collection) < 1:
            print('not enough people please rerun with more people')
            play = False
            break
            

        # present data table
        print("=====================================================")
        print("simulation result:")
        display_min(iter, min_total_collection, min_prob_collection)
        print("=====================================================")
        
        # calculate and present the average
        average_min_total = round(sum(min_total_collection)/len(min_total_collection))
        average_prob = round(sum(min_prob_collection)/ len(min_prob_collection), 2)
        print ('The average minimal number people needs to reach 50% probability where half of the people share the birthday with at least one person in the room is ', average_min_total,' .')    
        print ('The corresponding average probability is ', average_prob)


if __name__ == '__main__':
    main()
