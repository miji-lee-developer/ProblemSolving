#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    l = list(map(str, arr))
    cv = arr[len(arr) - 1]
    isD = False
    for i in range(len(arr) - 2, -1, -1):
        if int(l[i]) > cv:
            l[i + 1] = l[i]
        else:
            l[i + 1] = str(cv)
            isD = True

        print(' '.join(l))
        if isD:
            break

    if isD == False:
        l[0] = str(cv)
        print(' '.join(l))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
