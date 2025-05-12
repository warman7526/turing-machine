import lib.utils


def decode_instr_simple(instr):
    name, data = instr.split("=")
    return {name: [decode_action_simple(data[:3]), decode_action_simple(data[3:])]}


def decode_param_simple(instr):
    name, data = instr.split("=")
    name = name[1:]
    if name in ["size", "fill", "start", "max_iter"]:
        data = int(data)
    elif name in ["loop"]:
        data = lib.utils.parse_bool(data)
    return {name: data}


def decode_action_simple(data):
    return (
        {
            "actions": [
                {"type": "write", "value": int(data[0])},
                {"type": "move", "direction": data[1], "value": 1},
            ],
            "next": data[2],
        }
        if data[2] != "!"
        else {
            "actions": [
                {"type": "write", "value": int(data[0])},
                {"type": "move", "direction": data[1], "value": 1},
                {"type": "halt", "code": 0},
            ],
            "next": None,
        }
    )


def decode_simple(data):
    all = [line.strip() for line in data.split("\n")]
    instrs = [instr for instr in all if instr[0] != "@"]
    params = [param for param in all if param[0] == "@"]
    return {
        "parameters": lib.utils.combine_objects(
            [decode_param_simple(param) for param in params]
        ),
        "instructions": lib.utils.combine_objects(
            [decode_instr_simple(instr) for instr in instrs]
        ),
    }


def decode_file(path):
    with open(path, "r") as f:
        return decode_simple(f.read())
