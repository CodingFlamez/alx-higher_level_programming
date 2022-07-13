#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num_args = len(sys.argv) -1
    arguments = sys.argv

    print("{} {}{}".format(num_args, 
        ("argument" if num_args == 1 else "arguments"), 
        ('.' if num_args == 0 else ':')))
    if num_args > 0:
        for x in range(1, len(sys.argv)):
            print("{}: {}".format(x, sys.argv[x]))
