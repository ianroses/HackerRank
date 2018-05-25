#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the array2D function below.
def array2D(arr):
    maximun = -63 # -9 times 7
    temp = 0
    for i in range(0,4):
        for j in range(0,4):
            aux = sum(arr[i][j:j+3])
            aux += arr[i+1][j+1]
            aux += sum(arr[i+2][j:j+3])
            if aux > maximun:
                maximun = aux
    return maximun

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = array2D(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
