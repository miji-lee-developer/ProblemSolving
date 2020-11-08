#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(grid):
    m = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if (i == 0 or i == len(grid) - 1) and (j == 0 or j == len(grid) - 1):
                continue
            else:
                v = int(grid[i][j])
                if v > m:
                    m = v

    for i in range(len(grid)):
        for j in range(len(grid)):
            if (i == 0 or i == len(grid) - 1) and (j == 0 or j == len(grid) - 1):
                continue
            else:
                if int(grid[i][j]) == m:
                    grid[i] = grid[i][:j] + "X" + grid[i][j + 1:]

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