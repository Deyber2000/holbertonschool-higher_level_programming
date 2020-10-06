#!/usr/bin/python3
"""Module for 'MyInt' method"""


class MyInt(int):
    """Inherits from built-in 'int' but is backward"""

    def __eq__(self, other):
        """Changes == to !="""
        return (super().__ne__(other))

    def __ne__(self, other):
        """Changes != to =="""
        return (super().__eq__(other))
