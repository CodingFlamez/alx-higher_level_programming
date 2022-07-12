#!/usr/bin/python3

def multiple_returns(sentence):
    a = ()
    len_a = len(sentence)
    a += (len_a,)
    if len_a == 0:
        a += None,
    else:
        a += sentence[0],
    return a
