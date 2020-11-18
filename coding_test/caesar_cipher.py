#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    res = ''
    al = list('abcdefghijklmnopqrstuvwxyz')

    for i in range(len(s)):
        c = s[i]
        is_c = False

        if 65 <= ord(c) <= 90 or 97 <= ord(c) <= 122:
            if 65 <= ord(c) <= 90:
                is_c = True
                c = c.lower()

            idx = al.index(c)
            if idx + k > len(al) - 1:
                idx = (k % len(al)) - (len(al) - idx)
            else:
                idx += k

            if is_c:
                res += al[idx].upper()
            else:
                res += al[idx]
        else:
            res += c

    return res

if __name__ == '__main__':
    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    print(result + '\n')
