#!/usr/bin/python3
"""Module for Square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square that inherits from 'Rectangle'"""
    def __init__(self, size):
        """Instantiation with private size attribute"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Function to return area of square"""
        return (self.__size ** 2)
