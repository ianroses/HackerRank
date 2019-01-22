#!/bin/python3

n = int(input())
d = {}

numbers = list(map(int, input().rstrip().split()))
i = 1
for number in numbers:
    d[i] = number
    i = i +1
for number in numbers:
    print(d[number])
    
