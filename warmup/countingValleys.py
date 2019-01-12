s = "UDDDUDUU"
step = 0
sealevel = True
valley = False
mountain = False
valleys = 0

print("at sealevel")

for ud in list(s):
    if ud == "U":
        step += 1
        print("up 1")
        if step > 0 and sealevel == True:
            sealevel = False
            valley = False
            mountain = True
    elif ud == "D":
        step -= 1
        print("down 1")
        if step < 0 and sealevel == True:
            sealevel = False
            valley = True
            mountain = False
            valleys += 1
    if step == 0:
        print("at sealevel")
        sealevel = True
        valley = False
        mountain = False

print(valleys)


