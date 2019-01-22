#!/bin/python3

import os
import sys

#
# Complete the restaurant function below.
#
def restaurant(l, b):
    x = l
    y = b
    if x > y: 
        small = y
    else: 
        small = x 
    for i in range(1, small+1): 
        if((x % i == 0) and (y % i == 0)): 
            gcd = i 
    return int((l/gcd)*(b/gcd))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        lb = input().split()

        l = int(lb[0])

        b = int(lb[1])

        result = restaurant(l, b)

        fptr.write(str(result) + '\n')

    fptr.close()
