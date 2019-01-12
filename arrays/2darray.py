#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    print(arr)
    tottot = []
    row = 0
    while row < 4:
        col = 0
        print("row = " + str(row))
        a = e = 0
        b = d = f = 1
        c = g = 2
        while c < 6:
            print("col = " + str(col))
            arowtot = arr[row][a] + arr[row][b] + arr[row][c]
            drowtot = arr[row+1][d]
            erowtot = arr[row+2][e] + arr[row+2][f] + arr[row+2][g]
            tot = arowtot + drowtot + erowtot
            tottot.append(tot)
            a += 1
            b += 1
            c += 1
            d += 1
            e += 1
            f += 1
            g += 1
            col += 1
        row += 1

    maxtot = max(tottot)
    print("max: " + str(maxtot))

    return(maxtot)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
