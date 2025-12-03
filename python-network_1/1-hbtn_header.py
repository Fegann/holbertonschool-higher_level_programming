#!/usr/bin/python3
'''okey'''
import urllib
import sys

if __name__ == "__main__":
    url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    a = response.headers
    print(a['X-Request-Id'])
