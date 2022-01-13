#!/usr/bin/env python3
import os
import re
import subprocess
from subprocess import check_output
import labbook_log


def create_cases(arguments, config, logger):
    # get build matrix
    # execute case recipe
    file_logger = labbook_log.LogFile()
    case = arguments.get("case", None)
    case_config = config.get("cases", {}).get(case, None)
    if not case or not case_config:
        return

    logger.info("creating case " + case)
    if not os.path.exists(case):
        os.mkdir(case)

    build_matrix = case_config.get("values", [])

    raw_build_command = case_config["build"]
    steps = raw_build_command.split("\n")
    if build_matrix:
        for build_params in build_matrix:
            for step in steps:
                # TODO merge with build_submodule
                values = re.findall(r"\${{values\.(\w+)}}", step)
                for value in values:
                    step = step.replace(
                        "${{values." + value + "}}", build_params.get(value, "")
                    )
            logger.info("Execute: " + step)
            try:
                ret = check_output(step.split(" "), cwd=path)
                print(ret.decode("utf-8"))

            except subprocess.CalledProcessError as e:
                print(e.output.decode("utf-8"))
        file_logger.write(action="create_case", msg=case)
