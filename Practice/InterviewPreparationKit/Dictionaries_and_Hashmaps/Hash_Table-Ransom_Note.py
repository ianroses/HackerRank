#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazine.sort()
    note.sort()
    while len(note) > 0 and len(magazine)>0:
        a = magazine.pop(0)
        b = note.pop(0)
        while (a<b):
            if len(magazine)>0:
                a = magazine.pop(0)
            else:
                return "No"
        if (a>b):
            return "No"
    if (len(note)==0):
        return "Yes"
    else:
        return "No"


    
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))
