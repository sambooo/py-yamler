# py-yamler

A utility for making arbitrary modifications to YAML while preserving comments.

Note: the `copy` operation isn't currently supported, but only because I don't need it myself.

## Setup

With Python 3.7 installed, run `make local`. Alternatively, run `make image` to build with Docker and replace `python yamler.py` with `docker run samb1729/yamler` in the examples below.

## Usage

```
usage: yamler.py [-h] [--source SOURCE] [--patch PATCH]

optional arguments:
  -h, --help       show this help message and exit
  --source SOURCE  The yaml source; either a filename or '-' for STDIN
  --patch PATCH    JSON Patch to apply to the input
```

Note that JSON Pointers must start with an integer part. In the case of inputs specifying only a single document, this will be zero.

## Example

```
$ cat <<EOF | pipenv run python yamler.py --patch='[{"op":"add", "path":"/0/metadata/hello", "value":"there"}]'
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: foo
  hello: there
spec:
  template:
    metadata:
      labels:
        name: foo
    spec:
      containers:
      - name: bar
        image: baz
EOF
```
