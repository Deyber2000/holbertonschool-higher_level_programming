#!/usr/bin/python3
"""This module is for the Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class to inherit from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """returns size of Square"""
        return (self.width)

    @size.setter
    def size(self, size):
        """setter for size of Square"""
        self.width = size
        self.height = size

    def __str__(self):
        """override __str__ method"""
        return ('[Square] ({:d}) {:d}/{:d} - {:d}'.format(
            self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """Public getter for size"""
        return (self.width)

    @size.setter
    def size(self, value):
        """size setter for Square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes as args"""
        attributes = ["id", "size", "x", "y"]

        if args:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        elif kwargs is not None:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns dictionary representation of Square"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
