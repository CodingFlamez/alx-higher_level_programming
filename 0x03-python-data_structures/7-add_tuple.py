#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    if len_a < 2:
        for x in range(len_a, 2):
            tuple_a += (0,)
    if len_b < 2:
        for x in range(len_b, 2):
            tuple_b += (0,)
    a = [x + y for x, y in zip(tuple_a, tuple_b)]
    return tuple(a[:2])
