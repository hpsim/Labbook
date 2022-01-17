#!/usr/bin/env python3

import re
import os


def validate_env(arguments, _, logger):
    config_file = "labbook.yml"

    with open(config_file, "r") as config_handle:
        config = config_handle.read()

    ocurrances = set(re.findall(r"\${{env" + "\.(\w+)}}", config))

    for env in ocurrances:
        if not os.getenv(env):
            print(env + " is not set")
        else:
            print(env + " is set to " + os.environ.get(env))
