#!/usr/bin/python3
'''Takes in URL, sends request, displays response while handling errors'''
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    request = requests.get(url)
    if request.status_code >= 400:
        print('Error code: {}'.format(request.status_code))
    else:
        print(request.text)
