#!/usr/bin/python3

if __name__ == "__main__":
    import calculation_1 as calculator_1
    import sys

    args = sys.argv

    if len(sys.argv) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(args[1])
    b = int(args[3])

    if args[2] == '+':
       c = calculator_1.add(a, b)
    elif args[2] == '-':
       c = calculator_1.sub(a, b)
    elif args[2] == '*':
       c = calculator_1.mul(a, b)
    elif args[2] == '/':
       c = calculator_1.div(a, b)
    else:
       print("Unknown operator. Available operators: +, -, * and /")
       sys.exit(1)
    print("{} {} {} = {}".format(a, args[2], b, c))
    sys.exit(0)
