#!/usr/bin/python3
def print_last_digit(number):
    number = abs(number)
    a = number % 10
    print("{}".format(a), end='')
    return a
