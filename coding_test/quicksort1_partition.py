#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):
    p = arr[0]
    l = []
    e = [p]
    r = []
    for i in range(1, len(arr)):
        if arr[i] < p:
            l.append(arr[i])
        elif arr[i] == p:
            e.append(p)
        else:
            r.append(arr[i])

    return l + e + r

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    print(' '.join(map(str, result)))
    print('\n')
