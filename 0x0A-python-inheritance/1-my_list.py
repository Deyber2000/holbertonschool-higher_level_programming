#!/usr/bin/python3
"""Module for MyList class"""


class MyList(list):
    """Inherits from 'list'"""
    def print_sorted(self):
        """Method to print sorted list"""
        print(sorted(self))
