#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    a = [row[:] for row in matrix]
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] **= 2
    return a
