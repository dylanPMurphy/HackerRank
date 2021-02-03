#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    count = 0
    if s == 'a':
        return n
    elif n > 10000:
        half = n//len(s)
        remainder = n%len(s)
        for i in range(0, len(s)):
            if s[i%len(s)] == 'a':
                count+=1
        count*=half
        for i in range(0,remainder):
            if s[i%len(s)] == 'a':
                count+=1
        return count
    else:
        for i in range(0, n):
            if s[i%len(s)] == 'a':
                count+=1
        return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
