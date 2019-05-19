import json
import os
from pathlib import Path
from utils.change_dict import change_value_by_key_world, get_values_by_key
import xmltodict


class TestXMLToJson:

    def test_xml_to_json(self):
        dict_for_change = {"FIRST_NAME": "Julia",
                           "LAST_NAME": "Smirnova",
                           "YEAR_OF_BIRTH": "1982",
                           "MONTH_OF_BIRTH": "March",
                           "DAY_OF_BIRTH": "22",
                           "COMPANY": "Lohika",
                           "PROJECT": "Here",
                           "ROLE": "Automation QA",
                           "ROOM": "711",
                           "HOBBY": "Traveling"}
        project_folder = Path(os.getcwd()).parent
        xml_path = os.path.join(project_folder, "test_data.xml")
        assert os.path.exists(xml_path)

        with open(xml_path) as fd:
            dict_xml = dict(xmltodict.parse(fd.read()))
        keys_list = []
        get_values_by_key(dict_xml, "FIRST_NAME", keys_list)
        assert keys_list == ["Lector", "YOUR_FIRST_NAME", "TEST_FIRST_NAME"]

        change_value_by_key_world(dict_xml, "YOUR", dict_for_change)
        keys_list = []
        get_values_by_key(dict_xml, "FIRST_NAME", keys_list)
        assert keys_list == ["Lector", "Julia", "TEST_FIRST_NAME"]

        json_file = json.dumps(dict_xml)
        json_path = os.path.join(project_folder, "updated_tested_data.json")
        with open(json_path, 'w') as f:
            f.write(json_file)

        with open(json_path) as json_file:
            dict_json = json.load(json_file)
        keys_list = []
        get_values_by_key(dict_json, "FIRST_NAME", keys_list)
        assert keys_list == ["Lector", "Julia", "TEST_FIRST_NAME"]