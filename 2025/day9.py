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

    mx, my = 0, 0

    for p in ps:
        if p[0] > mx:
            mx = p[0]
        if p[1] > my:
            my = p[1]
    
    mx, my = mx+2, my+2

    g = []

    for _ in range(my):
        g.append(['.']*mx)
    
    pp = ps[0]
    for i, p in enumerate(ps):
        g[p[1]][p[0]] = "A"
        if i == 0:
            continue
        
        if pp[0] == p[0]:
            for y in range(abs(p[1]-pp[1])):
                g[min(p[1], pp[1])+y+1][p[0]] = "A"
        elif pp[1] == p[1]:
            for x in range(abs(p[0]-pp[0])):
                g[p[1]][min(p[0], pp[0])+x+1] = "A"
        
        pp = p

    if pp[0] == ps[0][0]:
        for y in range(abs(ps[0][1]-pp[1])):
            g[min(ps[0][1], pp[1])+y+1][ps[0][0]] = "A"
    elif pp[1] == ps[0][1]:
        for x in range(abs(ps[0][0]-pp[0])):
            g[ps[0][1]][min(ps[0][0], pp[0])+x+1] = "A"

    print('A')

    def flood_fill(grid, r, c):
        rows = len(grid)
        cols = len(grid[0])

        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if grid[r][c] != '.':
            return
        if grid[r][c] == 'X':
            return

        grid[r][c] = 'X'

        flood_fill(grid, r + 1, c)
        flood_fill(grid, r - 1, c)
        flood_fill(grid, r, c + 1)
        flood_fill(grid, r, c - 1)

    flood_fill(g, 0, 0)

    print('B')

    for ri, r in enumerate(g):
        for ci, c in enumerate(r):
            if c == '.':
                g[ri][ci] = 'A'

    print('C')

    ld = 0
    for p1 in ps:
        for p2 in ps:
            if p1 == p2:
                continue
            cd = (abs(p1[0] - p2[0])+1) * (abs(p1[1] - p2[1])+1)
            if cd > ld:
                sr, er = min(p1[0], p2[0]), max(p1[0], p2[0])
                sc, ec = min(p1[1], p2[1]), max(p1[1], p2[1])

                cf = True
                for r in range(sr, er + 1):
                    if cf == False:
                        break
                    for c in range(sc, ec + 1):
                        if g[c][r] != 'A':
                            cf = False
                            break
                if cf == True:
                    ld = cd 

    return ld

if __name__ == '__main__':
    print(solve())