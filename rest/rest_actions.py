import json

import requests
from requests.auth import HTTPBasicAuth


class RestActions:
    HEADERS = {'content-type': 'application/json'}
    HOST = None
    AUTH = None

    def __init__(self, host, user_name, user_pass):
        self.HOST = host
        self.AUTH = HTTPBasicAuth(user_name, user_pass)

    def login_rest(self, path):
        response = requests.get(self.HOST + path, auth=self.AUTH, headers=self.HEADERS)
        try:
            msg = response.json()['name']
        except json.decoder.JSONDecodeError as err:
            msg = response.text
        return response.status_code, msg

    def create_issue_rest(self, path, issue_data):
        key_issue = None
        id_issue = None
        error = None
        response = requests.post(self.HOST + path, auth=self.AUTH, data=issue_data, headers=self.HEADERS)
        if response.status_code == 201:
            key_issue = response.json()['key']
            id_issue = response.json()['id']
        else:
            error = response.json()['errors']['summary']
        return response.status_code, key_issue, id_issue, error

    def update_issue_rest(self, path, issue_data):
        response = requests.put(self.HOST + path, auth=self.AUTH, data=issue_data, headers=self.HEADERS)
        return response.status_code

    def get_issue_rest(self, path):
        response = requests.get(self.HOST + path, auth=self.AUTH, headers=self.HEADERS)
        return response.status_code, response.json()

    def search_issue_rest(self, path, jdl):
        response = requests.post(self.HOST + path + jdl, auth=self.AUTH, headers=self.HEADERS)
        return response.status_code, response.json()



