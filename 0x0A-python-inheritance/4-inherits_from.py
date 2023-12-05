#!/usr/bin/python3

"""
Inherites_form Module
Create a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
"""

def inherits_from(obj, a_class):
    """
    Function that checks if obj is an instance of class
    inherited from a_class (directly or indirectly.
    Args:
        obj: object
        a_class: class
    Notes:
        use type() to get specific class
        use isinstance() to get class and any parent class too
        use issubclass() to get what object is a subclass of

    Return: True of False
    """
    if not type(obj) == a_class and issubclass(type(obj), a_class):
        return (True)
    else:
        return (False)

