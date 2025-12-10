import math
import sys
import copy
from collections import defaultdict
import functools
from z3 import *

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
        bs = buttons[si]
        js = [int(x) for x in jolts[si]]
    
        vs = [Int(f'x{i}') for i in range(len(bs))]
        
        o = Optimize()

        for v in vs:
            o.add(v >= 0)

        for i in range(len(js)):
            co = []
            
            for bi in range(len(bs)):
                if str(i) in bs[bi]:
                    co.append(vs[bi])
            
            o.add(Sum(co) == js[i])
        
        o.minimize(Sum(vs))

        if o.check() == sat:
            model = o.model()
            t += sum([model[v].as_long() for v in vs])

        # f = False
        # for i in range(1, len(bs)+1):
        #     if f == True:
        #         break
        #     cc = combinations(bs, i)
        #     for c in cc:
        #         cs = ['.']*len(es)
        #         for b in c:
        #             for bp in b:
        #                 if cs[int(bp)] == '.':
        #                     cs[int(bp)] = '#'
        #                 elif cs[int(bp)] == '#':
        #                     cs[int(bp)] = '.'
        #         if es == cs:
        #             t+=len(c)
        #             f = True
        #             break

    return t

if __name__ == '__main__':
    print(solve())