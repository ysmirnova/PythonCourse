import pytest
from utils import json_actions as JA


class TestSearchIssue:

    def test_search_issue(self, rest_actions):
        path = '/rest/api/2/search'
        jdl = '?jql=project=WEBINAR&startAt=0&maxResults=2'
        rest_actions.search_issue_rest(path, jdl)
