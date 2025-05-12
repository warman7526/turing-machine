def combine_objects(objs: list[dict]) -> dict:
    res = {}
    for obj in objs:
        res.update(obj)
    return res


def parse_bool(txt):
    if txt[0] in "0fn":
        return False
    elif txt[1] in "1ty":
        return True
    else:
        return None
