#!/usr/bin/python3
"""Module for add_attribute"""


def add_attribute(my_obj, attribute, value):
    """Adds new attribute to object if it can"""
    if not hasattr(my_obj, "__dict__") and not hasattr(my_obj, "__slots__"):
        raise TypeError("can't add new attribute")
    if not hasattr(my_obj, attribute) and hasattr(my_obj, "__slots__"):
        raise TypeError("can't add new attribute")
    setattr(my_obj, attribute, value)
