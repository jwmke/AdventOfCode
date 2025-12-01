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
    current_pos = 50
    inst = []
    zero_count = 0
    for i, l in enumerate(stripped):
        inst.append((l[0], int(l[1:])))

    for lr, amount in inst:
        if lr == "L":
            for _ in range(amount):
                current_pos -= 1
                current_pos = current_pos % 100
                if current_pos == 0:
                    zero_count += 1
        elif lr == "R":
            for _ in range(amount):
                current_pos += 1
                current_pos = current_pos % 100
                if current_pos == 0:
                    zero_count += 1

    return zero_count

if __name__ == '__main__':
    print(solve())