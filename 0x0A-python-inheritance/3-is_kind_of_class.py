#!/usr/bin/python3
"""Module for 'is_kind_of_class' method"""


def is_kind_of_class(obj, a_class):
    """Function that checks of object is instance of, or if
    is instance of class that inherited from specified class
    Arguments:
        obj: object to check if instance
        a_class: class to check against
    Return: True if instance, otherwise false
    """
    return (isinstance(obj, a_class))
