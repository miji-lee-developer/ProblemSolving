#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    res = 0
    m = 0
    prices = sorted(prices)

    for i in range(len(prices)):
        if i == 0:
            if prices[i] <= k:
                m = prices[i]
                res += 1
            else:
                break
        else:
            if m + prices[i] <= k:
                m += prices[i]
                res += 1

    return res

if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    print(str(result) + '\n')
