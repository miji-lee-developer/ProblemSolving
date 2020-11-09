#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the strangeCounter function below.
def strangeCounter(t):
    res = 0
    v = 1
    s = 0
    while True:
        if v == 1:
            v = 3
            s = 3
        else:
            v *= 2
            s += v

        if s - v < t <= s:
            res = s - t + 1
            break

    return res

if __name__ == '__main__':
    t = int(input())

    result = strangeCounter(t)

    print(str(result) + '\n')
