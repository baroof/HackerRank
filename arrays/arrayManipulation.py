#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
  arr = [0] * (n + 1) 

  # difference array method modeled after https://www.geeksforgeeks.org/difference-array-range-update-query-o1/
  diff_arr = [0] * (n + 2)

  diff_arr[0] = arr[0]
  diff_arr[n] = 0

  for i in range (1, n):
    diff_arr[i] = arr[i] - arr[i - 1]
  
  #print("len(arr): {}, len(diff_arr): {}".format(len(arr), len(diff_arr)))
  for q in queries:
    left, right, x = q
    #print("got left: {}, right: {}, x: {}".format(left, right, x))
    diff_arr[left] += x
    diff_arr[right + 1] -= x

  for i in range(0, len(arr)):
    if (i == 0):
      arr[i] == diff_arr[i]
    else:
      arr[i] = diff_arr[i] + arr[i - 1]

  return(max(arr))

if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  files = "input00.txt", "input14.txt", "input15.txt", "input07.txt", "input-foo.txt"

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
