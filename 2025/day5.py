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
    rl = []
    for i, l in enumerate(stripped):
        if l == "":
            break
        a = l.split("-")
        rl.append((int(a[0]), int(a[1])))
    
    mi, ma = math.inf, 0
    for low, hi in rl:
        if low < mi:
            mi = low
        if hi > ma:
            ma = hi
    
    srl = sorted(rl)
    fil = []

    pl, ph = 0, 0
    for i, lh in enumerate(srl):
        cl, ch = lh
        if i == 0:
            pl, ph = cl, ch
            continue
        
        if cl >= ph+1:
            fil.append((pl, ph))
            pl, ph = cl, ch
        elif cl <= ph:
            ph = max(ph,ch)

    fil.append((pl, ph))
    
    for i in fil:
        t+= i[1]-i[0]+1

    return t

if __name__ == '__main__':
    print(solve())