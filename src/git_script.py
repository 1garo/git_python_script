#!/usr/bin/env python

import subprocess
import sys, os


def main():
    commit_hash = get_last_commit_hash()
    msg = os.system("git diff-tree --no-commit-id --name-only -r " + str(commit_hash))
    print(msg)


def get_last_commit_hash():
    """Get the hash of the last commited commit"""
    return os.system("git log -n 1 HEAD --pretty=format:\"%H\"")


if __name__ == '__main__':
    main()
