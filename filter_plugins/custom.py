#!/usr/bin/python
import re

def regex_matches(_key, _regex):
    for r in _regex:
        m = re.compile("(?:" + r + r")\Z")
        if m.match(_key):
            return True
    return False

def dict_process(_dict, _regex, _strip=False):
    """This function processes dicts with a regex
    Parameters:
        _dict  (dict):  Dictionnary to process
        _strip (int) :  True to strip, False to filter
        _regex (list):  List of regex to process the dict
    """
    tmp_dict = {}
    for key, value in _dict.items():
        if regex_matches(key, _regex) is not _strip:
            tmp_dict[key] = value
    # Return tmp_dict if _regex list 
    # isn't empty, otherwise return _dict
    return tmp_dict if _regex else _dict

def dict_filter_keys(_dict, _regex):
    return dict_process(_dict, _regex, False)

def dict_strip_keys(_dict, _regex):
    return dict_process(_dict, _regex, True)

class FilterModule(object):
    def filters(self):
        return {
            'dict_process': dict_process,
            'dict_filter_keys': dict_filter_keys,
            'dict_strip_keys': dict_strip_keys
        }
