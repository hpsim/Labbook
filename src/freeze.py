#!/usr/bin/env python3


def freeze(arguments, config, logger):
    logger.info("Freezing the current state")

    msg = arguments["message"]

    file_logger.write(action="init_labbook", msg=msg)

    # FIXME find a pygit way to do it
    check_output(["git", "add", "."])

    # FIXME find a pygit way to do it
    check_output(["git", "commit", "-m", msg])
