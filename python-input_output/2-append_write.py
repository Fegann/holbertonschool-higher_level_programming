#!/usr/bin/python3
'''okey'''


def append_write(filename="", text=""):
    '''okey'''

    with open(filename, "a", encoding="UTF-8") as f:
        f.write(text)
