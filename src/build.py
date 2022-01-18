#!/usr/bin/env python3

import subprocess
from labbook_core import execute


def build_submodule(logger, submodule):
    raw_build_command = submodule["run"]
    path = "Dependencies/" + submodule["name"]
    steps = raw_build_command.split("\n")
    success = execute(steps, path, {}, logger)


def labbook_build(arguments, config, logger):
    for submodule in config.get("submodules", []):
        if submodule.get("run", False):
            build_submodule(logger, submodule)
