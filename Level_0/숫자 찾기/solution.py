def searchNum(num, k):
    return str(num).find(str(k))+1 if str(num).find(str(k)) != -1 else -1

print(searchNum(29183,1))
print(searchNum(232443,4))
print(searchNum(123456,7))