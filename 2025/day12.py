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
    sc = 0
    al = []
    nl = []
    for i, l in enumerate(stripped):
        if l == "":
            sc +=1
            continue
        if sc == 6:
            ll = l.split()
            tl = ll[0].split("x")
            al.append((int(tl[0]), int(tl[1][:-1])))
            tn = 0
            for n in ll[1:]:
                tn += int(n)
            nl.append(tn)

    for i, a in enumerate(al):
        if (a[0]/3)*(a[1]/3) >= nl[i]:
            t+=1

    return t

if __name__ == '__main__':
    print(solve())