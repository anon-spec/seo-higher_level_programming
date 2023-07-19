#!/usr/bin/python3
def no_c(my_string):
    for char in len(my_string):
        if char != 'c' and char != 'C':
            newString = char
            return newString
    return my_string
