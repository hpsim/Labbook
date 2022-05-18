#!/usr/bin/env python3

from labbook_core import execute


def build_submodule(logger, submodule):
    raw_build_command = submodule["run"]
    path = "Dependencies/" + submodule["name"]
    steps = raw_build_command.split("\n")
    success = execute(steps, path, {}, logger)


def labbook_build(arguments, config, logger):
    for submodule in config.get("submodules", []):
        if submodule.get("run", False):
            select = arguments.get("select")
            if select:
                if select not in submodule.get("name"):
                    continue
            build_submodule(logger, submodule)
