import json

import requests
from requests.auth import HTTPBasicAuth


class RestLogin:
    DEFAULT_HEADER = 'application/json'

    def __init__(self):
        hh = 1

    def login_rest(self, url, user_name, user_pass):
        _headers = {'content-type': 'application/json'}

        _response = requests.get(url, auth=HTTPBasicAuth(user_name, user_pass), headers=_headers)
        return _response.status_code

    def create_issue_rest(self, url, user_name, user_pass):
        _headers = {'content-type': 'application/json'}

        _response = requests.post(url, auth=HTTPBasicAuth(user_name, user_pass), headers=_headers)
        return _response.status_code

