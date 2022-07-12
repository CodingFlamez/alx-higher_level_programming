#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    if len_a < len_b:
        tuple_a += (0,)
    elif len_b < len_a:
        tuple_b += (0,)
    a = [x + y for x, y in zip(tuple_a, tuple_b)]
    return tuple(a)
