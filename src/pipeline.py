#!/usr/bin/env python3

import labbook_core


def execute(arguments, config, logger):
    """init a new project labbook"""
    pipeline_name = arguments["pipeline"]
    case = arguments["case"]
    pipelines = config["pipelines"]

    for pipeline in pipelines:
        if not pipeline["name"] == pipeline_name:
            continue

        raw_build_command = pipeline["run"]
        path = case
        steps = raw_build_command.split("\n")

        labbook_core.execute(steps, path, {}, logger)
