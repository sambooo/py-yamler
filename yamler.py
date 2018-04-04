import sys
from pathlib import Path
from ruamel.yaml import YAML
from ruamel.yaml.compat import StringIO

def load_stream(path):
    y = YAML()
    if path == "-":
        stream = sys.stdin
    else:
        stream = Path(path)
    docs = y.load_all(stream)
    return list(docs)

def dump_to_string(docs):
    y = YAML()
    s = StringIO()
    y.dump_all(docs, s)
    return s.getvalue()

def get_path(obj, *args):
    if len(args) == 0:
        return obj
    head, tail = args[0], args[1:]
    return get_path(obj[try_coerce(head)], *tail)

def try_coerce(val):
    try:
        return int(val)
    except ValueError:
        return val
