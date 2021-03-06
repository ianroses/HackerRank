#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    lst = [0] * (n+1)
    for a in queries:
        lst[a[0]-1] += a[2]
        lst[a[1]] -= a[2]
    max_possible = 0
    a = 0
    for b in lst:
        a += b
        if a > max_possible:
            max_possible = a
    return max_possible

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
