#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        sub_len = len(matrix[i])
        for column in range(sub_len):
            if column != sub_len - 1:
                end_char = ' '
            else:
                end_char = ''
            print("{:d}".format(matrix[row][column]), end=end_char)
        print("")
