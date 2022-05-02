#!/usr/bin/env python3

import re
import os

import labbook_core


def validate_env(arguments, _, logger):
    config_file = "labbook.yml"

    with open(config_file, "r") as config_handle:
        config = config_handle.read()

    ocurrances = set(re.findall(r"\${{env" + "\.(\w+)}}", config))

    print("revision", list(labbook_core.get_revision().keys())[0][0:8])

    for env in ocurrances:
        if not os.getenv(env):
            print(env + " is not set")
        else:
            print(env + " is set to " + os.environ.get(env))
