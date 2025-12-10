import math
import sys
import copy
from collections import defaultdict
import functools
from itertools import combinations

def solve() -> int:
    sys.setrecursionlimit(200000)
    file = open('input.txt', 'r')
    read = file.readlines()
    stripped = list(map(lambda s : s.replace("\n", ""), read))
    t = 0
    jolts = []
    end_states = []
    buttons = []
    for i, l in enumerate(stripped):
        ll = l.split()
        cb = []
        for b in ll[1:-1]:
            cb.append(b[1:-1].split(","))
        buttons.append(cb)
        end_states.append(ll[0][1:-1])
        jolts.append(ll[-1][1:-1].split(","))

    for si in range(len(end_states)):
        es = list(end_states[si])
        bs = buttons[si]
        f = False
        for i in range(1, len(bs)+1):
            if f == True:
                break
            cc = combinations(bs, i)
            for c in cc:
                cs = ['.']*len(es)
                for b in c:
                    for bp in b:
                        if cs[int(bp)] == '.':
                            cs[int(bp)] = '#'
                        elif cs[int(bp)] == '#':
                            cs[int(bp)] = '.'
                if es == cs:
                    t+=len(c)
                    f = True
                    break

    return t

if __name__ == '__main__':
    print(solve())