#!/usr/bin/python3
def uniq_add(my_list=[]):
    a = set(my_list)
    b = 0
    result = map(lambda x : b+=x, a)
    return result
