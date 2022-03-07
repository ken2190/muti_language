def dict_to_object(dictObj, cls):
    if not isinstance(dictObj, dict):
        return dictObj
    inst = cls()
    for k, v in dictObj.items():
        inst.__setitem__(k, v)
    return inst
