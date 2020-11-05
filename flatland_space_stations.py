#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    if n == len(c):
        return 0
    elif len(c) == 1 and (c[0] == 0 or c[0] == n - 1):
        return n - 1
    else:
        l = []
        c = sorted(c)
        is_f = False
        is_e = False
        d_f = 0
        d_e = 0

        if c[0] != 0:
            c.insert(0, 0)
            is_f = True
        if c[len(c) - 1] != n - 1:
            c.append(n - 1)
            is_e = True

        for i in range(1, len(c)):
            if i == 1:
                v = c[i] - c[0]
                if is_f:
                    d_f = v
                l.append(v)
            else:
                v = c[i] - c[i - 1]
                if is_e and i == len(c) - 1:
                    d_e = v
                l.append(v)

        m = max(l)
        dm = m // 2
        if dm <= d_f or dm <= d_e:
            return d_f if d_f > d_e else d_e
        else:
            return dm

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    print(str(result) + '\n')
