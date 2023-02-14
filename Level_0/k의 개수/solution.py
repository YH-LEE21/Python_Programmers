def numberForK(i, j, k):
    answer = [s.count(str(k)) for r in range(i,j+1) for s in str(r)]
    return sum(answer)
print(numberForK(1,13,1))
print(numberForK(10,50,5))
print(numberForK(3,10,2))
