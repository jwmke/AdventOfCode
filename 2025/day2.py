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
    tf = set()
    id_ranges = []
    for r in stripped[0].split(","):
        x, y = r.split("-")
        id_ranges.append((int(x), int(y)))
    
    for r1, r2 in id_ranges:
        for i in range(r1, r2+1):
            si = str(i)
            css = []
            cur_sub_strings = []
            for ix in range(len(si)//2):
                css.append(si[ix])
                cur_sub_strings.append(''.join(css))
            for ss in cur_sub_strings:
                if len(si)%len(ss)==0:
                    all_same = True
                    for ssi in range(0, len(si), len(ss)):
                        sss = si[ssi:ssi+len(ss)]
                        if sss != ss:
                            all_same = False
                            break
                    if all_same:
                        tf.add(i)

    return sum(tf)

if __name__ == '__main__':
    print(solve())