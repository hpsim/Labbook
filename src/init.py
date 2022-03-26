#!/usr/bin/env python3

import os
import labbook_core
import templates
import pathlib
import labbook_log

from subprocess import check_output
import pygit2


class MyRemoteCallbacks(pygit2.RemoteCallbacks):
    def credentials(self, url, username_from_url, allowed_types):
        if allowed_types & pygit2.credentials.GIT_CREDENTIAL_USERNAME:
            return pygit2.Username("git")
        elif allowed_types & pygit2.credentials.GIT_CREDENTIAL_SSH_KEY:
            ret = pygit2.Keypair(
                "git", "/Users/go/.ssh/id_rsa.pub", "/Users/go/.ssh/id_rsa", ""
            )
            self.credential_tuple = ret
            return ret
        else:
            return None


def init_clean_labbook(arguments, config, logger, kind):
    cwd = pathlib.Path(os.getcwd())
    logger.info("Initialising new {} labbook project".format(kind))
    repo = pygit2.init_repository(os.getcwd())
    index = repo.index

    if not os.path.isfile(cwd / ".gitignore"):
        logger.info("Creating .gitignore file")
        template.copy_gitignore(cwd)
    index.add(".gitignore")
    index.write()

    if not os.path.isfile(cwd / "Readme.org"):
        logger.info("Creating Readme.org")
        template.copy_readme(cwd)
    index.add("Readme.org")
    index.write()

    if not os.path.exists(".labbook"):
        os.mkdir(".labbook")

    if not os.path.exists("Dependencies"):
        os.mkdir("Dependencies")

    for submodule in config.get("submodules", []):
        logger.info("Adding submodule " + submodule["name"])
        repo.add_submodule(
            path="Dependencies/" + submodule["name"],
            url=submodule["repo"],
            callbacks=MyRemoteCallbacks(),
        )

    if not os.path.exists("Results"):
        os.mkdir("Results")

    if not os.path.exists(".archive"):
        os.mkdir(".archive")

    base_case = config["config"]["case"]
    if os.path.exists(base_case["name"]):
        index.add(base_case["name"])
        index.write()
    elif base_case.get("type", None) == "submodule":
        repo.add_submodule(
            path=base_case["name"], url=base_case["repo"], callbacks=MyRemoteCallbacks()
        )
    elif base_case.get("type", None) == "path":
        logger.Error("Not implemented")

    tree = index.write_tree()
    # parent, ref = repo.resolve_refish(refish=repo.head.name)

    commit_message = """
[Labbook] Initial commit

{
"action"="initialise repo"
}
"""
    repo.create_commit(
        "refs/heads/main",
        repo.default_signature,
        repo.default_signature,
        commit_message,
        tree,
        [],
    )

    # FIXME find a pygit way to do it
    check_output(["git", "checkout", "main"])

    file_logger.write(action="init_labbook", msg="init clean labbook")


def init_labbook(arguments, config, logger):
    """init a new project labbook"""
    file_logger = labbook_log.LogFile()

    template = getattr(templates, arguments["template"])(logger)
    kind = template.kind()
    cwd = pathlib.Path(os.getcwd())

    if not os.path.exists(".git"):
        init_clean_labbook(arguments, config, logger, kind)
    else:
        logger.info("Initialising existing {} labbook project".format(kind))
        check_output(["git", "submodule", "init"])
        check_output(["git", "submodule", "update"])
        file_logger.write(action="init_labbook", msg="init existing labbook")
    # print(submodule_hashes.split("\n"))

    # for submodule in repo.listall_submodules():
    #     print(dir(repo.lookup_submodule(submodule).__hash__))
    #     print(repo.lookup_submodule(submodule).__hash__())
