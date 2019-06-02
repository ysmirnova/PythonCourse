import pytest
from utils import json_actions as JA


class TestUpdateIssue:

    @pytest.mark.parametrize("data_file, names_values, expected_status_code, expected_value",
                             [("issue_json/issue_update_assignee.json", "assignee, name", 204, "YuliiaSmirnova"),
                              ("issue_json/issue_update_summary.json", "summary", 204, "Updated REST issue summary"),
                              ("issue_json/issue_update_priority.json", "priority, name", 204, "Medium")])
    def test_update_issue(self, rest_actions, create_issue_id, data_file, names_values, expected_status_code, expected_value) :
        path = '/rest/api/2/issue/' + create_issue_id
        status_code = rest_actions.update_issue_rest(path, JA.json_file_to_string(data_file))
        assert status_code == expected_status_code
        status_code, resp_json = rest_actions.get_issue_rest(path)
        assert status_code == 200
        actual_value = resp_json['fields']
        values_list = names_values.split(', ')
        for val in values_list:
            actual_value = actual_value[val]
        assert actual_value == expected_value


