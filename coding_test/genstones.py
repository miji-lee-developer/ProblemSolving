#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gemstones function below.
def gemstones(arr):
    res = 0
    s_arr = ''.join(map(lambda x: ''.join(set(x)), arr))
    d = {}
    for i in range(len(s_arr)):
        s = s_arr[i]
        if s in d:
            d[s] += 1
            if d[s] == len(arr):
                res += 1
        else:
            d[s] = 1

    return res

if __name__ == '__main__':
    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    print(str(result) + '\n')
