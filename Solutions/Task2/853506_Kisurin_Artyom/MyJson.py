def list_or_tuple_tojson(obj, level):
    ret = '\n[\n'
    for i in obj[:-1]:
        ret += '\t' * level + indict_to_json(i, level + 1) + ',\n'
    ret += '\t' * level + indict_to_json(obj[-1], level + 1)
    ret += '\n'+'\t'*(level-1)+']'
    return ret

def dict_tojson(obj: dict, level):
    json="\n{\n"
    for key, value in list(obj.items()):
        if key!=list(obj.keys())[-1]:
             json += '\t' * level + '"{}": {}'.format(str(key), indict_to_json(value, level + 1)) + ',\n'
        else:
            json += '\t' * level + '"{}": {}'.format(str(key), indict_to_json(value, level + 1)) + '\n'
    json+="}"
    return json

def indict_to_json(obj:dict,level):
     ret=""
    
     if isinstance(obj, dict):
        ret = dict_tojson(obj, level)

     elif isinstance(obj, list) or isinstance(obj, tuple):
        ret = list_or_tuple_tojson(obj, level)

     elif isinstance(obj, int) or isinstance(obj, float) or isinstance(obj, complex):
        ret = str(obj)

     elif isinstance(obj, str):
        ret = '"{}"'.format(str(obj))

     elif obj is None:
        ret = 'null'

     elif isinstance(obj, bool):
        if obj==True:
            ret="True"
        else:
            ret="False"
     else:
        ret += into_json(obj, level)

     return ret

def into_json(obj:object,level):
    json="{\n"
    if isinstance(obj, dict):
        dict1 = obj
    else:
        dict1 = vars(obj)
    for key, value in list(dict1.items()):
        if key!=list(dict1.keys())[-1]:
             json += '\t' * level + '"{}": {}'.format(str(key), indict_to_json(value, level + 1)) + ',\n'
        else:
            json += '\t' * level + '"{}": {}'.format(str(key), indict_to_json(value, level + 1)) + '\n'

    json+="}"
    return json
def to_json(obj: object):  
    return into_json(obj, 0)
