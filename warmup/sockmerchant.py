#!/bin/python3

ar = [1,2,3,4,1,2,3,4,5]
sockcounter = {sock: 0 for sock in ar}
for sock in ar:
    sockcounter[sock] += 1
totalpairs = 0
for total in sockcounter.values():
    totalpairs += total // 2
print(totalpairs)
