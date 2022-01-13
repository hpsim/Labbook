#!/usr/bin/env python3

from subprocess import check_output
import labbook_log


def update(arguments, config, logger):
    file_logger = labbook_log.LogFile()

    logger.info("Updating dependencies")
    check_output(["git", "submodule", "update", "--recursive", "--remote"])
    file_logger.write(action="update_depencies", msg="updated")
