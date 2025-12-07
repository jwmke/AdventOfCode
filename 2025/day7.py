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
    g = []
    ix = 0
    for i, l in enumerate(stripped):
        g.append(l)
        if i == 0:
            for x in range(len(l)):
                if l[x] == "S":
                    ix = x

    @functools.cache
    def timeline(y, x, t):
        if y == len(g):
            return 1
        if g[y][x] == "^":
            l = timeline(y, x-1, t+1)
            r = timeline(y, x+1, t+1)
            return l + r
        else:
            return timeline(y+1, x, t)
        

    return timeline(1, ix, 0)

if __name__ == '__main__':
    print(solve())