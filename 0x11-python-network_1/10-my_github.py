#!/usr/bin/python3
'''Takes Github credentials and uses Github API to display id'''
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'
    request = requests.get(url, auth=(username, password))
    response = request.json()
    print(response.get('id', 'None'))
