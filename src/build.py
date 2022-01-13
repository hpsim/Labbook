#!/usr/bin/env python3

import os
import re
from subprocess import check_output
import labbook_log


def build_submodule(logger, submodule):
    raw_build_command = submodule["build"]
    path = "Dependencies/" + submodule["name"]
    steps = raw_build_command.split("\n")
    file_logger = labbook_log.LogFile()

    for step in steps:
        env_variables = re.findall(r"\${{env\.(\w+)}}", step)
        for env_var in env_variables:
            step = step.replace("${{env." + env_var + "}}", os.environ.get(env_var, ""))
        logger.info("Execute: " + step)
        print(check_output(step.split(" "), cwd=path))
    file_logger.write(action="build_submodule", msg=submodule["name"])


def labbook_build(arguments, config, logger):
    for submodule in config.get("submodules", []):
        if submodule.get("build", False):
            build_submodule(logger, submodule)
