#!/usr/bin/python3
"""Square with private attribute size, property getter size, property setter
   setter size, private instance position with setter and getter,
   public instance of area to return square area and my_print to print
   stdout square with '#'"""


class Square:
    """Square with private instance attribute and instantiation"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize data"""
        self.size = size
        self.position = position

    def area(self):
        """Return square area"""
        return (self.__size ** 2)

    def my_print(self):
        """Print square with # to stdout"""
        if self.__size <= 0:
            print()
            return
        for row in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for k in range(self.__size):
                    print('#', end='')
            print()

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

    @property
    def position(self):
        """Retrieve position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Sets position and handles errors"""
        if len(value) < 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def __str__(self):
        """Print string from main"""
        new_str = ""
        if self.__size is 0:
            return new_str

        for row in range(self.__position[1]):
            new_str += '\n'
        for i in range(self.__size):
            new_str += ' ' * self.__position[0]
            new_str += '#' * self.__size
            new_str += '\n'
        return (new_str[:-1])
