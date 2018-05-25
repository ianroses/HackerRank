#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    
    aux = []
    aux = a[d:] + a[:d]
    fptr.write(' '.join(map(str, aux)))
    fptr.close()
