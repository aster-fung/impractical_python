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
    # print('number of unique bdays: ', unique_bdays_count)
    #print('total ppl in the room: ', popul)
    #print('shared bday ppl no: ',popul_match)
    return popul_match

def polling(popul, master_dict_list):
    polled_dict = {}
    for iteration in master_dict_list:
        for total, match in iteration:
            polled_dict.add(total,None)



            True
    return None



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
        

    
    total_turn = 0                              # total no of iteration for monitoring
    total_popul_list_part_key = []              # key to zip total no. of ppl in the room
    match_popul_list_part_value = []            # value to zip no of ppl who have matches
    master_dict_list = []                       # to store all total:match dicts
                                                # [{m:d, m,d,...},
                                                #  {m:d, m,d,...},
                                                #  {m:d, m,d,...},   
                                                #   ...
                                                #  {m:d, m,d,...}]

    for turn in range(simulation_cycles):
        for popul in range(0,popul_range+2,2):
            total_turn += 1
            #print('total turn: ', total_turn)
            #print('iterate cycle: ', turn+1)
            
            bdays = generate_bdays(popul)                          
            popul_match = count_bday_match(popul, bdays)           
            total_popul_list_part_key.append(popul)
            match_popul_list_part_value.append(popul_match)
            #print('key: ', total_popul_list_part_key)
            #print('key len', len(total_popul_list_part_key))
            #print('value:', match_popul_list_part_value)
            #print('value len', len(match_popul_list_part_value))

        dict_per_iteration = {total: match for total, match in zip(total_popul_list_part_key, match_popul_list_part_value)}
        del dict_per_iteration[0]                   # quick fix clean up
        # print(dict_per_iteration)
        master_dict_list.append(dict_per_iteration) 
    
    for iteration in master_dict_list:
        print('\n')
        print(iteration)
    

    

             

if __name__ == '__main__':
    main()
