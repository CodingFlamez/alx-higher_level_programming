#!/usr/bin/python3

def magic_calculation(a, b):
    '''This is a python bytecode'''
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            result += a ** b / i
        except Exception:
            resukt = b + a
            break
    return result
