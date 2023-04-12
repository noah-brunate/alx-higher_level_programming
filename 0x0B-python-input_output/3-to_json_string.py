#!/usr/bin/python3
""" module converts an object to jason format """

import json


def to_json_string(my_obj):
    """
        function returns the JSON representation of an object (string)
        Args:
            my_obj: object to convert to jason
        Returns:
            returns the JSON representation of an object (string)
    """

    return json.dumps(my_obj)
