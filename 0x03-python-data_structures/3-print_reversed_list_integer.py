#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    a = len(my_list)
    my_list.reverse()
    for x in range(a):
        print("{:d}".format(my_list[x]))
