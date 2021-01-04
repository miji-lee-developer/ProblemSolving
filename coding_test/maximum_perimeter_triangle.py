#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumPerimeterTriangle function below.
def maximumPerimeterTriangle(sticks):
    res = []
    sticks = sorted(sticks, reverse=True)
    for i in range(len(sticks) - 2):
        a = sticks[i]
        b = sticks[i + 1]
        c = sticks[i + 2]
        if a + b > c and a + c > b and b + c > a:
            res = [c, b, a]
            break

    if len(res) == 0:
        res = [-1]
    return res

if __name__ == '__main__':
    n = int(input())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    print(' '.join(map(str, result)))
    print('\n')
