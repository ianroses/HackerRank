#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    divisors = []
    sroot = int(math.sqrt(n))+1
    for num in range (1,sroot):
        if(n%num == 0):
            divisors.append(num)
            divisors.append(int(n/num))
    topscore = 1
    candidate = 1
    for divisor in divisors:
        digits = str(divisor)
        temp = 0
        for digit in digits:
            temp = temp + int(digit)
        if temp> topscore:
            topscore = temp
            candidate = divisor
        elif temp == topscore:
            if candidate > divisor:
                candidate = divisor
    print (candidate)
