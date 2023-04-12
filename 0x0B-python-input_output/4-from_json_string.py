#!/usr/bin/python3
""" Module converts an object to jason string """


import json


def from_json_string(my_str):
    """
        function returns an object represented by a JSON string
        Args:
            my_str: jason string
        Returns:
            returns an object represented by a JSON string
    """

    return json.loads(my_str)
