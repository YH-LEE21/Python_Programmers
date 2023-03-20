import math
def combCalc(balls, share):
    #math.comb(balls,share)
    return math.factorial(balls)//(math.factorial(balls-share)*math.factorial(share))

print(combCalc(3,2)) #5
print(combCalc(5,3)) # 10