#!/usr/bin/python3
import urllib
import sys
'''okey '''

if __name__ == "__main__":
    url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    a = response.headers
    print(a['X-Request-Id'])
