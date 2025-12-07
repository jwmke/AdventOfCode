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
    g = []
    dl = set()
    for i, l in enumerate(stripped):
        g.append(l)
        if i == 0:
            for x in range(len(l)):
                if l[x] == "S":
                    dl.add(x)
    for y in range(len(g)):
        if y == 0:
            continue
        for x, c in enumerate(g[y]):
            if x in dl and c == "^":
                t+=1
                dl.add(x-1)
                dl.add(x+1)
                dl.remove(x)

    return t

if __name__ == '__main__':
    print(solve())