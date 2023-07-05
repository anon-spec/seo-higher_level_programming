#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range(0 - (len(my_list))):
        if (len(my_list)) == 0:
            print("")
        else:
            print("{:d}".format(my_list[i]))
