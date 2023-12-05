#!/usr/bin/python3

"""
Id_same_class Module.
Compare and return if object is exactly and instance of the specified class.
"""
def is_same_class(obj, a_class):
    """
    Function that compares if the object is 
    exactly and instance of a_class
    Args:
        obj: object
        a_class: class
    """
    if type(obj) is a_class:
        return True
    else:
        return False
