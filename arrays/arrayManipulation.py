#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
  arr = list(0 for i in range(0, n))
  for qlist in queries:
    start = qlist[0]
    end = qlist[1]
    summand = qlist[2]

    j = start
    while j <= end:
      arr[j-1] += summand
      j += 1

  return(max(arr))

if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  files = "input00.txt", "input14.txt", "input15.txt"

  for f in files:
    fh = open(f, "r")
    nm = fh.readline().split()

    n = int(nm[0])
    m = int(nm[1])
    queries = []
    for _ in range(m):
      queries.append(list(map(int, fh.readline().rstrip().split())))
      
    result = arrayManipulation(n, queries)

    print(result)

  fptr.write(str(result) + '\n')

  fptr.close()
