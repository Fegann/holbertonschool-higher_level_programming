#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    a = my_list.copy()
    for i in range(len(a)):
        if a[i] % 2 == 0:
            a[i] = True
        else:
            a[i] = False
    return a
