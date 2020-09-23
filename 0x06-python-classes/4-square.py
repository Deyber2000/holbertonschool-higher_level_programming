#!/usr/bin/python3
class Square:
    """Square with private instance attribute and instantiation"""

    def __init__(self, size=0):
        """Initialize data"""
        self.__size = size

    def area(self):
        """Return square area"""
        return (self.__size ** 2)

    @property
    def size(self):
        """Retrieve size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets size and handles errors"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
