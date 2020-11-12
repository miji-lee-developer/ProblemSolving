#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    res = 1
    for i in range(1, len(s)):
        if 65 <= ord(s[i]) <= 90:
            res += 1

    return res

if __name__ == '__main__':
    s = input()

    result = camelcase(s)

    print(str(result) + '\n')
