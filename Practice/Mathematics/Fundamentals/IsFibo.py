#!/bin/python3

import os
import sys
globvar=[0,1,2]

# Complete the solve function below.
def solve(n):
    if globvar.count(n):
        return "IsFibo"
    return "IsNotFibo"

if __name__ == '__main__':
    global globvar
    
    while not globvar[-1]>1000000000000:
        globvar.append((globvar[-1]+globvar[-2]))
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = solve(n)

        fptr.write(result + '\n')

    fptr.close()
