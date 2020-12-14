#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gameOfThrones function below.
def gameOfThrones(s):
    d = {}
    o_c = 0

    for t in s:
        if t in d:
            d[t] += 1
        else:
            d[t] = 1

    for v in d.values():
        if v % 2 != 0:
            o_c += 1

    if len(s) % 2 == 0 and o_c > 0:
        return 'NO'
    elif len(s) % 2 != 0 and o_c > 1:
        return 'NO'
    else:
        return 'YES'

if __name__ == '__main__':
    s = input()

    result = gameOfThrones(s)

    print(result + '\n')
