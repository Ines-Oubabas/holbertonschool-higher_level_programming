#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    int_sum = 0
    for i in range(1, len(argv)):
        int_sum += int(argv[i])
    print("{}".format(int_sum))
