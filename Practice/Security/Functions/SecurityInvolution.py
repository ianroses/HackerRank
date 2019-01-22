#!/bin/python3

n = int(input())
d = {}

numbers = list(map(int, input().rstrip().split()))
i = 1
for number in numbers:
    d[i] = number
    i = i +1
involution = True
for j in range(1,len(numbers)+1):
    if d[d[j]] != j:
        involution = False
if involution:
    print("YES")
else:
    print("NO")
        
