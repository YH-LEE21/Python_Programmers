def sumDivisor(n):
    return sum([i for i in range(1,n//2+1) if n%i==0])+n

#test value
print(sumDivisor(12)) #result value : 28
print(sumDivisor(5)) #result value : 6
