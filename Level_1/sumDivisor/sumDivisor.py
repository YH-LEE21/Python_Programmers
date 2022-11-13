def sumDivisor(n):
    divisor = []
    for i in range(1,n+1):
        if n % i == 0:
            divisor.append(i)

    return sum(divisor)

#test value
print(sumDivisor(12)) #result value : 28
print(sumDivisor(5)) #result value : 6
