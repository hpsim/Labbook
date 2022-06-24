#!/usr/bin/env python3

import os
import labbook_core
import subprocess


def get_campaign(config):
    submodule = config["config"]["submodule"]
    cmd = "git submodule foreach 'git branch --show-current'"
    ret = subprocess(cmd.split(" ")).decode("utf-8").split("\n")
    print(ret)
    for i in range(len(ret) / 2, 2):
        if submodule in ret[2 * i]:
            return ret[2 * i + 1]
    return False


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
        campaign = get_campaign(config)
        get_revision = config.get("revision", {}).get("submodule", None)
        results = pipeline.get("results")
        if results:
            revision = list(labbook_core.get_revision(get_revision).keys())[0][0:8]
            results_path = "results/" + campaign + "/" + revision + "/" + case
            os.makedirs(results_path, exist_ok=True)

            for results_folder in results:
                root, folder, files = next(os.walk(case + "/" + results_folder))
                for f in folder:
                    ret = subprocess.check_output(
                        ["cp", "-r", root + "/" + f, results_path]
                    )
                for f in files:
                    ret = subprocess.check_output(["cp", root + "/" + f, results_path])
