#!/usr/bin/env python3


def rebase(base, config, revision):
    # make a temporary copy of the current (dirty) base
    # cp -r base base.bck

    # revert state of base
    # git checkout base

    # create a revion folder in the archive
    # mkdir .archive/{revision}
    #
    # move old state to archive
    # mv base {dependent cases} .archive/revision

    # mv base.bck base
    # git add base .archive/revision

    # execute actions with rebase tag
    # execute(config,tag="rebase")

    # get hash of new base folder
    # revision = get_hash(base)
    # git_commit(action=update base case, revision=revision)
