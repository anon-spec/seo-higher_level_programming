#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list)):
        if (len(my_list)) == 0:
            print("")
        if my_list is None:
            my_list = []
        else:
            print("{:d}".format(my_list[-i - 1]))
