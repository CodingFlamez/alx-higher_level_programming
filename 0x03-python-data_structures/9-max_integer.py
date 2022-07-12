#!/usr/bin/python3

def max_integer(my_list=[]):
    a = 0
    for x in my_list:
        if x > a:
            a = x
    if my_list:
        return a
    else:
        return None
