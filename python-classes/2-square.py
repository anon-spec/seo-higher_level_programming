#!/usr/bin/python3
"""Example of docstrings for module"""


class Square:
    """class Square defined with private attribute size"""
    def __init__(self, size=0):
        """initializing object size"""
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
