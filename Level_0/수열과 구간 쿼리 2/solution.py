def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        arr2 = []
        for i in range(s,e+1):
            if k<arr[i]:
                arr2.append(arr[i])
        if arr2 == []:
            answer.append(-1)
        else :
            answer.append(min(arr2))
    return answer