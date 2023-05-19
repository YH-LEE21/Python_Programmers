def commonMultiple(number, n, m):
    return int(not(number%n)) and int(not(number%m))

print(commonMultiple(60,2,3))
print(commonMultiple(55,10,5))