def print_matrix_integer(matrix=[[]]):
    if not matrix or matrix == [[]]:
        return
    for row in matrix:
        print(' '.join("{:d}".format(num) for num in row))
