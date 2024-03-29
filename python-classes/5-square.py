#!/usr/bin/python3
"""Example of docstrings for module"""


class Square:
    """class Square defined with private attribute size"""

    @property
    def size(self):
        """retrieving instance attribute"""
        return self.__size

    def __init__(self, size=0):
        """initializing object size"""
        self.size = size

    @size.setter
    def size(self, value):
        """Property setter"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """finding area of a square"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints the square with # character """
        i, j = 0, 0
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
