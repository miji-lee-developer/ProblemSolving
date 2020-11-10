#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    d = {}
    is_c = True

    while is_c:
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                if i == 0:
                    s = s[i + 2:]
                else:
                    s = s[:i] + s[i + 2:]
                break

            if i == len(s) - 2:
                is_c = False

        if s == '':
            is_c = False

    if s == '':
        s = 'Empty String'

    return s


if __name__ == '__main__':
    s = input()

    result = superReducedString(s)

    print(result + '\n')
