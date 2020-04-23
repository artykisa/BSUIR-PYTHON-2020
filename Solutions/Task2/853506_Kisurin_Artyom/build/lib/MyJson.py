def list_or_tuple_tojson(obj, level):
    ret = '['
    for i in obj[:-1]:
        ret += indict_to_json(i, level + 1) + ', '
    ret += indict_to_json(obj[-1], level + 1)
    ret += ']'
    return ret


def dict_tojson(obj: dict, level):
    json = "{"
    for key, value in list(obj.items()):
        if key != list(obj.keys())[-1]:
            json += '"{}": {}'.format(str(key), indict_to_json(value, level + 1)) + ', '
        else:
            json += '"{}": {}'.format(str(key), indict_to_json(value, level + 1))
    json += "}"
    return json


def indict_to_json(obj: dict, level):
    ret = ""

    if isinstance(obj, dict):
        ret = dict_tojson(obj, level)

    elif isinstance(obj, list) or isinstance(obj, tuple):
        ret = list_or_tuple_tojson(obj, level)

    elif isinstance(obj, bool):
        if obj:
            ret = "true"
        else:
            ret = "false"

    elif isinstance(obj, int) or isinstance(obj, float) or isinstance(obj, complex):
        ret = str(obj)

    elif isinstance(obj, str):
        ret = '"{}"'.format(str(obj))

    elif obj is None:
        ret = 'null'

    else:
        ret += into_json(obj, level)

    return ret


def into_json(obj: object, level):
    json = "{"
    if isinstance(obj, dict):
        dict1 = obj
    for key, value in list(dict1.items()):
        if key != list(dict1.keys())[-1]:
            json += '"{}": {}'.format(str(key), indict_to_json(value, level + 1)) + ', '
        else:
            json += '"{}": {}'.format(str(key), indict_to_json(value, level + 1))

    json += "}"
    return json


def to_json(obj: object):
    return into_json(obj, 0)
