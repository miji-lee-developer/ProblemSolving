#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):
    c = 0

    for i in range(len(s1)):
        if s1[i] in s2:
            # print(s1[i])
            s2 = s2.replace(s1[i], '', 1)
            c += 1

    return (len(s1) - c) + len(s2)

if __name__ == '__main__':
    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    print(str(result) + '\n')
