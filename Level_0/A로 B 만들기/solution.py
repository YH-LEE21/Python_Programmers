def AtoB(before, after):
    p = 0
    for i in before:
        if i in after:
            if before.count(i) == after.count(i):
                p += 1   
            else :continue
    return  1 if  len(before)==p else 0

print(AtoB("olleh","hello"))
print(AtoB("allpe","apple"))
