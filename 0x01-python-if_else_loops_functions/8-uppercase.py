#!/usr/bin/python3
def uppercase(str):
    for x in range(len(str)):
        y = ord(str[x])
        if y in range(97, 123):
            y = y - 32
        if x == (len(str) - 1):
            print("{}".format(chr(y)))
        else:
            print("{}".format(chr(y)), end='')
        print()



