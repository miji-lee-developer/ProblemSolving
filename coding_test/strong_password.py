#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    ml = 6
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

    cb = 0
    for b in cl:
        if b == False:
            cb += 1

    if ml - n > cb:
        return ml - n
    else:
        return cb

if __name__ == '__main__':
    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    print(str(answer) + '\n')
