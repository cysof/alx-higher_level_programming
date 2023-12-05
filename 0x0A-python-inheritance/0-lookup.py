#!/usr/bin/python3

"""
Lookup object module
create a function with the prototype lookup(obj).
"""

def lookup(obj):
    """
    function that return
    list of available attributes and methods of an object
    """
    return dir(obj)
