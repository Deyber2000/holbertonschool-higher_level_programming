#!/usr/bin/python3
"""
defining a class rectangle
"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    """Counts number of instances"""

    print_symbol = '#'
    """Used as symbol for string representation"""

    def __init__(self, width=0, height=0):
        """Initialize data"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """Return str with character '#'"""
        string = ''
        for height in range(self.height):
            for width in range(self.width):
                string += str(self.print_symbol)
            string += '\n'
        return (string[:-1])

    def __repr__(self):
        """Return string representation of rectangle to recreate new one"""
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """Prints 'Bye rectangle...' when instance of Rectangle is deleted"""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns bigger Rectangle"""
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Return new Rectangle width == height == size"""
        return (cls(size, size))
