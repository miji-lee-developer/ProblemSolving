#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):
    res = 0
    q = len(s) // 2
    for i in range(q):
        res += abs(ord(s[i]) - ord(s[len(s) - i - 1]))

    return res

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        print(str(result) + '\n')
