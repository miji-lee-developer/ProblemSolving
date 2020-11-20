#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    cs = 'hackerrank'
    i = 0
    for idx in range(len(s)):
        if i == len(cs):
            break

        if s[idx] == cs[i]:
            i += 1

    if i == len(cs):
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        print(result + '\n')
