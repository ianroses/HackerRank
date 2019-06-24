#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    l = []
    start_symbols = ["{", "(", "["]
    end_symbols = {"}":"{", ")":"(", "]":"["}
    for letter in s:
        if letter in start_symbols:
            l.append(letter)
        else:
            if len(l)>0:
                if(l.pop() != end_symbols[letter]):
                    return "NO"
            else:
                return "NO"
    if len(l)==0:
        return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
