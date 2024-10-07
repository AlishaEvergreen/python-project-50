import json


def make_json(diffs):
    '''Converts a dictionary of differences into a formatted JSON string.'''
    return json.dumps(diffs, indent=1)
