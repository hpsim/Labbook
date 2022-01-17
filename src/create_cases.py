#!/usr/bin/env python3
import os
import re
import subprocess
from subprocess import check_output
from labbook_core import execute


def create_cases(arguments, config, logger):
    # get build matrix
    # execute case recipe
    case = arguments.get("case", None)
    cases_configs = config.get("cases", [])
    if not case or not cases_configs:
        return

    for case_config in cases_configs:
        if not case_config["name"] == case:
            continue
        logger.info("creating case " + case)
        if not os.path.exists(case):
            os.mkdir(case)

        build_matrix = case_config.get("matrix", [])

        raw_build_command = case_config["run"]
        steps = raw_build_command.split("\n")
        path = case

        if build_matrix:
            for build_params in build_matrix:
                execute(steps, path, build_params, logger)
