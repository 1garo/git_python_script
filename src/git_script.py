#!/usr/bin/env python
# --*-- encoding: iso-8859-1 --*--

import subprocess
import sys, os

DELETED_FILE_TOKEN = "D\t"


def execute_cmd(full_cmd, cwd=None):
    """Execute a git command"""

    process = subprocess.Popen(full_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd)
    (stdoutdata, stderrdata) = process.communicate(None)
    if 0 != process.wait():
        raise Exception("Could not execute git command")

    return stdoutdata.strip(), stderrdata.strip()


def get_last_commit_hash():
    """Get the hash of the last commited commit"""
    return execute_cmd("git log -n 1 HEAD --pretty=format:\"%H\"")[0]


def get_commit_file_list(hash):
    """Get the list of files impacted by a commit, each file is preceded by
    x\t where x can be A for added, D for deleted, M for modified"""
    file_list = execute_cmd("git show --pretty=\"format:\" --name-status "+ hash)[0]
    return file_list.split("\n")


def get_hash():
    """Allow you to launch the script in command line with any hash"""
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return get_last_commit_hash()


hash_var = get_hash()
file_list = get_commit_file_list(hash_var)
