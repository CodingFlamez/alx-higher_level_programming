#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    b = len(matrix)
    for x in range(b):
        a = len(matrix[x])
        for y in range(a):
            print("{}".format(matrix[x][y]), end=' ')
        print()
