# py-yamler

A utility for making arbitrary modifications to YAML while preserving comments.

## Setup

With Python 2 or 3 and Pip installed, run `pip install -r requirements.txt`. Alternatively, just build the Docker image with `make` if you don't want to install Python.

## Usage

```
usage: yamler.py [-h] [--source SOURCE] [--path PATH [PATH ...]] --value VALUE

optional arguments:
  -h, --help            show this help message and exit
  --source SOURCE       The yaml source; either a filename or '-' for STDIN
  --path PATH [PATH ...]
                        The keys/indices to traverse to reach the value which
                        must be updated
  --value VALUE         The value to be set at the given key
```

Note that `path` should always start with a number corresponding to the list index of the yaml document you wish to modify. In the case of inputs specifying only a single document, this will be zero.

## Examples

### Editing a file containing a single document

```
$ cat single.yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: foo
spec:
  template:
    metadata:
      labels:
        name: foo
    spec:
      containers:
      - name: foo
        image: foo:foo

$ python yamler.py --source single.yaml --value true --path 0 metadata annotations flux.weave.works/automated
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: foo
  annotations:
    flux.weave.works/automated: 'true'
spec:
  template:
    metadata:
      labels:
        name: foo
    spec:
      containers:
      - name: foo
        image: foo:foo
```

### Editing a file containing multiple documents

```
$ cat multi.yaml
---
foo: 123
bar: 234
---
baz: 345

$ python yamler.py --source multi.yaml --value hello --path 1 baz
foo: 123
bar: 234
---
baz: hello
```
