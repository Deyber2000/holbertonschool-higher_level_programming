#!/usr/bin/python3
"""
defines a class rentangle
"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initialize data"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width property"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Width property setter"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Height property"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Height property setter"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Area public instance method"""
        return (self.height * self.width)

    def perimeter(self):
        """Perimeter public instance method"""
        if self.width == 0 or self.height == 0:
            return (0)
        return ((self.height + self.width) * 2)
