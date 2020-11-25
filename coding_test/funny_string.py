#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    res = 'Funny'
    for i in range(len(s) - 1):
        n1 = abs(ord(s[i]) - ord(s[i + 1]))
        n2 = abs(ord(s[len(s) - i - 1]) - ord(s[len(s) - i - 2]))
        if n1 != n2:
            res = 'Not Funny'
            break

    return res

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        print(result + '\n')
