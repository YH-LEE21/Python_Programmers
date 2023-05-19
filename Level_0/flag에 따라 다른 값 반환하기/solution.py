def revertFlag(a, b, flag):
    return a+b if flag else a-b

print(revertFlag(-4,7,True))
print(revertFlag(-4,7,False))
