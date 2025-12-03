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
    for _, l in enumerate(stripped):
        fil = []
        ll = list(l)
        for i in range(12, 0, -1):
            cl = ll[:((-i)+1)]
            if i == 1:
                cl = ll
            mv = max(cl)
            ll = ll[cl.index(mv)+1:]
            fil.append(mv)
        t+= int(''.join(fil))

    return t

if __name__ == '__main__':
    print(solve())