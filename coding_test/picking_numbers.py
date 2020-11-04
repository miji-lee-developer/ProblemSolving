#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    a = sorted(a)
    k = 0
    d = {0:1}
    c = a[0]
    for i in range(1, len(a)):
        if a[i] - c > 1:
            c = a[i]
            k += 1
            d[k] = 0

        d[k] += 1

    return max(d.values())

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    print(str(result) + '\n')
