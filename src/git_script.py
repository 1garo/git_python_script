#!/usr/bin/env python


# hash do commit antigo a410a66cd4da793803c707d3beb3cee41e30ea8c...


import os
import subprocess
import sys
from os import path

from subprocess import Popen, PIPE
hash_value = []


def create():
    commit_hash = get_last_commit_hash()
    msg = """
    git show --pretty=\"format:\" --name-only {commit_hash}\""
    """.format(commit_hash=commit_hash)
    sys_msg = os.system(msg)
    # commit_commands = [msg, "status"]
    # pwd = os.system("pwd")

    return sys_msg


def get_last_commit_hash():
    """Get the hash of the last commited commit"""
    msg = os.popen("git log -n 1 master --pretty=format:\"%H\"").read()

    return msg


if __name__ == '__main__':
    create()
