#!/usr/bin/python3
'''Fetch a URL using requests and display body'''
import requests

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    response = requests.get(url)
    body = response.text

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
