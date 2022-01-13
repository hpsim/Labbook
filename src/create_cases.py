#!/usr/bin/env python3
#

def create_cases(arguments, config, logger):
    # create case path
    # get build matrix
    # execute case recipe

    for case in config.get("cases", []):
        if submodule.get("build", False):
            build_submodule(logger, submodule)
