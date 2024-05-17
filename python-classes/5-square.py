#!/usr/bin/python3
"""
Define a square class
"""
class Square:
    """
    define attribute of square
    """
    def __init__(self, size=0):
        """
        initialize a square
        Args:
            size (int, optional): size of the square. Defaults to 0.
        Raises:
                TypeError: size must be an integer
                ValueError: size must be >=0
        """
        self.size = size

    @property
    def size(self):
        """
        Returns:
            int: size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Args:
                value (int): size of square
        Raises:
                TypeError: size must be an integer
                ValueError: size must be >=0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Returns:
            int: return square of size
        """
        return self.__size ** 2

    def my_print(self):
        """
        print a square of self.__size with #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
