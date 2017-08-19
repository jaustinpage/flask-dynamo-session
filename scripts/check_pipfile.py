#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from pipfile import api as pipfileapi

def main():
    pipfile = pipfileapi.load()

    pipfile_lock_path = "{}.lock".format(pipfile.filename)

    with open(pipfile_lock_path) as pipfile_lock_file:
        pipfile_lock = json.load(pipfile_lock_file)

    if pipfile.hash == pipfile_lock['_meta']['hash']['sha256']:
        exit(0)
    exit(1)

if __name__ == "__main__":
    main()
