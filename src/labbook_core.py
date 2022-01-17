#!/usr/bin/env python3

import hashlib
import pygit2
import re
import os
import labbook_log
import subprocess


def parse_variables(in_str, args, domain):

    ocurrances = re.findall(r"\${{" + domain + "\.(\w+)}}", in_str)
    for inst in ocurrances:
        in_str = in_str.replace("${{" + domain + "." + inst + "}}", args.get(inst, ""))
    return in_str


def execute(steps, path, matrix, logger):
    file_logger = labbook_log.LogFile()
    for step in steps:
        if not step:
            continue
        step = parse_variables(step, os.environ, "env")
        step = parse_variables(step, {"cwd": path, "root": os.getcwd()}, "labbook")
        step = parse_variables(step, matrix, "matrix")
        logger.info("Execute: " + step)
        try:
            ret = subprocess.check_output(step.split(" "), cwd=path)
            print(ret.decode("utf-8"))
            file_logger.write(action="execute", msg=step)
        except subprocess.CalledProcessError as e:
            print(e.output.decode("utf-8"))
            return False
        return True


def get_revision():
    submodule_hashes = (
        subprocess.check_output(["git", "submodule", "status"])
        .decode("utf8")
        .split("\n")
    )

    submodule_hashes = [_.split() for _ in submodule_hashes if _]

    hashes = ""

    for commit, path, branch in submodule_hashes:
        hashes += commit

    revision = hashlib.sha1(hashes.encode("utf-8"))
    revision = {
        revision.hexdigest(): {path: commit for commit, path, _ in submodule_hashes}
    }
    print(revision)
    return revision
