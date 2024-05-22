#!/usr/bin/python3
""" Define a class named Rectangle"""


class Rectangle:
    """Constructor to initialize width and height, with default values of 0"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """Getter method for width"""
    @property
    def width(self):
        return self.__width

    """Setter method for width with type and value checks"""
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """Getter method for height"""
    @property
    def height(self):
        return self.__height

    """ Setter method for height with type and value checks"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """ Method to calculate the area of the rectangle"""
    def area(self):
        return self.__width * self.__height

    """ Method to calculate the perimeter of the rectangle"""
    def perimeter(self):
        """Check if either width or height is zero, in which case perimeter is 0"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
