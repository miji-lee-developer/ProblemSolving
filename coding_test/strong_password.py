#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    ln = 6
    if n <= 3:
        return ln - n
    else:
        cl = [False, False, False, False]
        special_char = "!@#$%^&*()-+"
        for i in range(n):
            if False in cl:
                if 48 <= ord(password[i]) <= 57:
                    cl[0] = True
                elif 65 <= ord(password[i]) <= 90:
                    cl[1] = True
                elif password[i] in special_char:
                    cl[2] = True
                elif 97 <= ord(password[i]) <= 122:
                    cl[3] = True
            else:
                break

        if False in cl:
            if n < ln:
                return n - ln
            else:
                r = 0
                for b in cl:
                    if b:
                        r += 1
                return len(cl) - r


if __name__ == '__main__':
    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    print(str(answer) + '\n')
