#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic):
    d = {}

    for i in range(len(topic) - 1):
        for j in range(i + 1, len(topic)):
            s = int(topic[i]) + int(topic[j])
            v = len(str(s).replace('0', ''))
            if v in d:
                d[v] += 1
            else:
                d[v] = 1

    m = max(d.keys())
    return [m, d[m]]

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    print('\n'.join(map(str, result)))
    print('\n')