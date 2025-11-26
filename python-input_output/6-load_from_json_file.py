#!/usr/bin/python3
''' okey '''
import json


def load_from_json_file(filename):
    ''' okey '''

    with open(filename) as f:
        a = f.read()
        return json.loads(a)
