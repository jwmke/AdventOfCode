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
    for i, l in enumerate(stripped):
        g.append(list(l))
    
    h, w = len(g), len(g[0])
    cc = 1
    while cc != 0:
        cc = 0
        tg = copy.deepcopy(g)
        for y in range(len(g)):
            for x in range(len(g[0])):
                if g[y][x] == "@":
                    rc = 0
                    if y != 0 and g[y-1][x] == "@":
                        rc +=1
                    if y != 0 and x != 0 and g[y-1][x-1]== "@":
                        rc +=1
                    if y != 0 and x != w-1 and g[y-1][x+1]== "@": 
                        rc +=1
                    if x != 0 and g[y][x-1]== "@":
                        rc +=1
                    if x != w-1 and g[y][x+1]== "@": 
                        rc +=1
                    if y != h-1 and g[y+1][x]== "@": 
                        rc +=1
                    if y != h-1 and x != 0 and g[y+1][x-1]== "@":
                        rc +=1
                    if y != h-1 and x != w-1 and g[y+1][x+1]== "@": 
                        rc +=1
                    if rc < 4:
                        tg[y][x] = "."
                        cc += 1
                        t+=1
        g = tg
    return t

if __name__ == '__main__':
    print(solve())