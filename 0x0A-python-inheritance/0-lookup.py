#!/usr/bin/python3

"""
Look up module
create a function that returns the list of
of available attributes and methods of an objects
"""

def lookup(obj):
    """
    function that return
    list of available attributes and methods of an object
    """
    return dir(obj)
