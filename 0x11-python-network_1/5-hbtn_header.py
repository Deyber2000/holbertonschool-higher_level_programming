#!/usr/bin/python3
'''Script that sends request to URL and displays value of
X-Request-Id in response header
'''
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
