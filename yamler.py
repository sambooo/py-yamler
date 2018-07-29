import argparse
import sys
from jsonpatch import JsonPatch
from pathlib import Path
from ruamel.yaml import YAML

def main():
    args = parse_args()
    docs = load_stream(args.source)
    args.patch.apply(docs, in_place=True)
    dump_stream(docs)

def parse_args():
    def patch(string):
        return JsonPatch.from_string(string)

    p = argparse.ArgumentParser()
    p.add_argument("--source", default="-", help="The yaml source; either a filename or '-' for STDIN")
    p.add_argument("--patch", default="[]", help="JSON Patch to apply to the input", type=patch)
    return p.parse_args()

y = YAML()
y.explicit_start = True
y.preserve_quotes = True

def load_stream(path):
    if path == "-":
        stream = sys.stdin
    else:
        stream = Path(path)
    docs = y.load_all(stream)
    return list(docs)

def dump_stream(obj, path=None):
    if path == None:
        stream = sys.stdout
    else:
        stream = Path(path)
    y.dump_all(obj, stream)

if __name__ == "__main__":
    main()
