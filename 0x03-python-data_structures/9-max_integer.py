#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list:
        a = my_list[0]
        for x in my_list:
            if x > a:
                a = x
        return a
    else:
        return None
