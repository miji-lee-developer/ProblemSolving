#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulBinaryString function below.
def beautifulBinaryString(b):
    res = 0
    s = '010'

    while b.find(s) > -1:
        b = b.replace(s, '111', 1)
        res += 1

    return res

if __name__ == '__main__':
    n = int(input())

    b = input()

    result = beautifulBinaryString(b)

    print(str(result) + '\n')
