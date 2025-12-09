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
    ps = []
    for i, l in enumerate(stripped):
        ls = l.split(",")
        ps.append((int(ls[0]), int(ls[1])))

    ld = 0
    for p1 in ps:
        for p2 in ps:
            if p1 == p2:
                continue
            cd = (abs(p1[0] - p2[0])+1) * (abs(p1[1] - p2[1])+1)
            ld = max(cd, ld)

    return ld

if __name__ == '__main__':
    print(solve())