#!/usr/bin/python3
def raise_exception():
    """Raises a TypeError with a custom message."""
    raise TypeError("This is a custom type error message.")
try:
    raise_exception()
except TypeError as e:
    print("Caught an exception:", e)
