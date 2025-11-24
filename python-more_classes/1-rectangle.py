#!/usr/bin/python3
'''okey'''


class Rectangle:
    '''okey'''

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @width.setter
    def width(self, value):
        if not isinstance(value ,int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be  >= 0")
        self.width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be  >= 0")
        self.height = value
