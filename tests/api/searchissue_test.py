import pytest


class TestSearchIssue:

    @pytest.mark.parametrize("number_searched_issue, expected_status_code",
                             [('1', 200),
                              ('5', 200)])
    def test_search_issue(self, rest_actions, number_searched_issue, expected_status_code):
        path = '/rest/api/2/search'
        jdl = '?jql=project=WEBINAR&startAt=0&maxResults=' + number_searched_issue
        status_code, resp_json = rest_actions.search_issue_rest(path, jdl)
        assert status_code == 200
        issue_list = resp_json['issues']
        assert len(issue_list) == int(number_searched_issue)
        for issue in issue_list:
            assert 'WEBINAR' in issue['key']

    def test_search_issue_noresult(self, rest_actions):
        path = '/rest/api/2/search'
        jdl = '?jql=project=WEBINARxxx'
        status_code, resp_json = rest_actions.search_issue_rest(path, jdl)
        assert status_code == 400
        assert resp_json['errorMessages'][0] == "The value 'WEBINARxxx' does not exist for the field 'project'."
