#!/usr/bin/python3
def no_c(my_string):
    newString = ''
    for char in my_string:
        if char != 'c' or char != 'C':
            newString = newString + char
        return newString
    return newString
