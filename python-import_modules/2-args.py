#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = len(argv) - 1
    if (args < 1):
        print("{} arguments.".format(args))
    elif (args == 1):
        print("{} argument:".format(args))
    else:
        print("{} arguments:".format(args))
    for i in range(args):
        print("{}: {:s}".format(i + 1, argv[i + 1]))
