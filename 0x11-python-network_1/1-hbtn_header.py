#!/usr/bin/python3
'''Script to take in URL, send request, and display value of X-Request-Id'''
import urllib.request
import sys


if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as response:
        header = response.info()
        print(header.get('X-Request-Id'))
