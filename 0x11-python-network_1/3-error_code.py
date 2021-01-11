#!/usr/bin/python3
'''Takes in URL, sends request, and displays body while managing errors'''
import urllib.request
import sys


if __name__ == "__main__":
    request = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(request) as r:
            print(r.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
