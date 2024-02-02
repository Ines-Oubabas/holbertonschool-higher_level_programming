#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for L in matrix:
        for i in range(len(L)):
            print("{:d}".format(L[i]), end=' ' if i != len(L) - 1 else '')
            print()
