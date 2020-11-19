#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    res = 0
    cs = 'SOS' * (len(s) // 3)

    for i in range(len(cs)):
        if s[i] != cs[i]:
            res += 1

    return res
if __name__ == '__main__':
    s = input()

    result = marsExploration(s)

    print(str(result) + '\n')
