#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    names = dir()
    for i in range(0, len(names)):
        if (names[i][:2] != "__"):
            print("{:s}".format(names[i]))
