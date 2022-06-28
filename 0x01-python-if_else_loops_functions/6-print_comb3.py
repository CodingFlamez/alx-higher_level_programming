#!/usr/bin/python3
for i in range(10):
    for x in range(10):
        if ( i < x):
            if (i == 8) and (x == 9):
                print(f"{i}{x}")
            else:
                print(f"{i}{x}", end=', ')
