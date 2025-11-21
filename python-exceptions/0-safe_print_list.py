#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = ''
    b = 0
    try:
        for i in range(x):
            a += str(my_list[i])
            b += 1
        a = int(a)
        return "{}\n{}".format(a,b)
    except:
        print("error")
