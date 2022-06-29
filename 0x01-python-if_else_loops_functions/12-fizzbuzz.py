#!/usr/bin/python3
def fizzbuzz():
    for x in range(1, 101):
        if (x % 3) and (x % 5):
            print("{}".format(x), end=' ')
        else:
            b = ''
            if (x % 3) == 0:
                b += 'Fizz'
            if (x % 5) == 0:
                b += 'Buzz'
            print("{}".format(b), end=' ')
