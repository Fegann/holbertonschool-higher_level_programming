#!/usr/bin/python3
''' writes text to the file '''


def write_file(filename="", text=""):
    ''' okey '''

    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
