#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 0 or my_list is None:
        return
    else:
        for i in range(len(my_list) - 1, -1, -1):
            print("{:d}".format(my_list[i]))
