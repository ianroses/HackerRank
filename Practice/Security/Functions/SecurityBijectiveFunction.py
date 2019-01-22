#!/bin/python3
n = int(input())

numbers = list(map(int, input().rstrip().split()))
s = set(numbers)

if len(numbers) == len(s):
    print("YES")
else:
    print("NO")

