import math
import sys
import copy
from collections import defaultdict
import functools

def solve() -> int:
    sys.setrecursionlimit(200000)
    file = open('input.txt', 'r')
    read = file.readlines()
    stripped = list(map(lambda s : s.replace("\n", ""), read))
    t = 0
    nl = []
    for i, l in enumerate(stripped):
        nl.append(l.split())
    ol = nl[len(nl)-1]
    nl = nl[:-1]

    for i in range(len(ol)):
        at = 0
        mt = 1
        for l in nl:
            if ol[i] == "+":
                at += int(l[i])
            else:
                mt *= int(l[i])
        if ol[i] == "+":
            t+= at
        else:
            t+=mt

    return t

if __name__ == '__main__':
    print(solve())