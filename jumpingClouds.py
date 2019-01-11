c = [0, 0, 1, 0, 0, 1, 0] # len = 7
#c = [0, 0, 0, 1, 0, 0] # len = 6
i = len(c)
j = 0
jumps = 0
while j < i:
    print("jumps: " + str(jumps))
    if (j + 2 < i) and c[j + 2] == 0: #safe to skip ahead
        j += 1
        print("bonus j: " + str(j))
    j += 1
    print("reg j: " + str(j))
    if (j < i):
        jumps += 1

print("total jumps:" + str(jumps))
