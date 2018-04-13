import sys
import argparse
from pathlib import Path
from ruamel.yaml import YAML
from ruamel.yaml.compat import StringIO

y = YAML()
y.explicit_start = True
y.preserve_quotes = True

def main():
    args = parse_args()
    docs = load_stream(args.source)
    set_path(docs, args.value, *args.path)
    y.dump_all(docs, sys.stdout)

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--source", default="-", help="The yaml source; either a filename or '-' for STDIN")
    p.add_argument("--path", default=[], nargs="+", help="The keys/indices to traverse to reach the value which must be updated")
    p.add_argument("--value", required=True, help="The value to be set at the given key")
    return p.parse_args()

def load_stream(path):
    if path == "-":
        stream = sys.stdin
    else:
        stream = Path(path)
    docs = y.load_all(stream)
    return list(docs)

def set_path(obj, val, *path):
    if len(path) == 0:
        # Either no path was given, or we somehow traversed too far.
        # Regardless, assigning directly to `obj` is a no-op so do nothing.
        return
    if len(path) == 1:
        obj[path[0]] = val
        return
    head, tail = path[0], path[1:]
    next_obj = get_and_ensure(obj, head)
    set_path(next_obj, val, *tail)

def get_and_ensure(obj, key):
    # In the case that the existing yaml doesn't contain the intermediate keys
    # that our change depends on, populate each such key with an empty map.
    key = try_coerce(key)
    try:
        return obj[key]
    except KeyError:
        obj[key] = dict()
        return obj[key]

def try_coerce(val):
    # For the purposes of indexing lists, attempt to coerce all keys to
    # integers. In the case that we're indexing a map, both string and int
    # will work, so no special case is required.
    try:
        return int(val)
    except ValueError:
        return val

def dump_to_string(docs):
    # This exists solely to make life easier when running in a REPL.
    s = StringIO()
    y.dump_all(docs, s)
    return s.getvalue()

if __name__ == "__main__":
    main()
