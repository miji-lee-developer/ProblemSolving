#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fairRations function below.
def fairRations(B):
    if len(B) == 2:
        return "NO"
    else:
        res = 0
        for i in range(len(B)):
            if B[i] % 2 != 0:
                res += 2
                B[i] += 1
                if i == len(B) - 1:
                    B[i - 1] += 1
                else:
                    B[i + 1] += 1

        return res

if __name__ == '__main__':
    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    print(str(result) + '\n')
