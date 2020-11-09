#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(grid):
    s = []

    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid) - 1):
            l = [int(grid[i - 1][j]), int(grid[i][j - 1]), int(grid[i][j + 1]), int(grid[i + 1][j])]
            if max(l) < int(grid[i][j]):
                s.append([i, j])

    for i, j in s:
        grid[i] = grid[i][:j] + 'X' + grid[i][j + 1:]

    return grid

if __name__ == '__main__':
    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    print('\n'.join(result))
    print('\n')