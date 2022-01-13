#!/usr/bin/env python3

import json
import os
import datetime
import labbook_core
from pygit2 import Repository


class LogFile:
    def write(self, action, msg):
        if not os.path.exists(".labbook"):
            os.mkdir(".archive")

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

        with open(fn, "rw") as fh:
            if exists:
                history = json.load(fh)
                history.append(dct)
                json.dump(history, fh)
            else:
                json.dump([dct], fh)
