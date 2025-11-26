#!/usr/bin/python3
''' writes text to the file '''

def write_file(filename="", text=""):
    with open(filename, encoding="UTF-8") as f:
        f.write(text)
