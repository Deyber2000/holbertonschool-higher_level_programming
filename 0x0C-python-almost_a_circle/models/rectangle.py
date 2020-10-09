#!/usr/bin/python3
"""This module creates class Rectangle"""


from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes Rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """private attribute getter for width"""
        return (self.__width)

    @property
    def height(self):
        """private attribute getter for height"""
        return (self.__height)

    @property
    def x(self):
        """private attribute getter for x"""
        return (self.__x)

    @property
    def y(self):
        """private attribute getter for y"""
        return (self.__y)

    @width.setter
    def width(self, width):
        """setter for width"""
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @height.setter
    def height(self, height):
        """setter for height"""
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @x.setter
    def x(self, x):
        """setter for x"""
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @y.setter
    def y(self, y):
        """setter for y"""
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """Method to return area value of Rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """Method to print Rectangle with character #"""
        for y in range(self.__y):
            print('')
        for row in range(self.__height):
            for x in range(self.__x):
                print(' ', end='')
            for col in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """Overrides __str__ method to return new print"""
        return ('[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(
            self.id, self.x, self.y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """method that assigns an argument to each attribute
           1st arg: id
           2nd arg: width
           3rd arg: height
           4th arg: x
           5th arg: y
        """
        attributes = ["id", "width", "height", "x", "y"]

        if args:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        elif kwargs is not None:
            for key, value in kwargs.items():
                if hasattr(self, key):
                        setattr(self, key, value)

    def to_dictionary(self):
        """returns dictionary representation of a Rectangle"""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
