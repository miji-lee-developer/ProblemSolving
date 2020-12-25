#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    v = sum(1 for i in range(len(contests)) if contests[i][1] == 1)

    if k >= v:
        return sum(contests[i][0] for i in range(len(contests)))
    else:
        c = 0
        min_v = 0
        sv = sum(1 for i in range(len(contests)) if contests[i][1] == 1) - k
        contests = sorted(contests)

        for i in range(len(contests)):
            if c == sv:
                break

            if contests[i][1] == 1:
                min_v += contests[i][0]
                c += 1

        return sum(contests[i][0] for i in range(len(contests))) - (min_v * 2)

if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    print(str(result) + '\n')
