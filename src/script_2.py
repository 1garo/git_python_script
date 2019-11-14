#!/usr/bin/env python3


def main(param):
    for i in range(len(param)):
        aux = param[i]
        name = aux.split("/", 1)[0]

        if name != "XXX":
            return 1
        else:
            return 0
