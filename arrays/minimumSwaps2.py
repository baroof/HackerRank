#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
  return("woo!")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    files = "input00.txt", "input01.txt", "input02.txt"
    for f in files:
      fh = open(f, "r")
      n = fh.readline()
      arr = list(map(int, fh.readline().rstrip().split()))

      res = minimumSwaps(arr)

      print(res)

    fptr.write(str(res) + '\n')
    fptr.close()
