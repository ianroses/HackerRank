#!/bin/python3
import math
import os
import sys

#
# Complete the primeCount function below.
#
def primeCount(n):
    if n == 2:
        return 1
    #print ("Primos de: "+str(n))
    count = 0
    y = int(math.sqrt( n ))
    b = 1
    prime = True
    for num in range(2,n):
    # prime numbers are greater than 1
        for i in range(2,num):
            if (num % i) == 0:
                prime = False
                break
        if prime:
            if b*num > n:
                return count
            else:
                b = b *num
                #print (num)
                count = count + 1
        else:
            prime = True
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = primeCount(n)

        fptr.write(str(result) + '\n')

    fptr.close()
