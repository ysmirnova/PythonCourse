import json
import os


def json_file_to_string(data_file):
    json_path = os.path.join(os.getcwd(), data_file)
    with open(json_path) as json_file:
        issue_data = json.load(json_file)
    return json.dumps(issue_data)