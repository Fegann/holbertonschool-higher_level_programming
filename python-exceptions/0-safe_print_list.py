#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = ''
    try:
        for i in range(x):
            a += str(my_list[i])
        return a
    except:
        print("error")
