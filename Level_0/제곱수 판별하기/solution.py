import math
def isSqrt(n):
    return 1 if math.ceil(math.sqrt(n))**2 == n else 2

print(isSqrt(144))
print(isSqrt(976))
