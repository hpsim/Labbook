#!/usr/bin/env python3
import logging
from shutil import copyfile
import pathlib
import os

class Template():

    def __init__(self, kind):
        self.kind_ = kind

    def kind(self):
        return self.kind_

class OpenFOAM(Template):

    def __init__(self, logger):
        super().__init__(
            kind="OpenFOAM",
        )
        self.logger = logger
        self.logger.debug("Creating an OpenFOAM project")

    def copy_gitignore(self, target):
        folder = pathlib.Path(__file__).parent.resolve()
        copyfile(
            folder / "Templates" / "OpenFOAM" / "gitignore",
            pathlib.Path(os.getcwd()) / ".gitignore" )
        self.logger.debug("copying gitignore")

    def copy_readme(self, target):
        folder = pathlib.Path(__file__).parent.resolve()
        copyfile(
            folder / "Templates" / "OpenFOAM" / "Readme.org",
            pathlib.Path(os.getcwd()) / "Readme.org" )
        self.logger.debug("copying Readme.org")
