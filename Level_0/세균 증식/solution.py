def bacterialGrowth(n, t):
    answer = n
    for i in range(0,t):
        answer = answer*2
    return answer

print(bacterialGrowth(2,10))
print(bacterialGrowth(7,15))
