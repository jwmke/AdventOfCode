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
    d = defaultdict(list)
    for i, l in enumerate(stripped):
        ll = l.split(" ")
        for o in ll[1:]:
            d[ll[0][:3]].append(o)
    
    @functools.cache
    def search(cn, ds, fs):
        tt = 0
        
        for n in d[cn]:
            if n == 'out' and fs == True and ds == True:
                return 1
            
            tt += search(n, cn == 'dac' or ds, cn == 'fft' or fs)
        
        return tt

    return search('svr', False, False)

if __name__ == '__main__':
    print(solve())