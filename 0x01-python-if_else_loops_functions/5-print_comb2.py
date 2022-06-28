#!/usr/bin/python3
for i in range(10):
    for x in range(10):
        if x == 9 and i == 9:
            print(f"{i}{x}")
        else:
            print(f"{i}{x}", end=', ')
