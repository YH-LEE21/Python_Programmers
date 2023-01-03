def numberOfOrderPairs(n):
    answer = 0
    for i in range(n):
        if n%(i+1)==0:
            answer+=1
    return answer

print(numberOfOrderPairs(20))
print(numberOfOrderPairs(100))
