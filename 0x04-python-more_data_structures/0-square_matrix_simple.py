#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for line in matrix:
        new_matrix = [i ** 2 for i in line]
    return (new_matrix)
