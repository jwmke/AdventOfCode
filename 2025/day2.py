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
    id_ranges = []
    for r in stripped[0].split(","):
        x, y = r.split("-")
        id_ranges.append((int(x), int(y)))
    
    for r1, r2 in id_ranges:
        for i in range(r1, r2+1):
            si = str(i)
            if len(si) % 2 == 0:
                if si[:len(si)//2] == si[len(si)//2:]:
                    t+=i
    
    

    return t

if __name__ == '__main__':
    print(solve())