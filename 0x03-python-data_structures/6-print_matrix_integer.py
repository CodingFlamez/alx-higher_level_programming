#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    b = len(matrix)
    for x in range(b):
        a = len(matrix[x])
        for y in range(a):
            if y < (a-1):
                print("{:d}".format(matrix[x][y]), end=' ')
            else:
                print("{:d}".format(matrix[x][y]))
   print()
