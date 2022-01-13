#!/usr/bin/env python3

from subprocess import check_output
import hashlib
import pygit2


def get_revision():
    submodule_hashes = (
        check_output(["git", "submodule", "status"]).decode("utf8").split("\n")
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
