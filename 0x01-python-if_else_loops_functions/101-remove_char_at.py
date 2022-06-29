#!/usr/bin/python3
def remove_char_at(str, n):
    y = len(str)
    b = ''
    for x in range(y):
        if x == n:
            continue
        else:
            b += str[x]
    return b
