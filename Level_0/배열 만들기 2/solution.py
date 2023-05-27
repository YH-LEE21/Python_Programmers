def solution(l, r):
    answer = []
    for i in range(l,r+1):
        if len(str(i)) == str(i).count("5")+ str(i).count("0"):
            answer.append(i)
    if len(answer) == 0:
        answer.append(-1)
    return 


print(solution(5,555))