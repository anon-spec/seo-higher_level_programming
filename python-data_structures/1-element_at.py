#!/usr/bin/python3
def element_at(my_list, idx):
    for i in my_list:
        if idx < 0:
            return None
        elif idx > range(my_list):
            return None
        else:
            print("{}".format(idx))
