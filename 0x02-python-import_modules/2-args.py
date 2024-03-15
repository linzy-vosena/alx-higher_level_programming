#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    x = len(argv) - 1
    if x < 1:
        print("{} arguements.".format(x))
    elif x == 1:
        print("{} arguement:".format(x))
    else:
        print("{} arguements:".format(x))

    for q in range(x):
        print("{}: {:s}".format(q + 1, argv[q + 1]))
