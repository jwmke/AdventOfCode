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
    lvpc = []
    for i, l in enumerate(stripped):
        ns = l.split()
        for j, n in enumerate(ns):
            if i == 0:
                lvpc.append(len(n))
            else:
                if len(n) > lvpc[j]:
                    lvpc[j] = len(n)
    
    nl = []
    for i, l in enumerate(stripped):
        cnl = []
        cp = 0
        for li in lvpc:
            cnl.append(l[cp:li+cp])
            cp+= li+1
        nl.append(cnl)

    ol = nl[len(nl)-1]
    nl = nl[:-1]

    tnl = [list(row) for row in zip(*nl)]

    for i, snl in enumerate(tnl):
        fa = []
        for k in range(len(snl[0])):
            cma = []
            for j in range(len(snl)):
                if cma != ' ':
                    cma.append(snl[j][k])
            fa.append(int(''.join(cma)))
        if ol[i][0] == "+":
            ma = 0
            for n in fa:
                ma+=n
            t+=ma
        else:
            ma = 1
            for n in fa:
                ma*=n
            t+=ma

    # for i in range(len(ol)):
    #     cl = []
    #     for l in nl:
    #         cl.append(l[i])
    #     ncl = []
    #     for l in cl:
    #         nsl = []
    #         if ol[i] == '+':
    #             for j in range(4):
    #                 if j < len(l):
    #                     nsl.append(l[j])
    #                 else:
    #                     nsl.append('0')
    #             ncl.append(''.join(nsl))
    #         else:
    #             ncl.append(l.zfill(4))
            
    #     print(ncl)
    #     if ol[i] == '+':
    #         ma = 0
    #         for k in range(4):
    #             cma = []
    #             for j in range(len(ncl)):
    #                 cma.append(ncl[j][k])
    #             ncma = []
    #             fn = False
    #             for e in reversed(cma):
    #                 if e != '0':
    #                     fn = True
    #                     ncma.append(e)
    #                     continue
    #                 if e == '0' and fn == False:
    #                     continue
    #                 ncma.append(e)

    #             if len(ncma) == 0:
    #                 print(cma)
    #             else:
    #                 ma+=int(''.join(reversed(ncma)))
    #         print(ma)
    #         t+=ma
    #     else:
    #         ma = 1
    #         for k in range(4):
    #             cma = []
    #             for j in range(len(ncl)):
    #                 cma.append(ncl[j][k])
    #             ncma = []
    #             fn = False
    #             for e in reversed(cma):
    #                 if e != '0':
    #                     fn = True
    #                     ncma.append(e)
    #                     continue
    #                 if e == '0' and fn == False:
    #                     continue
    #                 ncma.append(e)

    #             # print(list(reversed(ncma)))
    #             # print(cma)
    #             if len(ncma) == 0:
    #                 print(cma)
    #                 # pass
    #             else:
    #                 ma*=int(''.join(reversed(ncma)))
    #         print(ma)
    #         t+=ma

    return t

if __name__ == '__main__':
    print(solve())