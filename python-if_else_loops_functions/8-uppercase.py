#!/usr/bin/python3
def uppercase(str):
    b = ""
    for i in str:
	a = chr(ord(i)+32)
	b += a
    return b
