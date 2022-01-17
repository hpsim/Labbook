#!/usr/bin/env python3

from labbook_core import execute


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

        execute(steps, path, {}, logger)
