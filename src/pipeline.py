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

        if pipeline.get("results"):
            revision = labbook_core.get_revision().keys[0][0:8]
            print(revision)
            if not os.path.exists("results"):
                os.mkdir("results")
            if not os.path.exists("results/" + revision):
                os.mkdir("results/" + revision)
