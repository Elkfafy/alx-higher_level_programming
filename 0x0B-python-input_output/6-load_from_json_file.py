#!/usr/bin/python3
"""
module
"""

import json


def load_from_json_file(filename):
    """ function """

    with open(filename, encoding="UTF-8") as f:
        return json.loads(f.read())
