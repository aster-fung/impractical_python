"""
use monte carlo simulation to determine the minimal number of people to reach the probabilty where half of the people share the same birth month and day in a room

output:
- the miminal number of people needed to be in the room to be 50/50 chance that 2 of them share the same birth month and day
- plot probabilty of meeting a person with same birth month and day against the number of people in the room

"""
import datetime
from random import randrange
from collections import Counter
import numpy as np



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
    print("lenisequal", check)
    print ('0 in total: ', 0 in total)
    print('0 in match: ', 0 in match)
    print('------')
    return total, match

"""
def generate_probi_list(total_list, match_list):
    
    param: 
    total_list: 1D list: no of ppl in the room 
    match_list: 1D list: no of ppl with matching bdays corresponding to total 
    
    prob_list = []
    for i in range(1, len(total_list)):
        # try:
        print('match: ', match_list[i], 'total: ', total_list[i])
        prob = match_list[i]/total_list[i]
        prob_list.append(prob)
        # except ZeroDivisionError: 
        #    pass
    print('probaility:')
    print(prob_list[0:5])
    return prob_list 
"""


def main():

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
            else:
                print('please enter the numbers in the range specified')
        except ValueError:
            print('please input integers only')
            continue
    
    total_turn = 0                       # total no of iteration for monitoring
    total_popul_per_iter = []            # 'key' to zip total no. of ppl in the room
    match_popul_per_iter = []            # 'value' to zip no of ppl who have matches
    
    for iter in range(simulation_cycles):
        probi_per_iter = []
        for popul in range(0,popul_range+2,2):
            total_turn += 1
            # print('total turn: ', total_turn)
            # print('iterate cycle: ', turn+1)
            
            bdays = generate_bdays(popul)                          
            popul_match = count_bday_match(popul, bdays)           
            total_popul_per_iter.append(popul)
            match_popul_per_iter.append(popul_match)
            #print('total ppl')
            print(total_popul_per_iter)
            #print(len(total_popul_per_iter))
            # print('match')
            print(match_popul_per_iter)
            #print(len(match_popul_per_iter))
            
        total_popul_per_iter, match_popul_per_iter = zero_cleanup(total_popul_per_iter,match_popul_per_iter)   
        # probi_per_iter = generate_probi_list(total_popul_per_iter, match_popul_per_iter)

if __name__ == '__main__':
    main()
