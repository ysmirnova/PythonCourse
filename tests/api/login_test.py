import pytest

from rest.rest_actions import RestActions


class TestLogin:
    HOST = 'https://jira.hillel.it'
    USER = 'YuliiaSmirnova'
    PASSWORD = 'YuliiaSmirnova'

    @pytest.mark.parametrize("user, password, expected_status_code, expected_response_msg",
                             [("incorrect", PASSWORD, 401, "Unauthorized"),
                              (USER, "incorrect", 401, "Unauthorized"),
                              (USER, PASSWORD, 200, "YuliiaSmirnova")])
    def test_login(self,  user, password, expected_status_code, expected_response_msg):
        path = '/rest/auth/1/session'
        rest_actions = RestActions(self.HOST, user, password)
        status_code, response_msg = rest_actions.login_rest(path)
        assert status_code == expected_status_code
        assert expected_response_msg in response_msg



