#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    a = len(my_list)
    for x in range(a):
        print("{}".format(my_list.pop()))
