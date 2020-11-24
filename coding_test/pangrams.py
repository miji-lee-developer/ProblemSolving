#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    ss = set(list(s.lower().replace(' ', '')))
    if len(ss) == 26:
        return 'pangram'
    else:
        return 'not pangram'

if __name__ == '__main__':
    s = input()

    result = pangrams(s)

    print(result + '\n')
