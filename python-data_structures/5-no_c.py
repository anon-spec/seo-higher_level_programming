#!/usr/bin/python3
def no_c(my_string):
    newString = my_string.copy()
    for char in my_string:
        if char != 'c' or char != 'C':
            newString = newString + char
        return newString
    return my_string
