#!/usr/bin/python3

def uniq_add(my_list=[]):
    '''A function that adds all unique integers of a list'''

    new_list = set(my_list)
    sum = 0
    for i in new_list:
        sum = sum + i

    return sum
