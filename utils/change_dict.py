def change_value_by_key_world(obj, key_world, dict_for_change):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(value, str) and key_world in value:
                obj[key] = dict_for_change[key]
            change_value_by_key_world(value, key_world, dict_for_change)
    elif isinstance(obj, list):
        for item in obj:
            change_value_by_key_world(item, key_world, dict_for_change)


def get_values_by_key(obj, key_for_search, keys_list):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(value, str) and key == key_for_search:
                keys_list.append(obj[key])
            get_values_by_key(value, key_for_search, keys_list)
    elif isinstance(obj, list):
        for item in obj:
            get_values_by_key(item, key_for_search, keys_list)

