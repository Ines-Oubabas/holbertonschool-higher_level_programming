#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None or len(matrix) == 0:
        return []

    new_matrix = []
    for row in matrix:
        squared_row = [x**2 for x in row]
        new_matrix.append(squared_row)

    return new_matrix
