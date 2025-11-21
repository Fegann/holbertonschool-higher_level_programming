#!/usr/bin/python3
def best_score(a_dictionary):
    x = 0
    item = ""
    for i in a_dictionary.keys():
        if a_dictionary[i] > x:
            x = a_dictionary[i]
            item = i
    return item
