#!/usr/bin/python3
''' open and read file'''


def read_file(filename = ""):
    ''' open and read file '''

    with open("filename", encoding = "UTF-8") as f:
        a = f.read()
        print(a)
