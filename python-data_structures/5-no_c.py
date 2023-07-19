#!/usr/bin/python3
def no_c(my_string):
    for char in my_string:
        if char != 'c' and char != 'C':
            newString = my_string
            newString = newString + char
            return newString
    return my_string
