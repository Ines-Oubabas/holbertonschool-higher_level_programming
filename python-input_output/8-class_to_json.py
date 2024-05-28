#!/usr/bin/python3
"""
   function file for class_to_json
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer, and boolean) for JSON serialization
    of an object.

    Parameters:
    obj (object): An instance of a Class.

    Returns:
    dict: A dictionary representation of the object's attributes.
    """
    return obj.__dict__
