import json
import os

import pytest

from rest.rest_actions import RestActions


class TestLogin:
    HOST = 'https://jira.hillel.it'
    USER = 'YuliiaSmirnova'
    PASSWORD = 'YuliiaSmirnova'

    @pytest.mark.parametrize("user, password, expected_status_code, expected_response_msg",
                             [("incorrect", "YuliiaSmirnova", 401, "Unauthorized"),
                              ("YuliiaSmirnova", "incorrect", 401, "Unauthorized"),
                              ("YuliiaSmirnova", "YuliiaSmirnova", 200, "YuliiaSmirnova")])
    def test_login(self, user, password, expected_status_code, expected_response_msg):
        path = '/rest/auth/1/session'
        rest_actions = RestActions(self.HOST, user, password)
        status_code, response_msg = rest_actions.login_rest(path)
        assert status_code == expected_status_code
        assert expected_response_msg in response_msg

    @pytest.mark.parametrize("data_file, expected_status_code, expected_key, expected_error",
                             [("issue_full_field.json",  201, "WEBINAR", None),
                              ("issue_requared_field.json", 201, "WEBINAR", None),
                              ("issue_long_name.json", 400, None, "Summary must be less than 255 characters.")])
    def test_create_issue(self, data_file, expected_status_code, expected_key, expected_error):
        path = '/rest/api/2/issue'
        rest_actions = RestActions(self.HOST, self.USER, self.PASSWORD)
        json_path = os.path.join(os.getcwd(), data_file)
        with open(json_path) as json_file:
            issue_data = json.load(json_file)
        status_code, key_issue, id_issue, error = rest_actions.create_issue_rest(path, json.dumps(issue_data))
        assert status_code == expected_status_code
        assert expected_key in key_issue
        assert expected_error == error



