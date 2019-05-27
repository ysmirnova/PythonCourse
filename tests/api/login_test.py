import pytest

from rest.login import RestLogin


class TestLogin:

    @pytest.mark.parametrize("user, password, expected",
                             [("incorrect", "YuliiaSmirnova", 401),
                              ("YuliiaSmirnova", "incorrect", 401),
                              ("YuliiaSmirnova", "YuliiaSmirnova", 200)])
    def test_login(self, user, password, expected):
        rest_login = RestLogin()
        url = 'https://jira.hillel.it/rest/auth/1/session'
        rest_login.login_rest(url, user, password)


