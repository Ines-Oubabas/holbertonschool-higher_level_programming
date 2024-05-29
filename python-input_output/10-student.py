#!/usr/bin/python3
"""
fonction qui ecrit un student
"""


class Student:
    """class Student"""

    def __init__(self, first_name, last_name, age):
        """initilize the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return dictionary representation of Student"""
        if attrs is None:
            return self.__dict__
        else:
            return {attr: self.__dict__[attr]
                    for attr in attrs if attr in self.__dict__}
