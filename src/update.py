#!/usr/bin/env python3

from subprocess import check_output


def update(arguments, config, logger):
    logger.info("Updating dependencies")
    check_output(["git", "submodule", "init"])
    check_output(["git", "submodule", "update"])
    file_logger.write(action="update_depencies", msg="updated")
