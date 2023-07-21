#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        row_str = [str(item) for item in row]
        print(" ".join(row_str))
