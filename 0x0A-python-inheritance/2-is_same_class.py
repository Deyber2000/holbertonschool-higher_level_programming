#!/usr/bin/python3
"""Module for 'is_same_class' method"""


def is_same_class(obj, a_class):
    """Function to check if object is instance of class
    Arguments:
        obj: object to check
        a_class: specified class to check against
    Return:
        True if exactly an instance, otherwise False
    """
    return (type(obj) is a_class)
