#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the runningTime function below.
def runningTime(arr):
    res = 0
    for i in range(1, len(arr)):
        idx = i
        while idx > 0:
            if arr[idx - 1] > arr[idx]:
                t = arr[idx - 1]
                arr[idx - 1] = arr[idx]
                arr[idx] = t
                res += 1
            else:
                break
            idx -= 1

    return res

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    print(str(result) + '\n')
