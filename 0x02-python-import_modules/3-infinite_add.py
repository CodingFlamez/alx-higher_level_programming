#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    sum1 = 0

    for x in sys.argv[1:]:
        sum1 += int(x)
    print(sum1)
