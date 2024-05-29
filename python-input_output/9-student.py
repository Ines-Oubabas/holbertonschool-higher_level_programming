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

    def to_json(self):
        """return dictionary representation of Student"""
        return self.__dict__
