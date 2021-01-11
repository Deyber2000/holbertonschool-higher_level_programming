#!/usr/bin/python3
'''Script to take in URL and email, send POST request, displays response'''
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    request = requests.post(url, data=email)
    print(request.text)
