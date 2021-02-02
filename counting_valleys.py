#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    alt = 0
    invalley = False
    out = 0
    for c in range(0, steps):
        
        if alt == -1 and path[c] == 'U':
            out += 1
        if path[c] == 'D':
           alt -= 1
        elif path[c] == 'U':
            alt += 1
    return out
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
