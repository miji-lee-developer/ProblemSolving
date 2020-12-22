#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marcsCakewalk function below.
def marcsCakewalk(calorie):
    res = 0
    calorie = sorted(calorie, reverse=True)

    for i in range(len(calorie)):
        if i == 0:
            res += calorie[i]
        else:
            res += ((2 ** i) * calorie[i])

    return res

if __name__ == '__main__':
    n = int(input())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    print(str(result) + '\n')
