import pytest
from utils import json_actions as JA


class TestCreateIssue:
    @pytest.mark.parametrize("data_file, expected_status_code, expected_key, expected_error",
                             [("issue_json/issue_full_field.json", 201, "WEBINAR", None),
                              ("issue_json/issue_required_field.json", 201, "WEBINAR", None)])
    def test_create_positive_issue(self, rest_actions, data_file, expected_status_code, expected_key,
                                   expected_error):
        path = '/rest/api/2/issue'
        status_code, key_issue, id_issue, error = rest_actions.create_issue_rest(path,
                                                                                       JA.json_file_to_string(data_file))
        assert status_code == expected_status_code
        assert expected_key in key_issue
        assert expected_error == error

    def test_create_negative_issue(self, rest_actions):
        path = '/rest/api/2/issue'
        status_code, key_issue, id_issue, error = rest_actions.create_issue_rest(path,
                                                                                       JA.json_file_to_string('issue_json/issue_long_name.json'))
        assert status_code == 400
        assert key_issue is None
        assert error == "Summary must be less than 255 characters."
