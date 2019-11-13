#!/usr/bin/env python3

# chmod +x ~/Documents/git_python_script/src/git_script.py
# echo "Printing the folders that was changed by the last commit\n"
# ./git_script.py

# Read the README.md file for more details on how the script is working...
import os


def create():
    """Get the hash of the last commited commit"""
    message = os.popen("git log -n 1 master --pretty=format:\"%H\"").read()

    commit_hash = message
    msg = """
    git show --pretty=\"format:\" --name-only {commit_hash}\""
    """.format(commit_hash=commit_hash)
    sys_msg = os.system(msg)
    return sys_msg


if __name__ == '__main__':
    create()

