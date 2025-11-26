#!/usr/bin/python3
'''okey'''


Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    ''' okey '''

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
