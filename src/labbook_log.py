#!/usr/bin/env python3

import json
import os
import datetime
import labbook_core
from pygit2 import Repository


class LogFile:
    def write(self, action, msg):
        if not os.path.exists(".labbook"):
            os.mkdir(".labbook")

        host_name = os.uname().nodename
        branch = Repository(".").head.shorthand
        fn = ".labbook/history_" + host_name + "_" + branch
        exists = os.path.isfile(fn)

        revision = labbook_core.get_revision()
        dct = {
            "action": action,
            "msg": msg,
            "revision": revision,
            "timestamp": datetime.datetime.now().isoformat(),
            "host": host_name,
            "branch": branch,
        }

        if not os.path.isfile(fn):
            with open(fn, mode="w") as f:
                f.write(json.dumps([dct], indent=2))
        else:
            with open(fn) as feedsjson:
                feeds = json.load(feedsjson)

            feeds.append(dct)
            with open(fn, mode="w") as f:
                f.write(json.dumps(feeds, indent=2))


def show(arguments):
    pass
