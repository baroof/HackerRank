#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
  bribes = 0
  bribed = False
  lastPos = len(q) - 1

  # check for chaos
  for counter, position in enumerate(q, 1):
      if position - counter > 2:
        return "Too chaotic"
  # bubble sort to put them back in order, counting how many bribes were necessary
  for i in range(0,lastPos):
    for j in range(0, lastPos):
      if q[j] > q[j+1]:
        q[j],q[j+1] = q[j+1],q[j]
        bribes += 1
        bribed = True
    if bribed:
      bribed = False
    else:
      break
  return bribes


if __name__ == '__main__':
    t = int(input())
    results = []
    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        results.append(minimumBribes(q))

    for r in results:
      print(r)

