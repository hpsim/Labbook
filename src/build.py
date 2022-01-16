#!/usr/bin/env python3

import subprocess
import labbook_log
from core import execute


def build_submodule(logger, submodule):
    raw_build_command = submodule["build"]
    path = "Dependencies/" + submodule["name"]
    steps = raw_build_command.split("\n")
    file_logger = labbook_log.LogFile()
    success = execute(steps, path, {})
    if sucess:
        file_logger.write(action="build_submodule", msg="build" + submodule["name"])


def labbook_build(arguments, config, logger):
    for submodule in config.get("submodules", []):
        if submodule.get("build", False):
            build_submodule(logger, submodule)
