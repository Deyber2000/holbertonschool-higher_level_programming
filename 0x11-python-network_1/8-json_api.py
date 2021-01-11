#!/usr/bin/python3
'''Takes in a letter and sends POST request to URL with letter as parameter'''
import requests
import sys


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ''
    request = requests.post(url, data={'q': q})
    try:
        response = request.json()
        if len(response) == 0:
            print('No result')
        else:
            print('[{}] {}'.format(response.get('id'), response.get('name')))
    except:
        print('Not a valid JSON')
