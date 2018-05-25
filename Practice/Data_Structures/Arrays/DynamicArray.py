#!/bin/python3

import os
import sys

#
# Complete the dynamicArray function below.
#
def dynamicArray(n, queries):
    lastAnswer = 0
    lst = [[] for x in range(n)]
    result = []
    for query in queries:
        if query[0] == 1:
            seq = (query[1]^lastAnswer) % n
            lst[seq].append(query[2])
        else:
            seq = (query[1]^lastAnswer) % n
            index = query[2] % len(lst[seq])
            lastAnswer = lst[seq][index]
            result.append(lastAnswer)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
