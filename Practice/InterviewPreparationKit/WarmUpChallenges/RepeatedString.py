#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    a = s.count("a")
    m = n // len(s)
    c = n % len(s)
    a = a * m
    for i in range (c):
        if(s[i]=="a"):
            a = a + 1
    return a


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
