#!/usr/bin/env python3


def main(param):
    if param.endswith(".sh"):
        return 1
    else:
        return 0


