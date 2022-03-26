#!/usr/bin/env python3

import os
import templates
import log as log
import pathlib

from subprocess import check_output
import pygit2


class MyRemoteCallbacks(pygit2.RemoteCallbacks):
    def credentials(self, url, username_from_url, allowed_types):
        if allowed_types & pygit2.credentials.GIT_CREDENTIAL_USERNAME:
            print("foo")
            self.credential_tuple = "foo"
            return pygit2.Username("git")
        elif allowed_types & pygit2.credentials.GIT_CREDENTIAL_SSH_KEY:
            print("bar")
            ret = pygit2.Keypair(
                "git", "/Users/go/.ssh/id_rsa.pub", "/Users/go/.ssh/id_rsa", ""
            )
            self.credential_tuple = ret
            return ret
        else:
            print("baz")
            return None


def init_clean_labbook(arguments, config, logger, kind):
    """Init a clean labbook"""
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

    base_case = config["config"]["case"]["name"]
    if os.path.exists(base_case):
        index.add(base_case)
        index.write()

    tree = index.write_tree()

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


def init_labbook(arguments, config, logger):
    """init a new project labbook"""
    template = getattr(templates, arguments["--template"])(logger)
    kind = template.kind()

    if not os.path.exists(".git"):
        init_clean_labbook(arguments, config, logger, kind)
    else:
        logger.info("Initialising existing {} labbook project".format(kind))

    # log.Message("Adding base case to repository")
    # for root, dirs, files in os.walk(os.getcwd()):
    #     index.add(files)
