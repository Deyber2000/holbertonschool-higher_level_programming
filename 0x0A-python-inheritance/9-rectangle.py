#!/usr/bin/python3
"""Module for Rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from 'BaseGeometry'"""
    def __init__(self, width, height):
        """Instantiation with private attributes and validate they are ints"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Method to return area of rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Method to print Rectangle"""
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
