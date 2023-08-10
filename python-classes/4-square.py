#!/usr/bin/python3
"""Example of docstrings for module"""


class Square:
    """class Square defined with private attribute size"""
    def size(self):
        """retrieving instance attribute"""
        return self.__size
    
    def __init__(self, size=0):
        """initializing object size"""
        self.__size = size
    
    def size(self, value):
        """Property setter"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """finding area of a square"""
        return (self.__size * self.__size)
