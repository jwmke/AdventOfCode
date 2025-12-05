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
    rlf = True
    il = []
    for i, l in enumerate(stripped):
        if l == "":
            rlf = False
            continue
        if rlf == True:
            a = l.split("-")
            rl.append((int(a[0]), int(a[1])))
        else:
            il.append(int(l))
    
    for i in il:
        for r in rl:
            lb, hb = r
            if i >= lb and i <= hb:
                t+=1
                break

    return t

if __name__ == '__main__':
    print(solve())