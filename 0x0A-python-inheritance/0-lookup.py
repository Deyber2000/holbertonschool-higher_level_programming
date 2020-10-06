#!/usr/bin/python3
"""Module for lookup()"""


def lookup(obj):
    """Function that returns a list of available attributes
       and methods of an object
    Arguments:
        obj: the object to list attributes of
    Returns:
        list: list of all attributes
    """
    return (dir(obj))
