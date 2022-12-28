def hateEven(n):
    return [i for i in range(n+1) if i%2 == 1]
    #return [i for i in range(1,n+1,2)]
print(hateEven(10))
print(hateEven(15))