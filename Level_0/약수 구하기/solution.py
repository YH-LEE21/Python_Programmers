def divisor(n):
    return [i for i in range(1,n+1) if n%i==0]

print(divisor(24))
print(divisor(29))