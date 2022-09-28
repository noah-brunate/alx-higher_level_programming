#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    for i in range(2):
        for j in new_matrix[i]:
            j = j**2
    return new_matrix
