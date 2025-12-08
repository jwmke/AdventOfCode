import math
import sys
import copy
from collections import defaultdict
import functools
import itertools
import networkx as nx



def solve() -> int:
    sys.setrecursionlimit(200000)
    file = open('input.txt', 'r')
    read = file.readlines()
    stripped = list(map(lambda s : s.replace("\n", ""), read))
    t = 0
    xyz = []
    for i, l in enumerate(stripped):
        a = l.split(",")
        xyz.append((int(a[0]), int(a[1]), int(a[2])))

    cl = itertools.combinations(xyz, 2)
    def find_dist(p):
        p1, p2 = p
        return math.dist(p1, p2)
    
    cl = list(cl)
    
    cl.sort(key=find_dist)

    G = nx.Graph()
    for n in cl:
        G.add_edge(n[0], n[1])
        if len(xyz) == len(sorted(nx.connected_components(G), key=len, reverse=True)[0]):
            return (n[0][0]*n[1][0])

    # BAD - IGNORE
    # fp = []
    # nms = []
    # for _ in range(10):
    #     mp = ()
    #     md = math.inf
    #     for i1, p1 in enumerate(xyz):
    #         for i2, p2 in enumerate(xyz):
    #             if i1 == i2:
    #                 continue
    #             cp = sorted((p1, p2))
    #             cd = math.dist(p1, p2)
    #             if cd < md and cp not in fp:
    #                 mp = cp
    #                 md = cd
    #     fp.append(mp)
    #     print(mp)
    #     af = False
    #     for ns in nms:
    #         if mp[0] in ns or mp[1] in ns:
    #             af = True
    #             ns.add(mp[0])
    #             ns.add(mp[1])
    #     if af == False:
    #         nms.append(set([mp[0], mp[1]]))
    # for ns in nms:
    #     print(ns)
    # fns = []
    # for i1, ns in enumerate(nms):
    #     us = False
    #     for p in ns:
    #         for i2, ns2 in enumerate(nms):
    #             if i1 == i2:
    #                 continue
    #             if p in ns2:
    #                 us = True
    #                 fns.append(ns.union(ns2))
    #     if us == False:
    #         fns.append(ns)
    # print(fns)
    # cdd[str(mp[0])].add(mp[1])
    # cdd[str(mp[1])].add(mp[0])
    # for k in cdd.values():
    #     print(len(k))
    # return t

if __name__ == '__main__':

    print(solve())