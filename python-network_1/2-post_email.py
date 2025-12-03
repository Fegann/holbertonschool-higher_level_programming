#!/usr/bin/python3
'''post an email'''
import urllib.request
import urllib.parse
import sys
if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    data = urllib.parse.urlencode(values).encode('utf-8')
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
