#!/usr/bin/python3

def no_c(my_string):
    for x in my_string:
        if x in 'cC':
            continue
        else:
            print("{}".format(x), end='')
    print()
