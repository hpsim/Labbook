#!/usr/bin/env python3

from labbook_core import execute


def execute(arguments, config, logger):
    """init a new project labbook"""
    pipeline = arguments["pipeline"]
    case = arguments["case"]

    raw_build_command = config[pipeline]["run"]
    path = case
    steps = raw_build_command.split("\n")

    execute(steps, path, {}, logger)
