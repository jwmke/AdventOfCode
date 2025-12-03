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
    for i, l in enumerate(stripped):
        m1, m2 = 0,0
        mi = 0,
        for ic, c in enumerate(l):
            if int(c) > m1:
                mi = ic
                m1 = int(c)
        if mi == len(l)-1:
            for ic, c in enumerate(l[:-1]):
                if int(c) > m2:
                    m2 = int(c)
            t += int(''.join([str(m2), str(m1)]))
        else:
            for ic, c in enumerate(l[mi+1:]):
                if int(c) > m2:
                    m2 = int(c)
            t += int(''.join([str(m1), str(m2)]))

    return t

if __name__ == '__main__':
    print(solve())