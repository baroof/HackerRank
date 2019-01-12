#expect 7
#s = "aba"
#n = 10
###

#expect 1000000000000
s = "a"
n = 1000000000000
###

s = "kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm"
n = 736778906400

total = 0

if len(s) > n:
    total = s.count("a", 0, n)
else:
    acount = s.count("a")
    diff = n // len(s)
    remainder = n % len(s)
    remainders = s[:remainder].count("a")

    print("diff: " + str(diff))
    print("remainder: " + str(remainder))
    print("remainders: " + str(remainders))


    total = acount * diff + remainders
print(total)


