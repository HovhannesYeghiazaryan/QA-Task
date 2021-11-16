#!/usr/bin/env python
import ast
import requests

'''
Endpoint [GET] SINGLE USER (reqres.in/api/single_user) was not working, right url is https://reqres.in/api/users/2.
'''


def get_status_code(url):
    """
    :param url: https://reqres.in/api/users/2
    :return: status_code
    """
    return requests.get(url=url).status_code


def get_first_name(url):
    """
    :param url: https://reqres.in/api/users/2
    :return: first_name value
    """
    response = requests.get(url=url)
    response_bytes = response.content.decode('utf-8')
    response_body = ast.literal_eval(response_bytes)
    return response_body['data']['first_name']


if __name__ == '__main__':
    get_status_code('https://reqres.in/api/users/2')
    get_first_name('https://reqres.in/api/users/2')
