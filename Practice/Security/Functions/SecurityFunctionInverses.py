#!/bin/python3

n = int(input())
d = {}

numbers = list(map(int, input().rstrip().split()))
i = 1
for number in numbers:
    d[number] = i
    i = i +1
for j in range(1,len(numbers)+1):
    print (d[j])
