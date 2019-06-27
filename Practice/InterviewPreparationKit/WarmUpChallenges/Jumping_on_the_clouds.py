#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    c.pop(0)
    count = 0
    while len(c)>1:
        if c[1] == 1:
            count = count + 1
            c.pop(0)
        else:
            c.pop(0)
            c.pop(0)
            count = count + 1
    if len(c)>0:
        count = count + 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
