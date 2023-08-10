#!/usr/bin/python3
"""Example of docstrings for module"""


class Square:
    """class Square defined with private attribute size"""

    @property
    def size(self):
        """retrieving instance attribute"""
        return self.__size

    def __init__(self, size=0, position=(0, 0)):
        """initializing object size"""
        self.size = size
        self.position = position

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
            print('\n' * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    def position(self):
        """Retrieving private instance attribute"""
        return self.__position

    def position(self, value):
        """Property setter"""
        if len(position) != 2 or type(value) is not tuple or type(value[0]) is not tuple or type(value[1]) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
