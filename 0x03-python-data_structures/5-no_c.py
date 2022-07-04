#!/usr/bin/python3

def no_c(my_string):
    a = len(my_string)
    y = ""
    for x in range(a):
        if my_string[x] in 'cC':
            continue
        else:
            y += my_string[x]
    return y
