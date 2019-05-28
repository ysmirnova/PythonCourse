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

        _data = json.dumps({
                    "fields": {
                                "project":{
                                        "key": "Webinar (WEBINAR)"
                                         },
                                "summary": "REST ye merry gentlemen.",
                                "description": "Creating of an issue using project keys and issue type names using the REST API",
                                "issuetype": {
                                                "name": "Bug"
                                            }
                                }
                })

        _response = requests.post(url, auth=HTTPBasicAuth(user_name, user_pass), data= _data,  headers=_headers)
        return _response.status_code
